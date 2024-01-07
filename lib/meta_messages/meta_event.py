from lib.meta_messages.meta_message import MetaMessage

class MetaEvent():
    def __init__(self, delta_time: int, message: MetaMessage):
        self.delta_time = delta_time
        self.message = message

    def str_with_pre_time(self, time):
        return f"[{str(self.delta_time + time).rjust(10, '0')}] {self.message.__repr__()}"
    
    def __repr__(self):
        return f"Delta time = {str(self.delta_time).rjust(4, '0')}. {self.message.__repr__()}"