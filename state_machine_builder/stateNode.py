from .nodeLink import NodeLink
from .state import State


class StateNode:
    STATE_ELEMENT = 0
    LINK_ELEMENT = 1

    def __init__(self, state: State, linked_states: list[State] = None):
        self.node_links = []
        self.state = None

        if isinstance(state, State):
            self.state = state
        else:
            raise Exception("state parameter isn't an instance of State class")

        if linked_states is not None and isinstance(linked_states, list):
            for link in linked_states:
                id = StateNode.get_link_id_by_states(state, link)
                self.node_links.append(NodeLink(id, link.value))
        else:
            raise Exception("linked_states parameter is not a list of States")

    def __str__(self):
        if self.state is not None and len(self.node_links) > 0:
            result = "State:" + self.state.__class__.__name__ + "\nLinks:{\n"

            for link in self.node_links:
                result += "\t[" + link.id + "][transition value=" + str(link.value) + "]\n"

            result += "}\n"
            return result

    def set_link_event(self, task_callback=None, from_st=None, to=None):
        # TODO
        pass

    def set_state_event(self, task_callback=None):
        if not callable(task_callback):
            raise Exception('No callable task')

        self.state.setTask(task_callback)

    @staticmethod
    def get_link_id_by_states(state1: State, state2: State) -> str:
        return state1.__class__.__name__ + NodeLink.ID_SEPARATOR + state2.__class__.__name__
