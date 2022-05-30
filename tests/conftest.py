import pytest


@pytest.fixture(scope="session")
def list_of_duplicated_dicts():
    """A list of dictionary objects with the same id shared by two."""
    list_of_dicts = [
        {
            "author": "Rylee Paul",
            "authorId": 9,
            "id": 1,
            "likes": 960,
            "popularity": 0.13,
            "reads": 50361,
            "tags": ["tech", "health"],
        },
        {
            "author": "Zackery Turner",
            "authorId": 12,
            "id": 2,
            "likes": 469,
            "popularity": 0.68,
            "reads": 90406,
            "tags": ["startups", "tech", "history"],
        },
        {
            "author": "Rylee Paul",
            "authorId": 9,
            "id": 1,
            "likes": 960,
            "popularity": 0.13,
            "reads": 50361,
            "tags": ["tech", "health"],
        },
        {
            "author": "Apple Jacks",
            "authorId": 33,
            "id": 2,
            "likes": 1960,
            "popularity": 0.73,
            "reads": 50362,
            "tags": ["tech", "health"],
        },
    ]
    return list_of_dicts
