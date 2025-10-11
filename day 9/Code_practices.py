# Práctica Módulo Collections 1

from collections import Counter
 
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
 
contador = Counter(lista)
# Práctica Módulo Collections 2

from collections import defaultdict
 
mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44
# Práctica Módulo Collections 3

from collections import deque
 
lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# Práctica Módulo Datetime 1

from datetime import date
 
mi_fecha = date(1999, 2, 3)
# Práctica Módulo Datetime 2

from datetime import date
 
hoy = date.today()
# Práctica Módulo Datetime 3

from datetime import datetime
 
minutos = datetime.now().minute