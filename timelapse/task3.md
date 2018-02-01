# Task 3 Resources
**This document contains the resources you'll need to get started with writing the video creator**

**Aim:** Your goal is to write a program that can convert a set of images into video format, and then upload it to the internet automatically for you to see!

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

# Summary of aims
- find location on filesystem, `pwd`
- find full path of images folder, `path='/home/pi/...'`
- look inside images folder `ls /.../task3-img`
- copy images folder to keep original as backup
- count and rename all of the files to get img-000001.jpg, img-000002.jpg, ...
- using linux shell command in python with, e.g. os.system('ls')
- write video to file using shell command, `os.system('ffmpeg -r 10 -i img-%02d.png -c:v libx264 -pix_fmt yuv420p -y output.mp4')`
- `git add output.mp4`, `git commit -m "save video output"`, `git pull, git push`

### Step 1
You have been supplied with a folder that contains some test images to make a video out of. You will need to keep that set of files safe just in case something goes wrong.

Open up a terminal and type in the command `pwd` to find out which folder you are in (it stands for path to working directory). 

You need to locate a folder called 'task3-img', there's a trick you can do to see where it is

```bash
find /home -name task3-img
```
If the folder exists and you typed it correctly, you should see a line which tells you the full path to the folder, which might look like `/home/pi/blah/task3-img`

Open another terminal and then open an editor by typing `leafpad`, or `nano`, then put the following into it

```bash
#!/bin/bash

workfolder=testimages
images=
```

This is a Bash script (Bash is another programming language for linux), and currently it sets the variable `workfolder` to the word "testimages", and `images` to nothing

Copy the location of the folder with the images in it (found with the command `find ...`) to the line that says 'images=', so you are left with a line like `images=/home/pi/...`

Now you need to add a line which will copy the images folder to your workfolder.

```bash
#!/bin/bash

workfolder=testimages
images=

cp -r $images $workfolder 
```

Notice that in Bash, we assign variables (like assigning `x=5`) by using an `=` sign, but we get the value out of it (like the value `5`) by adding a dollar sign to the front of the variable name (like `$x`). In this case, where ever Bash sees `$workfolder`, it replaces it with the word `"testimages"`.

The command `cp -r` copies folders and files to other locations. It can accidentally overwrite files, so be careful where you copy to. In this case, we are copying the images folder to a work folder called.


Now save the file with the name `resetimages.sh`, we can use this script to undo any mistakes made with the images. 

Make the script executable by typeing the command 

```bash
chmod +x resetimages.sh
```

This means we will be able to actually run the script, otherwise the computer would say no.

## More steps to come


