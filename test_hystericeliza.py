import unittest

from hystericeliza import HystericEliza, ElizaState, Normal, Angry, Sad

class TestFunctionality(unittest.TestCase):
    def setUp(self):
        self.eliza = HystericEliza()
        self.eliza.load('doctor.txt')

    def test_normal(self):
        self.eliza.state = Normal(self.eliza)
        output = self.eliza.process_output("Hello")
        self.assertEqual(output, "Hello")

    def test_angry(self):
        self.eliza.state = Angry(self.eliza)
        output = self.eliza.process_output("Hello")
        self.assertEqual(output, "HELLO")

    def test_sad(self):
        self.eliza.state = Sad(self.eliza)
        output = self.eliza.process_output("Hello")
        self.assertEqual(output, "hello")

    def test_normal_to_angry(self):
        self.eliza.state = Normal(self.eliza)
        string = "Don't upset me"
        output = self.eliza.process_output(string)
        self.assertEqual(output, string.upper())
        self.assertIsInstance(self.eliza.state, Angry)

    def test_normal_to_sad(self):
        self.eliza.state = Normal(self.eliza)
        string = "Please"
        output = self.eliza.process_output(string)
        self.assertEqual(output, string.lower())
        self.assertIsInstance(self.eliza.state, Sad)

    def test_angry_to_normal(self):
        self.eliza.state = Angry(self.eliza)
        string = "Please"
        output = self.eliza.process_output(string)
        self.assertEqual(output, string)
        self.assertIsInstance(self.eliza.state, Normal)

    def test_angry_to_sad(self):
        self.eliza.state = Angry(self.eliza)
        string = "Why"
        output = self.eliza.process_output(string)
        self.assertEqual(output, string.lower())
        self.assertIsInstance(self.eliza.state, Sad)

    def test_sad_to_normal(self):
        self.eliza.state = Sad(self.eliza)
        string = "Do you think"
        output = self.eliza.process_output(string)
        self.assertEqual(output, string)
        self.assertIsInstance(self.eliza.state, Normal)

if __name__ == "__main__":
    unittest.main()
