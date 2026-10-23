"""Apply current display terminology without renaming preserved identifiers."""
import json
import re
from pathlib import Path

TERMS = json.loads((Path(__file__).resolve().parents[1] / 'data/terminology.json').read_text())
DISPLAY_NAME = TERMS['display_name']
LEGACY_NAMES = (
    '인플루언서 발굴·메일 발송 자동화 도구',
    '인플루언서 발굴·메일 발송 자동화',
    'IRM 업무 자동화 도구',
    'IRM 업무 자동화',
    'IRM 자동화 도구',
    'IRM 자동화',
    'IRM',
    '영업 자동화',
)
NAME_PATTERN = re.compile(r'(?<![A-Za-z0-9_/#])(?:' + '|'.join(map(re.escape, LEGACY_NAMES)) + r')(?![A-Za-z0-9_/-])')


def normalize_text(text):
    """Normalize display labels and the particles affected by the new name."""
    text = NAME_PATTERN.sub(DISPLAY_NAME, text)
    text = re.sub(re.escape(DISPLAY_NAME) + r'(?:\s+(?:업무\s+)?자동화\s+도구|\s+도구)', DISPLAY_NAME, text)
    for old, new in (('으로', '로'), ('은', '는'), ('을', '를'), ('과', '와')):
        text = text.replace(DISPLAY_NAME + old, DISPLAY_NAME + new)
    text = re.sub(re.escape(DISPLAY_NAME) + r'이(?=\s|[.,!?]|$)', DISPLAY_NAME + '가', text)
    return text


def normalize_html(source):
    """Update prose and accessibility text, retaining links, ids and paths."""
    source = re.sub(r'(?<=>)[^<]+(?=<)', lambda match: normalize_text(match[0]), source)
    return re.sub(r'\b(alt|aria-label|content|title)="([^"]*)"',
                  lambda match: f'{match[1]}="{normalize_text(match[2])}"', source)
