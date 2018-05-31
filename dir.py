import os

def search(dirname):
    for dirpath, dirs, files in os.walk(dirname):
        if "window" not in dirpath:
            for basename in files:
                

search("C:/")