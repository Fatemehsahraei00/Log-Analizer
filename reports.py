from collections import Counter
from typing import List, Dict

def generate_report(parsed_lines: List[Tuple[str, str, str]]) -> Dict:
    levels = [level for level, _, _ in parsed_lines]
    counter = Counter(levels)
    errors = [msg for level, _, msg in parsed_lines if level == "ERROR"]
    return {
        "total": len(parsed_lines),
        "counts": dict(counter),
        "errors": errors[:10]  # ۱۰ خطای اول
    }
