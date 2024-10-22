# Review: Diffing Files

This reading contains the code used in the instructional videos from [**Diffing Files**](https://www.coursera.org/learn/introduction-git-github/lecture/tnlzg/diffing-files)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

**cat rearrange1.py**

**Code output:**

```python
#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r"^([\w .]), ([\w .])$", name)
	if result == None:
		return name
	return "{} {}".format(result[2], result[1])
```


**cat rearrange2.py**

```python
#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r"^([\w .-]), ([\w .-])$", name)
	if result == None:
		return name
	return "{} {}".format(result[2], result[1])
```


**diff rearrange1.py rearrange2.py**

**Code output:**

```bash
6c6
<     result = re.search(r"^([\w .]), ([\w .])$", name)
---
>     result = re.search(r"^([\w .-]), ([\w .-])$", name)
```

**diff** validations1.py validations2.py

[ ]

**Code output:**

5c5,6

<	assert (type(username) == str), "username must be a string"

--

> if type(username != str:

> raise TypeError("username must be a string"

11a13,15

> return False

> # Usernames can't begin with a number

> if username[0].isnumeric():

**diff** **-u** validations1.py validations2.py

[ ]

**Code output:**

--- validations1.py	2019-06-06 14:28:49.639209499 +0200

+++ validations2.py	2019-06-06 14:30:48.019360890 +0200

@@ -2,7 +2,8 @@

 def validate_user(username, minlen):

- assert type(username) == str, "username must be a string"

+ if type(username) != str:
+ raise TypeError("username must be a string")

  if minlen < 1:

  raise ValueError("minlen must be at least 1")

@@ -10,5 +11,8 @@

    return False

    if not username.isalnum():

    return False

+ # Usernames can't begin with a number
+ if username[0].isnumeric():
+ return False

  return True
