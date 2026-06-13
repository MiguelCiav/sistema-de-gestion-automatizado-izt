# HU07 - Alertas Visuales de Stock Mínimo

## Summary
Visualizar notificaciones o alertas en la interfaz de usuario cuando un reactivo descienda de su umbral mínimo configurado.

## Description
As a Técnico de Laboratorio, I want to recibir alertas visuales cuando la cantidad de un reactivo esté por debajo de su umbral mínimo, so that pueda planificar el reabastecimiento antes de que se agote por completo.

## Acceptance Criteria
1. El sistema debe evaluar constantemente la condición `cantidad_actual <= umbral_minimo` para cada elemento de `StockReactivo`.
2. Los reactivos en estado de alerta de stock mínimo deben mostrarse con un indicador visual destacado (ej. color de alerta rojo/naranja) en la vista de inventario.
3. Debe existir una sección de "Alertas Activas" en el panel principal que agrupe todos los reactivos en estado crítico.
4. Al realizar un registro de consumo que haga descender el stock por debajo del umbral mínimo, el sistema debe notificar al usuario de forma inmediata en la pantalla mediante una alerta temporal.
