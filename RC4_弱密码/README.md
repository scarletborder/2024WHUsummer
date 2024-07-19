## RC4弱密钥破解
幽默RC4，感觉考察内容其实是socket

- dec2keystream.py : 根据已知密文的明文获得部分Keystream
- dec2plaintext.py ： 根据密文和keystream解密出明文
- findkeystream.py : 碰撞，获得密钥