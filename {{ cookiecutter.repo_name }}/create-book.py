import os

file_path = r'_toc.yml'
if os.path.exists(file_path):
    print('file already exists')
else:
    # create a file
    with open(file_path, 'w') as fp:
        # uncomment if you want empty file
        fp.write('# Table of contents\n')
        fp.write('# Learn more at https://jupyterbook.org/customize/toc.html')
        

