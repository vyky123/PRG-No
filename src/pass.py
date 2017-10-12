# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

heslo =  input("Zadej své heslo > ")

MALA = "qwertzuiopasdfghjklyxcvbnm"
VELKA = MALA.upper()
SPEC = "!@#$%^&*(){}[]\=+-\"~"
CISLA = "0123456789"
if len(heslo) < 8:
    print("Heslo je příliš krátké")
    exit(1)

jeMALA = 0
jeVELKA = 0
jeSPEC = 0
jeCISLA = 0

for znak in heslo:
    if znak in MALA:
         jeMALA = True         
    jeVELKA = (znak in VELKA) or jeVELKA
    jeSPEC = znak in SPEC
    if znak in CISLA:
        jeCISLA = True
print(jeMALA, jeVELKA, jeSPEC, jeCISLA)
if jeMALA + jeVELKA + jeSPEC + jeCISLA >=3:
    print("Heslo je v pořádku")
    exit(0)
else:
    print("Heslo je příliš jednoduché")
    exit(0)