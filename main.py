import urllib
import yaml
from datetime import datetime
from icalendar import Calendar

# Load configuration data
with open('config.yaml', 'r') as f:
    config = yaml.load(f)

calendar = config['calendar']
topic_format = config['irc']['topic']
date_format = config['date_format']

def next_event(ical_url):
    raw_ics = urllib.urlopen(ical_url).read()
    gcal = Calendar.from_ical(raw_ics)

    events = []

    for component in gcal.walk():
        if component.name != 'VEVENT':
            continue
        events.append(component);

    def compare(a, b):
        return cmp(a.get('dtstart').dt, b.get('dtstart').dt);

    sorted_events = sorted(events, compare)

    return sorted_events[0]

def chatroom_topic(event):
    start = event.get('dtstart').dt
    topic = topic_format.format(
        datetime=start.strftime(date_format),
        location=event.get('location')
    )
    return topic

print chatroom_topic(next_event(calendar))
