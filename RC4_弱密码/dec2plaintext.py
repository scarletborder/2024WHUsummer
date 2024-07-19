from prettytable import PrettyTable

# encrypted = "67 29 2e e6 c2 ea b8 c4 0e 1c f7 8c 31"
# encrypted = "4e 9f 59 30"
encrypted = "48 9e 60 aa 3d b4 06 cb"
enc_list = encrypted.split(" ")

# original = "今天"
original = "1f fb 0c c9 52 d9 63 f1"
original_list = original.split(" ")
stat = {}
table = PrettyTable(["加密", "密钥", "明文"])
zhu = []

for idx in range(len(enc_list)):
    enc_num = int(enc_list[idx], 16)
    # ori_ascii = ord(original[idx])
    key_num = int(original_list[idx], 16)
    mingwen = chr(enc_num ^ key_num)
    table.add_row([enc_list[idx], original_list[idx], mingwen])
    # stat[mingwen] = stat.get(mingwen, 0) + 1
    # binary_str = bin(enc_num ^ ori_ascii)[2:]
    # # 使用.zfill()方法在左侧填充0，使得字符串长度为8位
    # padded_binary_str = binary_str.zfill(8)
    # zhu.append(padded_binary_str)

print(table)
print(len(table.rows))

# for c in zhu:
#     print(c, end="")
# stat = dict(sorted(stat.items(), key=lambda item: item[1], reverse=True))
# print(stat)
