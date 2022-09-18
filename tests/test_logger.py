import sys, os, unittest, re
sys.path.append(os.path.realpath('.'))
from logger import *

class Test_Logger(unittest.TestCase):

    def test_log__with_stdout_no_exceptions(self):

        try:
            s = StdOutTarget()
            l = Logger([s])
            l.log_error('test logger stdout')

        except:
            self.fail()

        
    def test_log__with_logfile_no_exceptions(self):

        file_path = os.path.join(os.path.dirname(__file__), 'log')

        if os.path.exists(file_path):
            os.remove(file_path)

        f = LogFileTarget(filepath=os.path.dirname(__file__))
        l = Logger([f])
        l.log_info('test logger', 1)

        self.assertEquals(os.path.exists(file_path), True)

        with open(file_path, 'r') as file:
            first_line_str = file.readlines(1)[0][21:]

        self.assertEquals(first_line_str, '- test logger')

        os.remove(file_path)

    def test_init__with_wrong_type(self):

        class WrongClass:
            pass

        try:
            s = WrongClass()
            l = Logger([s])
            self.fail()

        except WrongTypeError:
            pass


if __name__ == '__main__':
    unittest.main()