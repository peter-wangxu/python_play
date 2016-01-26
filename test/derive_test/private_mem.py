class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


it = [1, 2, 3]
it1 = [4, 5, 6]
m = Mapping(it)

m.update(it1)
m1 = MappingSubclass(it)

m1.update([55, 11], [66, 22])