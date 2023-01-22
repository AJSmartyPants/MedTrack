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
    
    infotext = Label(infoscreen, text = "Cough: A cough is your body's way of responding when something irritates your throat or airways. An irritant stimulates nerves that send a message to your brain. The brain then tells muscles in your chest and abdomen to push air out of your lungs to force out the irritant. An occasional cough is normal and healthy. A cough that persists for several weeks or one that brings up discolored or bloody mucus may indicate a condition that needs medical attention. At times, coughing can be very forceful. Prolonged, vigorous coughing can irritate the lungs and cause even more coughing. It is also exhausting and can cause sleeplessness, dizziness or fainting, headaches, urinary incontinence, vomiting, and even broken ribs. Age 6 months to 1 year. Give warm clear fluids (such as apple juice or lemonade). Dose: 1-2 teaspoons (5-10 mL) four times per day when coughing. Under 3 months, see your child's doctor. Caution: Do not use honey until 1 year old. Age 1 year and older. Use Honey ½ to 1 teaspoon (2 to 5 mL) as needed. It thins the secretions and loosens the cough. If you don't have honey, you can use corn syrup. Research shows that honey works better than cough syrups to reduce nighttime coughing. Can also offer warm lemonade or herbal teas. Amount: a few ounces (30 mL) each time. Age 6 years and older. Use Cough Drops to decrease the tickle in the throat. If you don't have any, you can use hard candy. Avoid cough drops before 6 years. Reason: risk of choking. Coughing fits. The warm mist from a shower can help. See a doctor immediately if you: Are choking and can't speak, Have difficulty breathing, Find it hard to swallow, Notice blood in your phlegm, Have persistent night sweats, fever and weight loss. Here are some other things that can help with a cough: Honey, Ginger, Hot fluids, Steam, Marshmallow root, Saltwater gargle, Bromelain, and Thyme.", 
                     font = ('Bahnschrift SemiBold', 15, 'bold'), fg = '#ae00FF', bg = '#feffba', wraplength = 1250, justify = LEFT)#, command = lambda: infohs(infoscreen, 1,  100, 1200))
    infotext2 = Label(infoscreen, text = "Runny nose: A runny nose can be caused by anything that irritates or inflames the nasal tissues. Infections — such as the common cold and influenza — allergies and various irritants may all cause a runny nose. It is excess drainage, ranging from a clear fluid to thick mucus, from the nose and nasal passages. Drinking plenty of water and using a humidifier may help to relieve symptoms. If the runny nose is caused by allergies, taking a non-sedating antihistamine may also help. See a doctor if you: Experience symptoms that last more than 10 days, Develop a high fever, Have green nasal discharge along with pain or fever, Also have asthma or emphysema or take immune-suppressing medications, and/or Notice blood in your nasal discharge or a persistent clear discharge after a head injury. Here are some other things that can help with a runny nose: Hot teas, Facial steam, Hot shower, Neti pot, Nasal spray, and Warm compress.", 
                     font = ('Bahnschrift SemiBold', 15, 'bold'), fg = '#8a00FF', bg = '#feffba', wraplength = 1250, justify = LEFT)#, command = lambda: infohs(infoscreen, 1,  100, 1200))
    infotext3 = Label(infoscreen, text = "Diarrhea: Loose, watery stools that occur more frequently than usual. Diarrhea is usually caused by a virus, or sometimes, contaminated food. Less frequently, it can be a sign of another disorder, such as inflammatory bowel disease or irritable bowel syndrome. Symptoms include frequent, loose, watery stools and stomach pain. Most cases clear on their own. Some infections may need antibiotics. Severe cases can cause enough dehydration to require extra fluid assistance. One tried-and-true diet for diarrhea is the BRAT diet: bananas, rice, applesauce, and toast. Low in fiber, bland, and starchy, these foods can help replace lost nutrients and firm up your stools. Also, replacing lost fluids with an oral rehydration solution (ORS) may help to prevent dehydration. If your diarrhea persists for longer than 2-3 days, consult a doctor ASAP.", 
                     font = ('Bahnschrift SemiBold', 15, 'bold'), fg = '#6800FF', bg = '#feffba', wraplength = 1250, justify = LEFT)#, command = lambda: infohs(infoscreen, 1,  100, 1200))
    #infotext.attributes('-alpha', 0)
    infotext.grid(row = 1, column = 0, sticky = 'w')
    infotext2.grid(row = 2, column = 0, sticky = 'w')
    infotext3.grid(row = 3, column = 0, sticky = 'w')
    
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
    scs.configure(bg = '#feffba')
    scandetails = Label(scs, text = "This is the scan feature. Here, you can take a picture of your medicine and get its results on Google. A table will be generated, in which you can manually enter the expiry date of your medicine. Please do not edit the URL. Please note that you should keep your medicine catalog open before submitting your medicine, and do not close it afterwards. In the future, I will make this catalog local.", font = ('Britannic Bold', 20, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1300)
    scandetails.grid(row = 0, column = 0)
    scanbn = Button(scs, text = "Scan", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00', command = lambda: scan(scs))
    scanbn.grid(row=1, column=0, padx=10, pady=10)
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
    #cv2.imshow("Picture Taken", frame)
    # Define the image variable that we will use to extract medicine info from
    img = frame
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contrast_gray = cv2.convertScaleAbs(grayimg, alpha=1.5, beta=0)
    #cv2.imshow('Grayscale', contrast_gray)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(contrast_gray, lang = 'eng')
    #print(text)
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
    #sheet.set_sheet_data_and_display_dimensions(total_rows = 2, total_columns = 3)
    sheet.height_and_width(height = 300, width = 700)
    sheet.set_cell_data(0, 0, value = text, set_copy = True, redraw = False)
    sheet.set_cell_data(0, 1, value = 'Enter your expiry date', set_copy = True, redraw = False)
    sheet.set_cell_data(0, 2, value = URL, set_copy = True, redraw = False)
    submitbn = Button(screen, text = "Submit", font = ('Bahnschrift SemiBold', 20, 'bold'), fg = '#FFFF00', activeforeground = '#ae00ff', bg = '#ae00ff',
                   activebackground = '#FFFF00', command = lambda: createnewrow(sheet))
    submitbn.grid()
    global newrow
    #newrow = sheet.get_row_data(0, return_copy = True)
    #sheet.insert_row(values = newrow, idx = "end", height = 200, deselect_all = False, add_columns = False,
    #       redraw = False)

medsheet = False
def medicines():
    global newrow
    global medsheet
    msc = Tk()
    msc.state('zoomed')
    msc.title('Medicines Catalog')
    medsheet = tksheet.Sheet(msc)
    medsheet.grid()
    medsheet.headers(['Medicine Name (scanned)', 'Expiry Date', 'Information'])
    medsheet.set_sheet_data([[f"{ri+cj}" for cj in range(3)] for ri in range(0)])
    medsheet.set_all_column_widths(width = 200, only_set_if_too_small = False, redraw = True, recreate_selection_boxes = True)
    medsheet.set_all_row_heights(height = 200, only_set_if_too_small = False, redraw = True, recreate_selection_boxes = True)
    medsheet.height_and_width(height = 300, width = 700)
    msc.mainloop()
def createnewrow(s):
    global newrow
    newrow = s.get_row_data(0, return_copy = True)
    if medsheet:
        medsheet.insert_row(values = newrow, idx = "end", height = 200, deselect_all = False, add_columns = False, redraw = True)
    else:
        print('Please open the medicines page before submitting your medicine.')
#def addnewrow(sh):
#    global newrow
#    sh.insert_row(values = newrow, idx = "end", height = 200, deselect_all = False, add_columns = False, redraw = False)
def about():
    abtscreen = Tk()
    abtscreen.configure(bg = '#feffba')
    abttext = Label(abtscreen, text = "A rapidly increasing number of people are ingesting medicines and drugs in dangerous quantities, based on their own assumptions about healthcare. Most of us don’t have a proper way to track our medicines. It’s a common fact that people, nowadays, tend to believe that a simple Google search tells them all about their sickness and which medicine(s) to use to treat themselves. Instead of seeking professional help/advice, we are taking risks that can result in permanent damage. According to CNN, patient noncompliance is an epidemic. Over 50 percent of prescriptions written yearly are either taken incorrectly by the patient, or not taken at all. In the earlier times, 1 of 10 patients used to seek medication on the internet, but today that number has changed to 9 out of 10. Most of us aren’t getting the right answers, and how will they keep track of the real medicines that they actually have? The solution is MedTrack. MedTrack has 4 main features that add up to a perfect solution for this problem: Scan your medicine, information library, chatbot, and medicine history. The Scan and Medicine History features help you keep track of your medicines. Simply take a picture, enter the expiry date, and add the medicine to your catalog! In the future, I will save the Medicine History locally on the user’s device as I need to export it to a platform like ReactNative to make it a mobile application. I will also use webscraping (using a library like BeautifulSoup4) and NLP summarization tools (OpenAI is an example of an easy-to-use natural language processing tool) to get the summary of your medicine rather than the google search URL. The information library provides you instant and authentic information about generic ailments and their home remedies. Please read the disclaimer at the top before following advice. Finally, the chatbot allows you to ask anything about medicines and healthcare: It has questions and answers carefully curated from reliable consultation websites.",
                    font = ('Britannic Bold', 15, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1250)
    #appiimg = Label(abtscreen, image = appicon, bg = '#feffba')
    #appiimg.grid(row = 1, column = 0)
    abttext.grid(row = 0, column = 0, sticky = 'w')
    
    abtscreen.mainloop()
def instr():
    inscreen = Tk()
    inscreen.configure(bg = '#feffba')
    intext1 = Label(inscreen, text = "How to use Scan: Take a picture of your medicine and get its results on Google. A table will be generated, in which you can manually enter the expiry date of your medicine. Please do not edit the URL. Please note that you should keep your medicine catalog open before submitting your medicine, and do not close it afterwards. In the future, I will make this catalog local.", font = ('Britannic Bold', 15, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1250)
    intext2 = Label(inscreen, text = "How to use Information Library: In the information library, you can see some common ailments and their information & home remedies given. In the future, I will use webscraping and summarization to automate the information list rather than having to manually input the values.", font = ('Britannic Bold', 15, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1250)
    intext3 = Label(inscreen, text = "How to use Chatbot: When the chatbot opens, you can put it in full screen and ask all your questions.", font = ('Britannic Bold', 15, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1250)
    intext4 = Label(inscreen, text = "How to use Medicine History: The medicine history is currently a temporary record of the medicines you scan. Whenever you submit a medicine, a row with the medicine's data will be added for you to reference. In the future, I will save the medicine history locally and add features like 'delete medicine'. Note: When using the scan to add a medicine to your medicine history, open the medicine history first for visible results. Do not worry: This glitch will soon be resolved.", font = ('Britannic Bold', 15, 'normal'), fg = 'black', bg = '#feffba', wraplength = 1250)

    intext1.grid(row = 0, column = 0, sticky = 'w')
    intext2.grid(row = 1, column = 0, sticky = 'w')
    intext3.grid(row = 2, column = 0, sticky = 'w')
    intext4.grid(row = 3, column = 0, sticky = 'w')
def donate():
    donurl = "https://www.givingwhatwecan.org/donate/organizations"
    webview.create_window('Donate',donurl)
    webview.start()
    
#Create the widgets and add functionality
appiconimg = Label(root, image = appicon, bg = 'white')
abtbn = Button(root, text = 'About', bg = 'white', borderwidth = 0, image = abticon, compound = TOP, command = about)
insbn = Button(root, text = 'How to Use', bg = 'white', borderwidth = 0, image = insicon, compound = TOP, command = instr)
donbn = Button(root, text = 'Donate', bg = 'white', borderwidth = 0, image = donicon, compound = TOP, command = donate)
title = Label(root, text = "Welcome to\rMedTrack!", font = ('Berlin Sans FB Demi', 30, 'bold'), fg = '#ff4d00', bg = 'white')
hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = scanicon, compound = BOTTOM, command = scanscr)
hib = Button(root, text = 'Information Library', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = infoicon, compound = BOTTOM, command = info)
hcb = Button(root, text = 'Chatbot', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = chaticon, compound = BOTTOM, command = chat)
hmb = Button(root, text = 'Medicine History', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
             activebackground = '#99FFFF', height = 250, image = medicon, compound = BOTTOM, command = medicines)

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

