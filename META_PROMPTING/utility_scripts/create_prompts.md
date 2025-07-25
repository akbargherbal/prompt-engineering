```python

```


```python
import pandas as pd
import regex as re
import os
```


```python
import json
```


```python
df = pd.read_json('../docs/generation_jobs.json')
```


```python
df['jobs'].iloc[0]

df['category'] = df['jobs'].apply(lambda x: x['category'])
df['name'] = df['jobs'].apply(lambda x: x['name'])
df['description'] = df['jobs'].apply(lambda x: x['description'])
df['output_path'] = df['jobs'].apply(lambda x: x['output_path'])



CATEGORY_PLACEHOLDER = 'CATEGORY_PLACEHOLDER'
COMPONENT_NAME_PLACEHOLDER = 'COMPONENT_NAME_PLACEHOLDER'
DESCRIPTION_PLACEHOLDER = 'DESCRIPTION_PLACEHOLDER'


with open('../docs/PROMPT_SNIPPET_GENERATOR.md', encoding='utf-8') as f:
    prompt_template = f.read()

# assert existence of those placeholders in prompt template:
assert CATEGORY_PLACEHOLDER in prompt_template, "CATEGORY_PLACEHOLDER not found in prompt template"
assert COMPONENT_NAME_PLACEHOLDER in prompt_template, "COMPONENT_NAME_PLACEHOLDER not found in prompt template"
assert DESCRIPTION_PLACEHOLDER in prompt_template, "DESCRIPTION_PLACEHOLDER not found in prompt template"


def create_prompt(category, name, description, prompt_template=prompt_template):
    """
    Create a prompt for the given category, name, and description using the provided template.
    """
    prompt = prompt_template
    prompt = prompt.replace(CATEGORY_PLACEHOLDER, category)
    prompt = prompt.replace(COMPONENT_NAME_PLACEHOLDER, name)
    prompt = prompt.replace(DESCRIPTION_PLACEHOLDER, description)
    
    return prompt

df['PROMPT'] = df.apply(lambda x: create_prompt(
    x['category'], 
    x['name'], 
    x['description']
), axis=1)

# print(df['PROMPT'].iloc[0])

df['PROMPT_ID'] = df.index + 1 
df['PROMPT_ID'] = df['PROMPT_ID'].apply(lambda x: str(x).zfill(3))
# df

```


```python
# df.to_pickle('./INPUT_PROMPTS.pkl', protocol=4)
```


```python
output_df = pd.read_pickle('./results_20250723_220303/RESULTS.pkl')
```


```python
# convert output_df to json;

output_json = output_df['	PROMPT_ID	RESULT		category	name	description	output_path	PROMPT'.split()].to_json(
    './example_components.json',orient='records', force_ascii=False)
```


```python

```
