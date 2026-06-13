# HU10 - Recepción de Préstamos (Destino)

## Summary
Registrar la recepción física y entrada en stock de un reactivo que ha sido prestado por el otro laboratorio.

## Description
As a Técnico de Laboratorio (Destino), I want to registrar la entrada de un reactivo recibido en calidad de préstamo, so that incrementemos el stock local con el reactivo prestado y cerremos el ciclo de transferencia.

## Acceptance Criteria
1. El usuario del laboratorio de destino debe poder registrar la entrada del préstamo importando el archivo de transferencia generado por el laboratorio origen o ingresando manualmente los datos del préstamo (reactivo, cantidad, laboratorio origen).
2. Al procesar la entrada, la cantidad recibida debe sumarse al `StockReactivo` del laboratorio destino de forma inmediata.
3. El sistema debe registrar esta entrada en la bitácora local de movimientos con la etiqueta de "Préstamo Recibido" e identificarlo en el stock como "Préstamo de [Laboratorio Origen]".
4. Debe existir un control para registrar la devolución del reactivo prestado para devolver el stock a su origen y marcar el préstamo como "Devuelto y Cerrado".
