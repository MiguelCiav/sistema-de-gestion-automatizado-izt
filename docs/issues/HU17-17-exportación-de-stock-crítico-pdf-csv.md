# HU17 - Exportación de Stock Crítico (PDF/CSV)

## Summary
Exportar listados automatizados de reactivos críticos o con existencias por debajo del umbral mínimo de forma consolidada o por dependencia.

## Description
As a Técnico de Laboratorio / Jefe de Laboratorio, I want to exportar el listado de reactivos con existencias bajas o vencidos a formatos PDF y CSV, so that podamos enviar rápidamente listas de compras o reposición a la administración.

## Acceptance Criteria
1. Debe existir una opción de exportación accesible desde las pantallas de Inventario y Alertas.
2. El usuario debe poder seleccionar el formato de descarga: CSV (para hojas de cálculo) o PDF (diseño legible para impresión).
3. El reporte exportado debe contener de forma obligatoria: código del reactivo, nombre, cantidad actual, umbral mínimo, ubicación física y laboratorio de origen.
4. El proceso de exportación debe ejecutarse localmente en la máquina del usuario y descargarse en un tiempo no mayor a 3 segundos.
