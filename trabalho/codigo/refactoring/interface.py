from Tkinter import *

import cellular_automata

class Interface(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        
        self.parent = parent
        
        self.points = 5        
        self.pause = True
        self.t = 0
        self.ca = cellular_automata.CellularAutomata()
        
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

        self.canvas  = Canvas(
            self.parent,
            width=self.ca.lattice_size*self.points,
            height=self.ca.lattice_size*self.points,
            highlightthickness=0, 
            bd=0,
            bg='white'
        )

        self.cell = [
            [0 for y in range(self.ca.lattice_size)] 
               for x in range(self.ca.lattice_size)]

        for i in range(self.ca.lattice_size):
            for j in range(self.ca.lattice_size):
                self.cell[i][j] = self.canvas.create_rectangle(
                    (i*self.points, j*self.points, i*self.points+self.points, j*self.points+self.points),outline="gray",fill="white"
                )

        toolbar.pack(side=TOP, fill=X)
        self.canvas.pack(side=TOP)
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

        if self.t == 0:        
            self.ca.population, self.ca.lattice, self.ca.life_time, self.ca.genetic_code = self.ca.generate_population(0)

        self.t += 1

    def drawing(self):
        for i in range(self.ca.lattice_size):
            for j in range(self.ca.lattice_size):
                if self.ca.lattice[i][j] == 1:
                    self.canvas.itemconfig(self.cell[j][i], fill="yellow")

def main():
  
    root = Tk()
    app = Interface(root)    
    root.mainloop()  


if __name__ == '__main__':
    main()  
