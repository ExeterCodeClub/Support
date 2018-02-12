# Task 2 Resources
**This document contains the resources you'll need to get started with writing the program logic**

**Aim:** Your goal is to write a control script which will set the time between timelapse frames, and name the files properly. You will make the raspberry pi run this script when it is turned on.

**Links:** 

**Note:** No note.


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

### Summary of aims
- create a while loop which stops at a certain time
- save files in a folder
- name files with the time they were taken
- possibly add some new features like motion detection
- make the pi start the script on boot

### Step 1
For this project, a while loop will be needed to keep the code running for as long as we want it to. The idea is to create code that takes one picture, then loop/repeat the code as many times as you need. 

A while loop looks like this

```python
while True:
    print('loop')

print('finished')
```

The while statement in the first line checks whether the expression between the word `while` and the colon `:` is true after each loop. Since `True` itself is always true, the loop will run forever. It will run the indented code underneath the while statement, but will it print the word 'finished'? Press `ctrl c` to cancel the loop.

Code that looks like like 

```python
a=1
while a<2:
    print('loop')
```

will also run true forever, but this will be the starting point for how we move forward. We need to write something that will change with every loop until the statement is no longer true, which will cause the loop to stop running when we want it to.


```python
i=1
while i<10:
    print('loop{}'.format(i))
    i += 1
```

See now that the loop depends on a variable `i` being less than 10, and that variable is increased by 1 on the final line every loop. In the first line inside the loop, it prints out the word 'loop' with the variable stuck to the end. To print variables as strings, you need to write `'...{variablename}...'.format(variablename)`, notice the curly brackets which have the variable inside '{...}', if you fail to write the curly brackets, it'll print out exactly what you type. (Note: there are other ways to format strings, this one is usually the least painful. try `'a'+ str(1)`, for example)

Hopefully you've got the code running by now. Maybe you saw that it finished really quickly, can you think of some ways to make it take longer?


SPOILERS: One way would be to increase the number 10 to a big number like 10000. Another way is to make the code wait between each loop.

To make the code wait, you need the sleep function

```python
import time

i=1
while i<10:
    print(f'loop{i}')
    i += 1
    time.sleep(1)
```

Now this code imports a module called time, which contains the sleep function, see on the last line that sleep will be called (the notation to call a function that a module contains is `module.function()`). Try running it now, then try changing the argument (input) being given to sleep() and see what it means.

To do timelapse photography, it would be easier to tell the code what *TIME* we wanted the code to finish, and not have to tell it "stop in 92392395 loops, please". This means we need a truth statement like `timenow < finishtime`, which will turn false when timenow becomes greater than finishtime.

```python
import time


datestring = "00-00-00 00:00:00"

finishtime = time.strptime(datestring,"%Y-%m-%d %H:%M:%S")
finishtimeseconds = time.mktime(finishtime)

print('the loop will stop on {}, which is {} seconds away'.format(finishtime,finishtimeseconds - time.time()))
```

This code converts a date given as yy-mm-dd hh:mm:ss into a format the while loop can use easily. The variable `finishtimeseconds` is the number of seconds between our set date and some date far in the past, which makes it easier to compare with the current time (in the same format) than to use dates and times of day. Put in a future date so that the code prints a positive number of seconds. (Note: we don't care about that date which is set long in the past, but it's convention to use 1st Jan 1970.)

You should now be able to create a while loop which finishes at a certain time on a certain day.

```python
import time

datestring = "00-00-00 00:00:00"

finishtime = time.strptime(datestring,"%Y-%m-%d %H:%M:%S")
finishtimeseconds = time.mktime(finishtime)

i=1
while time.time() < finishtimeseconds:
    print('this is loop {}'.format(i))
    i+=1
    sleep(1)
```

Try get it to stop after one minute.

Maybe you could add more code which allows a user to type in how many days they want to run the code for. You'll have to find out how to automatically get the current datetime, convert it into seconds, add the number of seconds in a day onto it (or some multiple of it), then use the result as the finish time.


### Step 2
test that we can save files in the right place with good names
sensible naming scheme
sensible save folder
discover location, `pwd`
output dummy files, `name=f'blah{i}', dummy=open(name,'w'): dummy.write('hello'), dummy.close()`



It's a good idea to test that you will be able to write files properly. They need to be in the right place with names that are easy to parse (be interpreted) by the code in task3. Python, along with any other language, allows you to write files to the system using file input/output functions.

Test out the following code to see that it works

```python
filename = 'testfilename.blah'
testfile = open(filename,'w')
testfile.write('hello blah')
testfile.close()
```

File input/output always takes the form: open file, read/write file, close file. You must open the file before you may do anything to it, then you can use the <file>.write(), or <file>.read() methods. Finally you need to close the file before the script finishes, otherwise the system will think python still needs access to that file, blocking others from using it in the meantime. The open function has four main options, `'x', 'w', 'r', and 'a'`, which mean create (and write), write, read, and append, respectively. Append means to add data to the end of the file, rather than overwriting with the write command. You cannot write a file when opening in read mode, and vice versa. 

