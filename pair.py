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