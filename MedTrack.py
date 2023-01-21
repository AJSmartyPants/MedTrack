from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import pytesseract
import webview
import tksheet

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

def chat():
    url = "https://console.dialogflow.com/api-client/demo/embedded/c4aa01ea-269e-448e-84d9-b3f537b01b85"
    webview.create_window('MedTrack Chatbot',url)
    webview.start()
def info():
    infoscreen = Tk()
    infoscreen.configure(bg = '#feffba')
    isdetails = Label(infoscreen, text = "This is the information library. Here, you can find home remedies for some common ailments. Do keep in mind that we only provide suggestions that are verified by medical experts, and if you are allergic to any remedies, please do not take them. In case the remedies cause any negative reactions in the body, immediately stop taking them and consult a doctor. If the remedies do not benefit you within 4-7 days, consult a doctor.", font = ('Britannic Bold', 20, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1300)
    isdetails.grid(row = 0, column = 0, sticky = 'w')
    info1 = Button(infoscreen, text = "Cough", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00', command = lambda: infohs(infoscreen, 1, "A cough is your body's way of responding when something irritates your throat or airways. An irritant stimulates nerves that send a message to your brain. The brain then tells muscles in your chest and abdomen to push air out of your lungs to force out the irritant. An occasional cough is normal and healthy. A cough that persists for several weeks or one that brings up discolored or bloody mucus may indicate a condition that needs medical attention. At times, coughing can be very forceful. Prolonged, vigorous coughing can irritate the lungs and cause even more coughing. It is also exhausting and can cause sleeplessness, dizziness or fainting, headaches, urinary incontinence, vomiting, and even broken ribs.", 100, 1200))
    info2 = Button(infoscreen, text = "Fever", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00')
    info3 = Button(infoscreen, text = "Cold", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00')
    info4 = Button(infoscreen, text = "Diarrhea", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00')
    info5 = Button(infoscreen, text = "Abnormal levels of dandruff", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00')
    info1.grid(row = 1, column = 0, sticky = 'w')
    info2.grid(row = 2, column = 0, sticky = 'w')
    info3.grid(row = 3, column = 0, sticky = 'w')
    info4.grid(row = 4, column = 0, sticky = 'w')
    info5.grid(row = 5, column = 0, sticky = 'w')
    infoscreen.mainloop()
global ispressed
ispressed = 'false'
def infohs(s, r, t, x, w):
    global tu
    tu = Label(s, text = t, font = ('Bahnschrift SemiBold', 16, 'normal'), fg = 'black', bg = '#feffba', wraplength = w, anchor = 'w')
    global ispressed
    #tu.grid(row = r, column = 0, padx = x, sticky = 'w')
    if ispressed == 'false':
        tu.grid(row = r, column = 0, padx = x, sticky = 'w')
        ispressed = 'true'
    elif ispressed == 'true':
        tu.destroy()
        ispressed = 'false'
    print(ispressed)

def scanscr():
    scs = Tk()
    scs.state('zoomed')
    scs.title('Scan')
    scanbn = Button(scs, text = "Scan", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00', command = lambda: scan(scs))
    scanbn.grid(row=0, column=0, padx=10, pady=10)
    scs.mainloop()
def scan(screen):
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        # Display the frame
        cv2.imshow("Camera", frame)
        #Check if the user pressed 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imwrite("object.jpg", frame)
            break
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    cv2.imshow("Picture Taken", frame)
    # Define the image variable that we will use to extract medicine info from
    img = frame
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contrast_gray = cv2.convertScaleAbs(grayimg, alpha=1.5, beta=0)
    cv2.imshow('Grayscale', contrast_gray)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(contrast_gray, lang = 'eng')
    print(text)
    baseURL = "https://www.google.co.in/search?q="
    URL = baseURL + text
    webview.create_window('Medicine Information Results',URL)
    webview.start()
    sheet = tksheet.Sheet(screen)
    sheet.grid()
    sheet.headers(['Medicine Name (scanned)', 'Expiry Date', 'Information'])
    sheet.set_sheet_data([[f"{ri+cj}" for cj in range(3)] for ri in range(1)])
    # table enable choices listed below:
    sheet.enable_bindings(("single_select",
                           "row_select",
                           "column_width_resize",
                           "arrowkeys",
                           "right_click_popup_menu",
                           "rc_select",
                           "rc_insert_row",
                           "rc_delete_row",
                           "copy",
                           "cut",
                           "paste",
                           "delete",
                           "undo",
                           "edit_cell"))
    sheet.set_all_column_widths(width = 200, only_set_if_too_small = False, redraw = True, recreate_selection_boxes = True)
    sheet.set_all_row_heights(height = 200, only_set_if_too_small = False, redraw = True, recreate_selection_boxes = True)
    #sheet.sheet_display_dimensions(total_rows = 2, total_columns = 3)
    sheet.set_cell_data(0, 0, value = text, set_copy = True, redraw = False)
    sheet.set_cell_data(0, 1, value = 'Enter your expiry date', set_copy = True, redraw = False)
    sheet.set_cell_data(0, 2, value = URL, set_copy = True, redraw = False)

#Create the widgets and add functionality
appiconimg = Label(root, image = appicon, bg = 'white')
abtbn = Button(root, text = 'About', bg = 'white', borderwidth = 0, image = abticon, compound = TOP)
insbn = Button(root, text = 'How to Use', bg = 'white', borderwidth = 0, image = insicon, compound = TOP)
donbn = Button(root, text = 'Donate', bg = 'white', borderwidth = 0, image = donicon, compound = TOP)
title = Label(root, text = "Welcome to\rMedTrack!", font = ('Berlin Sans FB Demi', 30, 'bold'), fg = '#ff4d00', bg = 'white')
hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = scanicon, compound = BOTTOM, command = scanscr)
hib = Button(root, text = 'Information Library', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = infoicon, compound = BOTTOM, command = info)
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

