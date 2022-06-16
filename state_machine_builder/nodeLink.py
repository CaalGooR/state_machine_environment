class NodeLink:
    ID_SEPARATOR = "_to_"

    def __init__(self, identification: str, value: int, event=None):
        self.value = value
        self.transition_event = event
        self.id = identification

    def set_event(self, event):
        if callable(event):
            self.transition_event = event
        else:
            print("event parameter is not a callable function")
