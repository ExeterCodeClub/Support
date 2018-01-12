# Timelapse PiCamera Project Outline
### Connor Pettitt - 2018-01-11
**Abstract**: This document aims to outline the basic tasks to follow in order to complete the improvers' timelapse camera project. I believe that we need to provide more structure in order to increase the productivity of each session (and reduce the chaos just a little). We should still aim to allow room for imagination and spontaneity within the design of the project. We will need to figure an effective way to balance the project between everyone.

## Team Categories 
**(which tasks could be considered overarching and separately achievable?)**

1. Setup picam module to take good pictures and store files
2. design program logic (when to take pictures, movement detection?)
3. turn time lapse images into video to watch back over
4. design case to store rpi inside

## Task 1 - PiCam setup scripts with file handling procedure
This task will be almost pure programming to make the picam work, will involve searching for code snippets online. 
### Aims
- to write the set up script to apply correct settings (exposure time, iso, etc), and make changeable via external code (api). 
- the ability take pictures on command 
- to save and output files with useful names
- ...

## Task 2 - Program logic 
This task is about writing the brain behind the system, and should allow a degree of imagination in writing the code. 
### Aims
- trigger the picam to take images every n seconds
- (optional) only work when motion is detected
- (optional) change the exposure settings for interesting effects (play with long exposure + time lapse + leds?)
- ...

## Task 3 - Video replay system
This task will involve building an interface that displays image history to the user in a presentable form. This one might be considered quite difficult.
### Aims
- read the image directory and sequentially display images
- ability to set the time frame which should be displayed (read file names and pick those in range ti < datetime < tf)
- output a video file
- automatically push file to github for them to see at home (this would be a one liner using os/sys system call library - though not sure of exact details)
- ...

## Task 4 - Case design and creation
This task will involve producing a case for the whole system, so we can mount it all somewhere convenient in the library. i've included it so perhaps non-coders could join in. 
### Aims
- Design a case using some cad software or something else
- (opt) laser cutter design
- (opt) 3d printer design
- (opt) hand made
- ...
