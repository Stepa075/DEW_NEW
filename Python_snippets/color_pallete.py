from tkinter import Tk, Frame, Button, BOTH, SUNKEN, Label, Entry, END
from tkinter import colorchooser


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Цветовая палитра")
        self.pack(fill=BOTH, expand=1)

        self.btn = Button(self, text="Выберите цвет", command=self.onChoose)
        self.btn.place(x=20, y=30)
        self.lbl = Entry(self, text="", width=15)
        self.lbl.place(x=20, y=60)
        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)

    def onChoose(self):
        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)
        # self.lbl["text"] = hx
        self.lbl.delete(0, END)
        self.lbl.insert(0, hx)


def main():
    root = Tk()
    ex = Example()
    root.geometry("300x150+300+300")

    root.mainloop()


if __name__ == '__main__':
    main()