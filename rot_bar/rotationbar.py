from time import sleep  # sleep(1.80)
from typing import Dict, List, Tuple
from tkinter import * 
import pygame

#default characteristics
curr_style = 'Melee'
file_path = 'C:\python projects\rot_bar\abilities'

#alright well i guess heres my data
melee_bar = {'Cleave.png':'q', 'Dismember.png': 'w', 'Sever.png': 'e', 'Smash.png': 'r', 'Slice.png': 't', 'Fury.png': 'y'}
ranged_bar = {'Snipe.png':'q', 'Piercing_Shot.png': 'w', 'Fragmentation_Shot.png': 'e', 'Ricochet.png': 'r', 'Binding_shot.png': 't' }
magic_bar = {'Combust.png':'q', 'Sonic_Wave.png': 'w', 'Dragon_Breath.png': 'e', 'Chain.png': 'r', 'Impact.png': 't'}
other_bar = {'Antipation.png': 'F1', 'Freedom.png': 'F2', 'Resonance.png': 'F3', 'Devotion.png': 'F4', 'Def_melee.png': 1, 'Def_ranged.png': 2, 'Def_magic.png': 3,
                'melee2h.png': 'ctrl+1', 'Ranged2h.png': 'ctrl+2', 'magic2h.png': 'ctrl+3', 'Soulsplit.png': 'z', 'Vigour.png': 'x', 'Saradomin_brew.png': 'g',
                'Blubber.png': 'h'}


#Attach key bind with images

#window
rot_bar = Tk()

#window details
rot_bar.title('RS3 Ability Tracker')
rot_bar.geometry('675x120')

#Combat Style Labeling
combat_label = Label(rot_bar, text = 'Current Combat Style: ' + curr_style, font = ('bold', 14), pady=10)
combat_label.config(anchor=CENTER)
combat_label.pack()

#testing


#Main rotation bar display

#if melee
    #if pressed.key(x)
        #image(melee\x.png)

#start
rot_bar.mainloop()
