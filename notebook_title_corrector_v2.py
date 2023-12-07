import nbformat
import re

def process_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook_content = nbformat.read(file, as_version=4)

    for cell in notebook_content['cells']:
        if cell['cell_type'] == 'markdown':
            cell['source'] = process_markdown(cell['source'])

    processed_path = notebook_path.replace('.ipynb', '_processed.ipynb')
    with open(processed_path, 'w', encoding='utf-8') as file:
        nbformat.write(notebook_content, file)

    print(f"Notebook processed and saved to: {processed_path}")

def process_markdown(markdown):
    # Replace <h1>, <h2>, <h3>, <h4> tags with bold formatting
    markdown = re.sub(r'<h1(?:.*?)>(.*?)<\/h1>', r'**\1**', markdown)
    
    # Replace <h2> and <h3> tags with bold formatting and process id attribute
    markdown = re.sub(r'<h2(?:\s+id=".*?")?(?:.*?)>(.*?)<\/h2>', r'**\1**', markdown)
    markdown = re.sub(r'<h3(?:\s+id=".*?")?(?:.*?)>(.*?)<\/h3>', r'**\1**', markdown)
    
    markdown = re.sub(r'<h4(?:.*?)>(.*?)<\/h4>', r'**\1**', markdown)

    # Replace any characters between < and > with ** only when there's an id attribute
    markdown = re.sub(r'<([^<>]+)(?:\s+id=".*?")?>(.*?)<\/\1>', r'**\2**', markdown)

    return markdown

# Replace 'your_notebook.ipynb' with the path to your notebook
notebook_path = r"your_notebook.ipynb"
process_notebook(notebook_path)
