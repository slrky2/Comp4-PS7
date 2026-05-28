# Copyright Saad Kapadia 2026

import sys
import re
from datetime import datetime

i = 0
success = 0
# bootStart = r"\([a-z]{3}\.[a-z]\.\d{3}\) server started"
bootStart = r"\(log\.c\.166\)"
# bootEnd = r"[A-Z]{4}\:[a-z]{4}\..{17}\:.{7} "
bootEnd = r"INFO\:oejs\.AbstractConnector\:Started SelectChannelConnector\@0\.0\.0\.0\:9080"
grabDate = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

if len(sys.argv) > 1 :
        filename = sys.argv[1]
else: 
    print('you gotta give me args!')

success = 0
searching = False

# examples
# 2014-01-26 09:58:04.362:INFO:oejs.AbstractConnector:Started SelectChannelConnector@0.0.0.0:9080
# 2014-01-26 09:55:07: (log.c.166) server started 

output = filename +'.rpt'
with open(filename, 'r') as file, open(output, 'w') as out:
    for line in file:
        i+=1

        # WE NEED TO RUN A REGEX, AND THEN RUN ANOTHER REGEX TO FIND END

        start = re.search(bootStart, line)
        end = re.search(bootEnd, line)

        if start:
            date = re.search(grabDate, line)
            if searching:
            # if we find another start before we find the end regex it was an incomplete boot
                out.write ('**** Incomplete boot ****')
            
            searching = True

            beginTime = datetime.strptime(date.group(), "%Y-%m-%d %H:%M:%S")
            out.write(f'\n=== Device Boot ===\n{i} ({filename}): {date.group()} Boot Start\n')

        elif end:
            date = re.search(grabDate, line)
            if searching:
                endTime = datetime.strptime(date.group(), "%Y-%m-%d %H:%M:%S")
                out.write(f'{i} ({filename}): {date.group()} Boot Completed\n')
                out.write(f'\tBoot Time: {(endTime-beginTime).total_seconds() * 1000}ms')
                success += 1
                searching = False
print('we have had', success,  'successful boots!')
