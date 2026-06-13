# HU04 - Registro de Stock Físico

## Summary
Controlar el stock físico de reactivos en cada laboratorio, registrando la cantidad actual, ubicación física detallada, umbral de cantidad mínima y fecha de vencimiento.

## Description
As a Técnico de Laboratorio, I want to registrar el stock físico de un reactivo en el almacén de mi laboratorio, so that conozcamos la existencia física exacta y la ubicación de cada lote de reactivos.

## Acceptance Criteria
1. El usuario debe poder asociar existencias físicas (`StockReactivo`) a un reactivo registrado en el catálogo.
2. Los campos obligatorios son: cantidad actual (en la unidad correspondiente como ml, g, etc.), ubicación física detallada (ej. "Estante A, Fila 2") y umbral de cantidad mínima antes de alerta.
3. El campo fecha de vencimiento debe ser opcional. Si se ingresa, el sistema debe validar que sea una fecha futura a la del registro.
4. Al guardar el stock, este debe indexarse automáticamente bajo el laboratorio local configurado en la máquina (LEPA o LEM).
