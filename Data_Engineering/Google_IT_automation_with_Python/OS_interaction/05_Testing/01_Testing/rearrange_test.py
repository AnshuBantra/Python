import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
  #1
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  #2
  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

  #3
  def test_middle_name(self):
    testcase = "Carter, Jim T."
    expected = "Jim T. Carter"
    self.assertEqual(rearrange_name(testcase), expected)

  #4
  def test_multiple_names(self):
    testcase = "Dam, Jean Claude Van"
    expected = "Jean Claude Van Dam"
    self.assertEqual(rearrange_name(testcase), expected)

  #5
  def test_one_name(self):
    testcase = "Daata"
    expected = "Daata"
    self.assertEqual(rearrange_name(testcase), expected)

  #6
  def test_non_string(self):
    testcase = 12345
    expected = 12345
    self.assertEqual(rearrange_name(testcase), expected)

  #7
  def test_null_value(self):
    testcase = ''
    expected = ''
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()