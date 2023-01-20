"""THIS MODULE CREATES DISPLAY OUTPUT OF OPERATIONS WHICH ARE DONE IN THE BACKEND"""


from tkinter import *

class displayConfig:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Aboba")
        self.root.geometry("1600x400")
        self.root['background']='#000'

        self.mnemTxt = StringVar()
        self.seedTxt = StringVar()
        self.addrTxt = StringVar()
        self.publTxt = StringVar()
        self.privTxt = StringVar()
        self.countAttempts = StringVar()


        self.lblMnemonic = Label(self.root, bg = '#000', fg = '#4AF626', font = 'consolas', textvariable=self.mnemTxt)
        self.lblSeed = Label(self.root, bg = '#000', fg = '#4AF626', font = 'consolas', textvariable=self.seedTxt)
        self.lblAddress = Label(self.root, bg = '#000', fg = '#4AF626', font = 'consolas', textvariable=self.addrTxt)
        self.lblPublicKey = Label(self.root, bg = '#000', fg = '#4AF626', font = 'consolas', textvariable=self.publTxt)
        self.lblPrivateKey = Label(self.root, bg = '#000', fg = '#4AF626', font = 'consolas', textvariable=self.privTxt)

        self.lblCount = Label(self.root, bg = '#000', fg = '#4AF626', font = 'consolas', textvariable=self.countAttempts)

        self.lblMnemonic.place(x=10, y = 0)
        self.lblSeed.place(x=10, y = 20)
        self.lblAddress.place(x=10, y = 40)
        self.lblPublicKey.place(x=10, y = 60)
        self.lblPrivateKey.place(x=10, y = 80)

        self.lblCount.place(x=10, y = 120)

    def update(self, globMnemonic, globSeed, globAdress, globPubKey, globPrivKey, count) -> None:
        self.mnemTxt.set("Mnemonic: " + str(globMnemonic))
        self.seedTxt.set("Seed: " + str(globSeed))
        self.addrTxt.set("Address: " + str(globAdress))
        self.publTxt.set("PublicKey: " + str(globPubKey))
        self.privTxt.set("PrivateKey: " + str(globPrivKey))
        self.countAttempts.set("Attempts: " + str(count))


        
        self.lblMnemonic.config(textvariable=self.mnemTxt)
        self.lblSeed.config(textvariable=self.seedTxt)
        self.lblAddress.config(textvariable=self.addrTxt)
        self.lblPublicKey.config(textvariable=self.publTxt)
        self.lblPrivateKey.config(textvariable=self.privTxt)

        self.lblCount.config(textvariable=self.countAttempts)

        self.root.after(1)
        self.root.update()