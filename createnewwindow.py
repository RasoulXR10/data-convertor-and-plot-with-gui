import tkinter as Tk
from Interface import App
########################################################################


class MyApp(object):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        self.entry = Tk.Entry(parent)
        self.entry.insert(0, "Enter Password")
        self.entry.pack()
        btn = Tk.Button(self.frame, text="Login",
                        command=self.openFrame)
        btn.pack()

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        if self.entry.get() == "password":

            self.hide()
            app = App()
            # def handler(): return self.onCloseOtherFrame(otherFrame)
            # btn = Tk.Button(otherFrame, text="Close", command=handler)
            # btn.pack()

    # ----------------------------------------------------------------------

    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("200x200")
    app = MyApp(root)
    root.mainloop()
