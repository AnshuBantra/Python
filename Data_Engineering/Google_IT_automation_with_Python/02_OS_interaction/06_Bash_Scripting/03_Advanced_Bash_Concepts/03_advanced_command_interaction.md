# Review: Advanced Command Interaction

This reading contains the code used in the instructional videos from [**Advanced Command Interaction**](https://www.coursera.org/learn/python-operating-system/lecture/eSaS2/advanced-command-interaction)

## Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

**tail /var/log/syslog**

[ ]

**Code output:**

May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --

May 24 10:25:19 ubuntu.local systemd[1]: Reloading.

**tail /var/log/syslog | **cut** **-d**' '** **-f5**-

[ ]

**Code output:**

CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

rsyslogd: -- MARK --

systemd[1]: Reloading.

**cut** **-d**' '** **-f5**- /var/log/syslog | **sort** | uniq **-c** | **sort** **-nr** | head**

[ ]

**Code output:**

    41 systemd[1]: Starting Network Manager Script Dispatcher Service...

    41 systemd[1]: Started Network Manager Script Dispatcher Service.

    41 systemd[1]: NetworkManager-dispatcher.service: Succeeded.

    41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: start running ordered scripts...

    41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: new request (1 scripts)

    41 dhclient[757]: DHCPREQUEST for 192.168.122.103 on ens3 to 192.168.122.1 port 67 (xid=0x3a5ff7ed)

    41 dhclient[757]: DHCPACK of 192.168.122.103 from 192.168.122.1 (xid=0xedf75f3a)

    41 dbus-daemon[592]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'

    41 dbus-daemon[592]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.15' (uid=0 pid=599 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")

    9 systemd[1]: Started Run anacron jobs.

**#!/bin/bash**

**for** logfile **in** /var/log/*log; **do**

**    **echo** **"Processing: $logfile"

**    **cut** **-d**' '** **-f5**- **$logfile** | **sort** | uniq **-c** | **sort** **-nr** | head **-5**

**done**

[ ]

## About this code

This script is written in the Bash scripting language and designed to analyze log files. It analyzes each log file in the /var/log directory and displays the top 5 most frequently occurring messages along with their counts.

**./toploglines.**sh

[ ]

**Code output:**

(...)

Processing: /var/log/user.log

    23 system-updater[199481]: DEBUG Command exited with status: 0

    19 system-updater[46682]: DEBUG Command exited with status: 0

    16 system-updater[175060]: DEBUG Command exited with status: 0

    11 /usr/bin/lock: called by /bin/bash for . uid 0, euid 0.

    11 network-manager-dhclient-hooks: Dispatching run of '/etc/dhcp/dhclient-exit-hooks.d/hostname' ...

Processing: /var/log/Xorg.0.log

    87 Printing DDC gathered Modelines:

    87 Modeline "1920x1080"x0.0  141.00  1920 1936 1952 2104  1080 1083 1097 1116 -hsync -vsync (67.0 kHz eP)

    87 EDID vendor "AUO", prod id 5949

    78 vendor "AUO", prod id 5949

    78 DDC gathered Modelines:
