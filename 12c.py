import smbus
import time

##device address obtained through 12cdetect -y 1 command
DEVICE = 0x23 # Default device I2C address

# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1) 

##converts bits to numbers
def convertToNumber(data):
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  #reads the data at the specified address using the specified mode
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  #converts the returned bits to floating point number
  return convertToNumber(data)

##defines the lux by categories defined in task sheet
def lightCategory(lx):
    if(lx <= 20):
        return "too dark"
        #print("too dark")
    elif(lx > 20 and lx <= 30):
        return "dark"
    elif(lx > 30 and lx <= 40):
        return "medium"
    elif(lx > 40 and lx <= 100):
        return "bright"
    else:
        return"too bright"

def main():
    ##continuously read lux
    try:
        while True:
            lightLevel=readLight()
            ##print light level rounding to 2 decimal places
            print("Light Level : " + format(lightLevel,'.2f') + " is " + lightCategory(lightLevel))
            time.sleep(1)
    ##close program if keyboard interrupt pressed
    except KeyboardInterrupt:
        print("User quite program via keyboard interrupt")
        pass 
        

if __name__=="__main__":
   main()
