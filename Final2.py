
import time
import SI1145.SI1145 as SI1145


# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with I2C1_SCL = P9_17 and I2C1_SDA = P9_18
# Header pinout: http://beagleboard.org/static/images/cape-headers-i2c.png
# Configure the pins for I2C with these pins:
#   sudo config-pin p9.17 i2c



# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_APzM83R856VqwaJinm66EjVVXbCe'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'nataliebowen'

# Create an instance of the REST client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)






sensor = SI1145.SI1145()

print ('Press Cntrl + Z to cancel')





while True:
        vis = sensor.readVisible()
        ir = sensor.readIR()
        uv = sensor.readUV()
        uv = uv / 100.0

        print "Vis:        ", vis
        aio.send("vis", vis)
        print "IR:         ",  ir
        aio.send("ir",  ir)

        print "UV Index:  ", uv
        aio.send("uv",  uv)

