topiCal
=======

A simple python script for producing a new chatroom topic using data
from a calendar.

To use, create a config.yaml file in the following format:

```
calendar: "http://example.com/cal.ics" # the url to an ical formatted calendar

irc:
  chatroom: "#chatroom_name"
  server: "irc.server.net" # e.g. irc.freenode.net
  topic: "topic template" # e.g. Next Meeting {datetime} @ {location}

date_format: "%b %e %l%p" # the datetime format, e.g. Nov  2  7pm
```
