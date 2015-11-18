# coding: utf-8
import cherrypy
import json
import codecs
#--------------------------------------

class Application_cl(object):


#---------------------------------------------------
   def __init__(self):
#---------------------------------------------------
# constructor
        pass
#---------------------------------------------------


#---------------------------------------------------
   def module(self):
#---------------------------------------------------
      anfang_s = """
      <!DOCTYPE html>
      <html>
         <head>
            <script src="main.js">
            </script>
            <title>
               Titel
         </title>
         <meta charset= "UTF-8"/>
         </head>
         <body>"""
      
      ende_s = """
      </body>
      </html>"""
      
      # Inhalt der Datei "module.json" im Verzeichnis "data"
      # einlesen und als Python-Datenstruktur ablegen
      # verwenden Sie dazu das Modul "json"
      json_modul = codecs.open("./data/module.json", "r", "UTF-8")
      modul_inhalt = json.load(json_modul)
      json_modul.close()

      ##markup_s = modul_inhalt
      
      
      # anschließend einfaches Markup aufbauen:
      # einleitenden Teil des Markups zuweisen
      # Schleife über alle Einträge in der Python-Datenstruktur:
      #    Daten extrahieren und weiteres Markup damit erzeugen und anhängen
      # abschließenden Teil des Markups anhängen
      # erzeugtes Markup als Ergebnis zurückliefern
      markup_s = anfang_s
      #markup_s += "<ul>"
      for key_s in sorted(modul_inhalt): 
         markup_s += "<ul> <h3 onclick=\"change_view('" + str(key_s) + "')\"" + ">" + str(key_s) + '</h3>' + '<div style="display:block;" id="' + str(key_s) + '">' 
         for key2_s in sorted(modul_inhalt[key_s]):
            markup_s += '<li>' + str(modul_inhalt[key_s][key2_s])
         markup_s += '</ul> </div>'        
      #markup_s += "</ul>"
      
      markup_s += ende_s

      return markup_s 

   module.exposed = True
#---------------------------------------------------


#---------------------------------------------------
   def default(self, *arglist, **kwargs):
#---------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
         str (arglist) + \
         '' +\
         str (kwargs)
      raise cherrypy.HTTPError(404, msg_s)

   default.exposed = True
#---------------------------------------------------
# EOF