import re
from typing import Optional, Tuple

def parse_log_line(line: str) -> Optional[Tuple[str, str, str]]:
    
    pattern = r'\[(.*?)\]\s+(\w+):\s+(.*)'
    match = re.match(pattern, line)
    if match:
        return match.group(2), match.group(1), match.group(3)  # level, time, message
    return None
