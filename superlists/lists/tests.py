from django.test import TestCase

class SmokeTest(TestCase):
    # write test to fail as expected
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)
