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
    - Visualizar datos clave a través de gráficos interactivos.
    - (Próximamente) Predecir precios futuros con modelos de aprendizaje automático.

    👉 Navega por las secciones usando el menú lateral.

    ---

    **Autor**: Ignacio Rivas  
    **Repositorio**: [GitHub - electricity-project](https://github.com/tu_usuario/tu_repositorio)
    """)

# Análisis 
elif seccion == "📊 Análisis":
    st.header("📊 Visualizaciones Históricas")
    st.markdown("A continuación se muestran algunos gráficos relevantes del análisis.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Evolución del precio medio")
    with col2:
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evoluciondemanda.png", caption="Demanda eléctrica por año")

    st.markdown("### 🔍 Preguntas planteadas en este análisis")

    with st.expander("¿Hay más demanda de electricidad en días fríos?"):
        st.markdown("""
    ✅ Sí, la demanda aumenta cuando hace frío, pero también cuando hace calor. 
    Ambos extremos térmicos elevan el consumo eléctrico, probablemente por el uso intensivo de sistemas de calefacción en invierno y aire acondicionado en verano.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Relación entre temperatura y demanda eléctrica")

    with st.expander("¿Disminuye la generación de energía por métodos convencionales cuando sube la generación solar?"):
        st.markdown("""
    📉 Desde 2020, la producción solar ha crecido notablemente, mostrando una correlación inversa con las fuentes convencionales.
    A medida que la generación solar aumenta (especialmente en primavera, verano y otoño), la producción convencional (como gas o carbón) tiende a reducirse.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Generación solar frente a métodos convencionales")

    with st.expander("¿Y cuándo sube la generación de energía hidráulica?"):
        st.markdown("""
    💧 La energía hidráulica también desplaza parcialmente a las fuentes convencionales.
    Aunque su patrón estacional es diferente al de la solar: su producción es más alta en invierno, seguida de primavera y otoño. 
    En esos períodos, se observa una menor necesidad de generación convencional.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Generación hidráulica frente a convencional")

    with st.expander("¿Depende el precio de las estaciones?"):
        st.markdown("""
    📆 No se ha identificado una correlación clara entre las estaciones del año y el precio de la electricidad.
    Aunque hay cierta variabilidad, los precios no parecen seguir un patrón estacional constante.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Evolución estacional del precio de la electricidad")

    with st.expander("¿El precio de la electricidad se ve afectado por la manera en que es generada?"):
        st.markdown("""
    ⚡ Sí, el tipo de generación influye directamente en el precio.
    Las tecnologías más caras son el carbón y el ciclo combinado, mientras que la hidráulica y la solar contribuyen a abaratar el coste de la electricidad cuando predominan en la mezcla energética.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Precio eléctrico según fuente predominante")

    with st.expander("¿Cómo están evolucionando el precio y la demanda?"):
        st.markdown("""
    📈 El precio de la electricidad ha mostrado una tendencia creciente en los últimos años, con un pico muy marcado en 2022 debido a la guerra de Ucrania y la crisis energética.
    Desde entonces, los precios han empezado a descender. Por su parte, la demanda presenta una tendencia a la baja: tras un ligero aumento entre 2015 y 2018, el consumo ha ido disminuyendo de forma sostenida.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Evolución histórica del precio y la demanda")

    with st.expander("¿Cómo están evolucionando la temperatura, la humedad y las precipitaciones?"):
        st.markdown("""
    🌡️💧 La temperatura media ha aumentado de forma continua, y la humedad también ha crecido aunque en menor proporción.
    En cambio, las precipitaciones han disminuido ligeramente. Estos cambios climáticos afectan tanto al consumo como a la producción eléctrica, especialmente a las fuentes renovables.
    """)
        st.image("C:/Users/ignac/Desktop/202502PT/Proyecto final/Imagenes/Evolucionprecio.png", caption="Evolución de temperatura, humedad y precipitaciones")

# Predicción (placeholder por ahora)
elif seccion == "📉 Predicción":
    st.header("🔮 Predicción del Precio Eléctrico")
    st.warning("Esta sección está en desarrollo. Pronto se incluirán modelos predictivos desde AzureML.")

# Recursos
elif seccion == "📎 Recursos":
    st.header("📎 Fuentes y Documentación")
    st.markdown("""
    - 📂 Datos originales: Subidos en la carpeta `/data`
    - 📒 Notebook con el análisis: Ver en [notebooks/analisis.ipynb](https://github.com/Ignacio538/Spanish-Electricity-Analysis/blob/main/Analysis.ipynb)
    - 📊 Gráficos originales: Exportados desde Power BI
    - 🔗 GitHub del proyecto: [electricity-project](https://github.com/Ignacio538/Spanish-Electricity-Analysis)
    """)