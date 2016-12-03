import argparse
import socket
import sys
from poller import Poller

class Main:
    def __init__(self):
        self.parse_options()

    def parse_options(self):
        ''' parse arguments, which include '-p' for port '''
        parser = argparse.ArgumentParser(prog='Echo Server', description='A simple echo server that handles one client at a time', add_help=True)
        parser.add_argument('-p', '--port', type=int, action='store', help='port the server will bind to',default=3000)
        self.args = parser.parse_args()

    def run(self):
        p = Poller(self.args.port)
        p.run()

if __name__ == "__main__":
    m = Main()
    try:
        m.run()
    except KeyboardInterrupt:
        pass