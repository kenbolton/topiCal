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

        next_event = None
        unaware_right_now = datetime.now()
        utc = pytz.UTC
        right_now = utc.localize(unaware_right_now)

        for component in self.calendar.walk():
            if component.name != 'VEVENT':
                continue

            # Ignore Events with no time 
            if type(component.get('dtstart').dt) == date:
                continue

            # If event is in past
            if component.get('dtstart').dt < right_now:
                continue

            if not next_event or component.get('dtstart').dt < next_event.get('dtstart').dt:
                next_event = component

        return next_event
