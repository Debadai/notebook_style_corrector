# notebook_style_corrector

# Notebook Content Processing Solution

## Problem Description
In my Jupyter notebook, I encountered issues with inconsistent header formatting, particularly with `<h2>` and `<h3>` tags. Some headers were in Markdown format (using `##` and `###`, these ones were the headers I was using to establish the hierarchy in the table of contents), while others were in HTML format (`<h1>`, `<h2>`, `<h3>` and `<h4>`, these last ones came in cells I copied from other notebooks and included in my project). Additionally, there were variations in the presence of the `id` attribute in some headers, causing a hierarchy mismatch in the table of contents.

## Solution
To address these issues, I created a Python script using the `nbformat` and `re` libraries to programmatically process the notebook content. The script performs the following tasks:

1. Replaces Markdown-style headers (`<h1>`, `<h2>`, `<h3>`, `<h4>`)  with bold formatting (`**`).
2. Ensures consistent formatting for style headers (`##` and `###`).
3. Makes text inside HTML-style headers bold without affecting hierarchy.
4. Handles variations in the presence of the `id` attribute within `<h2>` and `<h3>` tags.

## How to Use
1. Install the `nbformat` library if not already installed: `pip install nbformat`.
2. Copy the provided Python script to a file (e.g., `process_notebook.py`).
3. Replace `'your_notebook.ipynb'` in the script with the path to your Jupyter notebook.
4. Make style and headers modifications as needed in your specific case.
5. Run the script using the command: `python process_notebook.py` (or `python3` on some systems).
6. The processed notebook will be saved as 'your_notebook_processed.ipynb'.

Please note VERY IMPORTANT: Always make a backup of your notebook before running the script to avoid unintended data loss.

Author: Federico Acerenza
