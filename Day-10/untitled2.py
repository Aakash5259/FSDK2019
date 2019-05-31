# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:53:49 2019

@author: aks
"""

 from PIL import Image
 from PIL import ImageFont
 from PIL import ImageDraw
 img = Image.open("Template.jpg")
 draw = ImageDraw.Draw(img)
 selectFont = ImageFont.truetype("font.ttf", size = 60)
 draw.text( (250,50), "Forsk Techonologys", (200,50,100), font=selectFont
 draw.text( (50,150),'This is to certify " AAKASH SHARMA" for completion', (200,50,100), font=selectFont
 draw.text( (250,50), "of summer traning", (200,50,100), font=selectFont
 img.save( 'certi.pdf', "PDF", resolution=100.0)