import pytest
from log_analyzer.parser import parse_log_line

def test_parse_valid_line():
    line = "[2026-08-07 10:15:32] INFO: User logged in"
    level, time, msg = parse_log_line(line)
    assert level == "INFO"
    assert time == "2026-08-07 10:15:32"
    assert msg == "User logged in"

def test_parse_invalid_line():
    assert parse_log_line("not a log line") is None
