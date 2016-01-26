class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()

for n in Fab(5):
    print n


def fab(max):
    a = 0
    b = 1
    i = 0
    while i < max:
        yield b
        a, b = b, a + b
        i += 1

it = fab(5)

for i in it:
    print i

