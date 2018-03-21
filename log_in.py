#!/bin/python3

# timesheet example
# IN    OUT   LUNCH
# 08:31,14:28,11:35,12:05

import argparse
from time import localtime

MONTHLOG = '/home/makopec/Documents/time_log/time.csv'
DAYLOG = '/home/makopec/Documents/time_log/day.tmp'


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", choices=['in', 'out', 'lunch'], default='in')
    return parser.parse_args()


def get_time():
    timestamp = str(localtime().tm_hour)
    timestamp += ":"
    minute = str(localtime().tm_min)
    if len(minute) == 1:
        timestamp += "0"
    timestamp += minute
    return timestamp


def write_file(content):
    with open(MONTHLOG, 'a') as csvfile:
        csvfile.write(content)


def update_day(action, timestamp):
    content = action + " " + timestamp + "\n"
    if action == "in":
        permission = 'w'
    else:
        permission = 'a'
    with open(DAYLOG, permission) as dayfile:
        dayfile.write(content)


def get_lunch_end(start):
    hour, minute = start.split(':')
    int_minute = int(minute)
    int_hour = int(hour)
    int_minute += 30
    if int_minute >= 60:
        int_hour += 1 # won't go above 24, so no need modulo
        int_minute -= 60
    if int_minute == 0:
        minute = "00"
    else:
        minute = str(int_minute)
    hour = str(int_hour)
    return hour + ":" + minute


def get_day_entry():
    with open(DAYLOG, 'r') as dayfile:
        content = dayfile.readlines()
    dict_content = dict()
    for line in content:
        action, time = line.split()
        dict_content[action] = time
    entry = dict_content["in"] + "," + dict_content["lunch"] + "," + \
            get_lunch_end(dict_content["lunch"]) + "," + \
            dict_content["out"] + "\n"
    return entry


def main():
    # Parse arguments
    args = parse_arguments()

    # Get timestamp from localtime
    timestamp = get_time()

    # Write timestamp to day file
    update_day(args.action, timestamp)

    # Add entry to month log
    if args.action == 'out':
        entry = get_day_entry()
        write_file(entry)

if __name__ == "__main__":
    main()
