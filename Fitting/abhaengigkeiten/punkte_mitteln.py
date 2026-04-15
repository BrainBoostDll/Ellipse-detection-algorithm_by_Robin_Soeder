import sys
sys.path.append("./")
#
import numpy as np
def punkte_mitteln(array):
    addieren_x = 0
    addieren_y = 0
    try:
        #for i in range(len(array[:,0])):
        addieren_x += array[:,0]
        addieren_y += array[:,1]
        mittel_x = addieren_x/len(array[:,0])
        mittel_y = addieren_y/len(array[:,1])
        # array erstellen
        gemittelter_startpunkt = np.array([[mittel_x,mittel_y]]).reshape(1,2)
    except (ZeroDivisionError) as zero:
        return np.array([[0,0]]).reshape(1,2)
    return gemittelter_startpunkt