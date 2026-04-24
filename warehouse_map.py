# Represents a warehouse as a graph
warehouse = {
    "Start": {"A": 2, "B": 5},
    "A": {"Start": 2, "C": 4, "D": 7},
    "B": {"Start": 5, "D": 3},
    "C": {"A": 4, "End": 6},
    "D": {"A": 7, "B": 3, "End": 2},
    "End": {}
}
