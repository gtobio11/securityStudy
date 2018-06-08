F = open("3.PNG", "rb")

str = F.read()

F.close()

stri = b''
i = 0

print(len(str))

while i < len(str):
    data = (str[i] * 256) + str[i+1]
    temp = ((data ** 6029) % 10403).to_bytes(1, byteorder='big')
    stri += temp
    i = i + 2

F = open("4.PNG", "wb")

F.write(stri)

F.close()
