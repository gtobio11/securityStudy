P = 103
Q = 101
N = 10403
# N = 217
QN = 10200
e = 269
d = 6029
# e = 109
# d = 2


stri = input('평문입력하세요 : ')

arr = ''
strin = ''


def encode(Str):
    array = ''
    for i in Str:
        array += chr((ord(i) ** e) % N)
    return array


def decode(array):
    string = ''
    for i in array:
        string += chr((ord(i) ** d) % N)
    return string


arr = encode(stri)
print(arr)

strin = decode(arr)
print(strin)