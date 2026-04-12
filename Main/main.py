import sys
sys.path.append("./")
# Bildaufbereitung
from Bildaufbereitung.graustufenumwandlung import graustufenumwandlung
from Bildaufbereitung.canny_edge import canny_edge
# Fitting
from Fitting.abhaengigkeiten.ellipsengleichung import ellipsengleichung
from Fitting.abhaengigkeiten.fit import fit
# canny bild
canny_bild = canny_bild(graustufenumwandlung())
# ellipsen in Bild zeichnen