import time
import network
import requests
import json
import micropython
import sys
from picoscroll import PicoScroll, WIDTH, HEIGHT

scroll = PicoScroll()

# Weather API
lat  = ""
lon  = ""
key  = ""
call = "https://api.openweathermap.org/data/3.0/onecall?lat=" + lat + "&lon=" + lon + "&units=metric&exclude=minutely,hourly&appid=" + key
wait = 900

# Wi-Fi Interface
ssid = 'YourNetwork'
password = 'YourPassword'

history = [1.0, 1.0, 1.0, 1.0, 
          1.0, 1.0, 1.0, 1.0,
          1.0, 1.0, 1.0, 1.0,
          1.0, 1.0, 1.0, 1.0,
          1.0]

def draw_exposure(levels):
    for x in range(17):
        for y in range(7):
            if y <= (levels[x] - 1):
                scroll.set_pixel(x, (6-y), 8)
            else:
                scroll.set_pixel(x, (6-y), 0)
    scroll.show()

def main():
    try:
        # Opening message 
        scroll.scroll_text('Hi!', 8, 100)
        time.sleep(1)

        # Init and connect to the network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        # Main loop
        while True:
            # debug
            micropython.alloc_emergency_exception_buf(100)
            micropython.mem_info()
            # Ensure Wi-Fi connection -- loop till it's good
            while True:
                if wlan.status() >= 3:
                    break
                time.sleep(5)
                scroll.scroll_text('...WiFi...', 8, 20)
            network_info = wlan.ifconfig()

            # Make the API call
            response         = requests.get(call)
            response_content = response.content
            response.close()

            # Pull out and keep only the details we need to save memory.
            weather = json.loads(response_content)
            now     = weather["current"]["dt"]
            latest  = weather["current"]["dt"]
            sunset  = weather["current"]["sunset"]
            sunrise = weather["daily"][1]["sunrise"]
            uvindex = '{:.1f}'.format(weather["current"]["uvi"])
            uvmax   = '{:.1f}'.format(weather["daily"][0]["uvi"])
            # Updating our history manually
            for i in range(16):
                history[i] = history[i+1]
            history[16]=weather["current"]["uvi"]
            # Cleaning out big variables for space efficiency
            del weather
            del response
            del response_content

            # Loop to wait until the next update
            while (now <= (latest + wait)):
                if (scroll.is_pressed(scroll.BUTTON_X) or scroll.is_pressed(scroll.BUTTON_Y)):
                    scroll.show_text(uvmax, 16, 0)
                    scroll.show()
                elif (scroll.is_pressed(scroll.BUTTON_A) or scroll.is_pressed(scroll.BUTTON_B)):
                    draw_exposure(history)
                else:            
                    scroll.show_text(uvindex, 16, 0)
                    if now % 5 == 0:
                        scroll.set_pixel(7, 5, 6)
                    scroll.show()           
                time.sleep(1)
                now += 1
            
            if now > (sunset + 900):
                deeply = sunrise - now - 900
                print("Sleeping...", deeply, "seconds.")
                scroll.show_text(' \x0a ', 16, 0)
                scroll.show()
                time.sleep(deeply)
    except:
        sys.exit()
            

if __name__ == "__main__":
    main()
