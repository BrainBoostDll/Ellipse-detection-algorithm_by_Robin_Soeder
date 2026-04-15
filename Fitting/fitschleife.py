import sys
sys.path.append("./")
import numpy as np
from Fitting.abhaengigkeiten.fit import fit
from Fitting.abhaengigkeiten.punkte_mitteln import punkte_mitteln
from Fitting.abhaengigkeiten.daten_zentrieren import daten_zentrieren
from Fitting.abhaengigkeiten.mittelpunkt_optimieren import mittelpunkt_optimieren
#
def fitschleife(array_liste):
    # counter für gefundene Ellipsen
    gefundene_ellipsen = 0
    for array in array_liste:
        # grober Mittelpunkt zur Umrechnung in Polar
        gemittelter_startpunkt = 
        # Daten zentrieren
        zentriert = (array)
        # Koordinaten Transformation
        polar = (zentriert)
        # initial guess als anfangsschätzung für die Fit-Parameter berechnen
        initial_guess = []
        # erster Fit
        fit1 = fit(polar,initial_guess)
        # rück transfomration 
        kart = 
        # optimierung des Mittelpunktes
        # kartesisch in Polar
        polar1 = 
        # zweiter Fit mit übernommenen parametern des ersten Fits
        fit2 = fit(polar1,fit1[0])
        # fit mit schwellenwerten überprüfen
        if abweichung < schwelenwert:
            gefundene_ellipsen += 1
            # ergebnis in eine txt datei schreiben
            with open() as file:
                pass
        else:
            continue
    # return
    return gefundene_ellipsen
