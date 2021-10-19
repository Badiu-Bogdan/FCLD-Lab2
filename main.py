class Pair:
    def __init__(self, key):
        self.value = 0
        self.key = key

    def getValue(self):
        return self.value

    def getKey(self):
        return self.key

    def setValue(self, newValue):
        self.value = newValue

    def setKey(self, newKey):
        self.key = newKey

    def __str__(self):
        return "Pair: Key={self.key}".format(self=self)


class SortedTable:
    def __init__(self):
        self.list = []

    def addPair(self, pair):
        # Here i should check if the key that I wanna add doesn't already exist in the list.
        for i in range(len(self.list)):
            if self.list[i].getKey() == pair.getKey():
                return
            if self.list[i].getKey() > pair.getKey():
                new_list = list[0:i]
                new_list.append(pair)
                new_list.append(self.list[i + i:len(self.list)])
                return
        self.list.append(pair)

    def checkIfElementExist(self, pair):
        for i in range(len(self.list)):
            if self.list[i].getValue() == pair.getValue():
                return i
            else:
                return -1

    def __str__(self):
        string = 'List is: \n'
        for i in range(len(self.list)):
            string = string + str(self.list[i]) + ' Pos:' + str(i) + '\n'

        return string

    # REturn positon !!!


def scanner():
    pass

if __name__ == '__main__':
    first = Pair('A')
    second = Pair('B')
    third = Pair('C')
    forth = Pair('C')
    listaSortata = SortedTable()
    listaSortata.addPair(first)
    listaSortata.addPair(second)
    listaSortata.addPair(third)
    listaSortata.addPair(forth)
    print(listaSortata)
    print('Hello World')
