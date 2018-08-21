import os
import Tkinter
import signal
import tkFont

top = Tkinter.Tk()


def OnHomeButtonClick():
    os.system("python home_position.py")
def OnKitchenButtonClick():
    os.system("python kitchen_position.py")
def OnDiningButtonClick():
    os.system("python dining_position.py")
def OnFollowButtonAClick():
    os.system("ssh ubuntu@10.14.195.17")
def OnFollowButtonBClick():
    os.system("autonomous")
def OnFollowButtonCClick():
    os.system("cd Desktop")
def OnFollowButtonDClick():
    os.system("./a.out")
def OnUnFollowButtonClick():
    os.system("signal.SIGINT")

helv20 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
homeButton = Tkinter.Button(text=u"HOME", font=helv20, command=OnHomeButtonClick)
homeButton.grid(column=1, row=0)
homeButton.config(width = 25, height =5)

kitchenButton = Tkinter.Button(text=u"KITCHEN", font=helv20, command=OnKitchenButtonClick)
kitchenButton.grid(column=1, row=1)
kitchenButton.config(width = 25, height = 5)

diningButton = Tkinter.Button(text=u"DINING", font=helv20, command=OnDiningButtonClick)
diningButton.grid(column=1, row=2)
diningButton.config(width = 25, height = 5)

followButtonD = Tkinter.Button(text=u"FOLLOW", font=helv20, command=OnFollowButtonDClick)
followButtonD.grid(column=1, row=3)
followButtonD.config(width = 25, height = 5)

unFollowButton = Tkinter.Button(text=u"UNFOLLOW", font=helv20, command=OnUnFollowButtonClick)
unFollowButton.grid(column=1, row=4)
unFollowButton.config(width = 25, height = 5)


top.mainloop()
