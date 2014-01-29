# -*- coding: latin-1 -*-

#
#  IS-105 LAB2
#
#  lab2.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Criyonit Kayoka', \
			'student2': 'Mirko Grimm', \
            'student3': 'Rand Zeid', \
 
#Oppgave 1 | Printer ut fugl naar man kalle fuksjon.
def ascii_fugl():
    print """ 
                  \/_ 
             \,   /( ,/
              \\\' ///
               \_ /_/
               (./
                '`
    """
#oppgave 2 | 
def bitAnd(x, y):
    return x&y

#Oppgave 4 |
def bitXor (x, y):
    return x^y

#Oppgave 5 | 
def bitOr (x, y):
    return x|y

# oppgave 6
def ascii8Bin(bokstav): 
	
	d=ord (bokstav)
	return '{0:08b}'.format(ord(bokstav)) 

ascii8Bin('d')  

print ascii8Bin ('d') 

# oppgave 7 
def transferBin (tekst): 
	liste = list (tekst)
	for bokstav in liste: 
	   print ascii8Bin(bokstav)

transferBin ("Hei")

#Oppgave 8
def ascii2Hex(bokstav):
 asciiNumber = ord(bokstav)
 return '{0:02x}'.format(asciiNumber)
def transferHex(string):
         l = list(string)
        for c in l:
         print ascii2Hex(c)