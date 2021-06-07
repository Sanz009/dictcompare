import unittest

__author__ = 'Sanz009'

from compare.compare_util import compare_values, compare_values_with_case_sensitivity


class CompareUtilsTest(unittest.TestCase):

    def test_compare_values_int_1_true(self):
        value_1 = 45
        value_2 = 45
        self.assertEqual(compare_values(value_1, value_2), True)

    def test_compare_values_int_2_false(self):
        value_1 = 45
        value_2 = 450
        self.assertEqual(compare_values(value_1, value_2), False)

    def test_compare_values_str_1_true(self):
        """
        case_sensitivity is False by default so this comparison will be true
        """
        value_1 = "Stratosphere"
        value_2 = "stratosphere"
        self.assertEqual(compare_values(value_1, value_2), True)

    def test_compare_values_with_case_sensitivity_str_1_true(self):
        """
        Case_sensitivity is set to True, so this comparison will fail. - Assert 1
        Case_sensitivity is set to False, so 2nd assert will be True.
        """
        value_1 = "Stratosphere"
        value_2 = "stratosphere"
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, False), True)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, True), False)
        self.assertEqual(compare_values(value_1, value_2), True)

    def test_compare_value_int_str_mix(self):
        """
        Try to compare string and integer, returns False always.
        """
        value_1 = 40
        value_2 = "stratosphere"
        self.assertEqual(compare_values(value_1, value_2), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, True), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, False), False)

    def test_compare_values_list_1_true(self):
        value_1 = [1, 2, 3, "a"]
        value_2 = [2, 1, 3, "A"]
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, True), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, False), True)

    def test_compare_values_list_2_dictionary_items_true(self):
        value_1 = [1, 2, 3, "a", {"a": 1, "b": 2}, {"c": 2, "d": 3}]
        value_2 = [2, 1, 3, "A", {"c": 2, "d": 3}, {"a": 1, "b": 2}]
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, True), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, False), True)

    def test_compare_values_list_3_dictionary_items_false(self):
        value_1 = [1, 2, 3, "a", {"a": 1, "b": 2}, {"c": 2, "d": 3}]
        value_2 = [2, 1, 3, "A", {"c": 2, "d": 3}, {"f": 1, "b": 2}]
        self.assertEqual(compare_values(value_1, value_2), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, True), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, False), False)

    def test_compare_values_list_4_list_items(self):
        value_1 = [[1, 2], [2, 3], [3, 4]]
        value_2 = [[3, 2], [2, 1], [4, 3]]
        value_3 = [[1, 2], [2, 3], [3, 44]]
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values(value_1, value_3), False)

    def test_compare_values_dictionary_1_nested_dict_value(self):
        """
        Comparison when there is a dictionary as a value for a key in a dictionary
        """
        value_1 = {1: {"a": 1, "b": 2}, 2: {"c": 2, "d": 3}}
        value_2 = {2: {"c": 2, "d": 3}, 1: {"b": 2, "a": 1}}
        value_3 = {1: {"c": 2, "d": 3}, 2: {"b": 2, "a": 1}}
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values(value_1, value_3), False)

    def test_compare_values_dictionary_2_list_items(self):
        value_1 = {1: [{"a": 1, "b": 2}, {"y": [1, 2, 3]}], 2: [{"c": 2, "d": 3}]}
        value_2 = {2: [{"c": 2, "d": 3}], 1: [{"y": [2, 3, 1]}, {"b": 2, "a": 1}]}
        value_3 = {1: [{"c": 2, "d": 3}], 2: [{"b": 2, "a": 1}]}
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values(value_1, value_3), False)

    def test_compare_values_dictionary_2_mix(self):
        value_1 = {"a": {"b": {"c": [1, 2, 3], "d": [4, 'a', [1, 2, 3]]}, "e": "END OF B"}, "f": "END OF A"}
        value_2 = {"f": "end OF A", "a": {"e": "end OF B", "b": {"d": [4, 'a', [2, 1, 3]], "c": [3, 2, 1]}}}

        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, True), False)
        self.assertEqual(compare_values_with_case_sensitivity(value_1, value_2, False), True)

    def test_compare_values_bool_1(self):
        value_1 = [[1, True], [2, 3], [3, 4]]
        value_2 = [[3, 2], [True, 1], [4, 3]]
        value_3 = [[1, False], [2, 3], [3, 44]]
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values(value_1, value_3), False)

    def test_compare_values_dict_5_bool_val(self):
        value_1 = {1: [{"a": True, "b": 2}, {"y": [1, 2, 3]}], 2: [{"c": 2, "d": 3}]}
        value_2 = {2: [{"c": 2, "d": 3}], 1: [{"y": [2, 3, 1]}, {"b": 2, "a": True}]}
        value_3 = {1: [{"c": 2, "d": 3}], 2: [{"b": 2, "a": True}]}
        self.assertEqual(compare_values(value_1, value_2), True)
        self.assertEqual(compare_values(value_1, value_3), False)

    def test_compare_values_empty_list_variants(self):
        self.assertEqual(compare_values([], []), True)
        self.assertEqual(compare_values([{}], [{}]), True)
        self.assertEqual(compare_values([{}, {}], [{}, {}]), True)
        self.assertEqual(compare_values([{"a": [{}]}], [{"a": [{}]}]), True)
        self.assertEqual(compare_values([{"a": []}], [{"a": []}]), True)

        self.assertEqual(compare_values([], [{}]), False)
        self.assertEqual(compare_values([{}], []), False)
        self.assertEqual(compare_values([{}], [{"a": []}]), False)
        self.assertEqual(compare_values([{"a": []}], [{"a": [1, 2, 3]}]), False)
        self.assertEqual(compare_values([{"a": [{}]}], [{"a": []}]), False)
