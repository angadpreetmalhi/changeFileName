# change file names
import os
def fileChanger(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1
# Enter the path of folder where you want to make changes
fileChanger(r"C:/Users/Angadpreet/Desktop/data",
        r"C:/Users/Angadpreet/PycharmProjects/class/aps.txt", ".txt" )
