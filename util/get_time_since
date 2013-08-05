#!/usr/bin/python2.7

import sys, os, time

format_string = "%s"

def usage():
    print 'Usage:'
    print '    $ get_time_since [ (-f | --format) "format string"] /path/to/file'
    sys.exit(0)

if len(sys.argv) == 4:
    if "-f" in sys.argv[1]:
        format_string = sys.argv[2]
    else:
        usage()
elif len(sys.argv) != 2:
    usage()

dtime = time.time()
dtime -= os.stat(sys.argv[-1]).st_mtime
answer = ''

if dtime < 60:
    answer = 'less than one minute ago'
elif dtime < 25*60:
    totalish = int(dtime/60) + (dtime%60 > 40) 
    answer = 'about ' + str(totalish) + 'min' + ['s', ''][totalish > 1] + ' ago'
elif dtime < 90*60:
    answer = 'about an hour ago'
else:
    totalish = int(dtime/(60*60)) + (dtime%(60*60) > 40)
    answer = 'about ' + str(totalish) + ' hours ago'

print format_string % answer


