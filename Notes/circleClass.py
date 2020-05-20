# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:08:19 2020

@author: Joseph Mathew
"""

import matplotlib.pyplot as plt
#%matplotlib inline

class Circle(object):
    
    def __init__(self, radius = 20, color = 'red' ):
        self.radius = radius
        self.color = color
        
        
    def add_radius(self, radius = 3):
        self.radius += radius
        
        
    def display_circle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
        
        #rectangle
        #plt.gca().add_patch(plt.Rectangle((0,0),self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()
        
        
        
redCircle = Circle(radius=3)
redCircle.display_circle()
print("Radius", redCircle.radius)


blueCircle = Circle(color='blue')
blueCircle.display_circle()
print("Radius", blueCircle.radius)

print(dir(blueCircle))