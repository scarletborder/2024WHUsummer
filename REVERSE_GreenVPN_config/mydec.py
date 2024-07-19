# eax = 0x95

ddl: list[int] = []
f = open("./system.ini", "rb")


while True:
    byte = f.read(1)  # 每次读取一个字节
    if not byte:
        break  # 读取到文件末尾时退出循环

    dl = int.from_bytes(byte, byteorder="big")
    # print(hex(dl))
    dl = dl ^ 0x0BD
    dl = dl + 0x69

    ddl.append(dl % 256)
    # eax -= 1
    # if eax == 0:
    #     break


f.close()

for c in ddl:
    print(chr(c), end="")

with open("parsed.txt", "wb") as output_file:
    for byte in ddl:
        output_file.write(byte.to_bytes(1, byteorder="big"))
