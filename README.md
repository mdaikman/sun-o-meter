# sun-o-meter
This is a UV meter project that I made to go beside my front door to encourage skin protection.
It runs off of the OpenWeatherMap API.

Time Estimate
=============
This is not too hard. A day or a weekend depending on your skill.

Requirements
============
Arduino Pico W
Pimoroni Pico Scroll Pack
Micropython for this device (https://shop.pimoroni.com/products/pico-scroll-pack?variant=32369496653907)
USB power for your Pico of your choosing

Optional
========
3d printer if you want to print the model I made
(I recommend having fun and building your own)

Usage
=====
1. Get a free API key from OpenWeatherMap.org
2. Get the Pimoroni custom Micropython 
3. Put Micropython on your Pico W
4. Attach the Pico Scroll
5. Edit main.py to include the relevant for your location and your API key at the top
6. Using an editor like Thonny, upload the Micropython sketch and test
7. Place the Pico W and Scroll Pack in the model of your choosing

Functionality
=============
* From just before sunrise to just after sunset, the meter will display the UV index on the front.
* Between sunset and sunrise, it will just show a smiley face. :)
* Press any of the side buttons to show a graph history of the UV in 15 minute increments to see if it is going up or down or is spotty.

Notes
=====
- This was made via the OpenWeatherMap API because it is free and reliable, unlike trying to weather proof an outdoor UV sensor for Arduino.
- It is NOT recommended to change the wait period (900 => 900 seconds = 15 minutes) as the API does not update any faster and you will eat through your free API calls.
- It is HIGHLY recommend to add a difuser to the front of the scroll pack. It makes it look nicer and easier to read and easier to press buttons.
    - The one I had use is not mine and is no longer available. Make your own or look for one like this: https://www.thingiverse.com/thing:4771704
    - Different difusers will likely need to have their size altered too to fit over your scroll pack.
- The history report only records UV index values between 1-7 being only 7 pixels high.
    - Anything below 1 is considered too low to worry about.
    - Anything above 7 is already well into problem territory. Take care of your skin!
- Read more about the UV index values here: https://www.canada.ca/en/environment-climate-change/services/weather-health/uv-index-sun-safety.html
