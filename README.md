# State Machine Environment


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
