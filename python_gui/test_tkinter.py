from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello world')
        self.helloLabel.pack()
        self.quitButton = Button(self, text = 'exit', command = self.quit)
        self.quitButton.pack()

if __name__ == '__main__':
    app = Application()
    app.master.title('Hello You')
    app.mainloop()