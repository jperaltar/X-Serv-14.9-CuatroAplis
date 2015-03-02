#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import sumador
import aleat
import sys

class adios(webapp.app):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body>Adios</body></html>\r\n")
        

class hola(webapp.app):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body>Hola</body></html>\r\n")

if __name__ == "__main__":
    try:
        hola = hola()
        adios = adios()
        sumador = sumador.Sumador()
        aleat = aleat.Aleat()
        testWebApp = webapp.webApp("localhost", 1234, {'/hola': hola,'/adios': adios,
                                                    '/suma': sumador, '/aleat': aleat})
    except KeyboardInterrupt:
        print "Closing service"
        sys.exit()