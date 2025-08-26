# Sanity Check Guide: Why Tests Pass But Apps Fail

## The Problem: Green Tests, Broken Reality

**Scenario:** LLM writes you 50 tests. All pass ✅. You deploy. Users complain the app is broken 🔥.

**Root Cause:** Tests validate that code works *as written*, not *as intended*.

---

## The "Sanity Check" Framework

### 1. **The Reality Gap Audit** 🕵️

**Before trusting any test suite, ask:**

```python
# ❌ LLM Test: Tests what the code does
def test_calculate_shipping():
    result = calculate_shipping(weight=10, distance=100)
    assert result == 50  # Code returns 50, test passes

# ✅ Reality Check: Tests what SHOULD happen
def test_calculate_shipping_makes_business_sense():
    # $50 shipping for 10lb package across 100 miles?
    result = calculate_shipping(weight=10, distance=100)
    
    # Sanity bounds based on REAL business logic
    assert 5 <= result <= 25  # Reasonable shipping cost
    
    # Test against known competitors
    competitor_cost = 12.50
    assert abs(result - competitor_cost) <= 5  # Within reasonable range
```

---

## Common "Green but Wrong" Test Patterns

### 🚨 **Pattern 1: "Circular Logic" Tests**

```python
# ❌ BAD: Tests the implementation, not the requirement
class UserService:
    def get_user_display_name(self, user_id):
        user = self.db.get_user(user_id)
        return f"{user.first_name}_{user.last_name}"  # Bug: underscore!

# LLM writes this test (and it passes):
def test_get_user_display_name():
    service = UserService()
    result = service.get_user_display_name(123)
    assert result == "John_Doe"  # ✅ Passes, but users see "John_Doe"!

# ✅ GOOD: Tests the actual requirement
def test_get_user_display_name_for_humans():
    service = UserService()
    result = service.get_user_display_name(123)
    
    # Test what users actually expect to see
    assert " " in result  # Should have space, not underscore
    assert "_" not in result  # Should not have underscores
    assert result == "John Doe"  # What users actually want
```

### 🚨 **Pattern 2: "Happy Path Only" Tests**

```python
# ❌ BAD: Only tests perfect scenarios
def test_process_payment():
    payment = create_valid_payment()
    result = process_payment(payment)
    assert result.success == True

# ✅ GOOD: Tests what actually happens in production
def test_payment_processing_reality():
    # Test network failures (happens 2-5% of the time)
    with mock_network_timeout():
        result = process_payment(valid_payment)
        assert result.has_retry_mechanism()
        
    # Test invalid cards (happens 10-15% of the time)
    invalid_card = Payment(card_number="1234567890123456")
    result = process_payment(invalid_card)
    assert result.error_message_is_user_friendly()
    
    # Test duplicate payments (common user behavior)
    process_payment(valid_payment)
    duplicate_result = process_payment(valid_payment)
    assert duplicate_result.prevents_double_charge()
```

### 🚨 **Pattern 3: "Mock Everything" Tests**

```python
# ❌ BAD: Mocks hide integration problems
@mock.patch('database.get_user')
@mock.patch('email_service.send_welcome')
@mock.patch('payment_processor.charge_card')
def test_user_registration(mock_payment, mock_email, mock_db):
    mock_db.return_value = fake_user
    mock_email.return_value = True
    mock_payment.return_value = success_response
    
    result = register_user(user_data)
    assert result.success == True  # ✅ Always passes!

# ✅ GOOD: Test with real dependencies (at least sometimes)
def test_user_registration_integration():
    # Use test database, real email service (with test mode)
    with test_database(), test_email_service():
        result = register_user(valid_user_data)
        
        # Verify ACTUAL side effects happened
        assert user_exists_in_database(result.user_id)
        assert welcome_email_was_sent(result.user_id)
        assert user_can_actually_login(result.user_id)
```

---

## The "Sanity Check" Checklist

### ⚡ **Quick Reality Checks (Run These First)**

```python
# 1. Boundary Value Reality Check
def test_realistic_boundaries():
    # If your app calculates prices, test realistic scenarios
    expensive_item = calculate_price(item="laptop")
    assert 100 <= expensive_item <= 10000  # Reasonable laptop price
    
    cheap_item = calculate_price(item="pen")
    assert 0.10 <= cheap_item <= 50  # Reasonable pen price

# 2. Time-Based Reality Check  
def test_reasonable_performance():
    start_time = time.time()
    result = search_users("john")
    duration = time.time() - start_time
    
    assert duration < 2.0  # Users won't wait longer than 2 seconds
    assert len(result) <= 100  # Don't return 10,000 results

# 3. User Experience Reality Check
def test_error_messages_make_sense():
    with pytest.raises(ValidationError) as exc_info:
        create_user(email="not-an-email")
    
    error_msg = str(exc_info.value).lower()
    # Users should understand the error
    assert "email" in error_msg
    assert "invalid" in error_msg or "format" in error_msg
    # Should NOT contain technical jargon
    assert "regex" not in error_msg
    assert "validation.py line 47" not in error_msg
```

### 🔍 **Deep Sanity Audit Questions**

**For each passing test, ask:**

