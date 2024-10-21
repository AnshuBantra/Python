# Review: Pipes and pipelines

This reading contains the code used in the instructional videos from [**Pipes and Pipelines**](https://www.coursera.org/learn/python-operating-system/lecture/d60kg/pipes-and-pipelines)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

```bash
ls -l | less
#(... A list of files appears...)

cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
	# 7 the
	# 3 up
	# 3 spider
	# 3 and
	# 2 rain
	# 2 itsy
	# 2 climbed
	# 2 came
	# 2 bitsy
	# 1 waterspout.
```


```bash
cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
	print(line.strip().capitalize())
```


```bash
cat haiku.txt
#advance your career,
#automating with Python,
#it's so fun to learn.
```


```bash
cat haiku.txt | ./capitalize.py
#Advance your career,
#Automating with python,
#It's so fun to learn.
```


```bash
./capitalize.py < haiku.txt
#Advance your career,
#Automating with python,
#It's so fun to learn.
```


## About this code

Text that is written as a comment, following #, is what the code output will show  on screen in the video at the Linux command line.
