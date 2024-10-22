# Review: Using variables and globs

This reading contains the code used in the instructional videos from [**Using Variables and Globs**](https://www.coursera.org/learn/python-operating-system/lecture/CBlpc/using-variables-and-globs)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

```bash
example=hello
echo $example
```


**Code output:
hello**



```bash
example = hello
```


**Code output:**

Command ‘example’ not found, did you mean:

    Command ‘gexample’ from deb pvm-examples (3.4.6-2build1)

Try: sudo apt install `<deb name>`


```bash
#!/bin/bash
line="-------------------------------------------------"

echo "Starting at: (date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

[ ]./gather-information**.sh **[ ]
```


**Code output:**

Starting at: Mi 22. Mai 17:30:30 CEST 2019

-----------------------------------------------

UPTIME

 17:30:30 up 8 days,  1:51,  2 users,  load average: 0,00, 0,00, 0,00

-----------------------------------------------

FREE

    total        used        free      shared  buff/cache   available

Mem:        4037132      862132      444720       10032     2730280     2875336

Swap:       2097148        6156     2090992

---------------------------------------------------

WHO

user     :0           2019-05-14 15:39 (:0)

user     pts/1        2019-05-14 15:40 (192.168.122.1)

------------------------------------------------------

Finishing at: Mi 22. Mai 17:30:30 CEST 2019


```bash
echo *.py
```


## About this code

When we write star dot py [****.py***], the shell turns it into a list containing all filenames that end with py in the current directory. We can also put the star at the end of an expression to get a list of all files that start with a certain prefix.

**Code output:**

action_deprecation.py areas.py capitalize.py charfreq.py  check_deprecation.py health_checks.py hello.py mycheck.py seconds.py  stdout_example.py streams.py test.py validations.py

**echo** c*

[ ]

## About this code

c* allows us to get all the files in the current directory that start with c.

**Code output:**

capitalize.py charfreq.py check_localhost.sh

**echo** *

[ ]

## About this code

The star with no prefix or suffix matches *all* the files in the current directory.

**Code output:**

(... all the files ...)

**echo** ?????.py

[ ]

## About this code

The question mark symbol can be used to match exactly one character, instead of any amount of characters.We can repeat it as many times as we need. In this example, we can get the Python files with five characters in their name by using five question marks together.

**Code output:**

areas.py hello.py
