import RPi.GPIO as GPIO
import time
import netifaces

GPIO.setmode(GPIO.BCM)

GPIO.setup( 16, GPIO.OUT )

ip = netifaces.ifaddresses("eth0")[2][0]["addr"]

for i in range( 3 ):
			GPIO.output( 16, 0 )
			time.sleep( 0.5 )
			GPIO.output( 16, 1 )
			time.sleep( 0.5 )
			
time.sleep( 2 )

for i in range( len( ip ) ):
	print( ip[ i ] )
	
	if ip[ i ] != ".":
		for n in range( int( ip[ i ] ) + 1 ):
			GPIO.output( 16, 0 )
			time.sleep( 0.2 )
			GPIO.output( 16, 1 )
			time.sleep( 0.2 )
		time.sleep( 2 )
	else:
		GPIO.output( 16, 0 )
		time.sleep( 1 )
		GPIO.output( 16, 1 )
		time.sleep( 2 )

