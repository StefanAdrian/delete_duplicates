import os

dir_path = r'C:\Users\adria\OneDrive\Desktop\Test'
for filename in os.listdir(dir_path):
    if filename.endswith("(1).jpg") or filename.endswith("(2).jpg") or \
            filename.endswith("(3).jpg") or filename.endswith(" - Copy.jpg"):
        file_path = dir_path + "\\" + filename
        os.remove(file_path)
