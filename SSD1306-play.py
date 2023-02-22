import time
from machine import Pin, SPI
spi = SPI(2,10000000, sck=Pin(32), mosi=Pin(33), miso=Pin(35))
from SSD1306 import SSD1306_SPI
oled = SSD1306_SPI(128, 64, spi,dc=Pin(26),cs=Pin(27),res=Pin(25))

for count in range(450):
    oled.show_bmp("after/%4.4d.bmp"%count)
    oled.show()

