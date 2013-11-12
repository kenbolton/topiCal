import yaml
from netcal import NetworkCalendar

# Load configuration data
with open('config.yaml', 'r') as f:
    config = yaml.load(f)

calendar_url = config['calendar']
topic_format = config['irc']['topic']
date_format = config['date_format']

calendar = NetworkCalendar(calendar_url)

def chatroom_topic(event):
    start = event.get('dtstart').dt
    topic = topic_format.format(
        datetime=start.strftime(date_format),
        location=event.get('location')
    )
    return topic

def main():
    print chatroom_topic(calendar.next_event())

main()
