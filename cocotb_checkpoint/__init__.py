import sys

__version__ = '0.1'

if sys.version_info[0] < 3:
    raise Exception("cocotb-checkpoint package requires Python 3")