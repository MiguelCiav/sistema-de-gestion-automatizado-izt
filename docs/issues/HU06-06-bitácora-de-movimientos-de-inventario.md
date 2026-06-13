# HU06 - Bitácora de Movimientos de Inventario

## Summary
Consultar el historial de consumos y movimientos para que los administradores sepan quién consumió qué reactivo y en qué cantidad.

## Description
As a Administrador / Jefe de Laboratorio, I want to visualizar una bitácora detallada de consumos y movimientos de stock, so that podamos auditar el uso de los recursos del laboratorio y saber quién usó qué insumo y cuánto.

## Acceptance Criteria
1. Debe existir una pantalla de bitácora que muestre en orden cronológico inverso todos los registros de consumo y movimientos de stock.
2. Cada entrada de la bitácora de inventario debe mostrar: fecha/hora, usuario responsable, reactivo, cantidad consumida/movida y tipo de movimiento (consumo, ajuste manual, préstamo).
3. La bitácora debe ser de solo lectura y no permitir edición ni eliminación de registros históricos para garantizar la integridad de la auditoría.
4. Debe incluir filtros de búsqueda por rango de fechas, usuario y reactivo.
