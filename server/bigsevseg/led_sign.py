from Adafruit_I2C import Adafruit_I2C
Addr = 0x04
i2c = Adafruit_I2C(address=Addr)
i2c.write8(0, ord('M'))
i2c.write8(0, ord('s'))