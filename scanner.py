import re
from pair import Pair
from sortedTable import SortedTable


class Scanner:
    def __init__(self, inFile, outFile, reservedWordsFile):
        self.in_file = inFile
        self.symbolTable = SortedTable()
        self.line = []
        self.lineNumber = -1
        self.out_file = outFile
        f = open(reservedWordsFile, 'r')
        self.reserved_words = f.read().split()
        self.tokenNumber = -1
        self.prevToken = 0
        self.pif = []

    def __iter__(self):
        return self

    def getPif(self, token, index):
        pair = Pair(token)
        self.pif.append(pair)

    def detectNextToken(self):
        while not len(self.line):
            self.line = self.in_file.readline()
            if not self.line:
                return 0
            self.line = self.line.split()
            self.lineNumber += 1
            self.tokenNumber = -1
        self.tokenNumber += 1
        token = self.line.pop(0)
        return token


    def detectNextLine(self):
        while not len(self.line):
            self.line = self.in_file.readline()
            if not self.line:
                return 0
            self.line = self.line.split()
        return self.line

    def checkIfIdentifier(self, line):
        if line[0] == 'var' and line[2] == ';':
            return line[1]
        else:
            return False

    def checkIfConstant(self, line):
        if line[1] == '<=' and line[3] == ';':
            pattern = '^".*"$'
            result = re.match(pattern, line[2])
            if result:
                return True
            if "".join(line[2].lstrip("+").lstrip("-").split('.')).isdigit():
                return True
            return False
        return False

    def checkIfReservedWord(self, token):
        if token in self.reserved_words:
            return True
        else:
            return False

    def checkIfSepartor(self, token):
        if token in {';', '*', '{', '}'}:
            return True
        else:
            return False

    def checkIfOperator(self, token):
        if token in {'<=', '=', '>', '<', '+', '-', ':', '*'}:
            return True
        else:
            return False

    def classifyToken(self, currentToken):
        if self.checkIfSepartor(currentToken): return 0  # separator
        if self.checkIfReservedWord(currentToken): return 2  # reserved-word
        if self.checkIfOperator(currentToken): return 1  # operator
        if self.checkIfIdentifier(currentToken): return 4  # identifier
        if self.checkIfConstant(currentToken): return 3  # constant
        return 5  # lexical error

    def codifyToken(self, token):
        tokenPair = Pair(token)
        if self.symbolTable.checkIfElementExist(tokenPair) != -1:
            return 1

        with open("token1.in") as f:
            for line in f:
                splitedLine = line.split()
                if token == splitedLine[0]:
                    return int(splitedLine[1])

        # identifier
        if self.prevToken == 3:
            self.symbolTable.addPair(token)
            return 1

        if self.prevToken == 12 and "".join(token.lstrip("+").lstrip("-").split('.')).isdigit():
            return 2

        #constant
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()) or \
            (token.startswith("[[") and token.endswith("]]")) \
                or (token.startswith("'") and token.endswith("'")) \
            or (token.startswith("\"") and token.endswith("\"")):
            self.symbolTable.addPair(token)
            return 2
        return -1

    def determineCodification(self, code):
        if code == 1:
            return 'identifier'
        if code == 2:
            return 'constant'
        if 3 <= code <= 12:
            return 'reserved-word'
        if 13 <= code <= 20:
            return 'operator'
        if 21 <= code <= 23:
            return 'separator'
        return 'lexical error'

    def writeInFile(self):
        f = open(self.out_file, 'w')
        currentToken = self.detectNextToken()
        while currentToken:
            f.write(currentToken + '\n')
            currentToken = self.detectNextToken()

        f.close()
