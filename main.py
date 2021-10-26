from scanner import Scanner
from pair import Pair

if __name__ == '__main__':
    myScanner = Scanner(open("p1.txt"), 'out.txt', 'reservedWords.txt')
    currentToken = myScanner.detectNextToken()
    error = 0
    while currentToken:
        tokenClassified = myScanner.determineCodification(myScanner.codifyToken(currentToken))
        if tokenClassified == 'lexical error':
            print("LEXICAL ERROR AT LINE " + str(myScanner.lineNumber) + ' TOKEN ' + str(myScanner.tokenNumber))
            error = 1
        if tokenClassified == 'reserved-word' or tokenClassified == 'operator' or tokenClassified == 'separator':
            myScanner.getPif(currentToken, 0)
        else:
            if tokenClassified == 'identifier' or tokenClassified == 'constant':
                pair = Pair(currentToken)
                myScanner.getPif(currentToken, myScanner.symbolTable.checkIfElementExist(pair))
        myScanner.prevToken = myScanner.codifyToken(currentToken)
        currentToken = myScanner.detectNextToken()

    f = open("ST.out", "w")
    for element in myScanner.symbolTable.getList():
        f.write(element.getKey() + ' ' + str(myScanner.symbolTable.checkIfElementExist(element)) + '\n')
    f.close()

    f = open("PIF.out", "w")
    for el in myScanner.pif:
        f.write(el.getKey() + ' ' + str(el.getValue()) + '\n')
    f.close()

    if not error:
        print("corect lexical")
