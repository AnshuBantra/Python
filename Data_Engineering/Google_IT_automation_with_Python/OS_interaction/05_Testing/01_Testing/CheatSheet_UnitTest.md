# Study guide: Unit tests

You’ve learned that unit tests are designed to test small pieces of code, like a single function or method, to ensure that each part of the code is working as it should. Unit testing helps to isolate errors so bugs can be identified and fixed earlier on during the software development process before they can become larger, more expensive issues to fix.

You’ve also learned about the object-oriented concepts of unittest, a unit testing framework in Python that developers can use to help test their code. In this reading, you’ll learn more about test cases, running unit tests using the command-line interface, unit test design patterns, and some common, basic assertions that you can use when developing your own unit tests.

## Test cases

The building blocks of unit tests within the unittest module are test cases, which enable developers to run multiple tests at once. To write test cases, developers need to write subclasses of TestCase or use FunctionTestCase.

To perform a specific test, the TestCase subclass needs to implement a test method that starts with the name test. This identifier is what informs the test runner about which methods represent tests.

Examine the following example for test cases:

```python
import unittest


class TestStringMethods(unittest.TestCase):


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): 
            s.split(2)


if __name__ == '__main__':
    unittest.main()
```

Notice how the following example contains three individual tests: test_upper(), test_isupper(), and test_split(), which are responsible for testing different string methods. This example code also includes four assertions (covered below) and a call to the command-line interface, which you’ll learn more about later in this reading.

## Assertions

The TestCase class also employs its own assert methods that work similarly to the assert statement: if a test fails, an exception is raised with an explanatory message, and unittest identifies the test case as a failure. In the above example, there are several assertions used:

An assertEqual() to check for an expected result

An assertTrue() and an assertFalse() to verify a condition

An assertRaises() to verify that a specific exception gets raised

Each of these assert methods is used in place of the standard assert statement so the test runner can gather all the test results and generate a report.

Below is a list of commonly used assert methods in the TestCase class. For more information on each method, select the embedded link in the list provided.

The assertEqual(a, b) 		method checks that a == b

The assertNotEqual(a, b) 	method checks that a != b

The assertTrue(x) 			method checks that bool(x) is True

The assertFalse(x)			method checks that bool(x) is False

The assertIs(a, b)			method checks that a is b

The assertIsNot(a, b)		method checks that a is not b

The assertIsNone(x)		method checks that x is None

The assertIsNotNone(x)		method checks that x is not None

The assertIn(a, b)			method checks that a in b

The assertNotIn(a, b)		method checks that a not in b

The assertIsInstance(a, b)	method checks that isinstance(a, b)

