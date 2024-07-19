from req import Request, ARequest
import asyncio
import random


class HexIterator:
    def __init__(self, start=0, end=0xFFFFFFFF, step=256):
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
            f"{i:08X}"
            for i in range(self.current, min(self.current + self.step, self.end + 1))
        ]
        self.current += self.step
        return next_block


# 使用示例


async def OnceTime(tmp):
    ok, msg = await ARequest(tmp)
    # if len(msg) < 64:
    # print(f"{tmp} ->{len(msg)}| {msg}")
    if len(msg) < 40:
        print(f"{tmp} ->{len(msg)}| {msg}")


def generate_hex_strings(count, length):
    hex_strings = []
    for _ in range(count):
        hex_string = "".join(random.choice("0123456789abcdef") for _ in range(length))
        hex_strings.append(hex_string)
    return hex_strings


async def main():
    iterator = HexIterator(start=0x00003FA0, step=8)
    for block in iterator:
        messages = []
        # current = "0123456789"
        # ok, msg = Request(current + "00")

        # lll = generate_hex_strings(256, 8)
        for c in block:

            # hc = str(hex(c).split("x")[-1])
            # if len(hc) < 2:
            #     hc = "0" * (2 - len(hc)) + hc
            # tmp = current + hc
            tmp = c
            messages.append(tmp)

        tasks = [OnceTime(msg) for msg in messages]
        await asyncio.gather(*tasks)
        print(block[0])
    # for result in results:
    #     print(result)


if __name__ == "__main__":
    asyncio.run(main())
