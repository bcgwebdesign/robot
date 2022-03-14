# Experiments with Pi Zero robot arm

## Parts List
- [DIYmore 6dof robot arm on amazon](https://www.amazon.co.uk/diymore-Aluminium-Mechanical-Robotic-Servos/dp/B08PDKP23X)
- [Pi Zero (1st gen)](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
- [Servo Hat](https://www.amazon.co.uk/Waveshare-16-Channel-Servo-Driver-HAT/dp/B07GYFTKZD/ref=sr_1_3?keywords=adafruit+servo+hat&qid=1647255859&sprefix=adafruit+servo%2Caps%2C75&sr=8-3)
- Various connectors servo cable extenders
- [PSU for the Hat](https://www.amazon.co.uk/Adapter-Display-Adjustable-Voltage-Universal/dp/B09DKXZLC5/ref=sr_1_3?keywords=3v+to+24v+power+supply&qid=1647256284&sprefix=power+adaptor+3v+to+24v%2Caps%2C150&sr=8-3)
- [Upgrade shoulder and elbow servo to 25kg/cm servos](https://www.amazon.co.uk/gp/product/B099PSWMJP/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
- Metal horns(?) for the servos

## The code (outline for now)
All in python
- Flask for communicating with the code via a web front end
- Some easing functions to make the servos start and finish smoothly
- multithreading to allow all servos to move in parallel
- and my own experiments to try to get all servo moves to start and finish at the same time

## TODO
- Organise code structure properly in line with Flask setup
- Better ajax(?) communication with the flask server
- graphical sliders for position
- limits on inputs!!!
- graphic of arm position??
- Inverse kinematics? ie just say where you want the gripper to be and the rest is worked out?

