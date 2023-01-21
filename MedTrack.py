from tkinter import *
#from tkinter.ttk import *
import cv2
import pytesseract
import webview

#create the tkinter window

root = Tk()
root.configure(bg = 'white')
root.state('zoomed')

#Load the images

aicon = PhotoImage(file = r"C:\Users\tinao\OneDrive\Desktop\MedTrack\Images\MedTrackAppIcon.png")
appicon = aicon.subsample(2, 2)
sicon = PhotoImage(file = r"C:\Users\tinao\OneDrive\Desktop\MedTrack\Images\ScanIcon.png")
scanicon = sicon.subsample(3, 3)

#Create the functions



#Create the widgets and add functionality

title = Label(root, text = "Welcome to MedTrack!", font = ('Berlin Sans FB Demi', 30, 'bold'), fg = '#ff4d00', bg = 'white')
hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', image = scanicon, compound = BOTTOM)

title.grid(row = 0, column = 0)
hsb.grid(row = 1, column = 0)
mainloop()

