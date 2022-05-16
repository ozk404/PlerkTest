# 🐍 Django - Backend - Entrevista (Plerk Challange)
(¡Hola! esta es mi prueba de para dev en Plerk! ¡Saludos! - (ozk404@gmail.com) - https://www.OscarMoralesGT.com

This Exercise is a Django REST API which provides data views from Plerk Transactions Database's

## 💻 Installation

I highly recommend the use of a virtual environment for the execution of this project, in this exercise we will use the 'virtualenv', to create a virtual environment, we will create a folder and we will use it to host our Django project.

```
git clone https://github.com/ozk404/PlerkTest
cd PlerkTest
virtualenv -p python3 .
cd Scripts
activate
cd..
```

After, use the package manager [pip](https://pip.pypa.io/en/stable/) to install the system requirements by the "requirements.txt" document.

```
pip install -r requirements.txt
```

## 💾 Creating de Database
When we have all the requirements installed, we will proceed to create the system database
```
python manage.py makemigrations
python manage.py migrate
```

## 🗄️ Import Companies and Transactiosn from database.csv in to Database:

```
Import Companies into Database:
  python manage.py loadcompany
  
Import Transactions into Database:
  python manage.py loadtransactions
```


## 🚀 Run the Django Server:

```
python manage.py runserver
```


## ⚙️ Usage:
For the convenience and ease of endpoint testing, the [Swagger ](https://swagger.io/)Swagger tool was used, is an open source and pro tools have helped millions of API developers, teams, and organizations deliver great APIs.

To access to Swagger Tool, type this URL on your browser:
```
localhost:8000
```

We have 5 endpoints 

| HTTP Type | Path | Used For |
| --- | --- | --- |
| `GET` | /company | List of all Customers in DB |
| `GET` | /company{id} | Customer for ID (Search) |
| `GET` | /summary | Summary with the most relevant data |
| `GET` | /top | Summary with the top of the companies with most transactions (top 10) |
| `GET` | /top{number} | Summary with the top of the companies with most transactions (top number) |

## 💯 Plus (Deployed in-real-time on Heroku) & Postman Collection:
Heroku Deployment:
https://plerk-challange.herokuapp.com/

Postman Collection:
https://documenter.getpostman.com/view/21004738/UyxjHmmD

## ✅ Tareas:
Esta parte la dejaré en español para que sea más fácil evaluar los puntos jaja :)

- [x] Servicio de resumen:: Este servicio no recibirá ningún parámetro, pero deberá regresar un resumen de lo que se encuentra en la base de datos previamente importada. Por ejemplo:
  - [x] La empresa con más ventas
  - [x] La empresa con menos ventas
  - [x] El precio total de las transacciones que SÍ se cobraron
  - [x] El precio total de las transacciones que NO se cobraron
  - [x] La empresa con más rechazos de ventas (es decir, no se cobraron)

- [x] Servicio de empresa: Este servicio deberá recibir el ID de la empresa y nos deberá regresar la siguiente información
  - [x] Nombre de la empresa
  - [x] Total de transacciones que SÍ se cobraron
  - [x] Total de transacciones que NO se cobraron
  - [x] El día que se registraron más transacciones

- [x] Propuesta personal: Este espacio es para proponer algún servicio con información que consideres importante para la operación o de conocimiento para la empresa.
  - [x] Se agregó un endpoint para ver todas las compañias/empresas existentes en el sistema
  - [x] Se agregó un sistema de "Top Empresas" el cual nos muestra las empresas con más recudación y total de transacciones, esto con el fin de poder premiar su preferencia
  - [x] Dicho endpoint de Top Empresas, retorna el top 10 cuando no se le envía ningun parametro, y retorna el top del valor del parametro cuando este es enviado. 

## ✅ Entregables:

- [x] Repositorio de GITHUB/GITLAB con el proyecto
- [x] Collection de POSTMAN (u otras alternativas)  para probar los endpoints
- [x] Pluss: Despliegue de la solución en alguna plataforma gratuita o servidor como:
    - [x] Heroku

¡Gracias por tu tiempo!
    
