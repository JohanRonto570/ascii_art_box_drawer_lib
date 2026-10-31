"""Core implementation of the ASCII Art Box Drawer.

All borders are drawn with 7-bit ASCII characters only.
"""

from enum import Enum, auto
from typing import List


class BoxStyle(Enum):
    """Available border styles.

    The characters are chosen to be visually distinct while staying within
    printable ASCII.  Rounded corners use '.' because ASCII has no arc
    character; this is a deliberate trade-off documented in the README.
    """

    SINGLE = auto()
    DOUBLE = auto()
    ROUNDED = auto()


# Mapping from style to (top_left, top_right, bottom_left, bottom_right,
# horizontal, vertical).  The order is fixed to keep the lookup simple.
_BORDER_CHARS = {
    BoxStyle.SINGLE: ("+", "+", "+", "+", "-", "|"),
    BoxStyle.DOUBLE: ("+", "+", "+", "+", "=", "|"),
    BoxStyle.ROUNDED: (".", ".", "'", "'", "-", "|"),
}


def draw_box(text: str, style: BoxStyle = BoxStyle.SINGLE) -> str:
    """Wrap *text* in a box drawn with the given *style*.

    The text may contain newlines; each line is placed on its own row inside
    the box.  The box width is the length of the longest line.  Short lines
    are padded with spaces on the right so that the right border is straight.

    Args:
        text: The content to wrap.  Leading and trailing whitespace on each
            line is preserved, but a trailing newline in *text* is ignored
            (it does not create an extra empty row).
        style: One of the :class:`BoxStyle` members.  Defaults to
            ``BoxStyle.SINGLE``.

    Returns:
        A string containing the box.  Lines are separated by ``\n`` and the
        result does not end with a newline.

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *style* is not a :class:`BoxStyle` member.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(style, BoxStyle):
        raise ValueError("style must be a BoxStyle member")

    # splitlines() drops a trailing newline, which is what we want: a string
    # ending in '\n' should not produce an extra empty line inside the box.
    lines = text.splitlines()
    if not lines:
        # An empty string becomes a single empty line so the box is still
        # visible (two horizontal borders with a one-space interior).
        lines = [""]

    return "\n".join(draw_box_lines(lines, style))


def draw_box_lines(lines: List[str], style: BoxStyle = BoxStyle.SINGLE) -> List[str]:
    """Wrap a list of lines in a box and return the resulting lines.

    This is the lower-level function used by :func:`draw_box`.  It does not
    join the lines; it returns a list so callers can process them further.

    Args:
        lines: The content lines.  Must be a list of strings.  An empty list
            is treated as a single empty line.
        style: One of the :class:`BoxStyle` members.

    Returns:
        A list of strings, each representing one row of the box.

    Raises:
        TypeError: If *lines* is not a list or contains non-strings.
        ValueError: If *style* is not a :class:`BoxStyle` member.
    """
    if not isinstance(lines, list):
        raise TypeError("lines must be a list")
    for line in lines:
        if not isinstance(line, str):
            raise TypeError("all lines must be strings")
    if not isinstance(style, BoxStyle):
        raise ValueError("style must be a BoxStyle member")

    if not lines:
        lines = [""]

    tl, tr, bl, br, h, v = _BORDER_CHARS[style]

    # The interior width is the length of the longest line.  We do not add
    # extra padding beyond one space on each side, because that would make
    # the box wider than necessary and surprise users who align boxes.
    max_len = max(len(line) for line in lines)

    top = tl + (h * (max_len + 2)) + tr
    bottom = bl + (h * (max_len + 2)) + br

    result = [top]
    for line in lines:
        # Pad on the right so the right border lines up.  We do not strip or
        # modify the line content otherwise.
        padded = line.ljust(max_len)
        result.append(f"{v} {padded} {v}")
    result.append(bottom)

    return result
