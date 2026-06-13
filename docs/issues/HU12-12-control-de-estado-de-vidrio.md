# HU12 - Control de Estado de Vidrio

## Summary
Registrar las condiciones cualitativas (bueno, agrietado, inutilizable) del material de vidrio disponible.

## Description
As a Técnico de Laboratorio, I want to registrar y actualizar el estado físico o cualitativo del material de vidrio, so that identifiquemos material dañado o agrietado que pueda representar un riesgo de seguridad.

## Acceptance Criteria
1. Cada registro de material de vidrio en el inventario debe incluir un campo de estado cualitativo (ej. "Excelente", "Agrietado", "Para Descarte").
2. Si un material de vidrio es marcado con el estado "Para Descarte", su cantidad disponible para experimentos debe reducirse a cero automáticamente.
3. Debe registrarse en un historial de incidencias de vidrio cuando un material sufra daños (quién reporta, qué material, tipo de daño y fecha).
4. El sistema debe permitir filtrar rápidamente el material que esté agrietado o requiera reemplazo urgente.
