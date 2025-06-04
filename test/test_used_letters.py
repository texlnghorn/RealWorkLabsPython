from used_letters import find_unused_letters

import unittest


class TestUnusedLetters(unittest.TestCase):
    def test_find_unused_letters(self):
        output = find_unused_letters("A slow yellow fox crawls under the proactive dog")
        assert output == "bjkmqz"

    def test_non_ascii_letters(self):
        output = find_unused_letters(
            "1234 A slow yellow fox crawls under the proactive dog #*&"
        )
        assert output == "bjkmqz"

    def test_all_ascii_letters_used(self):
        output = find_unused_letters("A quick brown fox jumps over the lazy dog")
        assert output == ""

    def test_empty_string(self):
        output = find_unused_letters("")
        assert output == "abcdefghijklmnopqrstuvwxyz"

    def test_null_string(self):
        output = find_unused_letters(None)
        assert output == "abcdefghijklmnopqrstuvwxyz"
