#! /usr/bin/env python
"""module docstring"""

# imports
import mylog
import logging

# constants
# exception classes
class DaemonError(Exception): pass


# interface functions
log = logging.getLogger('vDeploy.%s' % __name__)

# classes
class Server():
    def __init__(self,args):
        log.info("Starting daemon service")


# internal functions & classes
def main():
    #    import doctest
    #    doctest.testmod()
    pass


if __name__ == '__main__':
    status = main()
    sys.exit(status)

