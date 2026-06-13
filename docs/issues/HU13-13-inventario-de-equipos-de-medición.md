# HU13 - Inventario de Equipos de Medición

## Summary
Registrar los equipos de medición por laboratorio, indicando marca, modelo y si requiere calibración, limpieza o ambas.

## Description
As a Técnico de Laboratorio, I want to registrar y gestionar el inventario de equipos de medición (balanzas, pH-metros, espectrofotómetros), so that identifiquemos y llevemos el control de los activos físicos de medición en cada laboratorio.

## Acceptance Criteria
1. El sistema debe permitir registrar equipos de medición con los campos: nombre del equipo, marca, modelo, número de serie (opcional) y laboratorio asignado.
2. Al registrar el equipo, se debe configurar si este requiere mantenimiento del tipo "Calibración", "Limpieza" o ambos.
3. Cada equipo debe tener una ficha técnica editable donde se muestre su estado operativo actual ("Operativo", "En Mantenimiento", "Fuera de Servicio").
4. El sistema debe indexar el equipo bajo el laboratorio local configurado en la máquina.
