import web

class Visitas:
    def GET(self, nombre):
        try:
          cookie = web.cookies()
          visitas = "0" #Variable local
          print(cookie)

          #Condición para el nombre del usuario
          if nombre: 
            web.setcookie("nombre", nombre,expires="",domain=None)

          else:
            nombre = "Predeterminado" #Si no recibe nada en el parametro de nombre, será NA
            web.setcookie("nombre", nombre,expires="",domain=None)

          #Condición para el número de visitas
          if cookie.get("visitas"):
            visitas = int(cookie.get("visitas")) #Si ya existiera la variable, vamos a obtener el valor
            visitas += 1 #Se incrementaran en uno las visitas
            web.setcookie("visitas", str(visitas), expires="", domain=None)

          else:
            web.setcookie("visitas", str(1), expires="", domain=None) #Si no hubiera visitas, genera la primera
            visitas = "1" #Si no hay variable visitas, visitas va a ser igual a 1

          return "Visitas: " + str(visitas) + " Nombre: " + nombre #Concatenar el número de visitas con el nombre

        except Exception as e:
              return "¡Ah ocurrido un error!" + str(e.args)