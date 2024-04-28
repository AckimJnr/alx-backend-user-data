#!/usr/bin/env python3

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: A list of strings representing fields to obfuscate.
        redaction: A string representing the character to use for obfuscation.
        message: A string representing the log line.
        separator: A string representing the character
        separating all fields in the log line.

    Returns:
        A string with specified fields obfuscated.
    """
    return re.sub(r'({})[^{}]+'.format('|'.join(fields), separator),
                  lambda match: redaction * len(match.group(0)), message)
