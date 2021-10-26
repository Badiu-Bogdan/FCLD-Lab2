from pair import Pair

class SortedTable:
    def __init__(self):
        self.list = []

    def addPair(self, token):
        # Here i should check if the key that I wanna add doesn't already exist in the list.
        # If the key that I wanna add is already in the list it will return the position from the list
        # Or -1 otherwise
        pair = Pair(token)
        for i in range(len(self.list)):
            if self.list[i].getKey() == pair.getKey():
                return i
            if self.list[i].getKey() > pair.getKey():
                self.list.insert(i, pair)
                return i
        self.list.append(pair)

    def checkIfElementExist(self, pair):
        # Will return the pozition of the pair if it exists or -1 otherwise
        for i in range(len(self.list)):
            if self.list[i].getKey() == pair.getKey():
                return i
        return -1

    def __str__(self):
        string = 'List is: \n'
        for i in range(len(self.list)):
            string = string + str(self.list[i]) + ' Pos:' + str(i) + '\n'

        return string

    def getList(self):
        return self.list

    # REturn positon !!!
