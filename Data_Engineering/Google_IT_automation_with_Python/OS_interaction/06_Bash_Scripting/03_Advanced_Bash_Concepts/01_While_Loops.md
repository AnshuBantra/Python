# Review: While loops in Bash scripts

This reading contains the code used in the instructional videos from [**While Loops in Bash Scripts**](https://www.coursera.org/learn/python-operating-system/lecture/tlm5f/while-loops-in-bash-scripts)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

```bash
#!/bin/bash
n=1
while [ $n -le 5 ]; do
	echo "Iteration number $n"
	((n+=1))
done
```


./**while**.**sh**

**Code output:**

Iteration number 1

Iteration number 2

Iteration number 3

Iteration number 4

Iteration number 5

**cat** **while**.**sh**

[ ]

**Code output:**

#!/usr/bin/env python

import random

value=random.randint(0, 3)

print("Returning: " + str(value))

sys.exit(value)

**./random**-exit**.py**

**./random**-exit**.py**

**./random**-exit**.py**

[ ]

**Code output:**

Returning: 3

Returning: 2

Returning: 0

**#!/bin/bash**

**n=**0

**command=**$1

**while** ! **$command** && [ **$n** **-le** **5** ]; **do**

**        **sleep** **$n

**        ((n+=**1**))**

**        **echo** **"Retry #$n"

**done**;

[ ]

**./retry.**sh** ./random**

[ ]

**Code output:**

Returning: 3

Retry #1

Returning: 3

Retry #2

Returning: 1

Retry #3

Returning: 3

Retry #4

Returning: 0
