# HU03 - Consistencia de Códigos Compartidos

## Summary
Validar y asegurar que los reactivos compartidos por ambos laboratorios utilicen exactamente la misma codificación unificada.

## Description
As a Administrador del Sistema, I want to asegurar que los reactivos comunes compartidos entre LEPA y LEM tengan el mismo código único en ambas bases de datos, so that facilitemos el intercambio y mantengamos la consistencia de datos en el instituto.

## Acceptance Criteria
1. Si un reactivo es marcado en el catálogo como de "uso común / compartido", el sistema debe validar que su `codigo_unico` coincida con el estándar establecido para el IZT.
2. Al intentar registrar o editar un reactivo marcado como común con un código ya existente para otro reactivo exclusivo, el sistema debe arrojar un error de validación descriptivo.
3. Debe ser posible marcar un reactivo existente como común, lo que habilitará de forma automática su visualización en las opciones de préstamos.
4. Las actualizaciones de los datos del catálogo para un reactivo común deben poder exportarse para mantener la consistencia entre las instalaciones de LEPA y LEM.
