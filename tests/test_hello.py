"""测试 hello 模块"""
from yiwen_package.hello import hello


class TestHello:
    def test_hello_runs_without_error(self, capsys):
        """测试 hello 函数能正常运行"""
        hello()
        captured = capsys.readouterr()
        assert captured.out == "hello\n"

    def test_hello_prints_correct_message(self, capsys):
        """测试 hello 函数输出正确的消息"""
        hello()
        captured = capsys.readouterr()
        assert "hello" in captured.out
