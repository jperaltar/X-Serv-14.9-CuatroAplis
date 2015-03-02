#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random
import sys


class Aleat(webapp.app):
    def process(self, parsedRequest):
        rand_num = random.randint(0, 1000000000)

        return ("200 OK", "<html><body>Hola.<a href=" + "/aleat/" +
                str(rand_num) + "> Dame otra</a></body></html>\r\n")

if __name__ == "__main__":
    try:
        aleat = Aleat()
        testWebApp = webapp.webApp("localhost", 1234, {'/aleat': aleat})
    except KeyboardInterrupt:
        print "Closing service"
        sys.exit()
