#!/usr/bin/python3
import lcddriver
import os
import subprocess

def dirsize(folder):
        total_size = 0
        for path, dirs, files, in os.walk(folder):
                for f in files:
                        fp = os.path.join(path, f)
                        total_size += os.path.getsize(fp)
        return str(round((total_size/1024)/1024)) + "MB" 

display = lcddriver.lcd()
storage = "/media/pi/New Volume"

display.lcd_display_string("Capture stopped", 1)

try:
        with open(os.devnull, 'w') as fp:
                proc = subprocess.Popen('/usr/bin/tshark -i 1 -a filesize:2000000 -b files:100 -w "' + storage + '/capture.pcap"', shell=True, stdout=fp)
        while proc.poll() == None:
                display.lcd_display_string("Capture started", 1)
                display.lcd_display_string(dirsize(storage), 2)
finally:
        display.lcd_display_string("Capture stopped", 1)
