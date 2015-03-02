#!/usr/bin/python
#! -*- coding: utf-8 -*-

import webapp
import sys

class Sumador(webapp.app):
    first = None

    def parse(self, request, rest):
        splitted_req = request.split(' ')
        rest = str(splitted_req[1][1:])
        parsedRequest = rest.split('/')
        return parsedRequest[1]

    def process(self, parsedRequest):
        if not parsedRequest:
            return ("404 Bad Request", "<h1>Go Away!</h1>")

        if self.first is None:
            try:
                self.first = int(parsedRequest)
                reply = ("El primero es " + str(self.first) +
                    ". Dame otro")
            except ValueError:
                return None
        else:
            result = self.first + int(parsedRequest)
            reply = "El resultado es " + str(result)
            self.first = None

        return ("200 OK", "<html><body>" + reply +
                "</body></html>\r\n")


if __name__ == "__main__":
    try:
        sumador = Sumador()
        webapp.webApp('localhost', 1234, {'/suma': sumador})
    except KeyboardInterrupt:
        print "Closing service"
        sys.exit()
