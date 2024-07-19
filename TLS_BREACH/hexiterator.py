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
iterator = HexIterator()
for block in iterator:
    print(block)
