#imports
import tkinter as tk
import CardDetector
import Analyser
from PIL import Image, ImageTk

#Main-Window Properties
main = tk.Tk()
main.title("Card-Analyzer")
main.minsize(1280 ,720)
main.maxsize(1280, 720)
main.configure(background= '#35654d')
main.geometry("1280x720")

#Variables
cards = []
images = []
maincanvas = tk.Canvas(width="1080", height="350", background= '#35654d', bd=0, highlightthickness=0)
playercanvas = tk.Canvas(width="1280", height="380", background= '#35654d', bd=0, highlightthickness=0)
jump = False
pimgplace = 180
imgplace = 180



def drawcard(card):
    cards.append(card)

    if len(cards) <= 5 and len(cards) < 11:
        MainCards(card)

    elif len(cards) > 5 and len(cards) < 11:
        PlayerCards(card)

    else:
        PlayerCards(card)
        Analyser.getAllCards(cards)
    
    

def purgecards():
    global images
    global imgplace
    global cards
    global pimgplace
    global jump
    cards.clear()
    images.clear()
    imgplace = 180
    pimgplace = 180
    jump = False

    main.update()



def MainCards(newcard):
    global imgplace
    img = Image.open("./2Dcardimages/" + newcard + ".png")
    imgr = img.resize((150, 220), Image.ANTIALIAS)
    cardimg = ImageTk.PhotoImage(imgr)
    images.append(cardimg)

    maincanvas.create_image((imgplace, 200),image = cardimg)

    imgplace = imgplace + 165
    
    maincanvas.pack()
    main.update()




def PlayerCards(newcard):
    global jump
    global pimgplace

    img = Image.open("./2Dcardimages/" + newcard + ".png")
    imgr = img.resize((150, 220), Image.ANTIALIAS)
    cardimg = ImageTk.PhotoImage(imgr)
    images.append(cardimg)

    playercanvas.create_image((pimgplace, 250),image = cardimg)

    
    playercanvas.pack()
    main.update()


    if jump == False:
        pimgplace = pimgplace + 165
        jump = True
    
    else:
        pimgplace = pimgplace + 230
        jump = False