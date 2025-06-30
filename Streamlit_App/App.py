import streamlit as st
from PIL import Image
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Mercado Eléctrico España", layout="wide")

# Sidebar para navegación
seccion = st.sidebar.radio("Navegación", [
    "🏠 Inicio",
    "📊 Análisis",
    "📉 Predicción",
    "📎 Recursos"
])

# Página de inicio
if seccion == "🏠 Inicio":
    st.title("📈 Análisis del Mercado Eléctrico en España")
    st.markdown("""
En este proyecto se he analizado el mercado eléctrico español con el objetivo de identificar patrones en el consumo y el precio de la electricidad a lo largo del tiempo.  
A partir de datos históricos desde el año 2014, se he explorado cómo diferentes factores, como la demanda energética, la generación por tipo de fuente (renovable y no renovable) o las condiciones meteorológicas, influyen en la evolución del precio de la electricidad.

El análisis no solo busca comprender las dinámicas pasadas del mercado, sino también construir modelos que permitan predecir el comportamiento futuro de los precios eléctricos.  
Este enfoque puede resultar útil tanto para consumidores como para empresas e instituciones interesadas en anticipar tendencias y tomar decisiones más informadas en un contexto energético cada vez más complejo.

    🔍 Objetivos:
    - Comprender tendencias históricas de precios, demanda y generación.
    - Visualizar datos clave a través de gráficos.
    - (Próximamente) Predecir precios futuros con modelos de aprendizaje automático.

    👉 Navega por las secciones usando el menú lateral.

    ---

    **Autor**: Ignacio Rivas  
    """)

