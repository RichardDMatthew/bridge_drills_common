import logging
import unittest
from test_b1_c2 import TestBook1Chapter2
from test_b1_c3 import TestBook1Chapter3
from test_b1_c4 import TestBook1Chapter4
from test_b1_c5 import TestBook1Chapter5

if __name__ == '__main__':
    # set up logging
    open('bridge.log', 'w')     # overwrites last log file
    BRIDGE_LOG_FILE = 'bridge.log'
    bridge_log = logging.getLogger('bridge.log')
    bridge_log.setLevel(logging.DEBUG)
    bridge_log_file_handler = logging.FileHandler(BRIDGE_LOG_FILE)
    FORMAT = "[%(filename)s:%(lineno)s] %(funcName)5s() %(message)s"
    bridge_log_file_handler.setFormatter(logging.Formatter(FORMAT))
    bridge_log.addHandler(bridge_log_file_handler)
    bridge_log.info("Starting test")
    unittest.main()
    test_b1_c2 = TestBook1Chapter2()
    test_b1_c3 = TestBook1Chapter3()
    test_b1_c4 = TestBook1Chapter4()
    test_b1_c5 = TestBook1Chapter5()

