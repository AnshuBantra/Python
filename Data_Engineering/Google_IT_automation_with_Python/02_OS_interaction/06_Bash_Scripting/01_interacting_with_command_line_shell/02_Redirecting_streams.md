# Review: Redirecting streams

This reading contains the code used in the instructional videos from [**Redirecting Streams**](https://www.coursera.org/learn/python-operating-system/lecture/CAisf/redirecting-streams)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

```bash
cat stdout_example.py
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")

./stdout_example.py
#Output: Don't mind me, just a bit of text here...

./stdout_example.py > new_file.txt
cat new_file.txt
#Output: Don't mind me, just a bit of text here...

./stdout_example.py >> new_file.txt
cat new_file.txt
#Output:
#Don't mind me, just a bit of text here...
#Don't mind me, just a bit of text here...

cat streams_err.py
#!/usr/bin/env python3
data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR

./streams_err.py < new_file.txt 2> error_file.txt
#Output
#This will come from STDIN: Now we write it to STDOUT: Don't minde me, just a bit of text here...

cat error_file.txt
#Output
#Traceback (most recent call last):
#  File "./streams_err.py", line 5, in <module>
#    raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR

echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt 
#These are the contents of the file
```


## About this code

Text that is written as a comment, following #, is what the code output will show  on screen in the video at the Linux command line.
