from mockito import mock, verify
import unittest

from hello import hello

class HelloTest(unittest.TestCase):
    def test_should_issue_hello_message(self):
        out = mock()

        hello(out)

        verify(out).write("Hello world of Python\n")
