#!./venv/bin/python

class PowersOfTwo:
    def __init__(self, iterations):
        self._index = 0
        self._last = 1
        self._iterations = iterations

    def __iter__(self):
        self_index = 0
        self._last = 1

        return self

    def __next__(self):
        self._index += 1

        if self._index > self._iterations:
            raise StopIteration

        result = self._last
        self._last *= 2

        return self._index - 1, result


def main():
    for index, x in PowersOfTwo(10):
        print(index, x)

if __name__ == "__main__":  
    main()
