#!/usr/bin/env python3
"""Validate the normative Onyx contrast pairs without third-party dependencies."""
COLORS = {
    'paper':'FAFAF8', 'mist':'F2F2EF', 'jet':'0D0D0C', 'onyx':'20201E', 'ash50':'8C8C86',
    'orange':'E34A21', 'orange-strong':'B83B1A', 'green-strong':'12683F', 'green-bright':'47B882',
    'amber-strong':'875F00', 'amber-bright':'F2BD3A', 'red':'C9362B', 'red-bright':'E5655C',
    'blue':'246BCE', 'blue-bright':'6AA8FF'
}
def luminance(hex_value):
    channels = [int(hex_value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (.2126, .7152, .0722)))
def contrast(first, second):
    high, low = sorted((luminance(COLORS[first]), luminance(COLORS[second])), reverse=True)
    return (high + .05) / (low + .05)
TESTS = [
    ('light primary text', 'onyx', 'paper', 4.5), ('dark primary text', 'mist', 'jet', 4.5),
    ('light action/link', 'orange-strong', 'paper', 4.5), ('dark action foreground', 'orange', 'jet', 3),
    ('light success text', 'green-strong', 'paper', 4.5), ('dark success text', 'green-bright', 'jet', 4.5),
    ('light warning text', 'amber-strong', 'paper', 4.5), ('dark warning text', 'amber-bright', 'jet', 4.5),
    ('light error text', 'red', 'paper', 4.5), ('dark error text', 'red-bright', 'jet', 4.5),
    ('light info text', 'blue', 'paper', 4.5), ('dark info text', 'blue-bright', 'jet', 4.5),
    ('light focus ring', 'orange-strong', 'paper', 3), ('dark focus ring', 'mist', 'jet', 3)
]
failed = False
for label, foreground, background, minimum in TESTS:
    ratio = contrast(foreground, background)
    passed = ratio >= minimum
    print(f"{'PASS' if passed else 'FAIL'} {label}: {ratio:.2f}:1 (minimum {minimum}:1)")
    failed |= not passed
raise SystemExit(1 if failed else 0)
