# Import des modules
import RPi.GPIO
import time

#Pin

Xstep      = 17  # Out
Xdir       = 4   # Out
Ystep      = 22  # Out
Ydir       = 27  # Out
Zstep      = 26  # Out
Zdir       = 19  # Out
Laser      = 18  # Out
LedStatus  = 20  # Out
LedError   = 21  # Out

XendStop   = 5   # In
YendStop   = 6   # In
ZendStop   = 13  # In
EmgStop    = 16  # In
##############


#Variable
x = y = z = 0.0     # XYZ position
nbStep_X = 256 # Number of step / 0.1mm
nbStep_Y = 256 # Number of step / 0.1mm
nbStep_Z = 256 # Number of step / 0.1mm

timeStep  = 0.01 #  
directX   = LOW  #
directY   = LOW  #
directZ   = LOW  #

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Xstep, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Xdir, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Ystep, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Ydir, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Zstep, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Zdir, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LedStatus, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LedError, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(XendStop, GPIO.IN)
GPIO.setup(YendStop, GPIO.IN)
GPIO.setup(ZendStop, GPIO.IN)
GPIO.setup(EmgStop, GPIO.IN)





# Si on detecte un appui sur le bouton, on allume la LED 
# et on attend que le bouton soit relache



















while True:
    state = GPIO.input(19)
    if not state:
        # on a appuye sur le bouton connecte sur la broche 19
        GPIO.output(12, GPIO.HIGH)
        while not state:
            state = GPIO.input(19)
            time.sleep(0.02)  # Pause pour ne pas saturer le processeur
        GPIO.output(12, GPIO.LOW)
    time.sleep(0.02)  # Pause pour ne pas saturer le processeur

    
    
    
def BackHome ( ):
    # X go home
    home = GPIO.input(XendStop)


    return



def moveX ( direction, timeStep, nbStep ):
    # Set the direction
    GPIO.output(Xdir, direction)
    # Move
    for cpt in range(0, nbStep):
        GPIO.output(Xstep, GPIO.LOW)
        time.sleep(timeStep)
        GPIO.output(Xstep, GPIO.HIGH)

    if direction == HIGH
        x = x + 0.1
    else x = x - 0.1
    
