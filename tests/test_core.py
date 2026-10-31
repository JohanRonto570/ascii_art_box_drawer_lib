import unittest

from ascii_art_box_drawer_lib import BoxStyle, draw_box, draw_box_lines


class TestDrawBox(unittest.TestCase):
    def test_single_line_single_style(self):
        result = draw_box("hello")
        expected = "\n".join([
            "+-------+",
            "| hello |",
            "+-------+",
        ])
        self.assertEqual(result, expected)

    def test_multi_line_single_style(self):
        result = draw_box("one\ntwo")
        expected = "\n".join([
            "+-----+",
            "| one |",
            "| two |",
            "+-----+",
        ])
        self.assertEqual(result, expected)

    def test_double_style(self):
        result = draw_box("hi", style=BoxStyle.DOUBLE)
        expected = "\n".join([
            "+====+",
            "| hi |",
            "+====+",
        ])
        self.assertEqual(result, expected)

    def test_rounded_style(self):
        result = draw_box("hi", style=BoxStyle.ROUNDED)
        expected = "\n".join([
            ".----.",
            "| hi |",
            "'----'",
        ])
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = draw_box("")
        expected = "\n".join([
            "+--+",
            "|  |",
            "+--+",
        ])
        self.assertEqual(result, expected)

    def test_trailing_newline_ignored(self):
        result = draw_box("a\n")
        expected = "\n".join([
            "+---+",
            "| a |",
            "+---+",
        ])
        self.assertEqual(result, expected)

    def test_leading_and_trailing_spaces_preserved(self):
        result = draw_box("  x  ")
        expected = "\n".join([
            "+-------+",
            "|   x   |",
            "+-------+",
        ])
        self.assertEqual(result, expected)

    def test_ragged_lines_padded(self):
        result = draw_box("a\nlonger")
        expected = "\n".join([
            "+--------+",
            "| a      |",
            "| longer |",
            "+--------+",
        ])
        self.assertEqual(result, expected)

    def test_type_error_for_non_string_text(self):
        with self.assertRaises(TypeError):
            draw_box(123)

    def test_value_error_for_bad_style(self):
        with self.assertRaises(ValueError):
            draw_box("x", style="single")


class TestDrawBoxLines(unittest.TestCase):
    def test_empty_list(self):
        result = draw_box_lines([])
        expected = [
            "+--+",
            "|  |",
            "+--+",
        ]
        self.assertEqual(result, expected)

    def test_single_line(self):
        result = draw_box_lines(["hi"])
        expected = [
            "+----+",
            "| hi |",
            "+----+",
        ]
        self.assertEqual(result, expected)

    def test_double_style(self):
        result = draw_box_lines(["hi"], style=BoxStyle.DOUBLE)
        expected = [
            "+====+",
            "| hi |",
            "+====+",
        ]
        self.assertEqual(result, expected)

    def test_rounded_style(self):
        result = draw_box_lines(["hi"], style=BoxStyle.ROUNDED)
        expected = [
            ".----.",
            "| hi |",
            "'----'",
        ]
        self.assertEqual(result, expected)

    def test_type_error_for_non_list(self):
        with self.assertRaises(TypeError):
            draw_box_lines("not a list")

    def test_type_error_for_non_string_line(self):
        with self.assertRaises(TypeError):
            draw_box_lines(["ok", 123])

    def test_value_error_for_bad_style(self):
        with self.assertRaises(ValueError):
            draw_box_lines(["x"], style=123)


if __name__ == "__main__":
    unittest.main()
