from Tkinter import *

class Interface(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        
        self.parent = parent
        
        self.pause = True
        self.t = 0
        
        self.initUI()
    
    def initUI(self):
    
        self.parent.title("Cellular Automata")

        toolbar = Frame(self.parent, bd=1, relief=RAISED)

        button1 = Button(
            toolbar, text='Play', 
            command=lambda b='play': self.serviceToolbar(b)
        )
        button2 = Button(
            toolbar, text='Pause', 
            command=lambda b='pause': self.serviceToolbar(b)
        )
        button3 = Button(
            toolbar, text='Stop', 
            command=lambda b='stop': self.serviceToolbar(b)
        )
        button4 = Button(
            toolbar, text='Next', 
            command=lambda b='next': self.serviceToolbar(b)
        )

        button3.pack(side=LEFT, padx=2, pady=2)
        button1.pack(side=LEFT, padx=2, pady=2)
        button2.pack(side=LEFT, padx=2, pady=2)
        button4.pack(side=LEFT, padx=2, pady=2)

        exitButton = Button(toolbar, text='Quit', command=self.quit)
        exitButton.pack(side=RIGHT, padx=2, pady=2)

        N = 100
        XY = 5

        canvas  = Canvas(
            self.parent, width=N*XY, height=N*XY, highlightthickness=0, 
            bd=0, bg='white'
        )

        cell = [[0 for row in range(N)] for col in range(N)]

        for j in range(N):
            for i in range(N):
                cell[i][j] = canvas.create_rectangle(
                    (i*XY, j*XY, i*XY+XY, j*XY+XY),outline="gray",fill="white"
                )

        toolbar.pack(side=TOP, fill=X)
        canvas.pack(side=TOP)
        self.pack()

    def serviceToolbar(self, button):
        if button == 'play':
            self.pause = False
            self.onPlay()
        if button == 'pause':
            self.pause = True
        if button == 'stop':
            self.pause = True
            self.t = 0
        if button == 'next':
            self.pause = True
            self.onNext()

    def onExit(self):
        self.quit()

    def onPlay(self):
        if not self.pause:
            print ('play', self.t)
            self.t += 1
            self.after(100, self.onPlay)

    def onNext(self):
        print ('next', self.t)
        self.t += 1

def main():
  
    root = Tk()
    app = Interface(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
