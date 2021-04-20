from wordcount import numchars, numwords, numlines
import pytest
from pathlib import Path

TEST_CONTENTS = 'one two three\nfour five\n\nsix seven'
TEST_FILENAME = 'test2.txt'

@pytest.fixture
def makefile_obj():
    with open(TEST_FILENAME, 'w') as outf:
        outf.write(TEST_CONTENTS)

    inf = open(TEST_FILENAME, 'r')
    yield inf
    inf.close()
    Path(TEST_FILENAME).unlink()

def test_numchars(makefile_obj):
    assert len(TEST_CONTENTS) == numchars(filename=TEST_FILENAME)

def test_numwords(makefile_obj):
    assert len(TEST_CONTENTS.split()) == numwords(filename=TEST_FILENAME)

def test_numlines(makefile_obj):
        assert len(TEST_CONTENTS.split('\n')) == numlines(filename=TEST_FILENAME)

'''
  583  pytest -q
  584  pytest -v
  586  pip3 install coverage
  587  pytest
  588  coverage run -m pytest
  589  coverage report -m
'''
