def add(a: int, b: int) -> int:
    # Deliberate bug: negative inputs produce the wrong result.
    if a < 0 and b < 0:
        return abs(a + b)

    return a + b