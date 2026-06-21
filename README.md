# Boreas

a flight controller for a rocket.


made this project to both learn how to make flight controllers in general for my drone. making it i got some more practice in routing pcbs and how to read datasheets!
the plan for this board is to be used in a rocket im going to make, where hopefully with the gyro and motor pins i can get it to 1km altitude or higher. little ambitious for my first rocket project but i tihnk it should be fine! for its kind of a big pcb so it'll be hard to fit on the rocket but itll work fine i think. also the sd card will be useful to gain cool telemetry, and i plan to use it to generate interesting graphs that can tell me how to improve the rocket further.


it uses an STM32F7 as an mcu, connected to an imu, barometer, and magnometer. it also has 3 leds, two buttons, a buzzer, and 3 servo motor pins. it can also charge lipo batteries through usb-c! lastly it has an sd card reader for data display!


## Poster (Zine)
![poster](assets/POSTER.png)

## Render
![render](assets/RENDER.png)

## Schematic
![schem](assets/SCHEMATIC.png)

## PCB
![pcb](assets/PCB.png)

## To use

1. plug assembled PCB into computer
2. run ```make flash``` in firmware path after pressing boot and reset buttons to enter flashing mode on the STM32

## BOM

|Item    |Price (USD)|
|--------|-----------|
|PCB     |2          |
|PCBA    |198.65     |
|Shipping|26.51      |
|        |           |
|Total   |227.16     |
