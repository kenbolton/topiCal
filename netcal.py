import urllib
from icalendar import Calendar

class NetworkCalendar:
    def __init__(self, url):
        self.url = url
        self.calendar = self.parse(self.request())

    def request(self):
        self.raw_ics = urllib.urlopen(self.url).read()
        return self.raw_ics

    def parse(self, ics_str):
        return Calendar.from_ical(ics_str)

    def next_event(self):
        events = []

        for component in self.calendar.walk():
            if component.name != 'VEVENT':
                continue
            events.append(component);

        def compare(a, b):
            return cmp(a.get('dtstart').dt, b.get('dtstart').dt);

        sorted_events = sorted(events, compare)

        return sorted_events[0]
