# Review: Signaling processes

This reading contains the code used in the instructional videos from [**Signaling Processes**](https://www.coursera.org/learn/python-operating-system/lecture/xElRN/signalling-processes)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

```
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes[ ]
```


Press Control C:

--- www.example.com ping statistics ---

9 packets transmitted, 9 received, 0% packet loss, time 8013ms

rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms

```
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
```


  Press Control Z: the program stops.

```
fg
#ping www.example.com
#64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=5 ttl=51 time=93.6 ms
```


Press Control C:

--- www.example.com ping statistics ---

9 packets transmitted, 9 received, 0% packet loss, time 8013ms

rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms

## About this code

Text that is written as a comment, following #, is what the code output will show  on screen in the video at the Linux command line.
