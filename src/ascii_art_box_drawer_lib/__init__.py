"""ASCII Art Box Drawer library.

Wraps text in single, double, or rounded border boxes using pure ASCII characters.
"""

from .core import BoxStyle, draw_box, draw_box_lines

__all__ = ["BoxStyle", "draw_box", "draw_box_lines"]
