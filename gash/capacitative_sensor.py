import smbus
import time

DEVICE     = 0x5A #device address
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def readdata(addr=DEVICE):

  #read 6 bytes of data from the device address (0x05A) starting from an offset of four
  data = bus.read_i2c_block_data(addr,0x04, 6)

  print "Humidity = " + str(data[0]) + "." + str(data[1]) + "%"
  print "Temperature : " + str(data[2]) + "." + str(data[3]) + "C"

  if (data[0] + data[1] + data[2] + data[3] ==  data[4]):
    print "checksum is correct"
  else:
    print "checksum is incorrect, data error"

if __name__=="__main__":
    while True:
        readdata()
        time.sleep(1)
