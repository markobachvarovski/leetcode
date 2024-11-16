class Logger:

    def __init__(self):
        self.cache = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cache or timestamp - self.cache[message] >= 10:
            self.cache[message] = timestamp
            return True

        return False


if __name__ == '__main__':

    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))
    print(logger.shouldPrintMessage(2, "bar"))
    print(logger.shouldPrintMessage(3, "foo"))
    print(logger.shouldPrintMessage(8, "bar"))
    print(logger.shouldPrintMessage(10, "foo"))
    print(logger.shouldPrintMessage(11, "foo"))
