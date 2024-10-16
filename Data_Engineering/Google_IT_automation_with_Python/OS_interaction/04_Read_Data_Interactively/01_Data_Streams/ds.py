# %% Environment Variables
# # !/usr/bin/env python3
import os

print(f'HOME:  {os.environ.get("HOME", "")}')
print(f'HOME:  {os.environ.get("HOMEPATH", "")}')
print(f'SHELL: {os.environ.get("SHELL", "")}')
print(f'FRUIT: {os.environ.get("FRUIT", "")}')

# %% Parameters

import sys

print(sys.argv)
# %%
# %% Obtain System Output

import platform
import subprocess

def run_command():
    os_name = platform.system()

    if os_name == "Windows":
    # Windows commands
        sub_date = subprocess.run(['date', '/T'], shell=True)
        result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True, text=True)
        sub_rm = subprocess.run(["del", "does_not_exist"], capture_output=True, text=True, shell=True)
    else:
    # Unix-like commands
        sub_date = subprocess.run(['date'])
        result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
        print(result.stdout.decode().split())
        sub_rm = subprocess.run(["rm", "does_not_exist"], capture_output=True)
    
    print(sub_date)
    print(result.stdout)
    print(sub_rm)
    print(f'args: {sub_rm.args}')
    print(f'check_returncode: {sub_rm.check_returncode}')
    print(f'returncode: {sub_rm.returncode}')
    print(f'stdout: {sub_rm.stdout}')
    print(f'stderr: {sub_rm.stderr}')

run_command()

# %%
