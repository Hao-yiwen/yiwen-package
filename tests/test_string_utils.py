"""测试字符串工具函数"""
from yiwen_package.string_utils import (
    is_empty,
    truncate,
    remove_prefix,
    remove_suffix,
    camel_to_snake,
    snake_to_camel,
)


class TestIsEmpty:
    def test_empty_string(self):
        assert is_empty("") is True

    def test_whitespace_string(self):
        assert is_empty("   ") is True
        assert is_empty("\t\n") is True

    def test_non_empty_string(self):
        assert is_empty("hello") is False
        assert is_empty(" hello ") is False


class TestTruncate:
    def test_short_string(self):
        assert truncate("hello", 10) == "hello"

    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"

    def test_truncate_with_default_suffix(self):
        assert truncate("hello world", 8) == "hello..."

    def test_truncate_with_custom_suffix(self):
        assert truncate("hello world", 8, ">>") == "hello >>"

    def test_truncate_very_short(self):
        result = truncate("hello world", 3)
        assert len(result) == 3


class TestRemovePrefix:
    def test_remove_existing_prefix(self):
        assert remove_prefix("hello_world", "hello_") == "world"

    def test_no_prefix(self):
        assert remove_prefix("hello_world", "foo_") == "hello_world"

    def test_empty_prefix(self):
        assert remove_prefix("hello", "") == "hello"


class TestRemoveSuffix:
    def test_remove_existing_suffix(self):
        assert remove_suffix("hello_world", "_world") == "hello"

    def test_no_suffix(self):
        assert remove_suffix("hello_world", "_foo") == "hello_world"

    def test_empty_suffix(self):
        assert remove_suffix("hello", "") == "hello"


class TestCamelToSnake:
    def test_simple_camel_case(self):
        assert camel_to_snake("CamelCase") == "camel_case"

    def test_lower_camel_case(self):
        assert camel_to_snake("camelCase") == "camel_case"

    def test_multiple_words(self):
        assert camel_to_snake("MyClassName") == "my_class_name"

    def test_with_numbers(self):
        assert camel_to_snake("Test123Value") == "test123_value"

    def test_already_snake_case(self):
        assert camel_to_snake("snake_case") == "snake_case"


class TestSnakeToCamel:
    def test_simple_snake_case(self):
        assert snake_to_camel("snake_case") == "snakeCase"

    def test_capitalize_first(self):
        assert snake_to_camel("snake_case", capitalize_first=True) == "SnakeCase"

    def test_multiple_words(self):
        assert snake_to_camel("my_class_name") == "myClassName"
        assert snake_to_camel("my_class_name", capitalize_first=True) == "MyClassName"

    def test_single_word(self):
        assert snake_to_camel("word") == "word"
        assert snake_to_camel("word", capitalize_first=True) == "Word"
