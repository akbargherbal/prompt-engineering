#!/usr/bin/env python3
"""
Fast GitHub Pages Static Site Generator
Generates a working website from your docs in under 20 minutes
"""

import os
import shutil
from pathlib import Path
import markdown
from datetime import datetime

class FastSiteGenerator:
    def __init__(self, source_dir=".", output_dir="docs"):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.markdown_extensions = ['toc', 'tables', 'fenced_code', 'codehilite']
        
        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        
    def get_html_template(self):
        """Simple, responsive HTML template"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6; 
            color: #333; 
            background: #fff;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .header {{ 
            background: #2c3e50; 
            color: white; 
            padding: 1rem 0; 
            position: sticky; 
            top: 0; 
            z-index: 100;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .home-btn {{ 
            position: fixed; 
            top: 20px; 
            right: 20px; 
            background: #e74c3c; 
            color: white; 
            padding: 12px 16px; 
            border-radius: 50px; 
            text-decoration: none; 
            font-weight: bold; 
            z-index: 1000;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: all 0.3s;
        }}
        .home-btn:hover {{ background: #c0392b; transform: translateY(-2px); }}
        .breadcrumb {{ 
            background: #ecf0f1; 
            padding: 10px 0; 
            margin-bottom: 20px; 
            font-size: 14px;
        }}
        .breadcrumb a {{ color: #3498db; text-decoration: none; }}
        .breadcrumb a:hover {{ text-decoration: underline; }}
        .content {{ 
            background: white; 
            padding: 2rem; 
            border-radius: 8px; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .file-list {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); 
            gap: 1rem; 
            margin: 2rem 0; 
        }}
        .file-item {{ 
            padding: 1rem; 
            border: 1px solid #ddd; 
            border-radius: 8px; 
            background: #f8f9fa;
            transition: all 0.3s;
        }}
        .file-item:hover {{ 
            transform: translateY(-2px); 
            box-shadow: 0 4px 12px rgba(0,0,0,0.15); 
        }}
        .file-item a {{ 
            color: #2c3e50; 
            text-decoration: none; 
            font-weight: 500; 
            display: block;
        }}
        .file-item a:hover {{ color: #3498db; }}
        .file-type {{ 
            font-size: 12px; 
            color: #7f8c8d; 
            margin-top: 5px; 
        }}
        .tree {{ font-family: monospace; white-space: pre-line; background: #f8f9fa; padding: 1rem; border-radius: 8px; }}
        pre {{ background: #2c3e50; color: #ecf0f1; padding: 1rem; border-radius: 8px; overflow-x: auto; }}
        code {{ background: #ecf0f1; padding: 2px 4px; border-radius: 4px; font-size: 0.9em; }}
        pre code {{ background: none; padding: 0; }}
        h1, h2, h3, h4, h5, h6 {{ color: #2c3e50; margin: 1.5rem 0 1rem 0; }}
        h1 {{ border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        a {{ color: #3498db; }}
        a:hover {{ color: #2980b9; }}
        .footer {{ 
            text-align: center; 
            padding: 2rem; 
            color: #7f8c8d; 
            border-top: 1px solid #ecf0f1; 
            margin-top: 3rem; 
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 10px; }}
            .file-list {{ grid-template-columns: 1fr; }}
            .content {{ padding: 1rem; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="container">
            <h1>{header_title}</h1>
        </div>
    </div>
    <a href="/" class="home-btn">🏠 Home</a>
    <div class="container">
        <div class="breadcrumb">
            {breadcrumb}
        </div>
        <div class="content">
            {content}
        </div>
        <div class="footer">
            Generated on {timestamp}
        </div>
    </div>
</body>
</html>'''

    def create_breadcrumb(self, path):
        """Create breadcrumb navigation"""
        parts = path.parts if path != Path('.') else []
        breadcrumb = '<a href="/">Home</a>'
        
        current_path = ""
        for part in parts:
            current_path = f"{current_path}/{part}" if current_path else part
            breadcrumb += f' / <a href="/{current_path}/">{part}</a>'
        
        return breadcrumb

    def process_markdown(self, md_path, relative_path):
        """Convert markdown to HTML"""
        with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        md = markdown.Markdown(extensions=self.markdown_extensions)
        html_content = md.convert(content)
        
        # Create breadcrumb
        breadcrumb = self.create_breadcrumb(relative_path.parent)
        
        # Generate HTML
        html = self.get_html_template().format(
            title=md_path.stem,
            header_title=md_path.stem,
            breadcrumb=breadcrumb,
            content=html_content,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        return html

    def create_directory_listing(self, dir_path, relative_path):
        """Create directory listing page"""
        files = []
        dirs = []
        
        for item in sorted(dir_path.iterdir()):
            if item.name.startswith('.'):
                continue
                
            rel_item_path = relative_path / item.name
            
            if item.is_dir():
                dirs.append({
                    'name': item.name,
                    'path': f"/{rel_item_path}/",
                    'type': 'Directory'
                })
            elif item.suffix.lower() in ['.md', '.txt']:
                files.append({
                    'name': item.name,
                    'path': f"/{rel_item_path.with_suffix('.html')}",
                    'type': f'{item.suffix.upper()} File'
                })
        
        # Create content
        content = f"<h1>{relative_path.name if relative_path.name else 'Documentation'}</h1>"
        
        if dirs or files:
            content += '<div class="file-list">'
            
            # Directories first
            for dir_info in dirs:
                content += f'''
                <div class="file-item">
                    <a href="{dir_info['path']}">{dir_info['name']}/</a>
                    <div class="file-type">{dir_info['type']}</div>
                </div>'''
            
            # Then files
            for file_info in files:
                content += f'''
                <div class="file-item">
                    <a href="{file_info['path']}">{file_info['name']}</a>
                    <div class="file-type">{file_info['type']}</div>
                </div>'''
            
            content += '</div>'
        else:
            content += '<p>No files found in this directory.</p>'
        
        breadcrumb = self.create_breadcrumb(relative_path)
        
        html = self.get_html_template().format(
            title=relative_path.name if relative_path.name else "Home",
            header_title=relative_path.name if relative_path.name else "Documentation Home",
            breadcrumb=breadcrumb,
            content=content,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        return html

    def generate_site(self):
        """Generate the complete static site"""
        print("🚀 Starting fast site generation...")
        
        # Clean output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir()
        
        # Create .nojekyll file for GitHub Pages
        (self.output_dir / '.nojekyll').touch()
        
        # Process all directories and files
        for root, dirs, files in os.walk(self.source_dir):
            root_path = Path(root)
            relative_path = root_path.relative_to(self.source_dir)
            
            # Skip hidden directories and output directory
            if any(part.startswith('.') or part == self.output_dir.name for part in relative_path.parts):
                continue
                
            output_dir_path = self.output_dir / relative_path
            output_dir_path.mkdir(parents=True, exist_ok=True)
            
            # Process markdown and text files
            for file in files:
                if file.startswith('.'):
                    continue
                    
                file_path = root_path / file
                rel_file_path = relative_path / file
                
                if file.endswith(('.md', '.txt')):
                    try:
                        html_content = self.process_markdown(file_path, rel_file_path)
                        output_file = output_dir_path / f"{Path(file).stem}.html"
                        
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                        
                        print(f"✅ {rel_file_path}")
                    except Exception as e:
                        print(f"⚠️  Error processing {rel_file_path}: {e}")
            
            # Create directory listing
            try:
                dir_html = self.create_directory_listing(root_path, relative_path)
                index_file = output_dir_path / "index.html"
                
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(dir_html)
                
                print(f"📁 {relative_path}/")
            except Exception as e:
                print(f"⚠️  Error creating directory listing for {relative_path}: {e}")
        
        print(f"\n🎉 Site generated successfully in '{self.output_dir}'!")
        print(f"📊 Ready for GitHub Pages deployment")

def main():
    """Main execution"""
    generator = FastSiteGenerator()
    generator.generate_site()
    
    print("""
🚀 DEPLOYMENT INSTRUCTIONS:
1. git add docs/
2. git commit -m "Add documentation site"
3. git push origin main
4. Go to GitHub repo Settings → Pages
5. Set source to "Deploy from a branch"
6. Select "main" branch and "/docs" folder
7. Save and wait ~5 minutes

Your site will be live at: https://yourusername.github.io/yourrepo/
""")

if __name__ == "__main__":
    main()