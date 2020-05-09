import gpiozero
import os
import sys, getopt
from time import sleep


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp = (res.replace("temp=","").replace("'C\n",""))
    return temp

def main(argv):
    fanPin = 23
    tempThres = 55
    hysteresis = 5
    fan_is_off = True
    try:
        opts, args = getopt.getopt(argv,"hp:t:b:",["pin=","threshold_temp=","hysteresis="])
    except getopt.GetoptError:
        print ('autoFan.py -p <fan_GPIO> -t<threshold_temp(\'C)> -b <hysteresis>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ('autoFan.py -p <fan_GPIO> -t<threshold_temp(\'C)> -b <hysteresis>')
        elif opt in ("-p","--pin"):
            fanPin = arg
        elif opt in ("-t","--threshold_temp"):
            tempThres = float(arg)
        elif opt in ("-b","--hysteresis"):
            hysteresis = float(arg)

    fan = gpiozero.DigitalOutputDevice(fanPin)
    while(True):
        curr_temp = float(getCPUtemperature())
        if curr_temp>=tempThres:
            if fan_is_off:
                fan.on()
                fan_is_off = False
        else:
            if not fan_is_off:
                if curr_temp <= tempThres - hysteresis:
                    fan.off()
                    fan_is_off = True

        #print(f'CPU Temperature is :{curr_temp}')
        sleep(2)

if __name__ == '__main__':
    main(sys.argv[1:])