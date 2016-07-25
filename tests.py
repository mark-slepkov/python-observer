__author__ = 'mark'
import unittest
from . import observer


@observer
class Example(object):
    pass


class ObserverTest(unittest.TestCase):

    def setUp(self):
        self.example = Example()
        self.marker = None

    def test_on(self):
        def handler():
            self.marker = True
            return
        example = Example()
        example.on('some_event', handler)
        self.assertEqual(self.marker, None)
        example.trigger('some_event')
        self.assertEqual(self.marker, True)

        self.marker = None
        example.trigger('some_event')
        self.assertEqual(self.marker, True)

    def test_once(self):
        def handler():
            self.marker = True
            return
        example = Example()
        example.once('some_event', handler)
        self.assertEqual(self.marker, None)
        example.trigger('some_event')
        self.assertEqual(self.marker, True)

        self.marker = None
        example.trigger('some_event')
        self.assertEqual(self.marker, None)

    def test_off(self):
        self.marker_1 = None
        self.marker_2 = None

        def handler_1():
            self.marker_1 = True

        def handler_2():
            self.marker_2 = True

        example = Example()
        example.on('some_event', handler_1)
        example.on('some_event', handler_2)
        self.assertEqual(self.marker_1, None)
        self.assertEqual(self.marker_2, None)
        example.trigger('some_event')
        self.assertEqual(self.marker_1, True)
        self.assertEqual(self.marker_2, True)

        self.marker_1 = None
        self.marker_2 = None
        example.off('some_event', handler_1)
        example.trigger('some_event')
        self.assertEqual(self.marker_1, None)
        self.assertEqual(self.marker_2, True)

    def test_difference(self):
        def handler():
            self.marker = True
            return
        example_1 = Example()
        example_2 = Example()
        example_1.on('some_event', handler)
        example_2.trigger('some_event')
        self.assertEqual(self.marker, None)
        example_1.trigger('some_event')
        self.assertEqual(self.marker, True)
