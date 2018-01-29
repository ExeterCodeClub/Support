# Task 1 Resources
**This document contains the resources you'll need to get started with setting up the picamera.**

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

Now type `ls` to see if there is a file called image.jpg, if it exists then the camera is working, otherwise skip the next step.

Find the name of your pi's web browser by looking in the programs menu (top left), and use it to open the image file with the following command (replacing `<browsername>` with e.g. chromium, or firefox)

```bash
<browsername> image.jpg
```


If the file `image.jpg` doesn't exist, then try running the command

```bash
vcgencmd get_camera
```

Find where it says supported=x and detected=y. x and y will be either 1 or 0, we want them both to be 1. Make sure you check how the ribbon cable is inserted, looking at the checklist above. 

After you have fiddled with it a bit, try running that command again to check the status.


### Step 3
This is great, you can now take pictures with the camera by hand. If you would like to sit in the library for the next three weeks typing `raspistill -o image1.jpg...` every ten seconds, then the project is complete!

Otherwise, you will need to create a script that can be controlled by the pi itself automatically.

Open up a python IDE (any python testing environment) such as Thonny, or IDLE, and find the text editor.

Type the following into the editor (this is not a terminal, just enter the text) then save it to somewhere easy to find, like `Documents` or `Desktop`. Call your file findsettings.py

```python
import picamera
camera = picamera.PiCamera()
camera.capture('pythonimage.jpg')
camera.close()
```

The first line imports the module which allows you to easily control the picamera. 

The second line creates a camera 'instance' which is a virtual representation of the real picamera on the pi, so if you run one of the allowed commands on this instance, the actual camera should behave accordingly.

The third line is a command that tells the camera to take a picture (much like we were doing by hand!). 

The fourth line ensures that the virtual camera is deleted, and frees up the link to the picamera.

Run the script by finding the run button somewhere in the IDE and pressing it. Usually `ctrl s` to save, then `F5` works as well. 

If it runs without errors, check that there is a file called pythonimage.jpg in your chosen directory (e.g. `Documents` or `Desktop`).



