from .stateNode import StateNode
from state_machine_builder.state import State
from state_machine_builder.nodeLink import NodeLink


class StateMachine:
    NODE_ATTRIBUTE: str = 'node'
    LINKS_ATTRIBUTE: str = 'links'
    STATE_CALLBACKS: str = 'state_callbacks'
    LINK_CALLBACKS: str = 'link_callbacks'
    TASK_CALLBACK: str = 'task_callback'
    BEFORE_TASK_CALLBACK: str = 'before_task_callback'

    def __init__(self, map_nodes: dict):
        self.__is_first_node: bool = False
        self.__current_node: int = 0
        self.__root_node: int = 0
        self.__nodes: list[StateNode] = []
        self.build_route(map_nodes)

    def build_route(self, map_nodes: dict):
        self.__is_first_node = False
        self.__nodes = []
        counter = 0
        for element in map_nodes:
            if self.__is_first_node:
                self.__is_first_node = True
                self.__root_node = element[self.NODE_ATTRIBUTE]

            state = element[self.NODE_ATTRIBUTE]
            links = element[self.LINKS_ATTRIBUTE]
            new_node = StateNode(state, links)
            self.__nodes.append(new_node)
            counter += 1
        self.__current_node = self.__root_node

    def set_state_task(self, state_id, task_type: int = State.RUN_TASK_TYPE, task_callback=None):

        if isinstance(state_id, State):
            state_id = state_id.id

        if type(state_id) is str:
            for node in self.__nodes:
                if node == state_id:
                    if task_type == State.RUN_TASK_TYPE:
                        node.state.setTask(task_callback)
                    elif task_type == State.BEFORE_RUN_TASK_TYPE:
                        node.state.setBeforeTask(task_callback)
                    else:
                        raise Exception('Event type does not exist')

    def set_link_task(self, state_from, state_to, task_callback):

        link_id = ""

        if isinstance(state_from, State):
            state_from = state_from.id
        if isinstance(state_to, State):
            state_to = state_to.id

        link_id = state_from + NodeLink.ID_SEPARATOR + state_to
        for link in self.__nodes[self.__current_node].node_links:
            print(link.id)

    def get_current_node(self) -> StateNode:
        return self.__nodes[self.__current_node]

    def goto_state(self, value: int):
        pass

    def is_valid_transition(self, value: int) -> int:
        node_links = self.get_current_node().node_links
        for node_link in node_links:
            new_index = self.get_index_state_node(node_link.id)
        return 0

    def get_index_state_node(self, state: State) -> int:
        index_result = 0
        for node in self.__nodes:
            if state.__class__.__name__ == node.state.__class__.__name__:
                return index_result
            index_result += 1

        return -1

    def manage(self):
        # TODO
        pass
