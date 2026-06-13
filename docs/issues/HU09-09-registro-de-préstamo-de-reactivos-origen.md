# HU09 - Registro de Préstamo de Reactivos (Origen)

## Summary
Registrar la salida de un reactivo en calidad de préstamo a otro laboratorio (cantidad, responsable del préstamo, laboratorio destino).

## Description
As a Técnico de Laboratorio (Origen), I want to registrar la salida de un reactivo prestado al otro laboratorio, so that documentemos la transferencia temporal de insumos y mantengamos la trazabilidad del stock.

## Acceptance Criteria
1. El usuario debe poder iniciar un registro de préstamo seleccionando el reactivo común, la cantidad a prestar y el laboratorio de destino (LEPA o LEM).
2. Al guardar el préstamo, la cantidad prestada debe restarse temporalmente del stock local y marcarse bajo un estado de "Prestado - Pendiente de Recepción".
3. El sistema debe permitir exportar este registro de préstamo en un formato de transferencia rápido (por ejemplo, un archivo cifrado JSON o código QR para importar en el laboratorio destino).
4. El préstamo debe registrarse en la bitácora local de movimientos de inventario con el detalle del laboratorio destino y responsable.
