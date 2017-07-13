import unittest

from mockito import mock, verify

from helloworld import HelloWorld


class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        hello_world = HelloWorld()
        hello_world.helloworld(out)

        verify(out).write("Hello world of Python\n")
