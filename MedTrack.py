from tkinter import *
from PIL import Image, ImageTk
import cv2
import pytesseract
import webview

#create the tkinter window

root = Tk()
root.configure(bg = 'white')
root.state('zoomed')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.resizable(0,0)

#Load the images

aicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\MedTrackAppIcon.png").resize((100, 100), Image.LANCZOS)
appicon = ImageTk.PhotoImage(aicon)

sicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\ScanIcon.png").resize((150, 150), Image.LANCZOS)
scanicon = ImageTk.PhotoImage(sicon)

iicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\InfoLibIcon.png").resize((150, 150), Image.LANCZOS)
infoicon = ImageTk.PhotoImage(iicon)

cicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\ChatIcon.png").resize((150, 150), Image.LANCZOS)
chaticon = ImageTk.PhotoImage(cicon)

micon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\MedIcon.png").resize((150, 150), Image.LANCZOS)
medicon = ImageTk.PhotoImage(micon)

abicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\AboutIcon.png").resize((60, 60), Image.LANCZOS)
abticon = ImageTk.PhotoImage(abicon)

inicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\InstructionsIcon.png").resize((60, 60), Image.LANCZOS)
insicon = ImageTk.PhotoImage(inicon)

dicon = Image.open(r"C:\Users\tinao\OneDrive\Desktop\MedTrack\MedTrackGithub\Images\DonationIcon.png").resize((60, 60), Image.LANCZOS)
donicon = ImageTk.PhotoImage(dicon)

#Create the functions

def scan():
    print('hello')

def chat():
    url = "https://console.dialogflow.com/api-client/demo/embedded/c4aa01ea-269e-448e-84d9-b3f537b01b85"
    webview.create_window('MedTrack Chatbot',url)
    webview.start()

#Create the widgets and add functionality
appiconimg = Label(root, image = appicon, bg = 'white')
abtbn = Button(root, text = 'About', bg = 'white', borderwidth = 0, image = abticon, compound = TOP)
insbn = Button(root, text = 'How to Use', bg = 'white', borderwidth = 0, image = insicon, compound = TOP)
donbn = Button(root, text = 'Donate', bg = 'white', borderwidth = 0, image = donicon, compound = TOP)
title = Label(root, text = "Welcome to\rMedTrack!", font = ('Berlin Sans FB Demi', 30, 'bold'), fg = '#ff4d00', bg = 'white')
hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = scanicon, compound = BOTTOM)
hib = Button(root, text = 'Information Library', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = infoicon, compound = BOTTOM)
hcb = Button(root, text = 'Chatbot', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = chaticon, compound = BOTTOM, command = chat)
hmb = Button(root, text = 'Medicines', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = medicon, compound = BOTTOM)

appiconimg.grid(row = 0, column = 0, sticky = 'w')
title.grid(row = 0, column = 1, sticky = 'w')
abtbn.grid(row = 0, column = 2, sticky = 'w')
insbn.grid(row = 0, column = 3, sticky = 'w')
donbn.grid(row = 0, column = 4, sticky = 'w')
hsb.grid(row = 1, column = 0, sticky = 'w', pady = 20)
hib.grid(row = 1, column = 1, sticky = 'w', padx = 10, pady = 20)
hcb.grid(row = 1, column = 2, sticky = 'w', padx = 10, pady = 20)
hmb.grid(row = 1, column = 3, sticky = 'w', padx = 10, pady = 20)
mainloop()

