from mimetypes import init
from multiprocessing import *
import walletFunctions
from display import displayConfig
import filework

globCount = 0


def createAndCheck(num : int, addrSet: set):
    global globCount
    globCount += 1
    phrase = walletFunctions.generatePhrase(num)
    walletData = walletFunctions.bip39(phrase)
    d.update(walletData[0], walletData[1], walletData[2], walletData[3], walletData[4], globCount)
    checkAddress(walletData, addrSet)

def whichKeys() -> list:
    chosen = []
    keys = ["16", "20", "24", "28", "32"]
    print("What keys you want to generate 16/20/24/28/32 (CHOOSE ONE BY ONE)")
    print("Write number of a key:")
    userKey = input()
    while not userKey in keys:
        print("Write correct number of a key:")
        userKey = input()
    keys.remove(userKey)
    chosen.append(int(userKey))
    print("Do you want more keys? Y/N:")
    answer = input()
    if answer == "N":
        return chosen
    elif answer == "Y":
        while not answer == "N":
            print("Write number of a key:")
            userKey = input()
            while not userKey in keys:
                print("Write correct number of a key:")
                userKey = input()
            keys.remove(userKey)
            chosen.append(int(userKey))
            print("Do you want more keys? Y/N:")
            answer = input()
    return chosen


def amountProcesses() -> int:
    print("Write amount of process u want to use:")
    print("(RECOMMENDED FROM 1 TO 4 TO NOT OVERLOAD COMPUTER)")
    while True:
        num = input()
        try:
            return int(num)
        except:
            print("Print a number")

def generation(keys: list, addrSet: set) -> None:
    while True:
        for i in keys:
            createAndCheck(int(i), addrSet)

def startProcesses(keys: list, addrSet : set):
    Process(target=generation, args=(keys, addrSet)).start()

        
def main() -> None:
    for i in range(processes):
        startProcesses(user_chosen_keys, address_set)


def checkAddress(data : tuple, addrSet: set):
    if data[2] in addrSet:
        filework.storeData(data[0], data[1], data[2], data[3], data[4])

if __name__ == '__main__':
    address_set = filework.loadAddresFromFile()
    user_chosen_keys = whichKeys()
    processes = amountProcesses()
    init(main())

d = displayConfig()