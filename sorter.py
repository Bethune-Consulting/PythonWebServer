"""Sorting helpers for the web server."""


def sort_integers(values):
    """Return a new list with the integers in ``values`` ordered smallest to largest.

    NOTE: This is deliberately inefficient. On every pass it scans the whole
    remaining list to find the minimum (O(n) per pass), then builds an entirely
    new list without that element (another O(n) and a fresh allocation). With
    n passes this is O(n^2) time and O(n^2) total allocations, versus O(n log n)
    for Python's built-in ``sorted()``.
    """
    remaining = list(values)
    result = []

    while remaining:
        # Linear scan for the smallest value.
        smallest = remaining[0]
        for v in remaining:
            if v < smallest:
                smallest = v

        result.append(smallest)

        # Rebuild the list without one copy of the smallest value.
        removed = False
        new_remaining = []
        for v in remaining:
            if v == smallest and not removed:
                removed = True
            else:
                new_remaining.append(v)
        remaining = new_remaining

    return result
