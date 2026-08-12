import argparse
from .parser import parse_log_line
from .reporter import generate_report
from .logger_config import setup_logger


def main():
    parser = argparse.ArgumentParser(description="Log file analyzer")
    parser.add_argument("logfile", help="Path to the input log file")
    args = parser.parse_args()

    logger = setup_logger()
    logger.info(f"Starting analysis of file {args.logfile}")

    parsed = []
    with open(args.logfile, 'r', encoding='utf-8') as f:
        for line in f:
            result = parse_log_line(line)
            if result:
                parsed.append(result)
            else:
                logger.warning(f"Invalid line: {line.strip()}")

    report = generate_report(parsed)
    print(f"Total lines: {report['total']}")
    print("Count by level:", report['counts'])
    print("Sample errors:", report['errors'])
    logger.info("Analysis completed")
