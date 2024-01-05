from lib.meta_messages.meta_event import MetaEvent
from lib.messages.event import MidiEvent

import json

class Track:
    def __init__(self, length: int, events: 'list[MidiEvent | MetaEvent]'):
        self.length = length
        self.events = events

    def dict_repr(self) -> dict:
        event_strings = []
        time = 0
        for event in self.events:
            event_strings.append(event.str_with_pre_time(time))
            time = time + event.delta_time

        return {
            "length": self.length,
            "events": event_strings
        }
