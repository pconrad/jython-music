# midiIn1.py

from midi import *

midiIn = MidiIn()     

def printNote(eventType, channel, data1, data2):
   print "pitch =", data1, "volume =", data2

midiIn.onNoteOn(printNote)