# Análisis 
elif seccion == "📊 Análisis":
    st.header("📊 Visualizaciones Históricas")
    st.markdown("A continuación se muestran algunos gráficos relevantes del análisis.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Desgloseprecios.png", caption="Evolución del desglose del precio de la electricidad")
    with col2:
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Distribuciongeneracion.png", caption="Evolución de la distribución de generación eléctrica por tipo de fuente")

    st.markdown("### 🔍 Preguntas planteadas en este análisis")

    with st.expander("¿Hay más demanda de electricidad en días fríos?"):
        st.markdown("""
    ✅ Sí, la demanda aumenta cuando hace frío, pero también cuando hace calor. 
    Ambos extremos térmicos elevan el consumo eléctrico, probablemente por el uso intensivo de sistemas de calefacción en invierno y aire acondicionado en verano.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta1.png", caption="Relación entre temperatura y demanda eléctrica por estación")

    with st.expander("¿Disminuye la generación de energía por métodos convencionales cuando sube la generación solar?"):
        st.markdown("""
    📉 Desde 2020, la producción solar ha crecido notablemente, mostrando una correlación inversa con las fuentes convencionales.
    A medida que la generación solar aumenta (especialmente en primavera, verano y otoño), la producción convencional (como gas o carbón) tiende a reducirse.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta2.png", caption="Generación solar frente a métodos convencionales en base a la demanda")

    with st.expander("¿Y cuándo sube la generación de energía hidráulica?"):
        st.markdown("""
    💧 La energía hidráulica también desplaza parcialmente a las fuentes convencionales.
    Aunque su patrón estacional es diferente al de la solar: su producción es más alta en invierno, seguida de primavera y otoño. 
    En esos períodos, se observa una menor necesidad de generación convencional.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta3.png", caption="Generación hidráulica frente a convencional en base a la demanda")

    with st.expander("¿Depende el precio de las estaciones?"):
        st.markdown("""
    📆 No se ha identificado una correlación clara entre las estaciones del año y el precio de la electricidad.
    Aunque hay cierta variabilidad, los precios no parecen seguir un patrón estacional constante.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta4.png", caption="Evolución estacional del precio de la electricidad")

    with st.expander("¿El precio de la electricidad se ve afectado por la manera en que es generada?"):
        st.markdown("""
    ⚡ Sí, el tipo de generación influye directamente en el precio.
    Las tecnologías más caras son el carbón y el ciclo combinado, mientras que la hidráulica y la solar contribuyen a abaratar el coste de la electricidad cuando predominan en la mezcla energética.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta5.png", caption="Relación entre el precio de la electricidad y la generación por tipo de fuente")

    with st.expander("¿Cómo están evolucionando el precio y la demanda?"):
        st.markdown("""
    📈 El precio de la electricidad ha mostrado una tendencia creciente en los últimos años, con un pico muy marcado en 2022 debido a la guerra de Ucrania y la crisis energética.
    Desde entonces, los precios han empezado a descender. Por su parte, la demanda presenta una tendencia a la baja: tras un ligero aumento entre 2015 y 2018, el consumo ha ido disminuyendo de forma sostenida.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta6.png", caption="Evolución histórica del precio y la demanda")

    with st.expander("¿Cómo están evolucionando la temperatura, la humedad y las precipitaciones?"):
        st.markdown("""
    🌡️💧 La temperatura media ha aumentado de forma continua, y la humedad también ha crecido aunque en menor proporción.
    En cambio, las precipitaciones han disminuido ligeramente. Estos cambios climáticos afectan tanto al consumo como a la producción eléctrica, especialmente a las fuentes renovables.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Pregunta7.png", caption="Evolución de temperatura, humedad y precipitaciones")

elif seccion == "📉 Predicción":
    st.header("🔮 Predicción del Precio Eléctrico")

    st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/RealidadVSPrediccion.png", caption="Comparativa entre precios eléctricos reales y predichos")
    
    st.markdown("""
    La predicción de los precios eléctricos es un desafío complejo debido a la alta volatilidad de los factores que los afectan.
                  
    Entre ellos destacan variables climáticas como la cantidad de lluvia, que aumenta la generación hidráulica, o la radiación solar, que afecta la generación solar; ambos factores tienden a reducir el precio al hacer que disminuya la generación por fuentes convencionales, las cuales son más caras.  

    Además, eventos externos inesperados pueden impactar significativamente, como se observó en 2022, donde la guerra en Ucrania provocó una subida abrupta y sostenida de los precios que los modelos no pudieron anticipar con precisión, reflejándose en la gran diferencia entre valores predichos y reales.  

    Estos aspectos hacen que, a pesar del esfuerzo en modelado, la predicción precise un margen amplio de incertidumbre y continúe siendo un área abierta a mejoras y nuevas aproximaciones.
    """)

# Recursos
elif seccion == "📎 Recursos":
    st.header("📎 Fuentes y Documentación")
    st.markdown("""
    - 📂 Datos originales: Subidos en la carpeta `/data`
    - 📊 Gráficos originales: Generados en VSC y/o Power BI
    - 📒 Notebook con el análisis: Ver en [notebooks/analisis.ipynb](https://github.com/Ignacio538/Spanish-Electricity-Analysis/blob/main/Analysis.ipynb)
    - 🔗 GitHub del proyecto: [electricity-project](https://github.com/Ignacio538/Spanish-Electricity-Analysis)
    - 🌦️ Datos climatológicos: [SIAR](https://servicio.mapa.gob.es/websiar/SeleccionParametrosMap.aspx?dst=1)
    - ⚡ Precio de la electricidad, demanda y generación eléctrica: [REE](https://www.ree.es/es)
    - 🔮 Predicciones: Se han realizado en AzureML a través del método VotingEnsemble el cual combina los siguientes modelos:
        - RobustScaler, ElasticNet (14,28%)
        - RobustScaler, ElasticNet (42,88%)
        - ProphetModel (21,42%)
        - Arimax (21,42%)
    
                
    - ⚠️ Nota: Para los datos climatológicos se ha utilizado el servicio SIAR del Ministerio de Agricultura, Pesca y Alimentación de España, por tanto faltan los datos de aquellas comunidades que tienen la competencia en materia de agricultura y regadíos (estas son: Asturias, Cantabria, Cataluña y País Vasco).
    """)