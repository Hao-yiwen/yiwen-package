"""测试列表工具函数"""
from yiwen_package.list_utils import chunk, flatten, unique, group_by


class TestChunk:
    def test_exact_chunks(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_chunks(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_size_larger_than_list(self):
        assert chunk([1, 2], 5) == [[1, 2]]

    def test_empty_list(self):
        assert chunk([], 2) == []

    def test_chunk_size_one(self):
        assert chunk([1, 2, 3], 1) == [[1], [2], [3]]


class TestFlatten:
    def test_nested_list(self):
        assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_deeply_nested_list(self):
        assert flatten([[1, [2, 3]], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

    def test_flat_list(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_empty_list(self):
        assert flatten([]) == []

    def test_mixed_nesting(self):
        assert flatten([1, [2, 3], 4, [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]


class TestUnique:
    def test_remove_duplicates(self):
        assert unique([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]

    def test_preserve_order(self):
        assert unique([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_no_duplicates(self):
        assert unique([1, 2, 3]) == [1, 2, 3]

    def test_empty_list(self):
        assert unique([]) == []

    def test_with_key_function(self):
        data = [{'id': 1, 'val': 'a'}, {'id': 2, 'val': 'b'}, {'id': 1, 'val': 'c'}]
        result = unique(data, key=lambda x: x['id'])
        assert len(result) == 2
        assert result[0]['id'] == 1
        assert result[1]['id'] == 2

    def test_strings(self):
        assert unique(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']


class TestGroupBy:
    def test_group_numbers_by_parity(self):
        result = group_by([1, 2, 3, 4, 5, 6], lambda x: x % 2)
        assert result[0] == [2, 4, 6]
        assert result[1] == [1, 3, 5]

    def test_group_strings_by_length(self):
        result = group_by(['a', 'bb', 'ccc', 'dd', 'e'], lambda x: len(x))
        assert result[1] == ['a', 'e']
        assert result[2] == ['bb', 'dd']
        assert result[3] == ['ccc']

    def test_empty_list(self):
        result = group_by([], lambda x: x)
        assert result == {}

    def test_group_dicts_by_key(self):
        data = [
            {'type': 'A', 'value': 1},
            {'type': 'B', 'value': 2},
            {'type': 'A', 'value': 3},
        ]
        result = group_by(data, lambda x: x['type'])
        assert len(result['A']) == 2
        assert len(result['B']) == 1
