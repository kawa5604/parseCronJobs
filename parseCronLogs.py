#!/usr/bin/env python3

import sys
import re

#log file as argument 1
# will look from CRON line by line
# when found will look for username
#count the number of jobs scheduled by user

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) +1

print(usernames)


