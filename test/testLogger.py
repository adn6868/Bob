import unittest
import logger.logger.Logger as Logger
class TestLogger(unittest.TestCase):
    def setup(self):
        self.log = Logger()
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == "__main__":
    unittest.main()