# Task 3 Resources
**This document contains the resources you'll need to get started with writing the video creator**

**Aim:** Your goal is to write a program that can convert a set of images into video format, and then upload it to the internet automatically for you to see!

**Links:** 

**Note:** When asked to type in a command, it means that the command should be typed into a terminal, which can be brought up by pressing `ctrl shift t` briefly at the same time. For example, "Use the command `ls`", means bring up an old or new terminal, type in the command at the **prompt**, then press the return/enter key. In this case you should see the contents of the current directory listed.

**Note:** Where you see something like <your name> with the angled brackets around it, replace that with what it's asking you to, and not explicitly "<your name>". So you might type "Lucy" in its place, for example.


Some things you might now be asking:
 - a **prompt** is a string of characters which tells you where you can type in your next command, it 'prompts' you to type there. 
 - the prompt normally contains a small amount of information for you, and usually looks like `pi ~ $` which is telling you `username currentdirectory $`. In windows powershell it is `C:/ >`. When you type in a comand e.g `ls`, you should see `pi ~ $ ls`. No need to type the prompt in yourself!
 - If there are lots of prompts, the bottom-most one is the correct one.
 - `~` means your home directory, which is the same as /home/pi/
 - You can move to the documents directory from your home directory by typing `cd documents`, notice the prompt changes, you can move back up one step by typing `cd ..`. Moving around is a case of using `cd directoryname`, and then using `ls` to see what is inside your new directory. If you get lost, type `cd` to return home. 
 - There are faster ways to move around, which you might want to investigate, but this is the quickest to learn. 


# Summary of aims
- find location on filesystem, `pwd`
- find full path of images directory, `path='/home/pi/...'`
- look inside images directory `ls /.../task3-img`
- copy images directory to keep original as backup
- count and rename all of the files to get img-000001.jpg, img-000002.jpg, ...
- write video to file using shell command, `ffmpeg -r 10 -i img-%02d.png -c:v libx264 -pix_fmt yuv420p -y output.mp4`
- set up git (with the help of leader)
- `git add output.mp4`, `git commit -m "save video output"`, `git pull, git push`

### Step 1
In Bash, there are lots of commands that can do simple or complex things. You will be using some of the basic commands to move around between directories/folders (`cd`); move files (`mv`); copy files (`cp`); make directories (`mkdir`); and look inside directories (`ls`). Then you will get to use a more powerful command which converts files into videos (`ffmpeg`). These are all the same commands that happen when you use a mouse to move between directories on your computer, or use a program to make videos, except now you are typing them in instead of clicking with a mouse. It can be more useful this way because you can write scripts which do any task you want thousands of times over.


You have been supplied with a directory (folder) that contains some test images to make a video out of, ready to use on the real set of images later on. You will need to keep this set of images safe just in case something goes wrong.

Open up a terminal and type in the command `pwd` to find out which directory you are in (it stands for path to working directory). For a new terminal, this is usually `/home/pi`.

You need to locate a directory called 'task3-img', there's a trick you can do to see where it is

```bash
find /home -name task3-img
```

This is telling the command `find` to look inside the `/home` directory for directory/filenames which look like 'task3-img'. If the name exists and you typed it correctly, you should see a line which tells you the full path to the directory, which might look like `/home/pi/blah/task3-img`.

You want to copy the contents of that directory into a new directory we can mess aroudnd with, without worrying about deleting everything accidentally. 

Run the commands

```bash
mkdir testimages

cp <location of task3-img>/* testimages/
```

where <location of task3-img>  is whereever the find command told you it was (`/home/pi/blah...`) Here you are creating a new directory called testimages, then copying the contents of the task3-img directory into it. Type `ls testimages` to check that the contents were copied properly.

Open another terminal and then open an editor by typing `leafpad`, or `nano`, then put the following into the editor

```bash
#!/bin/bash

workdirectory=testimages
images=

echo workdirectory $workdirectory
echo images $images
```

This is a Bash script (Bash is another programming language for linux), which automates things you could do by hand on the terminal. Currently it sets the variable `workdirectory` to the word `testimages`, and the variable `images` to blank/nothing (make sure there are no spaces around the '=' sign.) The very first line `#!/bin/bash` tells the computer what programming language this is. One for python would be `#!/bin/python`.

Notice that in Bash, we assign values to variables by using an `=` sign, and we get the value out of it by adding a dollar sign to the front of the variable name. In this case, where ever Bash sees `$workdirectory`, it replaces it with the word "testimages", but it won't replace "workdirectory" with anything.

In python we assign values by typing `x=5`, where the variable is `x`, and the value is `5`. To get the value of the variable, we just type `x`. That is because Python automatically assumes that any non-string and non-number ("blah" or 12321) is a variable. Bash needs to be told explicitly when there is a variable instead of a string or number, since it doesn't see the difference between "hello" and hello, unlike python where you need to tell it what is a string explicitly.


