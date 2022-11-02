import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath("C:\\Users\\kyvin\\PycharmProjects\\QuantNeg_Webcrawler\\QNI.py") ) ) )
from QNI import find_quantifier_negation
from pathlib import Path

file_path = {}
directory_path = Path.cwd()

for file in directory_path.iterdir():
    if file.match("*.txt"):
        file_path[file.stem.split("_")[0]] = file

class Every_Detectiontest(unittest.TestCase):
    #quantifiers
    def test_detect_every_quant(self):
        pass

class No_Detectiontest(unittest.TestCase):
    def test_detect_no_quant(self):
        pass

    def test_detect_some_quant(self):
        pass

    #Standalone or continous
    def test_identify_standalone(self):
        pass

    def test_identify_continuous(self):
        pass


if __name__ == "__main__":
    pass