###########################
# This ability bar was created by Brandon Mefford
# The purpose of this app is to track in real-time
# the usage of abilities is an MMORPG (RS3).
# 
# This bar supports 3 combat styles, 
# food, potions, and defense abilities
#
# swapping combat styles is controlled by Ctrl+[1,2,3]
# 
# combat abilities are q,w,e,r,t,y
# 
# defense abilities are F1,F2,F3,4]
# 
# misc actions are 1,2,3,g,h,z,x
#
# DOES NOT SUPPORT UPPER CASE LETTERS
#
###########################

from typing import Dict, List, Tuple
from tkinter import Tk, Text, font, Label, CENTER, Grid, Canvas, NW
from PIL import ImageTk,Image


#tkinter window initializing
root = Tk()
root.title('RS3 Ability Tracker')
root.geometry('740x120')


#default characteristics
#by default: melee is the combat style
#abilities by default are unused so the list is full of 'unused.png' images
#and the list is capped at 10
curr_style = 'Melee'
unusedImg = "abilities\\other\\unused.png"
nextImg = [unusedImg, unusedImg,unusedImg, unusedImg,unusedImg, unusedImg, unusedImg, unusedImg, unusedImg, unusedImg]
nextImg = nextImg[:10]

#if the list is too long delete the first item in the list 
#to make room for new abilities
def cleanUp():
    if len(nextImg) > 9:
        del nextImg[0]


#dictionary of keybinds associated with images
#these abilites are only unique to me and does
#not suit other peoples playstyles
#PLEASE KEEP IN MIND TO SWITCH COMBAT STYLE IT IS CTRL+[1,2,3]
melee_bar = {'q':'Cleave.png', 'w':'Dismember.png','e':'Sever.png', 'r':'Smash.png', 't':'Slice.png', 'y':'Fury.png'}
range_bar = {'q':'Snipe.png', 'w':'Piercing_Shot.png','e':'Fragmentation_Shot.png', 'r':'Ricochet.png', 't':'Binding_shot.png'}
magic_bar = {'q':'Combust.png', 'w':'Sonic_Wave.png','e':'Dragon_Breath.png', 'r':'Chain.png', 't':'Impact.png'}
other_bar = {'F1':'Anticipation.png', 'F2':'Freedom.png','F3':'Resonance.png', 'F4':'Devotion.png', '1':'Def_melee.png', '2':'Def_ranged.png', 
                '3':'Def_magic.png', '<Control-Key-1>':'Melee.png','<Control-Key-2>':'Ranged2h.png', '<Control-Key-3>':'Magic.png', 'z':'Soulsplit.png', 
                'x':'Vigour.png', 'g':'Saradomin_brew.png','h':'Blubber.png'}



#keypress event (does not include ctrl+# or Function keys)
#the ability presented from a keybind is determined by which
#combat style you are on

#for each keypress:
#   1. determines current combat style to read from the dictionaries abover
#   2. cleans the list 
#   3. appends the new image onto the list
#   4. gets the value associated with with the key pressed 
#   5. updates all images
def key_press(event):
    if curr_style == 'Melee':
        if (format(event.char)) in melee_bar.keys():
            cleanUp()
            temp = melee_bar.get(format(event.char))
            nextImg.append("abilities\\melee\\"+temp)
            updateALL()

    if curr_style == 'Ranged':
        if (format(event.char)) in range_bar.keys():
            cleanUp()
            temp = range_bar.get(format(event.char))
            nextImg.append("abilities\\range\\"+temp)
            updateALL()

    if curr_style == 'Magic':
        if (format(event.char)) in magic_bar.keys():
            cleanUp()
            temp = magic_bar.get(format(event.char))
            nextImg.append("abilities\\magic\\"+temp)
            updateALL()

    if (format(event.char)) in other_bar.keys():
        cleanUp()
        temp = other_bar.get(format(event.char))
        nextImg.append("abilities\\other\\"+temp)
        updateALL()


#keypress events (Only ctrl+# and Function keys)
#switches the current weapon style to melee and reads from melee_bar dict
def melee_style(event):
    global curr_style 
    curr_style= 'Melee'
    combat_label.config(text = 'Current Combat Style: ' + curr_style)
    cleanUp()
    nextImg.append("abilities\\other\\Melee.png")
    updateALL()


#switches the current weapon style to ranged and reads from range_bar dict
def range_style(event):
    global curr_style 
    curr_style = 'Ranged'
    combat_label.config(text = 'Current Combat Style: ' + curr_style)
    cleanUp()
    nextImg.append("abilities\\other\\Ranged.png")

    updateALL()

#switches the current weapon style to magic and reads from magic_bar dict
def magic_style(event):
    global curr_style 
    curr_style = 'Magic'
    combat_label.config(text = 'Current Combat Style: ' + curr_style)
    cleanUp()
    nextImg.append("abilities\\other\\Magic.png")
    updateALL()

#these actions are part of the other_bar dict
def anticipation(event):
    cleanUp()
    nextImg.append("abilities\\other\\Anticipation.png")
    updateALL()
def freedom(event):
    cleanUp()
    nextImg.append("abilities\\other\\Freedom.png")
    updateALL()
