#wc_test.py
import unittest

from wc import *
import os

class TestWordsCharsLinesCount(unittest.TestCase):
#c1032,w166,l6
    def setUp(self):
        self.filename = 'test.txt'
        self.text = """Now indulgence dissimilar for his thoroughly has terminated. Agreement offending commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted.\n\nOf resolve to gravity thought my prepare chamber so. Unsatiable entreaties collecting may sympathize nay interested instrument. If continue building numerous of at relation in margaret. Lasted engage roused mother an am at. Other early while if by do to. Missed living excuse as be. Cause heard fat above first shall for. My smiling to he removal weather on anxious.\n\nFerrars all spirits his imagine effects amongst neither. It bachelor cheerful of mistaken. Tore has sons put upon wife use bred seen. Its dissimilar invitation ten has discretion unreserved. Had you him humoured jointure ask expenses learning. Blush on in jokes sense do do. Brother hundred he assured reached on up no. On am nearer missed lovers. To it mother extent temper figure better.\n"""
        self.file = open(self.filename,'w')
        self.file.write(self.text)
        self.file.close()
    def tearDown(self):
        os.remove(self.filename)
    def test_chars(self):
        self.assertEqual(1032,chars(self.filename))
    def test_words(self):
        self.assertEqual(166,words(self.filename))
    def test_lines(self):
        self.assertEqual(6,lines(self.filename))
if __name__ == '__main__':
    unittest.main()