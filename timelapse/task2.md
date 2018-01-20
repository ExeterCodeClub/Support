# Task 2 Resources
**This document contains some of the resources you'll need to get started with writing the program logic**


**Aim:** Your goal is to write a control script which will set the time between timelapse frames, and set the filenames in a useful fashion. You will make the raspberry pi run this script when it is turned on.

**Links:** This [website](https://www.raspberrypi.org/documentation/usage/camera/python/README.md) shows you how to set up and use the picamera

**Note:** When asked to type in a command, it means that the command should be typed into a terminal, which can be brought up using the key combination `ctrl shift t`, all held down briefly together. For example, "Use the command `ls`", means bring up a terminal new or old, type in the command at the **prompt**, then press the return/enter key. In this case you should see the contents of the current directory listed.

Some things you might now be asking:
 - a **prompt** is a string of characters which tells you where you can type in your next command, it 'prompts' you to type there. 
 - the prompt normally contains a small amount of information for the user, and usually looks like `pi ~ $` or more generally `username currentdirectory $`. In windows powershell it might be `C:/ >`. When you type in a comand e.g `ls`, you should see `pi ~ $ ls`. No need to type the prompt in yourself!
 - If there are lots of prompts, the bottom-most one is the correct one.
 - If the screen is really messy with output, try pressing enter a bunch of times at the prompt to make some space. `shift up` can scroll up.
 - `~` means your user's home directory, which is the same as /home/pi/, the documents directory inside your home folder will show as `~/documents/` 
 - You can move to the documents directory by typing `cd documents`, notice the prompt changes, you can move back up one step by typing `cd ..`. Moving around is a case of using `cd dirname`, where `..` is always the name of the directory above yours, and then using `ls` to see what is inside your new dir. 
 - There are better faster ways to move around, but this is the easiest to learn in five minutes.


### Some code snippet from the picamera documentation
```python
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(300) # wait 5 minutes
```

