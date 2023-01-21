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

# Open the JPG image file
aicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\MedTrackAppIcon.png").resize((70, 70), Image.LANCZOS)
# Create a PhotoImage object from the JPG image
appicon = ImageTk.PhotoImage(aicon)

sicon = PhotoImage(file = r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\ScanIcon.png")
scanicon = sicon.subsample(3, 3)

#Create the functions



#Create the widgets and add functionality

appiconimg = Label(root, image = appicon)
title = Label(root, text = "Welcome to\rMedTrack!", font = ('Berlin Sans FB Demi', 30, 'bold'), fg = '#ff4d00', bg = 'white')
hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', image = scanicon, compound = BOTTOM)
hib = Button(root, text = 'Information Library', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', image = scanicon, compound = BOTTOM)
hcb = Button(root, text = 'Chatbot', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', image = scanicon, compound = BOTTOM)
hmb = Button(root, text = 'Medicines', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', image = scanicon, compound = BOTTOM)

appiconimg.grid(row = 0, column = 0, sticky = 'w')
title.grid(row = 0, column = 1, sticky = 'w')
hsb.grid(row = 1, column = 0, sticky = 'w', pady = 20)
hib.grid(row = 1, column = 1, sticky = 'w', padx = 10, pady = 20)
hcb.grid(row = 1, column = 2, sticky = 'w', padx = 10, pady = 20)
hmb.grid(row = 1, column = 3, sticky = 'w', padx = 10, pady = 20)
mainloop()

