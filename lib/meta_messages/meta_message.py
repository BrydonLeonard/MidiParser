from lib.meta_messages.meta_data import *
from enum import Enum

class MetaMessage():
    def __init__(self):
        self.data = None # no-op

    def __repr__(self) -> str:
        return f"[Meta] {self.data}"

class TextMessageType(Enum):
    PLAIN = 1
    COPYRIGHT = 2
    TRACK_NAME = 3
    INSTRUMENT_NAME = 4
    LYRIC = 5
    MARKER = 6
    CUE_POINT = 7

class TextMessage(MetaMessage):
    def __init__(self, text_message_type: TextMessageType, data: TextData):
        MetaMessage.__init__(self)
        self.text_message_type = text_message_type
        self.data = data

class ChannelPrefixMessage(MetaMessage):
    def __init__(self, channel_prefix_data):
        MetaMessage.__init__(self)
        self.data = channel_prefix_data

class SetSeqNumberMessage(MetaMessage):
    def __init__(self, data: SetSeqNumberData):
        MetaMessage.__init__(self)
        self.data = data

class SetTempoMessage(MetaMessage):
    def __init__(self, data: SetTempoData):
        MetaMessage.__init__(self)
        self.data = data

class SmpteOffsetMessage(MetaMessage):
    def __init__(self, data: SmpteOffsetData):
        MetaMessage.__init__(self)
        self.data = data

class SetTimeSignatureMessage(MetaMessage):
    def __init__(self, data: SetTimeSignatureData):
        MetaMessage.__init__(self)
        self.data = data

class SetKeySignatureMessage(MetaMessage):
    def __init__(self, data: SetKeySignatureData):
        MetaMessage.__init__(self)
        self.data = data

class SetSeqInfoMessage(MetaMessage):
    def __init__(self, data: SetSeqInfoData):
        MetaMessage.__init__(self)
        self.data = data

class TrackCompleteMessage(MetaMessage):
    def __init__(self):
        self.data = ""

    def __repr__(self):
        return "[Meta] END OF TRACK"