def resonance(event):
    cleanUp()
    nextImg.append("abilities\\other\\Resonance.png")
    updateALL()
def devotion(event):
    cleanUp()
    nextImg.append("abilities\\other\\Devotion.png")
    updateALL()




#keypress bindings, if its not listed its not being used and can be ignored
root.bind('<KeyPress>', key_press)
root.bind('<Control-Key-1>', melee_style)
root.bind('<Control-Key-2>', range_style)
root.bind('<Control-Key-3>', magic_style)
root.bind('<F1>', anticipation)
root.bind('<F2>', freedom)
root.bind('<F3>', resonance)
root.bind('<F4>', devotion)



#Title labeling, current combat style is affected by key presses
combat_label = Label(root, text = 'Current Combat Style: ' + curr_style, font = ('bold', 14), pady=10)
combat_label.config(anchor=CENTER)
combat_label.grid(row = 1, column = 1, columnspan=8)


#10 labels for 10 images (initialized to unused)
lbl0 = ImageTk.PhotoImage(Image.open(nextImg[0]))
lbl1 = ImageTk.PhotoImage(Image.open(nextImg[1]))
lbl2 = ImageTk.PhotoImage(Image.open(nextImg[2]))
lbl3 = ImageTk.PhotoImage(Image.open(nextImg[3]))
lbl4 = ImageTk.PhotoImage(Image.open(nextImg[4]))
lbl5 = ImageTk.PhotoImage(Image.open(nextImg[5]))
lbl6 = ImageTk.PhotoImage(Image.open(nextImg[6]))
lbl7 = ImageTk.PhotoImage(Image.open(nextImg[7]))
lbl8 = ImageTk.PhotoImage(Image.open(nextImg[8]))
lbl9 = ImageTk.PhotoImage(Image.open(nextImg[9]))

testlbl0 = Label(root, image = lbl0)
testlbl0.grid(row=2,column=0, padx=5)
testlbl1 = Label(root, image = lbl1)
testlbl1.grid(row=2,column=1, padx=5)
testlbl2 = Label(root, image = lbl2)
testlbl2.grid(row=2,column=2, padx=5)
testlbl3 = Label(root, image = lbl3)
testlbl3.grid(row=2,column=3, padx=5)
testlbl4 = Label(root, image = lbl4)
testlbl4.grid(row=2,column=4, padx=5)
testlbl5 = Label(root, image = lbl5)
testlbl5.grid(row=2,column=5, padx=5)
testlbl6 = Label(root, image = lbl6)
testlbl6.grid(row=2,column=6, padx=5)
testlbl7 = Label(root, image = lbl7)
testlbl7.grid(row=2,column=7, padx=5)
testlbl8 = Label(root, image = lbl8)
testlbl8.grid(row=2,column=8, padx=5)
testlbl9 = Label(root, image = lbl9)
testlbl9.grid(row=2,column=9, padx=5)



#function for updating all images.
#<object>.image = may seem redundant 
#being preceded by <object>.configure 
#but it is purely for garbage collection
def updateALL():
    up0 = ImageTk.PhotoImage(Image.open(nextImg[0]))
    testlbl0.configure(image=up0)
    testlbl0.image = up0
    testlbl0.grid(row=2,column=0, padx=5)
    
    up1 = ImageTk.PhotoImage(Image.open(nextImg[1]))
    testlbl1.configure(image=up1)
    testlbl1.image = up1
    testlbl1.grid(row=2,column=1, padx=5)

    up2 = ImageTk.PhotoImage(Image.open(nextImg[2]))
    testlbl2.configure(image=up2)
    testlbl2.image = up2
    testlbl2.grid(row=2,column=2, padx=5)

    up3 = ImageTk.PhotoImage(Image.open(nextImg[3]))
    testlbl3.configure(image=up3)
    testlbl3.image = up3
    testlbl3.grid(row=2,column=3, padx=5)

    up4 = ImageTk.PhotoImage(Image.open(nextImg[4]))
    testlbl4.configure(image=up4)
    testlbl4.image = up4
    testlbl4.grid(row=2,column=4, padx=5)

    up5 = ImageTk.PhotoImage(Image.open(nextImg[5]))
    testlbl5.configure(image=up5)
    testlbl5.image = up5
    testlbl5.grid(row=2,column=5, padx=5)

    up6 = ImageTk.PhotoImage(Image.open(nextImg[6]))
    testlbl6.configure(image=up6)
    testlbl6.image = up6
    testlbl6.grid(row=2,column=6, padx=5)

    up7 = ImageTk.PhotoImage(Image.open(nextImg[7]))
    testlbl7.configure(image=up7)
    testlbl7.image = up7
    testlbl7.grid(row=2,column=7, padx=5)

    up8 = ImageTk.PhotoImage(Image.open(nextImg[8]))
    testlbl8.configure(image=up8)
    testlbl8.image = up8
    testlbl8.grid(row=2,column=8, padx=5)

    up9 = ImageTk.PhotoImage(Image.open(nextImg[9]))
    testlbl9.configure(image=up9)
    testlbl9.image = up9
    testlbl9.grid(row=2,column=9, padx=5)

#start the app
root.mainloop()

