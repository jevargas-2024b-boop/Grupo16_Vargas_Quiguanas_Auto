# Generador de Propuestas Comerciales de Marketing

## Descripción del Proyecto

Aplicación Streamlit multi-agente que genera propuestas comerciales de marketing personalizadas
usando LangGraph + Claude (Anthropic). Cuatro agentes especializados trabajan en cadena y
entregan la propuesta en formato `.md` y `.pdf`.

## Stack Tecnológico

- **Frontend:** Streamlit
- **Orquestación de agentes:** LangGraph
- **LLM:** Claude (claude-haiku-4-5-20251001) via `langchain-anthropic`
- **PDF:** ReportLab
- **Entorno:** Python 3.10+, `python-dotenv`

## Arquitectura de Agentes

MarketingProposalState
        │
        ▼
  [analyst] ──► [strategist] ──► [writer] ──► [editor]

## Comandos Clave

  pip install -r requirements.txt
  streamlit run app.py

## Variables de Entorno

| Variable           | Descripción                                        |
|--------------------|----------------------------------------------------|
| ANTHROPIC_API_KEY  | API Key de Anthropic (obligatoria)                 |