#!/usr/bin/env python3

import os, sys

def check_reboot():
    """
        Returns True if the computer has a pending reboot.
    """
    return os.path.exists('/run/reboot-required')

def main():
    if check_reboot():
        print('Pending Reboot.')
        sys.exit(1)
    print('Everything Ok.')
    sys.exit(0)

if __name__ == '__main__':
    main()