import os
import shutil
from_dir="C:/Users/benumim joga/Downloads/python/PRO_1-1_C102_AtividadeDoAluno1-main/PRO_1-1_C102_AtividadeDoAluno1-main"
to_dir="C:/Users/benumim joga/Music/imagens"
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name, extension=os.path.splitext(file_name)
    if extension=="":
        continue
    if extension in [".pdf"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"PDF files"
        path3=to_dir+"/"+"PDF files"+"/"+file_name
        if os.path.exists(path2):
          print("Movendo "+file_name+"...")
          shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Movendo "+file_name+"...")
            shutil.move(path1,path3)