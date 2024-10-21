# Review: For loops in bash scripts

This reading contains the code used in the instructional videos from [**For Loops in Bash Scripts**](https://www.coursera.org/learn/python-operating-system/lecture/REXHO/for-loops-in-bash-scripts)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

**cat fruits.sh**

[ ]

## About this code

Here we're iterating over three different elements that have the names of the fruits.

**Code output:**

#!/bin/bash

for fruit in peach orange pear; do

    echo "I like $fruit!"

done

**./fruits.**sh** **

[ ]

**Code output:**

I like peach!

I like orange!

I like pear!

**cd** old_website/

**/old_website$ **ls** **-l

[ ]

**Code output:**

total 0

-rw-r--r-- 1 user user 0 May 24 10:19 about.HTM

-rw-r--r-- 1 user user 0 May 24 10:20 contact.HTM

-rw-r--r-- 1 user user 0 May 24 10:20 footer.HTM

-rw-r--r-- 1 user user 0 May 24 10:20 header.HTM

-rw-r--r-- 1 user user 0 May 24 10:19 index.HTM

**/old_website$ basename index.HTM .HTM**

[ ]

## About this code

This command takes a filename and an extension, and then returns the name without the extension.

**#!/bin/bash**

**for** file **in** *.HTM; **do**

**        name=**$(basename "$file" .HTM)

**        **mv** **"$file"** **"$name.html"** **

**done**

[ ]

**#!/bin/bash**

**for** file **in** *.HTM; **do**

**        name=**$(basename "$file" .HTM)

**        **echo** **mv** **"$file"** **"$name.html"** **

**done**

[ ]

## About this code

The script iterates through all files with the ".HTM" extension in the current directory. For each file, it extracts the filename without the extension and generates the new filename with the ".html" extension. Finally, it prints the mv command that would rename the original file to the new filename.

**Note: **This script only prints the mv commands. To actually rename the files, you need to execute the script by running chmod +x script.sh && ./script.sh where script.sh is the name of the script file.

**/old_website$ **chmod** +x rename.**sh

**/old_website$ ./rename.**sh** **

[ ]

## About this code

Here the script gets saved as rename.sh

**Code output:**

mv about.HTM about.html

mv contact.HTM contact.html

mv footer.HTM footer.html

mv header.HTM header.html

mv index.HTM index.html

**/old_website$ ./rename.**sh** **

**/old_website$**

**/old_website$ **ls** **-l

[ ]

## About this code

These commands won’t print anything. That's expected because these commands don't print anything when they succeed.

**ls** **-l**

[ ]

## About this code

ls -l is a command in Linux and Unix systems used to list the contents of a directory in a long format. This format provides detailed information about each file

**Code output:**

total 4

-rw-r--r-- 1 user user  0 May 24 10:19 about.html

-rw-r--r-- 1 user user  0 May 24 10:20 contact.html

-rw-r--r-- 1 user user  0 May 24 10:20 footer.html

-rw-r--r-- 1 user user  0 May 24 10:20 header.html

-rw-r--r-- 1 user user  0 May 24 10:19 index.html

-rwxr-xr-x 1 user user 90 May 24 10:40 rename.sh
