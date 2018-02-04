# Task 3 Resources
**This document contains the resources you'll need to get started with writing the video creator**

**Aim:** Your goal is to write a program that can convert a set of images into video format, and then upload it to the internet automatically for you to see!

**Links:** 

**Note:** When asked to type in a command, it means that the command should be typed into a terminal, which can be brought up by pressing `ctrl shift t` briefly at the same time. For example, "Use the command `ls`", means bring up an old or new terminal, type in the command at the **prompt**, then press the return/enter key. In this case you should see the contents of the current folder listed.

Some things you might now be asking:
 - a **prompt** is a string of characters which tells you where you can type in your next command, it 'prompts' you to type there. 
 - the prompt normally contains a small amount of information for you, and usually looks like `pi ~ $` which is telling you `username currentfolder $`. In windows powershell it is `C:/ >`. When you type in a comand e.g `ls`, you should see `pi ~ $ ls`. No need to type the prompt in yourself!
 - If there are lots of prompts, the bottom-most one is the correct one.
 - `~` means your home folder, which is the same as /home/pi/
 - You can move to the documents folder from your home folder by typing `cd documents`, notice the prompt changes, you can move back up one step by typing `cd ..`. Moving around is a case of using `cd foldername`, and then using `ls` to see what is inside your new folder. If you get lost, type `cd` to return home. 
 - There are faster ways to move around, but this is the quickest to learn. 

In Bash, there are lots of commands that can do simple or complex things. You will be using some of the basic commands in bash to move around between folders (`cd`), move files (`mv`), copy files (`cp`), make folders (`mkdir`), and look inside folders (`ls`). Then you will get to use a more powerful command which converts files into videos (`ffmpeg`). These are all the same commands that happen when you use a mouse to move between folders on your computer, or use a program to make videos, except now you are typing them in instead of clicking with a mouse. It can be more powerful this way because you can write scripts which do any task you want hundreds of times over.

# Summary of aims
- find location on filesystem, `pwd`
- find full path of images folder, `path='/home/pi/...'`
- look inside images folder `ls /.../task3-img`
- copy images folder to keep original as backup
- count and rename all of the files to get img-000001.jpg, img-000002.jpg, ...
- write video to file using shell command, `ffmpeg -r 10 -i img-%02d.png -c:v libx264 -pix_fmt yuv420p -y output.mp4`
- set up git (with the help of leader)
- `git add output.mp4`, `git commit -m "save video output"`, `git pull, git push`

### Step 1
You have been supplied with a folder that contains some test images to make a video out of, ready to use on the real set of images later on. You will need to keep this set of images safe just in case something goes wrong.

Open up a terminal and type in the command `pwd` to find out which folder you are in (it stands for path to working directory). 

You need to locate a folder called 'task3-img', there's a trick you can do to see where it is

```bash
find /home -name task3-img
```

This is running the command `find` inside the `/home` directory, looking for folder/filenames which look like 'task3-img'. If the folder exists and you typed it correctly, you should see a line which tells you the full path to the folder, which might look like `/home/pi/blah/task3-img`.

You want to copy the contents of that folder into a new folder we can mess aroudnd with, without worrying about deleting everything. 

Run the command `mkdir testimages`, then `cp <location of task3-img>/* testimages/`, where <location of task3-img>  is whereever the find command told you it was; /home/pi/blah... Here you are creating a new folder called testimages, then copying the contents of the task3-img folder into it. Type `ls testimages` to check that the contents were copied properly.

Open another terminal and then open an editor by typing `leafpad`, or `nano`, then put the following into it

```bash
#!/bin/bash

workfolder=testimages
images=
```

This is a Bash script (Bash is another programming language for linux), which automates things you can do by hand on the terminal.Currently it sets the variable `workfolder` to the word "testimages", and `images` to nothing.

Copy the location of the folder with the images in it (found with the command `find ...`) to the line that says 'images=', so you are left with a line like `images=/home/pi/...`.

Now you need to add some lines which will copy the images folder to your workfolder.

```bash
#!/bin/bash

workfolder=testimages
images=

echo "copying files..."
rm $workfolder/*
cp $images/* $workfolder/
echo "done."
```

`Notice that in Bash, we assign values to variables (like assigning `x=5` in python) by using an `=` sign, and we get the value out of it (like the value `5`) by adding a dollar sign to the front of the variable name (like `$x`). In this case, where ever Bash sees `$workfolder`, it replaces it with the word "testimages". If we assigned the value 20 to the variable name banana, with `banana=20`, we can get that value from banana by doing `$banana`.

The command `rm` removes or deletes files for you. See that it says `rm $workfolder/*`, that means it is set to delete every file inside the testimages folder, where '/' means 'inside of this folder' and '*' means every single file.


The command `cp` copies folders and files to other locations. It can overwrite files, so be careful where you copy to. In this case, we are copying the 'images' folder to a work folder called 'workfolder'.


Now save the file with the name `resetimages.sh`, we can use this script to undo any mistakes made with the images. 

Make the script executable by typing the command.

```bash
chmod +x resetimages.sh
```

To make executable means the computer will allow us to run it without complaining, otherwise it will deny access because it hasn't been told that the file should ever be run. It's a security thing.

Check the file over to see that it's going to do what we expect (maybe ask a helper).

Now try running it with `./resetimages.sh`.

Did it work?


## Step 2
Now it is time to rename all of the images, because we cannot expect them to be numbered nicely for us. Also, one or two might be missing, which would confuse the video editing program.

First you should try renaming one of the files to see how it works. Type the command `ls` to see the best file to rename (the best file would be the first in the list), then type the command `mv <best filename> image-000001.jpg`. Shock! It's the same as the move command, except you're moving it to the same folder and with a different name.

Type `ls` again to see whether it was renamed. 

Doing that by hand for 20 files would be a pain, try 20000 files later on.

To automate this, we need a script again.

```bash
#!/bin/bash

list=$( ls )
sortedlist=$( sort $list )

i=1
for file in sortedlist; do

    filenumber=$(printf "%06.0f" $i)

    mv $file image-$filenumber.jpg

    i=$[ i+1 ]

done
```

Let's break this down. 

The line that says `list=$( ls )` is running the command `ls` in the terminal to get a list of the files, then that gets stored in the variable 'list'. `$( command )`, means run this command in the terminal and give back the output.

Guess what the next line is doing, with `sortedlist=...`

Next it creates a variable called `i`, which has the number 1 in it.

After that is a line that says `for file in sortedlist; do `, this starts someting called a 'for loop', which ends with the word `done` further down the script. Anything in between the lines `for ...` and `done`, will be run once for each name in the list `sortedlist`. With each loop, the for loop focuses on the next name in the list, and puts that name in the variable `file`. 

If that made no sense to you, ask for an explanation. Also, try running in the command line `for a in 1 2 3;do; echo $a; sleep 1; done`, maybe that'll help!

The line that says `filenumber=$(printf "%06.0f" $i)` first runs `printf ...` which turns the number stored in `i` into a six digit padded number, then that gets stored in the variable `filenumber`. We want the filenames to be of the format 'image-xxxxxx.jpg', where xxxxxx is a 6 digit number, so '1' becomes '000001'. We need to do this because ffmpeg likes them to be that way. 

Next we are renaming the current file the for loop is on to the name "image-$filenumber.jpg", the tenth file will be called "image-000010.jpg".

Finally we need to increase the number `$i` by 1 with each loop, since they need to be numbered in order. To do maths like adding numbers, Bash needs equations to be stored inside `$[ ... ]` to know what to do.


Save the file as imagerename.sh, then make the file executable. 


## Step 3












