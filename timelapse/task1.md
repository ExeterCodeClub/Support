# Task 1 Resources
**This document contains some of the resources you'll need to get started with
setting up the picamera.**

**Aim:** Your goal is to make sure that the pi can be used to take good pictures. There are a number of settings that can be applied to make the camera work in different ways. Once you have got the camera working, you can experiment with your own ideas and play with the camera.

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

### Step 1
First you'll need to get the raspberry pi detecting the picam.

Type in the following command,

```bash
sudo raspi-config
```

If it asks for a password, it is `raspberry` by default.

Dig around for the option to turn on the raspberry pi camera, and activate it, you can use the arrow keys and return key.

Once you've done this, quit the menu and type the command `reboot` (make sure you haven't got any unsaved files open).


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

Now type `ls` to see if there is a file called image.jpg, if it exists then the camera is working. 

Find the name of your pi's web browser by looking in the programs menu (top left), and use it to open the image file with the following command (replacing `<browsername>` with e.g. chromium, or firefox)

```bash
<browsername> image.jpg
```


If it doesn't exist, then try running the command

```bash
vcgencmd get_camera
```

Find where it says supported=x and detected=y. x and y will be either 1 or 0, we want them both to be 1. Make sure you check how the ribbon cable is inserted, looking at the checklist above. 

After you have fiddled with it a bit, try running that command again to check the status.

