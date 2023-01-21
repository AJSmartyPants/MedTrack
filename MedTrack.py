from tkinter import *
from PIL import Image, ImageTk
import cv2
import pytesseract
import webview

#create the tkinter window

root = Tk()
root.configure(bg = 'white')
root.state('zoomed')

#Load the images

aicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\MedTrackAppIcon.png").resize((70, 70), Image.LANCZOS)
appicon = ImageTk.PhotoImage(aicon)

sicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\ScanIcon.png").resize((150, 150), Image.LANCZOS)
scanicon = ImageTk.PhotoImage(sicon)

iicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\InfoLibIcon.png").resize((150, 150), Image.LANCZOS)
infoicon = ImageTk.PhotoImage(iicon)

cicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\ChatIcon.png").resize((150, 150), Image.LANCZOS)
chaticon = ImageTk.PhotoImage(cicon)

micon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\MedIcon.png").resize((150, 150), Image.LANCZOS)
medicon = ImageTk.PhotoImage(micon)

#Create the functions



#Create the widgets and add functionality

appiconimg = Label(root, image = appicon)
title = Label(root, text = "Welcome to\rMedTrack!", font = ('Berlin Sans FB Demi', 30, 'bold'), fg = '#ff4d00', bg = 'white')
hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = scanicon, compound = BOTTOM)
hib = Button(root, text = 'Information Library', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = infoicon, compound = BOTTOM)
hcb = Button(root, text = 'Chatbot', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = chaticon, compound = BOTTOM)
hmb = Button(root, text = 'Medicines', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = medicon, compound = BOTTOM)

appiconimg.grid(row = 0, column = 0, sticky = 'w')
title.grid(row = 0, column = 1, sticky = 'w')
hsb.grid(row = 1, column = 0, sticky = 'w', pady = 20)
hib.grid(row = 1, column = 1, sticky = 'w', padx = 10, pady = 20)
hcb.grid(row = 1, column = 2, sticky = 'w', padx = 10, pady = 20)
hmb.grid(row = 1, column = 3, sticky = 'w', padx = 10, pady = 20)
mainloop()

