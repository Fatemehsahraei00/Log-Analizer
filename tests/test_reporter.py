from log_analyzer.reporter import generate_report

def test_generate_report():
    data = [
        ("INFO", "t1", "msg1"),
        ("ERROR", "t2", "msg2"),
        ("INFO", "t3", "msg3"),
    ]
    report = generate_report(data)
    assert report["total"] == 3
    assert report["counts"]["INFO"] == 2
    assert report["counts"]["ERROR"] == 1
