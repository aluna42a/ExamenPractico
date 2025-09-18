Delta Data Consulting – Gestión de Créditos

Esta aplicación permite administrar créditos otorgados a clientes, incluyendo:

-Agregar, editar y eliminar créditos.
-Visualizar créditos en una tabla con detalles (cliente, monto, tasa de interés, plazo y fecha).
-Visualizar gráficas de barras y pastel que muestran los créditos por cliente y distribución de montos.
-Control de clientes con créditos activos (aviso modal).
-El proyecto utiliza Flask como framework web y SQLite como base de datos.

Requisitos
-Python 3.10 o superior
-Git (opcional, para clonar el repositorio)
-Navegador web moderno

Dependencias (incluidas en requirements.txt):
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
WTForms==3.2.1
Jinja2==3.1.6
Werkzeug==3.1.3
numpy==1.24.2
matplotlib==3.6.3
pandas==1.5.3

--INSTALACION--
1.- Clonar el repositorio:
git clone https://github.com/aluna42a/ExamenPractico.git
cd REPOSITORIO PROPIO

2.-Crear un entorno virtual(es opcional pero recomendado):
python -m venv venv 

3.-Activar el entorno virtual:
Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

4.-Instalar dependencias:

pip install -r requirements.txt

5.-Ejecución
Asegurarse de estar en la carpeta raíz del proyecto y con el entorno virtual activado.
Ejecutar la aplicación:

python app.py

6.-Abrir el navegador y acceder a:

http://127.0.0.1:5000/

Desde la interfaz web se puede:
-Agregar un nuevo crédito.
-Editar o eliminar créditos existentes.
-Visualizar gráficas y distribución de créditos.
-Recibir aviso si un cliente ya tiene un crédito activo. 


Estructura del proyecto
tu-repo/
│
├── app.py                 # Archivo principal de Flask
├── requirements.txt       # Dependencias de Python
├── README.md              # Este archivo
├── credits.db             # Base de datos SQLite
├── templates/             # Plantillas HTML
│   ├── index.html
│   └── form.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── chart.js
    └── img/
        └── fondofinanzas.jpg

Notas importantes

-Cada crédito agregado es independiente; un mismo cliente puede tener múltiples créditos con fechas y tasas distintas.
-El aviso de cliente con crédito activo solo se muestra con un modal y se cierra al presionar Aceptar.
-La base de datos SQLite (credits.db) se crea automáticamente si no existe.
