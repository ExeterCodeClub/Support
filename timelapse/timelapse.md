# Timelapse PiCamera Project Outline
### Connor Pettitt - 2018-01-11
**Abstract**: This document aims to outline the basic tasks to follow in order to complete the improvers' timelapse camera project. I believe that we need to provide more structure in order to increase the productivity of each session (and reduce the chaos just a little). We should still aim to allow room for imagination and spontaneity within the design of the project. We will need to figure an effective way to balance the project between everyone.

### Allocations
**Task 1, camera setup** All
**Task 2, program logic** Bradley
**Task 3, video upload** John
**Task 4, case design** Tom, Tom, Marcus

### Links
- [project inspiration](https://www.raspberrypi.org/forums/viewtopic.php?t=72435)

## Team Categories 
**(which tasks could be considered overarching and separately achievable?)**

1. Setup picam module to take good pictures and store files
2. design program logic (when to take pictures, movement detection?)
3. turn time lapse images into video to watch back over
4. design case to store rpi inside

## Task 1 - PiCam setup scripts with file handling procedure
This task is to make the picam work and take good pictures. tutorial found [here](https://github.com/ExeterCodeClub/Support/blob/master/timelapse/task1.md).

### Aims
- to write the set up script to apply correct settings (exposure time, iso, etc), and make changeable via external code (api). 
- the ability take pictures on command 
- to save and output files with useful names
### Items
- rpi
- picam module
- OR usb webcam, since some pis i tested had difficulty detecting the picam i own

## Task 2 - Program logic 
This task is about writing the brain behind the system, tutorial found [here](https://github.com/ExeterCodeClub/Support/blob/master/timelapse/task2.md).
### Aims
- trigger the picam to take images every n seconds
- (optional) only work when motion is detected
- (optional) change the exposure settings for interesting effects (play with long exposure + time lapse + leds?)
- ...
### Items
- rpi
- sensor modules
- a set of testing images

## Task 3 - Video replay system
This task is about turning the images into a video, tutorial found [here](https://github.com/ExeterCodeClub/Support/blob/master/timelapse/task3.md).
### Aims
- read the image directory and sequentially display images
  - python library to display an image to the screen, 
  - use library to control the resulting gui (matplotlib has such functions)
  - case of adding image1, waiting, deleting image1, adding image 2 ... to act as a 'video' feed
- ability to set the time frame which should be displayed (read file names and pick those in range ti < datetime < tf)
  - break down the filename into a date format
  - check if date > or < ti and tf, python library will help with this
- output a video file
  - [rpi images -> video solution](https://unix.stackexchange.com/questions/98602/convert-images-into-avi-with-raspberry-pi#98607)
  - e.g. os.sys('ffmpeg image%.jpg')
- automatically push file to github for them to see at home 
  - this would be a one liner using os.system('git push') after setting up a github connection  
### Items
- rpi
- a set of testing images
### Prerequisites
- install a video encoding library for the pi to use

## Task 4 - Case design and creation
This task is about making a nice looking case for the camera, tutorial found [here](https://github.com/ExeterCodeClub/Support/blob/master/timelapse/task4.md).
### Aims
- Design a case 
  - use of supplied cad software on pi maybe
- (opt) laser cutter design
- (opt) 3d printer design
- (opt) hand made
### Items
- cad software
- drawing stationery
- 3mm acrylic sheet
- 3mm mdf sheet
- polystyrene
- craft knife
- glue
- stuff from fablab ..
