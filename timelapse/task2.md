# Task 2 Resources
**This document contains the resources you'll need to get started with writing the program logic**

**Aim:** Your goal is to write a control script which will set the time between timelapse frames, and name the files properly. You will make the raspberry pi run this script when it is turned on.

**Links:** 

**Note:** When asked to type in a command, it means that the command should be typed into a terminal, which can be brought up by pressing `ctrl shift t` briefly at the same time. For example, "Use the command `ls`", means bring up an old or new terminal, type in the command at the **prompt**, then press the return/enter key. In this case you should see the contents of the current folder listed.

Some things you might now be asking:
 - a **prompt** is a string of characters which tells you where you can type in your next command, it 'prompts' you to type there. 
 - the prompt normally contains a small amount of information for you, and usually looks like `pi ~ $` which is telling you `username currentfolder $`. In windows powershell it is `C:/ >`. When you type in a comand e.g `ls`, you should see `pi ~ $ ls`. No need to type the prompt in yourself!
 - If there are lots of prompts, the bottom-most one is the correct one.
 - If the screen is really messy with output, try pressing enter a bunch of times at the prompt to make some space. `shift up` can scroll up.
 - `~` means your home folder, which is the same as /home/pi/
 - You can move to the documents folder from your home folder by typing `cd documents`, notice the prompt changes, you can move back up one step by typing `cd ..`. Moving around is a case of using `cd foldername`, and then using `ls` to see what is inside your new folder. If you get lost, type `cd` to return home. 
 - There are faster ways to move around, but this is the quickest to learn. 


### a code snippet from the picamera documentation
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

# draft
