"""
Dict Compare Utils - Methods to compare simple/nested dictionaries with
String, Integer, Bool, Lists[of any of these], or even dictionaries as values.

Case Sensitivity can be checked/unchecked.
"""

__author__ = 'Sanz009'


from typing import Union, List, Dict, Optional


def compare_dict_values(dict_1, dict_2, case_sensitivity=False):
    # type: (Dict, Dict, Optional[bool]) -> bool
    """
    Compares 2 dictionaries and return True/False based on whether they are equal or not
    :param case_sensitivity: If string comparisons are to be made with case_sensitivity in mind.
    :param dict_1: Dictionary to be compared against dict_2
    :param dict_2: Dictionary to be compared against dict_1
    :return:
    """
    if len(dict_1.keys()) != len(dict_2.keys()):
        return False
    flag = False
    for key, value in dict_1.items():
        if key in dict_2 and compare_values(value, dict_2[key], case_sensitivity):
            flag = True
        else:
            return False
    return flag


def _compare_list_keys(exclude_index, item, list_2, case_sensitivity):
    # type: (List, Union[str, Dict, List, int, bool], Union[str, Dict, List, int, bool], bool) -> bool
    flag = 0
    for i in range(0, len(list_2)):
        if i in exclude_index:
            continue
        elif compare_values(item, list_2[i], case_sensitivity):
            exclude_index.append(i)
            flag = 1
            break
        else:
            flag = 0
    return True if flag else False


def compare_list_values(list_1, list_2, case_sensitivity=False):
    # type: (List, List, Optional[bool]) -> bool
    """
    Compares 2 lists and returns True/False based on whether they are equal or not
    Eg: list1 -> [1,2,2] equal to list2 ->[2,1,2]
        list1 -> [2, {"a":3}, {"b":2"}] equal to list2 -> [{"b":2}, {"a":3}, 2]
    :param case_sensitivity: If string comparisons are to be made with case_sensitivity in mind.
    :param list_1: First list to compare
    :param list_2: Second list to compare
    :return:
    """
    if len(list_1) != len(list_2):
        return False
    else:
        exclude_index = []
        for item in list_1:
            if not _compare_list_keys(exclude_index, item, list_2, case_sensitivity):
                return False
        return True


def compare_values(value_1, value_2, case_sensitivity=False):
    # type: (Union[str, Dict, List, int, bool], Union[str, Dict, List, int, bool], Optional[bool]) -> bool
    """
    Does comparison of value 1 and value 2
    Value 1 and Value 2 can be any data type of [int, str, List, Dict]
    Value 1/2 can be a combination of these <s>supported<a> data<n> types<0> also<z>
    Eg: [[1,2],[2,3],'a', 1, {"a":1}] -> This is a<0> list<9> containing lists , integer, string and even a dict as items.
    This list is equal to [1, 'a', [2,1], [3,2], {"a":1}]
    By default case_sensitivity is true.
    :param case_sensitivity: If string comparisons are to be made with case_sensitivity in mind.
    :param value_1: value to be compared against value 2
    :param value_2: value to be compared against value 1
    :return:
    """
    if type(value_1) != type(value_2):
        return False
    elif isinstance(value_1, int) or isinstance(value_1, bool):
        return value_1 == value_2
    elif isinstance(value_1, str):
        return value_1.lower() == value_2.lower() if not case_sensitivity else value_1 == value_2
    elif isinstance(value_1, dict):
        return compare_dict_values(value_1, value_2, case_sensitivity)
    elif isinstance(value_1, list):
        return compare_list_values(value_1, value_2, case_sensitivity)


def compare_values_with_case_sensitivity(value_1, value_2, case_sensitivity):
    # type: (Union[str, Dict, List, int, bool], Union[str, Dict, List, int, bool], bool) -> bool
    """
    Provides a method to compare 2 values, considering case_sensitivity for string comparisons
    If case_sense is set to False, then string comparisons are done without considering case_sensitivity
    Else: Case sensitivity is considered for string comparisons.

    Default value is False for case sensitivity.
    This method calls compare_values to compare value_1 and value2.
    :param case_sensitivity: If string comparisons are to be made with case_sensitivity in mind.
    :param value_1: First value to compare
    :param value_2: Second value to compare
    :return:
    """
    return compare_values(value_1, value_2, case_sensitivity)