1. **"Would a user actually do this?"**
   ```python
   # ❌ Tests unrealistic user behavior
   def test_user_enters_perfect_data():
       user = User(name="John", email="perfect@email.com", age=30)
   
   # ✅ Tests realistic user behavior  
   def test_user_enters_messy_data():
       user = User(name="  john smith  ", email="JOHN@GMAIL.COM", age="30")
       cleaned = clean_user_data(user)
       assert cleaned.name == "John Smith"
       assert cleaned.email == "john@gmail.com"
   ```

2. **"What happens when external services fail?"**
   ```python
   # Test your app when the payment processor is down
   def test_payment_service_unavailable():
       with mock_service_unavailable('payment_processor'):
           result = checkout(cart)
           # Should gracefully handle, not crash
           assert result.user_friendly_error_message
           assert cart.items_are_still_saved()
   ```

3. **"Does this work with real data volumes?"**
   ```python
   # ❌ Tests with 3 records
   def test_with_tiny_dataset():
       users = [user1, user2, user3]
       result = process_users(users)
   
   # ✅ Tests with realistic data size
   def test_with_realistic_dataset():
       users = generate_test_users(count=10000)  # More realistic
       start_time = time.time()
       result = process_users(users)
       
       assert time.time() - start_time < 30  # Should complete in reasonable time
       assert not memory_usage_exceeded_limit()
   ```

---

## The "Manual Spot Check" Protocol

### 🛠️ **After Tests Pass, Do This:**

```python
# 1. Actually Run Your App Manually
"""
- Open your browser
- Go through the signup flow
- Try to break things on purpose
- Use weird inputs: "Robert'); DROP TABLE users;--"
- Try on mobile
"""

# 2. Check Logs for Warnings
def test_no_scary_logs():
    with capture_logs() as log_capture:
        result = run_typical_workflow()
        
    logs = log_capture.records
    # Tests should not generate warnings/errors
    assert not any("ERROR" in log.message for log in logs)
    assert not any("WARNING" in log.message for log in logs)
    assert not any("CRITICAL" in log.message for log in logs)

# 3. Database State Sanity Check
def test_database_state_makes_sense():
    # Run a typical workflow
    user = create_user("test@example.com")
    order = create_order(user, items=[laptop, mouse])
    
    # Check database state manually
    db_user = User.objects.get(email="test@example.com")
    assert db_user.orders.count() == 1
    assert db_user.orders.first().total > 0
    
    # Check for data corruption
    assert all_foreign_keys_valid()
    assert no_orphaned_records()
```

---

## Red Flags: When to Distrust Passing Tests

### 🚩 **Suspicious Test Patterns:**

```python
# 🚩 Red Flag 1: Tests that never fail
def test_that_always_passes():
    result = some_function()
    assert True  # This test is useless!

# 🚩 Red Flag 2: Tests with hardcoded expectations
def test_hardcoded_expectations():
    users = get_all_users()
    assert len(users) == 5  # What if you add/remove users?

# 🚩 Red Flag 3: Tests that don't test edge cases
def test_only_happy_path():
    result = divide(10, 2)
    assert result == 5
    # Missing: divide(10, 0), divide(0, 10), divide(-5, 2), etc.
```

### 🚩 **Environmental Red Flags:**

```bash
# If your tests need perfect conditions to pass:
export PYTHONPATH=/perfect/path
export DATABASE_URL=sqlite://perfect_test.db
export API_KEY=fake_key_that_never_expires

# Real apps need to handle imperfect environments
```

---

## Practical "Sanity Suite" for Your Apps

### 🎯 **For Django Apps:**

```python
# tests/sanity_checks.py
class SanityTestSuite:
    
    def test_admin_actually_works(self):
        """Can admin user actually use Django admin?"""
        self.client.login(username='admin', password='admin')
        response = self.client.get('/admin/')
        assert response.status_code == 200
        assert "Django administration" in response.content.decode()
    
    def test_static_files_load(self):
        """Do CSS/JS files actually exist and load?"""
        response = self.client.get('/static/css/main.css')
        assert response.status_code == 200
        assert len(response.content) > 0
    
    def test_database_migrations_work(self):
        """Do all migrations actually apply cleanly?"""
        from django.core.management import call_command
        call_command('migrate', '--check')  # Should not raise
```

### 🎯 **For FastAPI Apps:**

```python
def test_api_docs_accessible():
    """Users should be able to see API documentation"""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "swagger" in response.text.lower()

def test_health_check_meaningful():
    """Health check should actually verify app health"""
    response = client.get("/health")
    health_data = response.json()
    
    # Should check real dependencies
    assert health_data["database"] == "connected"
    assert health_data["external_api"] == "reachable"
    assert "uptime" in health_data
```

### 🎯 **For Data Pipelines:**

```python
def test_pipeline_with_real_sample_data():
    """Use actual production data sample (anonymized)"""
    sample_data = load_production_sample("last_week_sample.csv")
    result = run_pipeline(sample_data)
    
    # Verify realistic expectations
    assert len(result) > 0
    assert all(record.is_valid() for record in result)
    assert no_data_was_corrupted(sample_data, result)
```

---

## Key Takeaway

**Green tests don't guarantee working software.**

The sanity check mindset is:
1. **Test what users actually experience**
2. **Use realistic data and scenarios**  
3. **Manually spot-check critical paths**
4. **Question tests that seem "too easy"**

Think of sanity checks as **"Would I trust this with my own money?"** tests.

If you wouldn't use your own app based on what the tests cover, your tests need work.