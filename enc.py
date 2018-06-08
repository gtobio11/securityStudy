F = open("2.PNG", "rb")

str = F.read()

F.close()

stri = b''
for i in str:
    temp = ((i**269) % 10403).to_bytes(2, byteorder='big')
    stri += temp

F = open("3.PNG", "wb")

F.write(stri)

F.close()