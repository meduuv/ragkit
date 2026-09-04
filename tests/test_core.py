from ragkit import top_k


def test_top_k():
    items = [{"id": "a", "score": 0.2}, {"id": "b", "score": 0.9}]
    assert top_k(items, 1) == [items[1]]
