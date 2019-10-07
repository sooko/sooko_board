# pada contoh digital input kita telah progam menyalakan led dengan button mnggunakan perulangan While
# pada contoh ini kita membuat tommbol dengan irq atau callback
from machine import Pin
class Button(object):
    button = Pin(0, Pin.IN)
    led_hijau =Pin(2 ,Pin.OUT)
    led_merah =Pin(4 ,Pin.OUT)
    def __init__(self ,*args ,**kwargs):
        super(Button ,self).__init__(**kwargs)
        self.button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.callback)
    def callback(self ,dt):
        print(dt.value())
        if self.button.value( )==1:
            self.led_hijau.value(0)
            self.led_merah.value(1)
        else:
            self.led_hijau.value(1)
            self.led_merah.value(0)
Button()




