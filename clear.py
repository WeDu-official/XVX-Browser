import subprocess
import os
folder_to_remove:str = f"C:\\Users\\{os.path.basename(os.environ['USERPROFILE'])}\\AppData\\Local\\main"
def remove_folder_recursively(folder_path):
    if not os.path.isdir(folder_path):
        exit()
    for root, dirs, files in os.walk(folder_path):
        print(f"Folder: {root}")
        for dir in dirs:
            print(f"  Subfolder: {os.path.join(root, dir)}")
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except (PermissionError,OSError):
                pass
        for dir in dirs:
            try:
                os.rmdir(os.path.join(root,dir))
            except (PermissionError,OSError):
                pass
    print(f"Folder '{folder_path}' and its contents have been removed.")
remove_folder_recursively(folder_to_remove)
subprocess.Popen('python main.py',creationflags=subprocess.CREATE_NO_WINDOW)