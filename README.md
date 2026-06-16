# **Content Enrichment**
- - -
## **Herramienta_consulta_wikipedia**
Herramienta que enriquece de texto 
***
### 📝**Descripción del proyecto**
Esta herramienta permite al usuario introducir un tema, consultar Wikipedia mediante scraping, extraer el contenido principal, enriquecerlo con IA, traducirlo a cualquier idioma y exportarlo en formato *text* y *PDF*.

Es una aplicación CLI (Command Line Interface), ideal para automatizar procesos sin necesidad de interfaz gráfica.
***
### ✨ **Características principales**
- Scraping de Wikipedia

- Enriquecimiento del contenido con IA

- Traducción automática

- Exportación a TXT y PDF

- Validación de inputs

- Manejo de errores HTTP

- Testing con Pytest
***
### 🧩 **Arquitectura del sistema**

/herramienta_consulta_wikipedia/

│── output/
    │──.text
    │──.pdf
│── src/
    │──wikipedia_client.py  
    │── content_enricher.py
    │── translator_client.py
    │── file_manager.py
    │── /fonts
    │── validators.py
    │── /tests
│── main.py
│── requirements.txt
│── .env
│── README.md
***
### 🛠️ **Tecnologías utilizadas**
- 🐍 Python + PEP8
- 🍜 BeautifulSoup
- 🔗 Requests
- 🤖 Gemini (IA)
- 🌍 DeepL
- 📄 FPDF2
- 🧪 Pytest
***
### 📥 **Instalación**
1. Clonar el repositorio:

- *gitclone*
- ir el directorio con *cd*

---
2. Instalar dependencias:
pip install -r requirements.txt
---
3. ▶️ **Uso**
Ejecutar la aplicación:
python main.py