The assertNotIsInstance(a, b)	method checks that not isinstance(a,

You can also use assert methods to generate exceptions, warnings, and log messages. For example, another important assert method in unit testing is assertRaises. It allows you to test whether exceptions are raised when they should be, ensuring that your program can handle errors. assertRaises also allows developers to check which specific exception type is raised, ensuring that the correct error handling is in place.

Command-line interface
The command-line interface allows you to interact with an application or program through your operating system command line, terminal, or console by beginning your code with a text command. When you want to run tests in Python, you can use the unittest module from the command line to run tests from modules, classes, or even individual test methods. This also allows you to run multiple files at one time.

To call an entire module:

python -m unittest test_module1 test_module2

To call a test class:

python -m unittest test_module.TestClass

To call a test method:

python -m unittest test_module.TestClass.test_method

Test modules can also be called using a file path, as written below:

python -m unittest tests/test_something.py

[source:
https://docs.python.org/3/library/unittest.html
]

In each instance, the structure of the command remained the same, with the test class and test method being added to the original module that was called.

You can also use the command line for test discovery, for running all of the tests in a single project, or even for just a subset of tests.

Unit test design patterns
One pattern that you can use for unit tests is made up of three phases: arrange, act, and assert. Arrange represents the preparation of the environment for testing; act represents the action, or the objective of the test, performed; and assert represents whether the results checked are expected or not.

Imagine building a system for a library. The objective is to test whether a new book can be added to the library's collection and then to check if the book is in the collection. Using the above structure of arrange, act, and assert, consider the following example code:

What’s given (arrange): A library with a collection of books

When to test (act): A new book is added to the collection

Then check (assert): The new book should be present in the library's collection

```python
class Library:
	def __init__(self):
		self.collection = []

	def add_book(self, book_title):
		self.collection.append(book_title)

	def has_book(self, book_title):
		return book_title in self.collection

# Unit test for the Library system
class TestLibrary(unittest.TestCase):

	def test_adding_book_to_library(self):
    	# Arrange
		library = Library()
		new_book = "Python Design Patterns"

    	# Act
    	library.add_book(new_book)

    	# Assert
    	self.assertTrue(library.has_book(new_book))

# Running the test
library_test_output = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
print(library_test_output)
```

 Tests can be grouped together according to the features they test. In unittest, this functionality is known as a test suite, and it allows developers to organize how and in which order their tests are run.

In each respective phase, an instance of the library class was created. The title of the book was defined as “Python Design Patterns,” a new book was added to the library using the add_book method, and a check was run to see if the new book was successfully added to the library’s collection using the has_book method.

Test suites
Testing can be time-intensive, but there are ways that you can optimize the testing process. The following methods and modules allow you to define instructions that execute before and after each test method:

setUp() can be called automatically with every test that’s run to set up code.

tearDown() helps clean up after the test has been run.

If setUp()raises an exception during the test, the unittest framework considers this to be an error and the test method is not executed. If setUp() is successful, tearDown() runs even if the test method fails. You can add these methods to your unit tests, which you can then include in a test suite. Test suites are collections of tests that should be executed together—so all of the topics covered in this reading can be included within a test suite.

Consider the following code example to see how each of these unit testing components is used together and run within a test suite:

```python
import unittest
import os
import shutil

# Function to test
def simple_addition(a, b):
	return a + b

# Paths for file operations
ORIGINAL_FILE_PATH = "/tmp/original_test_file.txt"
COPIED_FILE_PATH = "/mnt/data/copied_test_file.txt"

# Global counter
COUNTER = 0

# This method will be run once before any tests or test classes
def setUpModule():
	global COUNTER
	COUNTER = 0
  
	# Create a file in /tmp
	with open(ORIGINAL_FILE_PATH, 'w') as file:
    	file.write("Test Results:\n")

# This method will be run once after all tests and test classes
def tearDownModule():
	# Copy the file to another directory
	shutil.copy2(ORIGINAL_FILE_PATH, COPIED_FILE_PATH)
  
	# Remove the original file
	os.remove(ORIGINAL_FILE_PATH)

class TestSimpleAddition(unittest.TestCase):

	# This method will be run before each individual test
	def setUp(self):
    	global COUNTER
    	COUNTER += 1

	# This method will be run after each individual test
	def tearDown(self):
    	# Append the test result to the file
    	with open(ORIGINAL_FILE_PATH, 'a') as file:
        	result = "PASSED" if self._outcome.success else "FAILED"
        	file.write(f"Test {COUNTER}: {result}\n")

	def test_add_positive_numbers(self):
    	self.assertEqual(simple_addition(3, 4), 7)

	def test_add_negative_numbers(self):
    	self.assertEqual(simple_addition(-3, -4), -7)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleAddition)
runner = unittest.TextTestRunner()
runner.run(suite)

# Read the copied file to show the results
with open(COPIED_FILE_PATH, 'r') as result_file:
	test_results = result_file.read()

print(test_results)
```

Key takeaways
The real strength of unit testing is when you combine it with exceptions. Because exceptions are objects, the object-oriented nature of the unittest framework makes them synergize well together. Assertions help to document expected behavior, create more specific test codes, and help to safeguard against future changes. Unit testing is also a way to optimize a process within the software development lifecycle—through automated testing. Remember, writing code is important, but writing strong tests is even more so!

For more information on unittest and unit testing, visit
https://docs.python.org/3/library/unittest.html
