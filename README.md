# ⚡ Análisis del Mercado Eléctrico Español

![Banner](images/Pregunta6.png)

**Autor**: Ignacio Rivas  
**Centro**: Upgrade Hub  
**Repositorio del proyecto**: https://github.com/Ignacio538/Spanish-Electricity-Analysis

---

## 🎯 Objetivo

Analizar la evolución del precio de la electricidad en España entre 2014 y 2024 y explorar cómo factores como la temperatura, la generación renovable y la demanda afectan al precio.  

También se busca prever precios futuros utilizando modelos de predicción (en desarrollo).

---

## 🧰 Herramientas utilizadas

- Python (Pandas, Seaborn, Matplotlib)
- Power BI (visualizaciones)
- Streamlit (app web)
- Azure ML (predicción futura, en desarrollo)
- GitHub

---

## 🗂️ Estructura del repositorio

📦 Spanish-Electricity-Analysis
├── data/ → Datasets originales y limpios
├── images/ → Imágenes exportadas de Power BI y VSC
├── notebooks/ → Notebook con el análisis exploratorio
├── streamlit_app/ → Aplicación web con Streamlit (app.py)
├── README.md → Este archivo
├── requirements.txt → Librerías necesarias para ejecutar la app

---

## 📊 ¿Qué incluye el análisis?

Se responden preguntas como:

- ¿Hay más demanda en días fríos?
- ¿La generacíón solar desplaza a las fuentes convencionales?
- ¿Cómo evolucionan temperatura, humedad y precio?
- ¿Qué tecnologías encarecen o abaratan el precio?

Puedes explorarlas en la app interactiva con gráficos y respuestas explicadas.

---

## 🔗 Accede al proyecto

- 📎 App (local): ejecuta `streamlit run Streamlit_App/app.py`
- 📂 Datos: carpeta `/data`
- 📒 Análisis completo: [notebooks/analisis.ipynb](notebooks/analisis.ipynb)
- 🔗 Proyecto completo: [GitHub](https://github.com/Ignacio538/Spanish-Electricity-Analysis)

---

## 🌍 Fuentes de datos

- Clima: [SIAR - Ministerio Agricultura](https://servicio.mapa.gob.es/websiar/SeleccionParametrosMap.aspx?dst=1)
- Electricidad: [REE - Red Eléctrica Española](https://www.ree.es/es)

---

### ▶️ Cómo ejecutar esta app

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Ignacio538/Spanish-Electricity-Analysis.git
     ```

2. Entra en la carpeta del proyecto:

    ```bash
    cd Spanish-Electricity-Analysis
    ```
3. Ejecuta la app con Streamlit:

    ```bash
    streamlit run streamlit_app/app.py
    ```