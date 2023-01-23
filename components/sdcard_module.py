import machine, os, sdcard

class machine.SDCard(
    slot=1,
    width=1,
    cd=34,
    wp=None,
    sck=14,
    miso=12,
    mosi=13,
    cs=5,
    freq=2000000
)

sd = sdcard.SDCard(machine.SPI(1), machine.Pin(34)) 
vfs = os.VfsFat(sd)

os.mount(vfs, “/fc”)
print(“Filesystem check”)
print(os.listdir(“/fc”))