#!/usr/bin/python
# #-*- coding:utf-8 -*-
import os
#os.system('ipconfig')
#s1 = input("input server ipaddress:")
s1="192.168.31.5"
#s = input("input target ipaddress:")
s="192.168.31.23"
os.system('adb devices')
os.system('adb connect '+ s)
os.system('adb uninstall vido.apk')

os.system('adb disconnect '+ s)
#os.system('./adb shell am start -n com.kmplayer/.MainActivity '+'http://'+s1+'/2.mp4')
#os.system('adb shell am start -n com.perfect.player/.ui.player.VideoActivity '+'http://'+s1+'/2.mp4')

print(s)
print('ok')