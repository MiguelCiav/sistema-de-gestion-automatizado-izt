# HU02 - Catálogo Unificado de Reactivos

## Summary
Crear y gestionar el catálogo de reactivos químicos con campos de código único, nombre, fórmula química, riesgo y valores del rombo de riesgo (NFPA 704).

## Description
As a Técnico de Laboratorio / Administrador, I want to registrar y gestionar reactivos en un catálogo unificado, so that tengamos un registro estandarizado de todos los tipos de reactivos químicos del instituto sin duplicidades.

## Acceptance Criteria
1. El sistema debe permitir registrar un reactivo en el catálogo con los campos: código único del reactivo (ID químico), nombre comercial/químico, fórmula química, clasificación de riesgo y los cuatro valores del rombo de riesgo NFPA 704 (Salud, Inflamabilidad, Inestabilidad, Riesgo Especial).
2. El código único del reactivo (e.g., código CAS o interno normalizado) debe ser obligatorio y validarse para evitar duplicados en el catálogo local.
3. Múltiples existencias o lotes físicos de reactivos del mismo tipo en los almacenes deben referenciar a un mismo registro único del catálogo.
4. Los usuarios pueden buscar reactivos en el catálogo por nombre, código único o fórmula química.
5. Los campos del rombo de riesgo NFPA 704 deben validarse para permitir únicamente valores numéricos del 0 al 4 y caracteres especiales válidos para el riesgo específico.
