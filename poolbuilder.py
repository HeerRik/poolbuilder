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
        self.parent.iconbitmap("assets/pythonio.ico")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        self.loadChampions()
        champions = self.loadChampions()
        self.buildMode = True

        self.champsLabel = Label(text="Champions")
        self.champBox = Listbox(self)
        self.champBoxScrollbar = Scrollbar(self.champBox, orient=VERTICAL)
        self.champBox.config(yscrollcommand=self.champBoxScrollbar.set)
        self.champBoxScrollbar.config(command=self.champBox.yview)

        self.addButton = Button(self, text=">>", command=self.addChampToPool)
        self.removeButton = Button(self, text="<<", command=self.removeChampFromPool)
        self.saveButton = Button(self, text="Save champion pool", width=18, command=self.saveChampPool)
        self.loadButton = Button(self, text="Load champion pool", width=18, command=lambda: self.loadChampPools(1))

        self.poolLabel = Label(text="Champion Pool")
        self.poolBox = Listbox(self)
        self.poolBoxScrollbar = Scrollbar(self.poolBox, orient=VERTICAL)
        self.poolBox.config(yscrollcommand=self.poolBoxScrollbar.set)
        self.poolBoxScrollbar.config(command=self.poolBox.yview)
        self.poolBox.bind("<<ListBoxSelect>>", self.choosePool)

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
        file = open('assets/Champions.txt', 'r')
        champions = file.readlines()
        file.close()
        return champions

    def choosePool(self):
        if self.buildMode:
            print "oops"
        else:
            print "pls work now"
            self.loadChampPools(2)

    def loadChampPools(self, level):
        if level == 1:
            self.buildMode = False
            self.champBox.delete(0, END)
            file = open('assets/champpools.txt', 'r')
            champPools = file.readlines()
            self.saveButton.config(state=DISABLED)
            self.loadButton.config(state=DISABLED)
            for pool in champPools:
                self.poolBox.insert(END, pool)
            file.close()
        elif level == 2:
            print "level 2"
            self.poolBox.delete(0, END)
        else:
            print "level null"

    def addChampToPool(self):
        idx = self.champBox.curselection()
        if idx and self.buildMode:
            name = self.champBox.get(idx)
            self.poolBox.insert(END, name)
            self.champBox.delete(idx)

    def removeChampFromPool(self):
        idx = self.poolBox.curselection()
        if idx and self.buildMode:
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
