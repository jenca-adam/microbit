from microbit import *
#NOTE:toto je testovaci program pre SIPO 74HCT595(shift register)
CLK_RESET=0
INTERVAL_HZ=1000
#prepocitaj hz na milisekundy
INTERVAL_MS=(1/INTERVAL_HZ)*1000
data=1
SER_PIN=pin0
SRCLK_PIN=pin1
RCLK_PIN=pin2
#jeden pulz hodin
def clock():
    if CLK_RESET:
        #resetni
        SRCLK_PIN.write_digital(0)
        #nastav CLK_RESET na nabeznu hranu
        CLK_RESET=0
        #pockaj
        sleep(INTERVAL_MS)
    else:
        #nabezna hrana
        SRCLK_PIN.write_digital(0)
        #nastav CLK_RESET na resetovanie
        CLK_RESET=1
        #pockaj
        sleep(INTERVAL_MS)
#nakrm vstup Serial IN(jeden bit)
def feed_SER1B(pin,data):
    pin.write_digital(data)
#nakrm vstup Serial IN(osem bitov)
def feed_SER8B(pin,data):
    #sprav for cez data
    for bit in data:
        #nakrm tymto bitom pin
        feed_SER1B(pin,bit)
        #zapulzuj hodinami do RESET
        clock()
        #este raz do nabeznej hrany
        clock()
def pust_feed():
    #vypusti zadane informacie

    RCLK_PIN.write_digital(1)
def test():
    #toto pole budeme feedovat
    initial=[0,1,1,1,1,1,1,1]
    #nakrm SER_PIN
    feed_SER8B(SER_PIN,initial)
    #pusti feed
    pust_feed()
