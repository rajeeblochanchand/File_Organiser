import os
import shutil

script_name = 'file_organiser.py'
file_mappings = {
      '.txt': 'TextFiles',
      '.jpg': 'ImageFiles',
      '.png': 'ImageFiles',
      '.jpeg': 'ImageFiles',
      '.webp': 'ImageFiles',
      '.py': 'PythonFiles'
}

def move_file(file_path, destination_folder):
    if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
                print(f'Created folder: {destination_folder}')
    else:
                print(f'Folder already exists: {destination_folder}')
    shutil.move(file_path, destination_folder)
    print(f'Moved: {file_path} to {destination_folder}')

folderpath = '.'
filenames = os.listdir(folderpath)
for filename in filenames:
    if(filename == script_name):
           continue
    file_path = os.path.join(folderpath, filename)
    if os.path.isfile(file_path):
        print(filename)
        name, ext = os.path.splitext(filename)
        if(ext in file_mappings):
               destination_folder = os.path.join(folderpath,file_mappings[ext] )
        else:
               destination_folder = os.path.join(folderpath,'OtherFiles')
        move_file(file_path, destination_folder)

print('File Organisation Complete!')
