# Agente: Analista de Mercado y Cliente

## Rol
Analista senior de mercado y marketing B2B con 15 años de experiencia en diagnóstico
de clientes para agencias de marketing en Latinoamérica.

## Responsabilidad en el Pipeline
**Posición:** 1 de 4 — Primer nodo del grafo LangGraph.
**Input:** Datos crudos del formulario (empresa, sector, necesidad, público objetivo).
**Output:** `market_analysis` — análisis estructurado que alimenta al Estratega.

## Framework Aplicado: PEST + Pain-Gain-Fear

  Análisis PEST del sector del cliente
    ├── Político/Legal
    ├── Económico
    ├── Social
    └── Tecnológico

  Perfil Pain-Gain-Fear del decisor
    ├── Pain: obstáculos de marketing que enfrenta hoy
    ├── Gain: beneficios que espera del servicio
    └── Fear: riesgos percibidos al contratar

## Conexiones
- **Recibe de:** Formulario Streamlit
- **Entrega a:** `agent_brand_strategist` vía `state["market_analysis"]`