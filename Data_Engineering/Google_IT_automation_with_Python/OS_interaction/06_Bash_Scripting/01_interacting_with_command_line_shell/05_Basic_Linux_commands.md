# Study guide: Basic Linux commands

Basic Linux commands are beneficial to developers when interacting with a Linux operating system through the command line interface. They are used when working with files and directories. Typically, they are easy to learn and apply, and provide developers with additional commands for more advanced situations. If needed, these commands are also easy to look up on your preferred search engine.

In this reading, you will review basic Linux commands with examples provided along the way.

## Managing files and directories

Many applications configure themselves by reading files. They are designed to read and write files in specific directories. Because of this, developers need to understand how to move and rename files, change their permissions, and do simple operations on their contents. Here are some common commands:

- mv is used to move one or more files to a different directory, rename a file, or both at the same time.

**Note:** Linux is case-sensitive, so mv can also be used to change the case of a filename.

- mv myfile.txt dir1/ This command moves a file to the directory.

- mv file1.txt file2.txt file3.txt dir1/ This command moves multiple files.

- cp is used to copy one or more files. Some examples include:

- cp file1.txt file2.txt

- cp file1.txt file2.txt file3.txt dir1/

- chmod/chown/chgrp is used to make a file readable to everyone on the system before moving it to a public directory. A common example is:

- chmod +r file.html && mv file.html /var/www/html/index.html

## Operating with the content of files

Every programmer will use files for something. Whether it’s for configuration, data, or input and output, programmers work with files and need to know how to operate with their contents.

- cut is a command that extracts fields from a data file. Two examples are:

- cut -f1 -d”,” addressbook.csv This command extracts the first field from a .csv file.

- cut -c1-3,5-7,9-12 phones.txt This command extracts only the digits from a list of phone numbers.

- sort is a command that sorts the contents of a file. Some examples include:

- sort names.txt This command sorts inputs alphabetically.

- sort -r names.txt This command sorts inputs in reverse alphabetical order, starting with the letter z.

- sort -n numbers.txt This command treats the inputs as numbers and then sorts them numerically.

Some examples that include combining multiple commands are:

- ls -l | cut -w -f5,9 | sort -rn | head -10 This command displays the 10 largest files in the current directory.

- cut -f1-2 -d”,” addressbook.csv | sort This command extracts the first and last names from a .csv file and sorts them.

## Additional commands

Additional commands that programmers commonly use are:

id  is a command that prints information about the current user. This command is useful if you are getting a permissions denied error and think you should be granted access to a file.

- $ id

    uid=3000(tradel) gid=3000(tradel)
	groups=3000(tradel),0(root),100(users),545(builtin_users),999(docker)

free is a command that prints information about memory on the current system.

- free -h This command prints in human-readable units instead of bytes.

## Key takeaways

Basic Linux commands assist developers in different types of tasks related to managing files and directories and working with the content of each file. These commands allow developers to work more efficiently and effectively.
