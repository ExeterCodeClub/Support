# Task 1 Resources
**This document contains some of the resources you'll need to get started with
setting up the picamera.**

### Aim: Your goal is to make sure that the pi can be used to take good pictures. There are a number of settings that can be applied to make the camera work in different ways. Once you have got the camera working, you can experiment with your own ideas and play with the camera.

### Links:
This [website](https://www.raspberrypi.org/documentation/usage/camera/python/README.md) shows you how to set up and use the picamera

**Note:** When asked to type in a command, it means that the command should be typed into a terminal, which can be brought up using the key combination `ctrl shift t`, all held down (briefly) together, don't press it a million times. For example, "Use the command `ls`", means locate your current terminal (or open a new one if you need to), type in the command at the prompt (it usually looks like `pi ~ $` or `username directory $`, or in windows powershell it might be `C:/ >`) giving you `pi ~ $ ls`, then press the return/enter key. In this case you should see the contents of the current directory listed (`~` means your user's home directory, which is the same as /home/pi/, and `$` is linux for "you are issuing commands as a regular user account").

### Step 1
First you'll need to get the raspberry pi detecting the picam.

Open up a terminal and type in the following command,

```bash
sudo raspi-config
```

If it asks for a password, it is 'raspberry' by default (without the quotes).

Dig around for the option to turn on the raspberry pi camera, you can use the arrow keys and return key.

Once you've done this, quit the menu and type `reboot` into the terminal (make sure you haven't got any unsaved files open).


### Step 2
Now install the picamera into the camera slot (be gentle!)

Ensure that:
    1. the ribbon cable is installed with the blue tab facing the ethernet port
    2. the ribbon is in the slot labelled 'camera', not 'display', between the ethernet port and the hdmi port.
    3. the ribbon is inserted fully into the slot. Notice that you can pull up the little black bit on top, this unlocks the slot. 
Try running the command 

```bash
raspistill -o image.jpg
```

T
    vcgencmd get_camera (Returned supported=1 detected=0)
    Check to make sure ribbon was facing the right way (it was)
    Check to make sure ribbon is all the way in the connector slot (it was)
    Check to make sure ribbon is in proper connector slot: the one between the ethernet port and the HDMI port (it was NOT!)
    Reconnect camera in the proper slot
    vcgncmd get_camera (now returns supported=1 detected=1)
    Good to go!


ivcgencmd get_camera
