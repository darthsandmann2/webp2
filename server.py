#coding: utf-8

import os
import cherrypy

from app import application

#--------------------------------------
def main():
#--------------------------------------
# Get current directory
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        current_dir = os.path.dirname(os.path.abspath(sys.executable))
    # disable autoreload and timeout_monitor
    cherrypy.engine.autoreload.unsubscribe()
    cherrypy.engine.timeout_monitor.unsubscribe()
    # Static content config
    static_config = {
        '/': {
        'tools.staticdir.root': current_dir,
        'tools.staticdir.on': True,
        'tools.staticdir.dir': '',
        }
    }

    # Mount static content handler
    root_o = cherrypy.tree.mount(application.programm(), '/', static_config)
    # suppress traceback-info
    cherrypy.config.update({'request.show_tracebacks': True})
    cherrypy.config.update({'server.socket_port' : 8080})
    # Start server
    cherrypy.engine.start()
    cherrypy.engine.block()
#--------------------------------------
if __name__ == '__main__':
#--------------------------------------
    main()
# EOF