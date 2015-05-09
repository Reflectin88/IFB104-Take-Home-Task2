from Tkinter import Tk, Button

def enigma():
    conundrum['text'] = mystery['text']

puzzle = Tk()

conundrum = Button(puzzle, text = '???')
conundrum.pack()

mystery = Button(puzzle, text = '!!!', command = enigma)
mystery.pack()

puzzle.mainloop()