# Chatbot Rasa
El objetivo de este trabajo es realizar un chatbot orientado al aprendizaje de conceptos de astronomía. El proyecto se divide en dos partes principales: la programación del chatbot con Rasa Open Source y el diseño de una interfaz web. Este repositorio corresponde a la parte de programación.

# Guía de instalación
### Instalación de Python
- Descargar las dependencias requeridas para la instalación de Python a partir del código fuente
~~~
	sudo apt update
~~~
~~~
	sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2- dev
~~~

- Utilizar el comando wget para descargar el archivo de la versión de Python deseada a través del enlace de descarga (en este caso Python 3.7.2):
~~~
	wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
~~~

- Extraer el archivo comprimido:
~~~
	tar -xf Python-3.7.2.tgz
~~~

- Navegar al directorio y asegurar que todas las dependencias están instaladas correctamente:
~~~
	cd Python-3.7.2
~~~
~~~
	./configure --enable-optimizations --enable-shared
~~~

- Instalar la versión de Python sin sobreescribir sobre otras:
~~~
	sudo make altinstall
~~~

- Por último, verificar si se ha instalado correctamente:
~~~
	python3.7 --version
~~~
	
### Instalación de Rasa
- Crear un directorio nuevo de trabajo:
~~~
	mkdir RasaProject
~~~
~~~
	cd RasaProject
~~~
	
- Crear un entorno virual especificando la versión de Python (en este caso el entorno virtual toma el nombre de rasa1):
~~~
	python3.7 -m venv rasa1
~~~

- Activar el entorno virtual:
~~~
	source rasa1/bin/activate
~~~
	
- Instalar Rasa Open Source (antes de ello actualizar la versión de pip):
~~~
	pip3 install -U pip
~~~
~~~
	pip3 install rasa
~~~
	
- Instalar las dependencias de SpaCy y su modelo en el idioma español:
~~~
	pip3 install rasa[spacy]
~~~
~~~
	python3 -m spacy download en_core_web_md
~~~

- Verificar la versión de rasa instalada:
~~~
	rasa --version
~~~

### Ejecución del proyecto
- Iniciar un proyecto de Rasa:
~~~
	rasa init
~~~
- Clonar este repositorio en el directorio local:
~~~
	git clone https://github.com/Aww919/chatbot_rasa.git
~~~

- Abrir dos terminales, una para ejecutar el modelo entrenado y otra para las actions:
~~~
	rasa run -m models --enable-api --cors "*" --debug
~~~
~~~
	rasa run actions
~~~
