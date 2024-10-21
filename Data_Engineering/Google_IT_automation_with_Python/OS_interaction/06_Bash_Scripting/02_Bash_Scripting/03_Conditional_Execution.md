# Review: Conditional execution in Bash

This reading contains the code used in the instructional videos from [**Conditional Execution in Bash**](https://www.coursera.org/learn/python-operating-system/lecture/x3PqP/conditional-execution-in-bash)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

```bash
cat check_localhost.sh
```

## About this code

Here  we’ll start with theif keyword, followed by the grep command. This is how we’ll check for success. At the end of the command, we have a semicolon [;], followed by the word then. After that comes the body of the conditional.

**Code output:**

#!/bin/bash
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

**./check_localhost.sh**

**Code output:**




127.0.0.1	localhost

Everything ok

**if** test **-n** **"$PATH"**; **then** **echo** **"Your path is not empty"**; **fi**

[ ]

**Code output:**

Your path is not empty

**if** [ **-n** **"$PATH"** ]; **then** **echo** **"Your path is not empty"**; **fi**

[ ]

**Code output:**

Your path is not empty


* [https://ryanstutorials.net/bash-scripting-tutorial/](https://ryanstutorials.net/bash-scripting-tutorial/)
* [https://linuxconfig.org/bash-scripting-tutorial-for-beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
* [https://www.shellscript.sh](https://www.shellscript.sh/)
