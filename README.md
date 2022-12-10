# State Machine Environment
State Machine Engine can now build your SM using a list of dictionaries that contain a state (called 'node' in the dictionary attribute) and their links related to other states.

```python
# Example:
from state_machine_builder.state import State
state1 = State('state1')
state2 = State('state2')
state3 = State('state3')
state4 = State('state4')
route_mapping = [
    {
        'node': state1,
        'links': [state2, state3, state4]
    },
    {
        'node': state2,
        'links': [state1, state4]
    },
    {
        'node': state3,
        'links': [state4],
    },
    {
        'node': state4,
        'links': [state1]
    }
]
```
