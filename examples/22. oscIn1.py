# oscIn1.py

from osc import *

oscIn = OscIn( 57110 ) 

def simple(message):      
   print "Hello world!"

oscIn.onInput("/helloWorld", simple)