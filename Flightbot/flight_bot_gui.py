import os
import Tkinter
import signal
import tkFont

top = Tkinter.Tk()

def OnSeatOneButtonClick():
    os.system("python seat_one_position.py")
def OnSeatTwoButtonClick():
    os.system("python seat_two_position.py")
def OnSeatThreeButtonClick():
    os.system("python seat_three_position.py")
def OnSeatFourButtonClick():
    os.system("python seat_four_position.py")
def OnSeatFiveButtonClick():
    os.system("python seat_five_position.py")
def OnSeatSixButtonClick():
    os.system("python seat_six_position.py")
def OnSeatSevenButtonClick():
    os.system("python seat_seven_position.py")
def OnSeatEightButtonClick():
    os.system("python seat_eight_position.py")
def OnSeatNineButtonClick():
    os.system("python seat_nine_position.py")
def OnSeatTenButtonClick():
    os.system("python seat_ten_position.py")
def HomeButtonClick():
    os.system("python home_position.py")

helv20 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)

seatOneButton = Tkinter.Button(text=u"Seat 1", font=helv20, command=OnSeatOneButtonClick)
seatOneButton.grid(column=1, row=0)
seatOneButton.config(width = 25, height = 5)

seatTwoButton = Tkinter.Button(text=u"Seat 2", font=helv20, command=OnSeatTwoButtonClick)
seatTwoButton.grid(column=1, row=1)
seatTwoButton.config(width = 25, height = 5)

seatThreeButton = Tkinter.Button(text=u"Seat 3", font=helv20, command=OnSeatThreeButtonClick)
seatThreeButton.grid(column=1, row=2)
seatThreeButton.config(width = 25, height = 5)

seatFourButton = Tkinter.Button(text=u"Seat 4", font=helv20, command=OnSeatFourButtonClick)
seatFourButton.grid(column=1, row=3)
seatFourButton.config(width = 25, height = 5)

seatFiveButton = Tkinter.Button(text=u"Seat 5", font=helv20, command=OnSeatFiveButtonClick)
seatFiveButton.grid(column=1, row=4)
seatFiveButton.config(width = 25, height = 5)

seatSixButton = Tkinter.Button(text=u"Seat 6", font=helv20, command=OnSeatSixButtonClick)
seatSixButton.grid(column=2, row=0)
seatSixButton.config(width = 25, height = 5)

seatSevenButton = Tkinter.Button(text=u"Seat 7", font=helv20, command=OnSeatSevenButtonClick)
seatSevenButton.grid(column=2, row=1)
seatSevenButton.config(width = 25, height = 5)

seatEightButton = Tkinter.Button(text=u"Seat 8", font=helv20, command=OnSeatEightButtonClick)
seatEightButton.grid(column=2, row=2)
seatEightButton.config(width = 25, height = 5)

seatNineButton = Tkinter.Button(text=u"Seat 9", font=helv20, command=OnSeatNineButtonClick)
seatNineButton.grid(column=2, row=3)
seatNineButton.config(width = 25, height = 5)

seatTenButton = Tkinter.Button(text=u"Seat 10", font=helv20, command=OnSeatTenButtonClick)
seatTenButton.grid(column=2, row=4)
seatTenButton.config(width = 25, height = 5)

homeButton = Tkinter.Button(text=u"Home", font=helv20, command=HomeButtonClick)
homeButton.grid(column=3, row=0)
homeButton.config(width=25, height = 5)

top.mainloop()
