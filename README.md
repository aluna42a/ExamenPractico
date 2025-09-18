# Delta Data Consulting – Gestión de Créditos

Esta aplicación permite administrar créditos otorgados a clientes, incluyendo:  
-Agregar, editar y eliminar créditos.  
-Visualizar créditos en una tabla con detalles (cliente, monto, tasa de interés, plazo y fecha).  
-Visualizar gráficas de barras y pastel que muestran los créditos por cliente y distribución de montos.  
-Control de clientes con créditos activos (aviso modal).  
-El proyecto utiliza Flask como framework web y SQLite como base de datos.

### Requisitos
-Python 3.10 o superior  
-Git (opcional, para clonar el repositorio)  
-Navegador web moderno

Dependencias (incluidas en requirements.txt):  
Flask==3.1.2  
Flask-SQLAlchemy==3.1.1  
WTForms==3.2.1 

### ----CONSIDERACIONES---: 

Tener en cuenta el sistema operativo y los comandos requeridos para la activacion del entorno virtual.  
La opcion de usar git, es para mayor facilidad. Si se descarga la carpeta, basta con colocarse en ella e ir al paso 2.

### --INSTALACION--

1.- En la terminal de comandos del sistema o de una IDE como visual studio code se debera clonar el repositorio:

    git clone https://github.com/aluna42a/ExamenPractico.git

Se descargara el repositorio.   
Abrir la carpeta donde se encuentra el repositorio:

    cd ExamenPractico

2.-Crear un entorno virtual (es opcional pero recomendado):  

    python -m venv venv 

3.-Activar el entorno virtual:
Windows:

cmd:

    venv\Scripts\activate

powershell:

    .\venv\Scripts\Activate.ps1

Linux/Mac:

    source venv/bin/activate

4.-Instalar dependencias:

    pip install -r requirements.txt

5.-Ejecución

Asegurarse de estar en la carpeta raíz del proyecto y con el entorno virtual activado (se utiliza venv).
Deberia mostrar algo como:

    C:\Users\USUARIO\Documents\ExamenPractico>

Ejecutar la aplicación:

    python app.py

6.-Abrir el navegador y acceder a:

http://127.0.0.1:5000/

Desde la interfaz web se puede:

-Agregar un nuevo crédito(la primera letra de los nombres y apellidos se mostrara en mayuscula en la tabla aun si fue escrita con minuscula).  
-Editar o eliminar créditos existentes.  
-Visualizar gráficas y distribución de créditos.  
-Recibir aviso si un cliente ya tiene un crédito activo y sumar ese monto dentro de la grafica con el cliente ya registrado. 


Estructura del proyecto:

    tu-repo/

    │
    ── app.py                 # Archivo principal de Flask

    ├── requirements.txt       # Dependencias de Python

    ├── README.md              # Este archivo

    ├── templates/             # Plantillas HTML

        ├── index.html

        ├── form.html
    └── static/

        ├── css/
    
        │   └── style.css
    
        ├── js/
    
        │   └── chart.js
    
        └── img/
    
            └── fondofinanzas.jpg

                           SE INCLUYE IGUAL CARPETA _pycache_ , instance , venv

Notas importantes

-Cada crédito agregado es independiente; un mismo cliente puede tener múltiples créditos con fechas y tasas distintas pero en la grafica se refleja el monto total del cliente.  
-El aviso de cliente con crédito se cierra al presionar Aceptar.  
-La base de datos SQLite (credits.db) se crea automáticamente si no existe.
