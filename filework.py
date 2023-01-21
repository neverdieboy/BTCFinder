"""THIS MODULE STORES DATA TO FILE/LOADS DATA/AND CHECKS THE NAME OF THE FILE INSERTED BY USER"""

def storeData(mnem : str, seedStr : str, addr : str, pubK : str, privK : str) -> None:
    f = open('walletData.txt', 'a')
    f.write("Mnemonic: " + mnem + '\n')
    f.write("Seed: " + seedStr + '\n')
    f.write("Address: " + addr + '\n')
    f.write("PublicKey: " + pubK + '\n')
    f.write("PrivateKey: " + privK + '\n' + '\n')
    f.write('\n')
    f.close()

def loadAddresFromFile() -> set:
    print("Type your adress file .txt name: ")
    fileName = input()
    while not checkType(fileName):
        print("Type your adress file .txt name: ")
        fileName = input()
    s = set(line.strip() for line in open(fileName))
    return s
    

def checkType(name : str) -> bool:
    l = name[-4:]
    return l == ".txt"




