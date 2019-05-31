# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:40:33 2019

@author: aks
"""

"""
Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""
################################################################
 from PIL import Image
 from PIL import ImageFont
 from PIL import ImageDraw
 img = Image.open("Template.jpg")
 draw = ImageDraw.Draw(img)
 selectFont = ImageFont.truetype("font.ttf", size = 60)
 draw.text((250,50), "Forsk Techonologys", (120,150,100), font=selectFont)
 selectFont1 = ImageFont.truetype("font.ttf", size = 30)
 draw.text((150,200),'This is to certify that " AAKASH SHARMA" has',(100,100,100),font=selectFont
 draw.text((150,250),'succesfully completed the summer training with Forsk',(100,100,100),font=selectFont
 draw.text(100,300),'Technologies for 2 months.',(100,100,100),font=selectFont          
 img.save( "certi.jpg","JPEG", resolution=100.0)














