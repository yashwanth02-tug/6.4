def normalize(scores):
    """Normalizes a list of numeric scores to the [0, 1] range.

    Each score is scaled so that the minimum value becomes 0 and the maximum becomes 1.
    If all scores are equal, returns a list of zeros of the same length.
    If the input list is empty, returns an empty list.

    Args:
        scores (list of float or int): The list of scores to normalize.

    Returns:
        list of float: The normalized scores in the [0, 1] range.

    Examples:
        >>> normalize([10, 20, 30])
        [0.0, 0.5, 1.0]
        >>> normalize([5, 5, 5])
        [0.0, 0.0, 0.0]
        >>> normalize([])
        []
        >>> normalize([3])
        [0.0]
    """
    if not scores:
        return []
    m = max(scores)
    n = min(scores)
    if m == n:
        return [0.0] * len(scores)
    return [(x - n) / (m - n) for x in scores]


# Unit tests
def test_normalize():
    # Test normal case
    assert normalize([10, 20, 30]) == [0.0, 0.5, 1.0]
    # Test all elements equal (m == n)
    assert normalize([5, 5, 5]) == [0.0, 0.0, 0.0]
    # Test empty list
    assert normalize([]) == []
    # Test single element (m == n)
    assert normalize([3]) == [0.0]
    # Test negative numbers
    assert normalize([-2, 0, 2]) == [0.0, 0.5, 1.0]
    # Test floats
    assert normalize([1.5, 2.5, 3.5]) == [0.0, 0.5, 1.0]
    # Test m == n with negative number
    assert normalize([-7, -7, -7]) == [0.0, 0.0, 0.0]
    print("All tests passed.")

if __name__ == "__main__":
    test_normalize()
