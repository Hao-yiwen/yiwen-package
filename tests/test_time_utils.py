"""测试时间工具函数"""
from datetime import datetime, timedelta
from yiwen_package.time_utils import (
    now_timestamp,
    now_timestamp_ms,
    format_datetime,
    parse_datetime,
    time_ago,
    add_days,
)


class TestTimestamps:
    def test_now_timestamp_returns_integer(self):
        ts = now_timestamp()
        assert isinstance(ts, int)
        assert ts > 0

    def test_now_timestamp_ms_returns_integer(self):
        ts = now_timestamp_ms()
        assert isinstance(ts, int)
        assert ts > 0

    def test_timestamp_ms_is_larger(self):
        ts_sec = now_timestamp()
        ts_ms = now_timestamp_ms()
        # 毫秒时间戳应该大约是秒时间戳的 1000 倍
        assert ts_ms // 1000 == ts_sec or ts_ms // 1000 == ts_sec + 1


class TestFormatDateTime:
    def test_format_default(self):
        dt = datetime(2023, 11, 6, 14, 30, 45)
        result = format_datetime(dt)
        assert result == "2023-11-06 14:30:45"

    def test_format_custom(self):
        dt = datetime(2023, 11, 6, 14, 30, 45)
        result = format_datetime(dt, fmt='%Y/%m/%d')
        assert result == "2023/11/06"

    def test_format_now(self):
        # 测试不传 dt 参数，应该格式化当前时间
        result = format_datetime()
        assert isinstance(result, str)
        assert len(result) == 19  # "YYYY-MM-DD HH:MM:SS"

    def test_format_iso(self):
        dt = datetime(2023, 11, 6, 14, 30, 45)
        result = format_datetime(dt, fmt='%Y-%m-%dT%H:%M:%S')
        assert result == "2023-11-06T14:30:45"


class TestParseDateTime:
    def test_parse_default_format(self):
        dt = parse_datetime("2023-11-06 14:30:45")
        assert dt.year == 2023
        assert dt.month == 11
        assert dt.day == 6
        assert dt.hour == 14
        assert dt.minute == 30
        assert dt.second == 45

    def test_parse_custom_format(self):
        dt = parse_datetime("2023/11/06", fmt='%Y/%m/%d')
        assert dt.year == 2023
        assert dt.month == 11
        assert dt.day == 6

    def test_parse_iso_format(self):
        dt = parse_datetime("2023-11-06T14:30:45", fmt='%Y-%m-%dT%H:%M:%S')
        assert dt == datetime(2023, 11, 6, 14, 30, 45)


class TestTimeAgo:
    def test_seconds_ago(self):
        dt = datetime.now() - timedelta(seconds=30)
        result = time_ago(dt)
        assert "秒前" in result

    def test_minutes_ago(self):
        dt = datetime.now() - timedelta(minutes=5)
        result = time_ago(dt)
        assert "分钟前" in result

    def test_hours_ago(self):
        dt = datetime.now() - timedelta(hours=3)
        result = time_ago(dt)
        assert "小时前" in result

    def test_days_ago(self):
        dt = datetime.now() - timedelta(days=5)
        result = time_ago(dt)
        assert "天前" in result

    def test_months_ago(self):
        dt = datetime.now() - timedelta(days=60)
        result = time_ago(dt)
        assert "个月前" in result

    def test_years_ago(self):
        dt = datetime.now() - timedelta(days=400)
        result = time_ago(dt)
        assert "年前" in result


class TestAddDays:
    def test_add_positive_days(self):
        dt = datetime(2023, 11, 6)
        result = add_days(dt, 5)
        assert result == datetime(2023, 11, 11)

    def test_add_negative_days(self):
        dt = datetime(2023, 11, 6)
        result = add_days(dt, -5)
        assert result == datetime(2023, 11, 1)

    def test_add_zero_days(self):
        dt = datetime(2023, 11, 6)
        result = add_days(dt, 0)
        assert result == dt

    def test_cross_month_boundary(self):
        dt = datetime(2023, 11, 28)
        result = add_days(dt, 5)
        assert result == datetime(2023, 12, 3)

    def test_cross_year_boundary(self):
        dt = datetime(2023, 12, 30)
        result = add_days(dt, 5)
        assert result == datetime(2024, 1, 4)
