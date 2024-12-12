# Ejercicio2rms
Solución al segundo ejercicio del examen de entornos de desarrollo
He instalado GithubCopilot y Emmet, que son las extensiones que me pide el ejercicio para poder desarrollar mas rapido
![image](https://github.com/user-attachments/assets/cdf5c472-f330-46d7-aacd-6fe7a0b2a2d9)
Ahora, Lo primero es instalar la extension de RapidAPI Client para poder trabajar con ellas directamente en VS Code
https://rapidapi.com/Alejandro99aru/api/exercise-db-fitness-workout-gym
Voy a utilizar esta API, a la que le puedo preguntar cosas relacionadas con fitness y gimnasio
He tenido que registrarme en rapidapi para obtener una clave API con la que llamar a la API que yo quiera
Usaré una llamada mediante GET, que me dará ejercicios para el musculo que yo le diga, en este caso pecho(chest)
![image](https://github.com/user-attachments/assets/2df5b153-82cd-442c-8c29-86535f85a1b9)
He hecho un fichero en python para hacer una llamada a la API
![image](https://github.com/user-attachments/assets/9f07a258-c6f8-41a7-8f09-75dcef948e88)
Me he suscrito a la API gratuitamente para poder hacerle llamadas
Ahora para poder realizar la llamada a la API con mi fichero de python, he realizado el siguiente comando pip install request --upgrade pip para actualizar pip a su ultima version
He conseguido llamar a la api ejecutando en la consola el comando "python peticion.py" y me ha dado una respuesta muy largas de ejercicios de pecho
![image](https://github.com/user-attachments/assets/4d811839-614b-48e1-abfc-f3e220b47473)
No he tenido la necesidad de usar la extension de Copilot ya que el codigo que he cogido ha sido de la pagina de la propia API
