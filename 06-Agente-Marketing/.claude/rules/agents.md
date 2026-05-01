# Reglas de Desarrollo de Agentes

## Principios Generales
1. Cada agente tiene un rol claro y único
2. El human message siempre incluye el contexto completo necesario
3. Los agentes solo leen de `state` y solo escriben su clave de output

## Tokens y Modelos

| Agente     | max_tokens | Justificación                      |
|------------|------------|------------------------------------|
| analyst    | 1500       | Análisis estructurado, conciso     |
| strategist | 1500       | Estrategia y mensajes clave        |
| writer     | 3500       | Propuesta completa (11 secciones)  |
| editor     | 4096       | Propuesta completa + mejoras       |

## Añadir un Nuevo Agente
1. Crear la función `agent_<nombre>(state: MarketingProposalState) -> dict`
2. Agregar la clave de output al TypedDict
3. Registrar el nodo en `build_graph()`
4. Agregar el edge correspondiente
5. Documentar en `.claude/agents/<nombre>.md`