If everything went well, there should now be a file with whatever name you gave it, somewhere on the system. You didn't actually tell the code where to save it, so it just assumed where to put the file. 

To find it, open up a terminal and type the following, replacing <..> with the appropriate text

```bash
find / -name <filename>
```

It should spit out the full pathname of the file. See that it's in the same folder as your python script (unless you told it otherwise). In general, programming languages will operate by default on the directory where the script is running.

To save a file in another directory, you need to use either the 'absolute' or 'relative' pathnaming scheme. Pathnames are the file path and the filename stuck together, so '/home/pi/' is the path the folder, and 'file.txt' is the filename.

Relative pathnames are interpreted relative to the folder that the python script is in. There is a little bit of notation to understand. If the script is in the home folder for pi, with its pathname `/home/pi/script.py`, then to save a file in the folder above, with path `/home/`, you would write `../file.txt`, as its 'filename' in the open() function. The `..` means 'folder above this one'. To save the file in a folder that's inside `/home/pi/`, then you would write `foldername/file.txt`. 

Absolute pathnames are always relative to the root directory `/` (just a forward slash), which is the highest directory in the system. They are more exact, and are useful when you need to save files far away from where the script is saved. To save a text file in the system temporary folder, you would write `/var/tmp/file.txt`, notice the slash at the start, if you forget that then python will assume you mean relative pathname and not absolute. To save a text file directly in the pi home folder you would write `/home/pi/file.txt`.


It might be worth creating a folder named after the current date, ready to save the files into. That's easy to do by hand, but that would be boring. 

```python
import os, time

currdate=time.strftime('%Y-%m-%d',time.gmtime(time.time()))

if os.exists(currdate):
	os.mkdir(currdate)

testwrite=open('{}/testfile.txt'.format(currdate),'x')
testwrite.write('hello')
testwrite.close()
```

This script gets the current date in yyyy-mm-dd format, then checks that the folder does not first exist, then tries to create the folder. If you type help(time.strftime) into a python console, etc, you'll get information on what is going on.

Hopefully you'll see a file inside the folder, newly created.


From here, we need to apply a sensible naming scheme to the file, since there are going to be lots of them! A good scheme might be `image-<timeseconds>.jpg`, where you'd use `int(time.time())` to get <timeseconds> (remember to use ''.format()). This would put all of the files in order as pictures are taken, and also date them individually so we know exactly when they were taken. You could also try numbering them.


### Step 3
Now try to merge the two concepts you have encountered by creating unique well-named files inside a date-terminating while loop.

Make sure you only create a new folder before the while loop, otherwise you'll have a new one for every day, which would split apart the time lapse images which wouldn't be very helpful.

### Step 4
You can make any additions you would like here, an example could be to add a pir sensor to detect movement and change the rate of photography as a result. Look online or find the christmas project files to see how to use the pir sensor again.

Let's say we want the script to take a picture every ten seconds, but when someone is around to trigger the sensor, take a picture every two seconds instead (that would make for an interesting effect!)

This could be done like the following (written in pseudocode)

```pseudo
sleeptime := 10

while currenttime < endtime
	if motion is detected
		sleeptime := 2
	else
		sleeptime := 10
	
	write file with name 'image-<currenttime as integer>.jpg'

	sleep for sleeptime seconds
```

Have a think how you might use the other modules to give some interesting effects.

### Step 5
It would be a good idea to make the code a little more fault tolerant by getting it to start on boot.

To prepare your script, make the following line the very first line of the script

```python
#!/usr/bin/python
```

This tells the system what interpreter to read the file with (it has a choice from languages like python, perl, and bash)

Before you make it run on boot, make sure the script is not trying to make a directory or file inside `/etc/init.d/`, since it might break things or be denied. Instead it should try to create the folder and files inside `/home/pi/`, where we have easy access to them.

Test that your script creates files etc where expected by running the following commands one after the other

```bash
chmod a+x <your script name>

./<your script name>
```

The command `chmod a+x` makes a file executable, and `./filename` is notation to run a user script in the terminal (rather than using an IDE.)

To make the pi run a script on startup, the script needs to be placed inside the folder `/etc/init.d/`, which will require administrator permission. Run the following lines one after the other in the console

```bash
sudo mv <your script name> /etc/init.d/
sudo update-rc.d /etc/init.d/<your script name> defaults
```

Making sure you're in the same directory as your script when you use `mv`, otherwise you'd use the pathname of the script (something like /home/pi/script.py.) 

Try restarting the pi, and logging in. Check the folder where you told the script to create files, and see whether new files are being created over time. If this is working, you are very nearly finished.


### Step 6
Finally you'll need to integrate a function from task1 into your code to actually take the pictures.

Move the script into the same directory as your script (`/etc/init.d/`), then add the following line

```python
import task1
```

assuming the name of the script is task1.py

If created as instructed, the function expects a single argument, the filename, meaning you can replace your code which creates files with the following line

```python
task1.takePic(filename)
```

That's it, probably time to debug.

