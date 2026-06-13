# HU05 - Registro de Consumo de Reactivos

## Summary
Registrar cada salida o consumo de reactivos especificando el usuario, el reactivo, la cantidad consumida y la fecha.

## Description
As a Investigador / Estudiante / Técnico, I want to registrar la cantidad consumida de un reactivo específico, so that el inventario de stock físico se actualice automáticamente en tiempo real.

## Acceptance Criteria
1. El sistema debe proveer una interfaz rápida y simple para registrar el consumo de un reactivo en stock.
2. Los campos obligatorios para registrar el consumo son: nombre del usuario que consume, reactivo seleccionado, cantidad consumida y fecha del consumo (por defecto la fecha y hora actual).
3. Al guardar el registro, la cantidad consumida debe restarse inmediatamente de la `cantidad_actual` en el stock correspondiente.
4. El sistema debe validar que la cantidad consumida no sea mayor que la cantidad actualmente disponible en stock, arrojando una alerta si se intenta sobrepasar.
