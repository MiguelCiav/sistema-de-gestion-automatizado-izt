# HU08 - Alertas de Vencimiento de Reactivos

## Summary
Mostrar avisos de caducidad para los reactivos que cuenten con fecha de vencimiento y estén próximos a expirar.

## Description
As a Técnico de Laboratorio, I want to visualizar alertas diferenciadas para reactivos próximos a vencer y vencidos, so that evitemos el uso de reactivos degradados y gestionemos los desechos químicos de forma segura.

## Acceptance Criteria
1. El sistema debe comparar diariamente la fecha de vencimiento de cada `StockReactivo` con la fecha actual del sistema.
2. Se deben generar alertas visuales diferenciadas para reactivos "Próximos a Vencer" (rango configurable, ej. en los próximos 30 días) y "Vencidos".
3. Los reactivos vencidos deben deshabilitarse automáticamente para el consumo regular, requiriendo una confirmación administrativa para ser descargados o descartados.
4. La vista de inventario debe permitir ordenar o filtrar los reactivos según su fecha de vencimiento o su estado de alerta de caducidad.