### Step 4
Change the script to look like this (you'll see why in a minute)
```python
import picamera
camera = picamera.PiCamera()
camera.capture('original.jpg')

#settings go below here 


#settings go above here 

camera.capture('altered.jpg')
```

Lines beginning with `# ... ` are comments, they do nothing but tell the person  who is reading the script something they should know, it can be a little note, a warning, a smiley face.

The following is a list of camera settings which will alter the way that the images look

```python
#change the quality of the camera image
camera.resolution = (1280, 720)

#flip the image horizontally or vertically
camera.hflip = False
camera.vflip = False
camera.rotation = 0

#cut the edges of the image off
camera.crop = (0.0, 0.0, 1.0, 1.0)

#change how sharp lines are in the image
camera.sharpness = 0

#change the difference between the darkest and the lightest pixels (low contrast means light and dark colours become kind of grey instead, high contrast means that dark things look really black, and light things look really white)
camera.contrast = 0

#change how bright the image looks
camera.brightness = 50 #take a guess what this does
camera.saturation = 0 #adds more colour
camera.ISO = 0 #changes the sensitivity of the camera, high iso is good for low light
```

Try inserting those settings into your script and seeing how they alter the original image when you change the values. Some values might be limited to a certain range like 0-1, or 0-100 (no need to copy the comments out). If you think a particular setting might as well be left alone, 'comment it out' by adding a `#` to the start of the line.

Run the script to check that there are no errors, then see the output files.

### Step 5
Once you've put the settings into your script, you can try to automate the process of finding your perfect image.

This step will require a for loop, and for loops take the form

```python
ilist=[1,2,3,4]
for i in ilist:
    print(f'loop {i}')
    print(i)
    print()
```

In python you can 'loop over' lists, which look like `[1,2,3,4,5]` or `['asfda','ashrg','abcd']` or `[1,2,'three','four']`, you can have numbers and strings in a list, and they can be as long as you like. 

A for loop runs a block of code once for each item in the list. The block of code must be indented, and by the same number of spaces.

In the snippet above, `i` and `ilist` are variables, which you choose the names of. The second variable needs to be a list, whether one that has already been created or a list expression like this `for i in [1,2,3,4]:`.

The first variable (`i`) is newly created at the start of the loop, and gets its value set to each successive item in the list (`ilist`) with every loop, starting at the first item.

One of the print statements has the line `f'loop {i}'` inside it, this is python for "insert variable `i` into this string". Note that the string must start with an f, otherwise it will literally print `'loop {i}'` instead of `'loop 2'` (if `i=2`).

Have a guess at what will happen when if you run the above code. Try opening another python file in your IDE, putting it into the text editor, then running it.


Modify findsettings.py to contain a for loop which will change a particular setting, while leaving the rest alone, use the following as an example

```python
import picamera
from numpy import arange        #<<< this is new
camera = picamera.PiCamera()
camera.capture('original.jpg')

#settings go below here 

camera.resolution = (1280, 720)
camera.hflip = False
camera.vflip = False
camera.rotation = 0
camera.crop = (0.0, 0.0, 1.0, 1.0)
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50 #take a guess what this does
camera.saturation = 0 #adds more colour
camera.ISO = 0 #changes the sensitivity of the camera, high iso is good for low light

#settings go above here 

min=0
max=100
step=10
setting='brightness'

for settingValue in arange(min,max,step):

    camera.brightness=settingValue

    camera.capture(f'altered{setting}{settingValue}.jpg')
    print(f'picture taken with {setting} setting value: {settingValue}')
    sleep(0.5)
```

The arange function creates a list with its first number as `min`, and with each number increasing in steps of `step` until it reaches the final number `max`.

Can you see what will happen with this loop? 

Look through the output images to see which one looks the best, note down which setting value it was on, then replace the setting in the loop with another from the list that you want to investigate. 
e.g. move `camera.brightness=70` up to the settings list, put `camera.ISO=settingValue` into the loop, change the variable `setting` to iso with `setting='iso'`, and change the variables `min`,`max`,`step` to the appropriate values (try `0`,`800`,`100`).

Settings and their ranges (min,max) you might want to play with include 
 - brightness (0,100)
 - rotation   (0,360)
 - sharpness  (0,find out!) < probably (0,100)
 - contrast   (0,find out!)
 - saturation (0,find out!)
 - ISO        (0,800)

once you have found the settings you would like to use, save then continue to the next step.



### Step 6

Now you have the absolute basic functionality for the script, it is time to start adding the ability for another script to control yours. this is what Task2 with the program logic tries to take advantage of.

Save your file with a new name camerapic.py, such that it has all the same contents, you will be modifying it to interface (or interact with) another python script.

This step requires the use of a function, and functions take the form

```python
def funcname(argument1,argument2):
    print('I will now add the two arguments together')

    added = argument1 + argument2
    print(f'This is the result: {added}')

    return

print('calling functions')
funcname(1,2)
funcname('hello ','world')
```

A function is a block of code much like any other code you've written so far, except that you need to define it before you can use it. They are helpful because they can be reused as many times as needed without having to rewrite the entire block out again, with different inputs (or 'arguments', but not the kind you have with your parents).

First is the function definition, which starts with the line `def funcname(argument1,argument2):` and ends with `return`, all functions need to start with `def <insert function name>(<insert arguments>):`, but they don't have to end with `return`, find out what it does when you get the chance. All functions need to have an indented code block of at least one line inside them (like `for` loops).

Try copying the above code into a new file, then run that file. 

Notice that 'calling functions' is the first output. This is because a function definition doesn't do anything on its own, the function must be 'called', which is what the script does in the lines below `print('calling functions')`. By now you are familiar with the `print` function, try typing just `print` into a python terminal, it tells you that it is a function definition! However `print(argument)` is an example of a function 'call', and calls do something with the argument they're given. So the python notation to call a function is to add `()` to the end of the function definition, with the required arguments inside the brackets.


Modify camerapic.py to look like the following (while using the settings you've found to work best)

```python
import picamera
camera = picamera.PiCamera()

def init(cam):
    cam.resolution = (1280, 720)
    cam.hflip = False
    cam.vflip = False
    cam.rotation = 0
    cam.crop = (0.0, 0.0, 1.0, 1.0)
    cam.sharpness = 0
    cam.contrast = 0
    cam.brightness = 50 #take a guess what this does
    cam.saturation = 0 #adds more colour
    cam.ISO = 0 #changes the sensitivity of the camera, high iso is good for low light
    cam.brightness=50
    
    print('Camera initialised.')

def takePic(cam,num):
    cam.capture(f'image{num}.jpg')

if __name__ == 'main':
    init(camera)
    takePic(camera, 1)
```

As you can see, this script has two functions inside it. 

The first function takes one argument `cam`, and changes its settings. It is expecting `cam` to be a virtual camera object, so if you called `init('cows')` for example, it would crash.

The second function accepts two arguments `cam` and `num`, then uses `cam` to take a picture and output a file with `num` in the name. As you might expect, `cam` is treated as a camera object, while `num` can be either a string or a number.j

Now run the script. It should output a file with the name image1.jpg.

Notice the line that says `if __name__=='main':`, that is python for "if this script is being run directly by hand, do the stuff in the indented block below. Otherwise, don't do anything."

The script is now ready, and this part of the project is finished.
