import socket


class HexIterator:
    def __init__(self, start=0, end=0xFF, step=256):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        next_block = [
            f"{i:02X}"
            for i in range(self.current, min(self.current + self.step, self.end + 1))
        ]
        self.current += self.step
        return next_block


def create_socket_connection(ip, port, byt):
    try:
        # 创建一个 socket 对象
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 连接到指定的 IP 和端口
        client_socket.connect((ip, port))

        # print(f"Successfully connected to {ip}:{port}")

        # 发送数据（可选）
        # message = "Hello, Server!"
        client_socket.sendall(byt)

        # 接收数据（可选）
        response = client_socket.recv(1024)
        print(f"{byt.hex()}=>" + response.decode())
        # if "null is not allowed" in response.decode():
        #     print(f"{str(byt)}Received from server: {response.decode()}")
        #     client_socket.close()
        #     return True

        # 关闭连接
        client_socket.close()

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Other exception: {e}")

    return False


if __name__ == "__main__":
    ip = "192.168.30.67"  # 替换为目标 IP 地址
    port = 8899  # 替换为目标端口
    existed = ""
    init = ""
    while True:
        for hh in range(0xFF):
            hbyte = f"{(hh):02x}"
            # byt = bytes.fromhex(init + hbyte)
            byt = bytes.fromhex("489e60aa3db406cb67292ee6c2eab8c40e1cf78e3c")
            if create_socket_connection(ip, port, byt):
                init = init + f"{((hh + 1) % 256):02x}"
                existed = existed + f"{(hh):02x}"
                print(existed)
                break
