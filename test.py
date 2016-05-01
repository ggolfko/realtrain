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
	result = firebase.patch('trainSystem/vehicles/35', {'arrTime' : '06:35',
        'depTime' : '14:45',
        'endedAt' : 'no',
        'heading' : 'SPE',
        'id' : '4507',
        'lat' : data.latitude,
        'line' : 'south',
        'lon' : data.longitude,
        'name' : "Bangkok - Hatyai Jn.",
        'routeTag' : '35',
        'speedKmHr' : 'gpsd.fix.speed',
        'timestamp' :  {'.sv': 'timestamp'},
        'vtype' : 'train'})
	print result

