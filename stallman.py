#### TODO: 
#### [ ] Get all posts from last day/week, maybe add args for scale?
#### [x] Format date to display with each post
#### [x] Deal with <a> tags gracefully
#### [ ] Either cron task OR save a file with last timestamp 

import feedparser
import os
import sys
import re

sys.stdout.flush()
cols = os.popen('stty size', 'r').read().split()[1]

d = feedparser.parse('https://stallman.org/rss/rss.xml')
recent = d['entries']#[:6]

def linebreak(char):
  for col in range(int(cols)):
    sys.stdout.write(char)

def formatdate(date):
  match = re.search('(.*)20\d\d', date)
  return match.group(0) 

def removehtml(body):
  match = re.findall('<(.*?)>', body)
  for tag in match:
    body = body.replace('<' + tag + '>', '')
    # Print any links contianed in body
    if tag[0] == 'a':
      print tag[7:].replace('"', '')
  return '\n' + body.replace('\n', ' ')


linebreak('+')
print d['feed']['title']
linebreak('+')
print '\n'

for entry in recent:
  print formatdate(entry['published'])
  print entry['title']
  print removehtml(entry['summary'])
  linebreak('#')
  print '\n'


