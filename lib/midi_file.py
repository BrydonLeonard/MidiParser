from lib.track import Track
import json

FILE_FORMATS = [
    "a single track", 
    "multiple synchronous tracks",
    "multiple simultaneous tracks"
]

class MidiFile:
    def __init__(self, file_format: int, track_count: int, ticks_per_crotchet: int, tracks: 'list[Track]'):
        self.file_format = file_format
        self.track_count = track_count
        self.ticks_per_crotchet = ticks_per_crotchet
        self.tracks = tracks

        if len(self.tracks) != self.track_count:
            raise Exception(f"The track count ({self.track_count}) differed from the actual number of tracks ({len(self.tracks)})")

    def __repr__(self):
        return json.dumps({
            "format": f"{self.file_format} ({FILE_FORMATS[self.file_format]})",
            "track_count": self.track_count,
            "ticks_per_crotchet": self.ticks_per_crotchet,
            "tracks": list(map(lambda track : track.dict_repr(), self.tracks))
        }, indent = 4)