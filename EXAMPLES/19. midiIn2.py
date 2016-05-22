# midiIn2.py

from midi import *

midiIn = MidiIn()     

def printEvent(eventType, channel, data1, data2):
   print "MIDI message:", eventType, channel, data1, data2

midiIn.onInput(ALL_EVENTS, printEvent)