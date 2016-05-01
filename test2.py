import serial
import pynmea2
from firebase import firebase
firebase = firebase.FirebaseApplication('https://boiling-fire-7865.firebaseio.com')


serialStream = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

while True:
    sentence = serialStream.readline()
    if sentence.find('GGA') > 0:
        data = pynmea2.parse(sentence)
        print "{time} : {lat},{lon} ".format(time=data.timestamp,lat=data.latitude,lon=data.longitude)
	result = firebase.patch('trainSystem/vehicles/36',{ 'lat' : data.latitude, 'lon' : data.longitude,
         'timestamp' :  {'.sv': 'timestamp'}
       })
	print result

