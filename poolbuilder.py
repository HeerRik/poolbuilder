from ttk import Frame, Label, Button, Style
from Tkinter import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Champion Pool Builder")
        self.parent.iconbitmap("c:\Python27\DLLs\pythonio.ico")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        self.loadChampions()
        champions = self.loadChampions()

        self.champsLabel = Label(text="Champions")
        self.champBox = Listbox(self)
        self.champBoxScrollbar = Scrollbar(self.champBox, orient=VERTICAL)
        self.champBox.config(yscrollcommand=self.champBoxScrollbar.set)
        self.champBoxScrollbar.config(command=self.champBox.yview)

        self.addButton = Button(self, text=">>", command=self.addChampToPool)
        self.removeButton = Button(self, text="<<", command=self.removeChampFromPool)
        self.saveButton = Button(self, text="Save champion pool", width=18, command=self.saveChampPool)
        self.loadButton = Button(self, text="Load champion pool", width=18, command=self.loadChampPools)

        self.poolLabel = Label(text="Champion Pool")
        self.poolBox = Listbox(self)
        self.poolBoxScrollbar = Scrollbar(self.poolBox, orient=VERTICAL)
        self.poolBox.config(yscrollcommand=self.poolBoxScrollbar.set)
        self.poolBoxScrollbar.config(command=self.poolBox.yview)

        for champion in sorted(champions):
            self.champBox.insert(END, champion)

        self.champsLabel.place(x=5, y=5)
        self.champBox.place(x=5, y=30)

        self.addButton.place(x=150, y=60)
        self.removeButton.place(x=150, y=100)
        self.saveButton.place(x=350, y=30)
        self.loadButton.place(x=350, y=60)

        self.poolLabel.place(x=200, y=5)
        self.poolBox.place(x=200, y=30)

        self.champBox.focus_set()

    def centerWindow(self):
        w = 500
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def loadChampions(self):
        file = open('Champions.txt', 'r')
        champions = file.readlines()
        file.close()
        return champions

    def loadChampPools(self):
        file = open('champpools.txt', 'r')
        champPools = file.readlines()
        champPoolFile = champPools[0]
        file.close()
        file = open(champPoolFile, 'r')
        champPool = file.readlines()
        print champPool
        file.close()

    def addChampToPool(self):
        idx = self.champBox.curselection()
        if idx:
            name = self.champBox.get(idx)
            self.poolBox.insert(END, name)
            self.champBox.delete(idx)

    def removeChampFromPool(self):
        idx = self.poolBox.curselection()
        if idx:
            name = self.poolBox.get(idx)
            self.champBox.insert(END, name)
            self.poolBox.delete(idx)

    def saveChampPool(self):
        championPool = self.poolBox.get(0, END)
        for champion in championPool:
            print champion

def main():
    root = Tk()
    root.resizable(0,0)
    ex = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
