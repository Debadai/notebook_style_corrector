import nbformat

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
    # Your processing logic here, for example using regular expressions
    # This is a simplified example, modify as needed
    markdown = markdown.replace('<h1>', '**').replace('</h1>', '**')
    markdown = markdown.replace('<h2>', '**').replace('</h2>', '**')
    markdown = markdown.replace('<h3>', '**').replace('</h3>', '**')
    markdown = markdown.replace('<h4>', '**').replace('</h4>', '**')
    return markdown

# Replace 'your_notebook.ipynb' with the path to your notebook
notebook_path = r"G:\My Drive\Programacion\Archivos\Notebooks\4. IBM Data Analysis - Respaldo 2.ipynb"
process_notebook(notebook_path)