# State Machine Environment
State Machine Engine can now build your SM using a list of dictionaries that contain a state (called 'node' in the dictionary attribute) and their links related to other states.

```python
# Example:
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
