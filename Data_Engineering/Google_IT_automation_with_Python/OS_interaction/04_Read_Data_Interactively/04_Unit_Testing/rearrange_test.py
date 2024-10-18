import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

  def test_middle_name(self):
    testcase = "Carter, Jim T."
    expected = "Jim T. Carter"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_multiple_names(self):
    testcase = "Dam, Jean Claude Van"
    expected = "Jean Claude Van Dam"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_one_name(self):
    testcase = "Daata"
    expected = "Daata"
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()