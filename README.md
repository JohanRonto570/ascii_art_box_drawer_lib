# ascii_art_box_drawer_lib

Wraps text in single, double, or rounded border boxes using pure ASCII characters.

```python
from ascii_art_box_drawer_lib import draw_box, BoxStyle

print(draw_box("Hello\nWorld"))
# +-------+
# | Hello |
# | World |
# +-------+

print(draw_box("Hi", style=BoxStyle.DOUBLE))
# +====+
# | Hi |
# +====+

print(draw_box("Hi", style=BoxStyle.ROUNDED))
# .----.
# | Hi |
# '----'
```

## Why this library exists

Most box-drawing libraries use Unicode line-drawing characters, which look
better but break in environments that only handle 7-bit ASCII (some terminals,
legacy systems, or restrictive log pipelines).  This library deliberately
restricts itself to printable ASCII.  The trade-off is that the "rounded"
style cannot use true arcs; it uses `.` for the top corners and `'` for the
bottom corners, which is the closest visual approximation available in ASCII.

## API

- `BoxStyle` – enum with `SINGLE`, `DOUBLE`, and `ROUNDED` members.
- `draw_box(text, style=BoxStyle.SINGLE) -> str` – returns the box as a
  single string with `\n` line separators and no trailing newline.
- `draw_box_lines(lines, style=BoxStyle.SINGLE) -> list[str]` – lower-level
  function that takes a list of lines and returns the box as a list of lines.

## Edge cases

- An empty string or an empty list produces a minimal box with a single
  empty interior line (two horizontal borders and one row of spaces).
- A trailing newline in the input is ignored; it does not create an extra
  empty row.
- Lines shorter than the longest line are padded with spaces on the right
  so the right border is straight.
- Leading and trailing spaces on each line are preserved.
