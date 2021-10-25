
class Scanner:
    def __init__(self, problem):
        self.problem = problem
        self.line = []

    def __iter__(self):
        return self

    def detectNextToken(self):
        while not len(self.line):
            self.line = self.problem.readline()
            if not self.line:
                return 0
            self.line = self.line.split()
        return self.line.pop(0)

    def checkIfIdentifier(self, token):
        return

    def checkIfConstant(self, token):
        return

    def checkIfReservedWord(self, token):
        return

    def checkIfSepartor(self, token):
        return

    def checkIfOperator(self, token):
        return

    def classifyToken(self, currentToken):
        if self.checkIfSepartor(currentToken): return 0  # separator
        if self.checkIfOperator(currentToken): return 1  # operator
        if self.checkIfReservedWord(currentToken): return 2  # reserved-word
        if self.checkIfConstant(currentToken): return 3  # constant
        if self.checkIfIdentifier(currentToken): return 4  # identifier
        return 5  # lexical error

    def codifyToken(self):
        return
