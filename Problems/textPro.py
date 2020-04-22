# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:46:17 2020

@author: Joseph Mathew
"""

def sentence_maker( phrase ):
    interrogatives = ( "how", "what", "why", "are" )
    capatalized = phrase.capitalize()
    
    if( phrase.lower().startswith( interrogatives ) ):
        return "{}?".format( capatalized )
    else:
        return "{}.".format( capatalized )
    
response = []

while True:
    res = input( "Say something: " )
    
    if res == "\end":
        break
    
    response.append( sentence_maker( res ) )

print( " ".join( response ) )