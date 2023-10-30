#!/usr/bin/env python3
"""Parameterized Unittests"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class to test the access_nested_map funtion"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Function tests the output of access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Function tests some exceptions and raises KeyError"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Function tests get_jsons output"""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Class to test the memoize function"""
    def test_memoize(self):
        """method to test memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_func:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_func.assert_called_once()


if __name__ == '__main__':
    unittest.main()
