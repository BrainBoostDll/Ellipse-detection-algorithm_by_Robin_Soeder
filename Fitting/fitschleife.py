import sys
sys.path.append("./")
def fitschleife(array_liste):
    # counter für gefundene Ellipsen
    gefundene_ellipsen = 0
    for array in array_liste:
        # grober Mitelpunk tzur Umrechnung in Polar

        # Daten zentrieren
        zentriert = 
        # Koordinaten Transformation
        polar = 
        # erster Fit
        fit1 = fit()
        # rück transfomration 
        kart = 
        # optimierung des Mittelpunktes
        # kartesisch in Polar
        poar1 = 
        # zweiter Fit mit übernommenen parametern des ersten Fits
        fit2 = fit(polar1)
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
