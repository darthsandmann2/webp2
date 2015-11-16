# coding:utf-8

import os.path
import cherrypy

from app import test
#----------------------------------------------------------
def main():
#----------------------------------------------------------
   
   # aktuelles Verzeichnis ermitteln, damit es in der Konfigurationsdatei als
   # Bezugspunkt verwendet werden kann   
   try:                                    # aktuelles Verzeichnis als absoluter Pfad
      currentDir_s = os.path.dirname(os.path.abspath(__file__))
   except:
      currentDir_s = os.path.dirname(os.path.abspath(sys.executable))
   cherrypy.Application.currentDir_s = currentDir_s

   configFileName_s = 'server.conf' # im aktuellen Verzeichnis   
   if os.path.exists(configFileName_s) == False:
      # Datei gibt es nicht
      configFileName_s = None
      #print("doof")
   #print("cool")
   # autoreload und timeout_Monitor hier abschalten
   # für cherrypy-Versionen >= "3.1.0" !
   #print(configFileName_s)
   cherrypy.engine.autoreload.unsubscribe()
   cherrypy.engine.timeout_monitor.unsubscribe()
   cherrypy.config.update(configFileName_s)

   cherrypy.tree.mount(
      None, '/', configFileName_s
   )
   
   cherrypy.tree.mount(
      test.test_cl(), '/test', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )    
  
   cherrypy.engine.start()
   cherrypy.engine.block() 

#----------------------------------------------------------
if __name__ == '__main__':
#----------------------------------------------------------
   main()