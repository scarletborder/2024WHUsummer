from prettytable import PrettyTable

# encrypted = "67 29 2e e6 c2 ea b8 c4 0e 1c f7 8c 31"
# encrypted = "4e 9f 59 30"
encrypted = "64 28 2d e5 c0 eb bb c4 07 1c f7 8f 35 2b d6 4c 86 93 9e 7d 72 84 52 19 2f c3 50 34 78 40 0d bb a3 27 c9 d6 38 a9 97 83 1f 1a 15 16 9c d1 aa ba a6 f1 09 4c 36 c6 b7 23 e8 12 2e 7a cc 07 b3 34 07 c9 45 44 eb f2 ae ed 2e a5 b2 17 62 6f"
enc_list = encrypted.split(" ")

# original = "今天"
# original = "2022302181125"
stat = {}
table = PrettyTable(["加密", "原", "异或数"])
zhu = []

for idx in range(len(enc_list)):
    enc_num = int(enc_list[idx], 16)
    # ori_ascii = ord(original[idx])
    ori_ascii = ord("1")
    keysteam = hex(enc_num ^ ori_ascii)
    table.add_row([enc_list[idx], hex(ori_ascii), keysteam])
    stat[keysteam] = stat.get(keysteam, 0) + 1
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
