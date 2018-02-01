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
- learn while loops
- control script to set time between loops
- name output files properly
- save them in the right place
- use motion detection to take pictures
- alter raspberry pi settings to start script on boot
- call another script to take pictures 


### Step 1
For this project, a while loop will be needed to keep the code running for as long as we want it to. The idea is that to define code that takes one picture, then the loop repeatedly runs that code as many times as you need. Try copying these bits of code into a python editor and see what they do as you move through the project.

A while loop looks like this

```python
while True:
    print('loop')
```

The while statement in the first line checks whether the expression between the word `while` and the colon `:` is true after every loop. Since `True` itself is always true, the loop will print 'loop' forever (but we don't want it to run forever, we want it to run for a long time)

If you were to write `while 1<2:` instead, this would also always be true because 1 will always be less than 2. So we will need to figure out something that will change with every loop until the statement is no longer true, and that will cause the loop to stop running when we want it to.

```python
i=1
while i<10:
    print(f'loop{i}')
    i += 1
```

See now that the loop depends on a variable being less than 10, and that variable is increased by 1 on the final line every loop. In the second line, it prints out the word 'loop' with the variable stuck to the end. To print variables as strings, you need to write `f'...{variablename}...'`, notice the 'f' and the curly brackets which have the variable inside '{...}'.

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

Now this code imports a module called time, which contains the sleep function, see on the last line that sleep will be called. Try running it now, then try changing the argument (input) being given to sleep() and see what it means.

To do timelapse photography, it would be easier to tell the code what TIME we wanted the code to finish, and not have to tell it "stop in 92392395 loops, please". This means we need a truth statement like `timenow < finishtime`, which will turn false when timenow becomes greater than finishtime.

```python
import time


datestring = "00-00-00 00:00:00"

finishtime = time.strptime(datestring,"%Y-%m-%d %H:%M:%S")
finishtimeseconds = time.mktime(finishtime)

print(f'the loop will stop on {finishtime}, which is {finishtimeseconds - time.time()} seconds away')
```

This code converts a date given as yy-mm-dd hh:mm:ss into a format the while loop can use easily. Finishtimeseconds is the number of seconds since some set date in the past, and it is much easier to compare one number like seconds than it is to compare dates and times of day. See if you can get put in a future date so that it is a positive number of seconds away.

You should now be able to create a while loop which finishes at a certain time on a certain day

```python
import time

datestring = "00-00-00 00:00:00"

finishtime = time.strptime(datestring,"%Y-%m-%d %H:%M:%S")
finishtimeseconds = time.mktime(finishtime)

while time.time() < finishtimeseconds:
    print(f'this is loop {i}')
    sleep(1)
```

Try get it to stop after one minute.


## More steps to come

### Step 2
test that we can save files in the right place with good names
sensible naming scheme
sensible save folder
discover location, `pwd`
output dummy files, `name=f'blah{i}', dummy=open(name,'w'): dummy.write('hello'), dummy.close()`

### Step 3
set up pir sensor to detect people walking by
when detected, take images every ten seconds for e.g. ten minutes, and then stop

### Step 4
set the pi up to run the script on boot
`cd`
initrc config file is the place to go

### Step 5
wait for task1 to finish to insert code import task1, task1.takePic(name,num))