Copy the location of the directory with the images in it (found with the command `find ...`) to the line that says 'images=', so you are left with a line like `images=/home/pi/...`.

Now save the file with the name `resetimages.sh`, then make the script executable by typing the command

```bash
chmod +x resetimages.sh
```

To 'make executable' means to tell the computer that we want to be able to run the script without the computer complaining, otherwise it will deny access because it hasn't been told that the script should ever be run. It's a security thing.

Try running the script by typing `./resetimages.sh` into your console.

Compare the script to what was output, does that makes sense? You can see the script without opening it up by typing `cat <script name>`.


Now you need to add some lines which will copy the images directory to your workdirectory.

```bash
#!/bin/bash

workdirectory=testimages
images=<location of images file>

echo workdirectory $workdirectory
echo images $images


echo "copying files..."

rm $workdirectory/*

cp $images/* $workdirectory/

echo "done."
```


The command `rm` removes or deletes files for you. See that it says `rm $workdirectory/\*`, that means it is set to delete every file inside the testimages directory, where '/' means 'inside of this directory' and '\*' means every single file.

The command `cp` copies directories and files to other locations. It can overwrite files, so be careful where you copy to. In this case, we are copying the 'images' directory to a work directory called 'testimages'.

Guess what the command `echo` does. Try running that command in a console with some random words after it. How about `a=banana`, then `echo a`, and finally `echo $a`.


We can use this script to undo any mistakes made with the images by replacing them all. If you're using nano, you save by pressing `crtl x`, then pressing `y` and `enter` when it prompts you to.


Check the file over to see that it's going to do what we expect (maybe ask a helper).


Now run the script in the console.

Did it work? 


## Step 2
Now it is time to rename all of the images, because we cannot expect them to be numbered in a way that ffmpeg will be able to parse (understand). Also, one or two might be missing, which would confuse the video editing program.

First you should try renaming one of the files to see how it works. Type the command `ls` to see the best file to rename (the best file would be the first in the list), then type the command 

```bash
mv <best filename> image-000001.jpg
```

Shock! It's the same as the move command, except you're moving it to the same place but with a different name.

Type `ls` again to see whether it was renamed. 

Doing that by hand for 20 files would be a pain, try 20000 files later on.

To automate this, we need a script 

```bash
#!/bin/bash

workdirectory=testimages

imagelist=$( ls $workdirectory )
sortedlist=$( sort $imagelist )


i=1
for image in sortedlist; do

    imagenumber=$(printf "%06.0f" $i)

    mv $workdirectory/$image $workdirectory/image-$imagenumber.jpg

    i=$[ i+1 ]

done
```

Let's break this down. 

First we assign the variable `workdirectory` the value `testimages` again, since that's where the images we will rename are stored.

The line that says `list=$( ls $workdirectory )` is running the command `ls testimages` in the terminal to get a list of the image filenames, which looks like 

```bash
image1.jpg
image2.jpg 
image3.jpg
...
```

These files are stored inside the testimages folder. That list of names gets stored in the variable `imagelist`. You can try running that line by hand in another terminal, then `echo $imagelist` to see that list printed out.

Guess what the next line is doing, with `sortedlist=...`.

The bits that say `$( command )` mean run this command in the terminal and give back the output.

Then it creates a variable called `i`, and assigns it the number `1`.

After that is a line that says `for image in sortedlist; do `, this starts someting called a 'for loop', which ends with the word `done` further down the script. Anything in between the lines `for ...` and `done`, will be run once for each name in the list `sortedlist`. With each loop, the for loop focuses on the next name in the list, and assigns that name to the variable `image`. 


If that made no sense to you, ask for an explanation. Try running in the command line `for a in 1 2 3;do; echo $a; sleep 1; done`, maybe that'll help!


The line that says `filenumber=$(printf "%06.0f" $i)` first runs `printf ...` which turns the number stored in `i` into a six digit padded number, then that gets stored in the variable `filenumber`. We want the filenames to be of the format 'image-xxxxxx.jpg', where xxxxxx is a 6 digit number, so '1' becomes '000001'. We need to do this because ffmpeg likes them to be that way. 

Try typing `printf "%03.2f" 11.5` into the terminal, you can change the numbers between %...f to have a play.

Next we are renaming the current file the for loop is focusing on to the name "image-$filenumber.jpg", the tenth file will be called "image-000010.jpg", and so on...

Finally we need to increase the number `$i` by 1 with each loop, since they need to be numbered in order. To do maths like adding numbers, Bash needs equations to be stored inside `$[ <equation> ]` to know what to do with them.


Save the script as imagerename.sh, then make the script executable. 

After checking that things look right, try running it.

## Step 3












