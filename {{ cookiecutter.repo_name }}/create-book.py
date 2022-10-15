import os

file_path = r'_toc.yml'
if os.path.exists(file_path):
    print('file already exists')
else:
    # create a file
    with open(file_path, 'w') as fp:
        # uncomment if you want empty file
        fp.write(
            '# Table of contents\n'
            '# Learn more at https://jupyterbook.org/customize/toc.html\n'
            
            'format: jb-book\n'
            'root: intro\n'
            'chapters:\n'
            '\t- file: notebooks/markdown\n'
            '\t- file: notebooks/notebooks\n'
            '\t- file: notebooks/markdown-notebooks'        

        )



        

