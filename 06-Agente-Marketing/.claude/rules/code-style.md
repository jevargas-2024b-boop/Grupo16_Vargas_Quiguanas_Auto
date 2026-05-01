# Convenciones de Código

## Python
- Formateo: PEP 8, líneas máx. 100 caracteres
- Nombres de funciones de agente: `agent_<rol>` en snake_case
- Nombres de nodos LangGraph: snake_case corto (analyst, writer)
- Nunca hardcodear la API key en el código

## Streamlit
- Configuración de página en `st.set_page_config()` al inicio
- CSS custom vía `st.markdown(..., unsafe_allow_html=True)`
- Estado de sesión con `st.session_state["proposal"]`

## Gestión de Errores
- Capturar errores de autenticación, rate limit y genéricos por separado
- Mostrar mensajes de error en español

## Archivos del Proyecto
| Archivo          | Propósito                        |
|------------------|----------------------------------|
| `app.py`         | App principal Streamlit          |
| `requirements.txt` | Dependencias Python            |
| `.env`           | Variables de entorno locales     |