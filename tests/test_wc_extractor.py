from pywc.wc_extractor import WCExtractor
from pywc.wc_extractor_processor import WCExtractorProcessor, DIRECTION

import unittest
from unittest.mock import MagicMock


class TestWCExtractor(unittest.TestCase):

    def test_generate_table(self):

        extractor = WCExtractor(direction=DIRECTION.DESCENDING, limit=3)

        list_wc = [{'word': 'the', 'word_count': 119, 'files': {'doc1.txt': ["The story", "And the book"]}}, {'word': 'and', 'word_count': 103, 'files': {'doc1.txt': ["Me and you", "This and that"]}}, {'word': 'to', 'word_count': 93, 'files': {'doc1.txt': ["To here.", "there to"]}}]

        # Test table is generated in the right format with the defaults
        expected_headers = ['word', 'count', 'files', 'sentences']
        expected_rows = [['the', '119', 'doc1.txt', "The story, And the book"], ['and', '103', 'doc1.txt', "Me and you, This and that"], ['to', '93', 'doc1.txt', "To here., there to"]]

        headers, rows = extractor._generate_table(list_wc)

        self.assertEqual(expected_headers, headers)
        self.assertEqual(expected_rows, rows)


        # Test that table is generated in the right format with limit of columns and char_limit
        headers, rows = extractor._generate_table(list_wc, char_limit=5, columns=['word','sentences'])

        expected_headers = ['word', 'sentences']
        expected_rows = [['the', "The s..."], ['and', "Me an..."], ['to', "To he..."]]

        self.assertEqual(expected_headers, headers)
        self.assertEqual(expected_rows, rows)

