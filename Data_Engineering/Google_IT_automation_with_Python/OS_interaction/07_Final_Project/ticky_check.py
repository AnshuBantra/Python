#!/usr/bin/env python3

import sys, re, operator
import pandas as pd

def read_log(file):
    lst_errors = []
    lst_info = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if "INFO" in line:
                lst_info.append(line)
            elif "ERROR" in line:
            # else:
                lst_errors.append(line)
    f.close()
    return (lst_info, lst_errors)

def report_error(lst_errors: list):
    dict_errors = {}
    for err in lst_errors:
        type_error = re.search(r'.+ ERROR (.+) \(.+\)', err)[1]
        if type_error in dict_errors:
            dict_errors[type_error] += 1
        else:
            dict_errors[type_error] = 1
    dict_errors = dict(sorted(dict_errors.items(), key=operator.itemgetter(1), reverse=True))
    dict_errors = [(key, value) for key, value in dict_errors.items()]
    return dict_errors

def report_user(lst_errors: list, lst_info: list):
    dict_user_error = {}
    for err in lst_errors:
        user = re.search(r'.+ \((.+)\)', err)[1]
        if user in dict_user_error:
            dict_user_error[user] += 1
        else:
            dict_user_error[user] = 1
    dict_user_info = {}
    for err in lst_info:
        user = re.search(r'.+ \((.+)\)', err)[1]
        if user in dict_user_info:
            dict_user_info[user] += 1
        else:
            dict_user_info[user] = 1
    users = dict_user_info.keys() | dict_user_error.keys()
    user_info = [(user, dict_user_info.get(user, 0), dict_user_error.get(user, 0)) for user in users]
    user_info.sort(key = lambda x: x[0])
    user_info.insert(0, ('Username', 'INFO', 'ERROR'))
    return user_info


def main():
        lst_info, lst_errors = read_log('syslog.log')
        error_message = report_error(lst_errors)
        user_statistics = report_user(lst_errors, lst_info)
        with open('error_message.csv', 'w') as f:
            for line in error_message:
                f.write(''.join(re.findall(r'[a-zA-Z ,0-9]+', str(line)))+'\n')
        with open('user_statistics.csv', 'w') as f:
            for line in user_statistics:
                f.write(''.join(re.findall(r'[a-zA-Z ,0-9]+', str(line)))+'\n')

if __name__=='__main__':
        main()