from api.utils.routes import remove_duplicates_by_key


def test_remove_duplicates_by_key(list_of_duplicated_dicts):
    """
    GIVEN a list of dictionaries with a unique key and duplicate entries
    WHEN creating new list with unique entries
    THEN return new list with duplicates removed
    """

    list_of_duplicated_dicts_length = len(list_of_duplicated_dicts)

    unique_list = remove_duplicates_by_key(list_of_duplicated_dicts, key="id")
    unique_list_length = len(unique_list)

    if len(unique_list):
        dict1, dict2 = unique_list[0], unique_list[1]

    assert type(unique_list) is list
    assert unique_list_length > 0, "all entries removed, not just duplicates"
    assert unique_list_length != list_of_duplicated_dicts_length, "same length as original, no duplicates removed"
    assert not (unique_list_length > 2), "too many removed"
    assert not (unique_list_length < 2), "duplicate entry missed"
    assert dict1["author"] == "Rylee Paul"
    assert dict2["author"] == "Zackery Turner"
