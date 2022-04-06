import tkinter as tk

number = 0
comp_turn = False

class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def quit(self):
        self.destroy()

    def increase_number(self, input_num):
        global number
        number += input_num
        self.check_end()

    def check_end(self):
        global number
        global comp_turn
        if number >= 31:
            self.switch_frame(WinnerPage)
        else:
            print(number)
            comp_turn = not comp_turn
            if comp_turn:
                self.compTurn()
            else:
                self.switch_frame(UserPlayPage)

    def checkEnd(self):     # checkEnd for minimax algorithm to return True or False
        global number
        if number >= 31:
            return True
        return False


    def minimax(self):
        global number
        score = 100
        increase_number = 0

        for i in range(1,4):
            number += i

            temp = self.maxSearch()

            if temp < score:
                score = temp
                increase_number = i

            number -= i

        return increase_number


    def maxSearch(self):
        global number
        global comp_turn
        if self.checkEnd() and comp_turn == True:
            # computer lose
            return 10
        elif self.checkEnd() and comp_turn == False:
            # computer win
            return -10
        elif number % 4 == 2 and comp_turn == True:
            return -5
        elif number % 4 == 2 and comp_turn == False:
            return 5

        score = -100

        for i in range(1,4):
            comp_turn = not comp_turn
            number += i

            score = max(score, self.minSearch())

            comp_turn = not comp_turn
            number -= i

        return score


    def minSearch(self):
        global number
        global comp_turn
        if self.checkEnd() and comp_turn == True:
            # computer lose
            return 10
        elif self.checkEnd() and comp_turn == False:
            # computer win
            return -10
        elif number % 4 == 2 and comp_turn == True:
            return -5
        elif number % 4 == 2 and comp_turn == False:
            return 5

        score = 100


        for i in range(1,4):
            comp_turn = not comp_turn
            number += i

            score = min(score, self.maxSearch())

            comp_turn = not comp_turn
            number -= i

        return score


    def compTurn(self):
        global number
        self.switch_frame(CompPlayPage)
        number += self.minimax()


    def setCompFirst(self):
        global comp_turn
        comp_turn = True
        self.compTurn()

    
            

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Baskin Robbins 31", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self, text="New Game?", font=("Helvetica", 12)).pack()
        tk.Button(self, text="Yes", command=lambda: master.switch_frame(SetPage)).pack()
        tk.Button(self, text="No", command=lambda: master.switch_frame(EndPage)).pack()

class SetPage(tk.Frame):
    def __init__(self, master):
        global number
        global comp_turn
        number = 0
        comp_turn = False
        tk.Frame.__init__(self, master)
        tk.Label(self, text="\nWho's gonna be the first player?\n", font=("Helvetica", 12)).pack()
        tk.Button(self, text="User", command=lambda: master.switch_frame(UserPlayPage)).pack()
        tk.Button(self, text="Computer", command=lambda: master.setCompFirst()).pack()

class UserPlayPage(tk.Frame):
    def __init__(self, master):
        global number
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Current Number: " + str(number), font=("Helvetica", 12, "bold")).pack()
        tk.Label(self, text="User's Turn! \nClick one of the button below.", font=("Helvetica", 10)).pack()
        tk.Button(self, text="1", command=lambda: master.increase_number(1)).pack()
        tk.Button(self, text="2", command=lambda: master.increase_number(2)).pack()
        tk.Button(self, text="3", command=lambda: master.increase_number(3)).pack()

class CompPlayPage(tk.Frame):
    def __init__(self, master):
        global number
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Current Number: " + str(number), font=("Helvetica", 12, "bold")).pack()
        tk.Label(self, text="Computer's Turn! \nClick 'Next turn' button to have your turn :)", font=("Helvetica", 10)).pack()
        tk.Button(self, text="Next turn->", command=lambda: master.check_end()).pack()

class WinnerPage(tk.Frame):
    def __init__(self, master):
        global comp_turn
        tk.Frame.__init__(self, master)
        if comp_turn == True:
            tk.Label(self, text="The Winner is User !", font=("Helvetica", 15, "bold")).pack()
        else:
            tk.Label(self, text="The Winner is Computer !", font=("Helvetica", 15, "bold")).pack()
        tk.Label(self, text="New Game?", font=("Helvetica", 12)).pack()
        tk.Button(self, text="Yes", command=lambda: master.switch_frame(SetPage)).pack()
        tk.Button(self, text="No", command=lambda: master.switch_frame(EndPage)).pack()

class EndPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="\nSee you again :)\n", font=("Helvetica", 12, "bold")).pack()
        tk.Button(self, text="close window", command=lambda: master.quit()).pack()

if __name__ == "__main__":
    game = Game()
    game.geometry("400x150")
    game.mainloop()
