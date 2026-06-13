# HU15 - Programación de Calibraciones y Limpiezas

## Summary
Visualizar de forma consolidada el estado del próximo mantenimiento planificado (cuándo se hicieron y cuándo toca la siguiente calibración o limpieza).

## Description
As a Técnico de Laboratorio, I want to programar la frecuencia de calibración o limpieza de cada equipo de medición, so that el sistema alerte visualmente cuando un mantenimiento preventivo esté próximo a vencer.

## Acceptance Criteria
1. El sistema debe permitir configurar la frecuencia de mantenimiento de cada equipo (ej. cada 30 días, 90 días, 180 días).
2. El sistema debe calcular automáticamente la "fecha del próximo mantenimiento" basándose en la fecha del último mantenimiento registrado y la frecuencia configurada.
3. Debe existir una pantalla de "Próximos Mantenimientos" que muestre un listado de equipos ordenado por urgencia cronológica de calibración o limpieza.
4. El sistema debe alertar visualmente (color rojo o icono de advertencia) cuando un mantenimiento esté vencido o próximo a vencer en los siguientes 7 días.
