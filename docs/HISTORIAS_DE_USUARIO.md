# Historias de Usuario Propuestas: Sistema de Gestión Automatizado LEPA-LEM

Este documento recopila las historias de usuario propuestas para el desarrollo del **Sistema de Gestión Automatizado LEPA-LEM**, organizadas por módulos y clasificadas según su relevancia para el **Producto Mínimo Viable (MVP)** en función de la restricción de **100 horas de desarrollo**.

---

## Módulo 1: Configuración de Infraestructura y Datos Maestros (Core - MVP)
* **HU01 - Configuración de Laboratorio Local:** Inicializar la aplicación seleccionando el laboratorio físico (LEPA o LEM) para la operación independiente en la red local de cada máquina.
* **HU02 - Catálogo Unificado de Reactivos:** Crear y gestionar el catálogo de reactivos químicos con campos de código único, nombre, fórmula química, riesgo y valores del rombo de riesgo (NFPA 704).
* **HU03 - Consistencia de Códigos Compartidos:** Validar y asegurar que los reactivos compartidos por ambos laboratorios utilicen exactamente la misma codificación unificada.

## Módulo 2: Control de Inventario y Existencias (Core - MVP)
* **HU04 - Registro de Stock Físico:** Controlar el stock físico de reactivos en cada laboratorio, registrando la cantidad actual, ubicación física detallada, umbral de cantidad mínima y fecha de vencimiento (cuando aplique).
* **HU05 - Registro de Consumo de Reactivos:** Registrar cada salida o consumo de reactivos especificando el usuario, el reactivo, la cantidad consumida y la fecha.
* **HU06 - Bitácora de Movimientos de Inventario:** Consultar el historial de consumos y movimientos para que los administradores sepan quién consumió qué reactivo y en qué cantidad.
* **HU07 - Alertas Visuales de Stock Mínimo:** Visualizar notificaciones o alertas en la interfaz de usuario cuando un reactivo descienda de su umbral mínimo configurado.
* **HU08 - Alertas de Vencimiento de Reactivos:** Mostrar avisos de caducidad para los reactivos que cuenten con fecha de vencimiento y estén próximos a expirar.

## Módulo 3: Préstamos Inter-Laboratorios (MVP - Crítico por Requisitos)
* **HU09 - Registro de Préstamo de Reactivos (Origen):** Registrar la salida de un reactivo en calidad de préstamo a otro laboratorio (cantidad, responsable del préstamo, laboratorio destino).
* **HU10 - Recepción de Préstamos (Destino):** Registrar la recepción física y entrada en stock de un reactivo que ha sido prestado por el otro laboratorio.

## Módulo 4: Control de Material de Vidrio (Baja Prioridad - Fuera del MVP)
* **HU11 - Inventario de Material de Vidrio:** Registrar y actualizar la cantidad, ubicación física y tipo de material de vidrio por laboratorio.
* **HU12 - Control de Estado de Vidrio:** Registrar las condiciones cualitativas (bueno, agrietado, inutilizable) del material de vidrio disponible.

## Módulo 5: Gestión y Bitácoras de Equipos (Baja Prioridad - Fuera del MVP)
* **HU13 - Inventario de Equipos de Medición:** Registrar los equipos de medición por laboratorio, indicando marca, modelo y si requiere calibración, limpieza o ambas.
* **HU14 - Bitácora de Uso de Equipos:** Registrar el uso diario de los equipos de medición (quién lo usó, qué equipo, fecha, horas de uso y el tipo de uso o experimento).
* **HU15 - Programación de Calibraciones y Limpiezas:** Visualizar de forma consolidada el estado del próximo mantenimiento planificado (cuándo se hicieron y cuándo toca la siguiente calibración o limpieza).
* **HU16 - Registro de Mantenimiento Ejecutado:** Registrar la realización de calibraciones o limpiezas en la bitácora de mantenimiento (fecha, observaciones del técnico, responsable y reprogramación automática del próximo ciclo).

## Módulo 6: Reportes y Listados (Prioridad Media)
* **HU17 - Exportación de Stock Crítico (PDF/CSV):** Exportar listados automatizados de reactivos críticos o con existencias por debajo del umbral mínimo de forma consolidada o por dependencia.
