"""测试文件工具函数"""
from pathlib import Path
from yiwen_package.file_utils import (
    read_json,
    write_json,
    ensure_dir,
    get_file_size,
    format_file_size,
)


class TestJsonOperations:
    def test_write_and_read_json(self, tmp_path):
        """测试 JSON 读写"""
        file_path = tmp_path / "test.json"
        data = {"name": "test", "value": 123, "items": [1, 2, 3]}

        write_json(file_path, data)
        result = read_json(file_path)

        assert result == data

    def test_write_json_with_chinese(self, tmp_path):
        """测试中文 JSON 写入"""
        file_path = tmp_path / "test_chinese.json"
        data = {"名称": "测试", "值": 456}

        write_json(file_path, data)
        result = read_json(file_path)

        assert result == data

    def test_write_json_custom_indent(self, tmp_path):
        """测试自定义缩进"""
        file_path = tmp_path / "test_indent.json"
        data = {"a": 1, "b": 2}

        write_json(file_path, data, indent=4)

        with open(file_path, 'r') as f:
            content = f.read()

        assert '    "a"' in content  # 4 spaces indent


class TestEnsureDir:
    def test_create_new_directory(self, tmp_path):
        """测试创建新目录"""
        new_dir = tmp_path / "new_folder"
        result = ensure_dir(new_dir)

        assert new_dir.exists()
        assert new_dir.is_dir()
        assert result == new_dir

    def test_existing_directory(self, tmp_path):
        """测试已存在的目录"""
        existing_dir = tmp_path / "existing"
        existing_dir.mkdir()

        result = ensure_dir(existing_dir)

        assert result == existing_dir
        assert existing_dir.exists()

    def test_nested_directories(self, tmp_path):
        """测试创建嵌套目录"""
        nested_dir = tmp_path / "a" / "b" / "c"
        result = ensure_dir(nested_dir)

        assert nested_dir.exists()
        assert nested_dir.is_dir()


class TestGetFileSize:
    def test_get_size_of_file(self, tmp_path):
        """测试获取文件大小"""
        file_path = tmp_path / "test.txt"
        content = "Hello World!"
        file_path.write_text(content)

        size = get_file_size(file_path)

        assert size == len(content.encode('utf-8'))

    def test_empty_file(self, tmp_path):
        """测试空文件"""
        file_path = tmp_path / "empty.txt"
        file_path.write_text("")

        size = get_file_size(file_path)

        assert size == 0


class TestFormatFileSize:
    def test_bytes(self):
        assert format_file_size(100) == "100.00 B"
        assert format_file_size(1023) == "1023.00 B"

    def test_kilobytes(self):
        assert format_file_size(1024) == "1.00 KB"
        assert format_file_size(1536) == "1.50 KB"

    def test_megabytes(self):
        assert format_file_size(1024 * 1024) == "1.00 MB"
        assert format_file_size(1024 * 1024 * 2.5) == "2.50 MB"

    def test_gigabytes(self):
        assert format_file_size(1024 * 1024 * 1024) == "1.00 GB"

    def test_terabytes(self):
        assert format_file_size(1024 * 1024 * 1024 * 1024) == "1.00 TB"

    def test_zero(self):
        assert format_file_size(0) == "0.00 B"
