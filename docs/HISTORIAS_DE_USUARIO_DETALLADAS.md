# Catálogo Detallado de Historias de Usuario: Sistema de Gestión Automatizado LEPA-LEM

Este documento describe con detalle las Historias de Usuario del **Sistema de Gestión Automatizado LEPA-LEM**, incluyendo sus Criterios de Aceptación (DoR/DoD), con base en el documento del proyecto y la reunión plasmada en [REQUISITOS.txt](file:///home/miguel-ciavato/Documents/github-repos/sistema-de-gestion-automatizado-izt/REQUISITOS.txt).

---

## Módulo 1: Configuración de Infraestructura y Datos Maestros (Core - MVP)

### HU01 - Configuración de Laboratorio Local
* **Descripción:** Como Administrador del Sistema, quiero poder inicializar y configurar la aplicación para asociarla permanentemente al laboratorio físico correspondiente (LEPA o LEM), de modo que funcione de manera independiente en la red local y registre datos bajo la identidad del laboratorio correcto.
* **Criterios de Aceptación:**
  1. Durante la primera ejecución de la aplicación, el sistema debe mostrar una pantalla de inicialización para seleccionar el laboratorio (opciones: "Laboratorio de Ecología de Plantas Acuáticas - LEPA" o "Laboratorio de Ecología de Microorganismos - LEM").
  2. Una vez seleccionado y confirmado el laboratorio, la aplicación debe guardar esta configuración localmente de forma persistente.
  3. No se debe permitir la reconfiguración directa del laboratorio a menos que se realice una acción administrativa especial (ej. reset de configuración con credenciales).
  4. La interfaz de usuario debe mostrar claramente en la barra superior o cabecera el nombre y código del laboratorio configurado.

### HU02 - Catálogo Unificado de Reactivos
* **Descripción:** Como Analista de Laboratorio, quiero registrar y gestionar un catálogo maestro de reactivos químicos, para que tengamos una lista estandarizada de reactivos con sus riesgos de seguridad asociados.
* **Criterios de Aceptación:**
  1. El sistema debe permitir crear, leer, actualizar y dar de baja (lógica) reactivos en el catálogo.
  2. Los campos obligatorios para el reactivo son: Código Único del Reactivo (químico), Nombre del Reactivo, Fórmula Química, Nivel de Riesgo (general) y los 4 valores numéricos del Rombo de Riesgo NFPA 704 (Salud, Inflamabilidad, Inestabilidad, Riesgos Especiales).
  3. El Código Único de Reactivo debe ser validado para evitar duplicados en la base de datos local.
  4. Si un reactivo tiene el mismo código químico, debe compartir la misma ficha técnica independientemente del laboratorio.

### HU03 - Consistencia de Códigos Compartidos
* **Descripción:** Como Administrador del Sistema, quiero asegurar que los códigos de reactivos compartidos sean exactamente los mismos en ambas redes locales, para facilitar el cruce de datos y futuros préstamos o consolidaciones.
* **Criterios de Aceptación:**
  1. Al registrar un nuevo reactivo, si se ingresa un código ya existente en la nomenclatura unificada compartida, el sistema debe autocompletar la información del catálogo (Nombre, Fórmula Química, Riesgo, Rombo NFPA 704).
  2. El sistema debe permitir importar/exportar un archivo maestro de catálogo (ej. formato JSON/CSV) para sincronizar los códigos entre los dos laboratorios de forma manual (ya que trabajan de manera independiente en redes locales).
  3. El sistema debe validar que los reactivos catalogados como "comunes" (es_comun = true) utilicen el formato estándar de codificación aprobado.

---

## Módulo 2: Control de Inventario y Existencias (Core - MVP)

### HU04 - Registro de Stock Físico
* **Descripción:** Como Analista de Laboratorio, quiero registrar las existencias físicas de los reactivos en mi laboratorio, para conocer la cantidad actual y ubicación de cada insumo físico.
* **Criterios de Aceptación:**
  1. El sistema debe permitir asociar un reactivo del catálogo al stock físico del laboratorio configurado localmente.
  2. Los campos a registrar son: Cantidad actual disponible, Umbral de cantidad mínima (para alerta de escasez), Ubicación física detallada (estante, nevera, caja, etc.) y Fecha de vencimiento (opcional/a veces aplica).
  3. La ubicación física no puede estar vacía y debe limitarse a texto plano legible.
  4. Al guardar un stock físico, la cantidad actual debe inicializarse en 0 o más (no se permiten números negativos).

### HU05 - Registro de Consumo de Reactivos
* **Descripción:** Como Investigador o Analista de Laboratorio, quiero registrar el consumo o retiro de un reactivo del stock, de modo que el inventario se actualice en tiempo real y quede trazabilidad de la acción.
* **Criterios de Aceptación:**
  1. El usuario debe poder seleccionar un reactivo en stock y registrar una salida de cantidad.
  2. Los campos obligatorios son: Nombre del responsable (quién consume), Cantidad consumida y Fecha de consumo (por defecto el día actual).
  3. El sistema debe validar que la cantidad consumida no supere el stock actual disponible; de lo contrario, se debe denegar la transacción con un mensaje de error claro ("Cantidad insuficiente en stock").
  4. Una vez guardado el consumo, el stock actual del reactivo debe restarse automáticamente por la cantidad consumida.

### HU06 - Bitácora de Movimientos de Inventario
* **Descripción:** Como Administrador del Sistema, quiero consultar una bitácora detallada de los consumos y movimientos de stock, para saber quién, cuándo y cuánto reactivo se ha consumido.
* **Criterios de Aceptación:**
  1. Debe existir una pantalla de bitácora que muestre una lista cronológica inversa de todos los registros de consumo y movimientos.
  2. Cada entrada en la bitácora debe mostrar: Fecha y hora de la transacción, Tipo de movimiento (Consumo, Ajuste de Inventario, Ingreso de Stock, Préstamo), Nombre del responsable, Reactivo y Cantidad.
  3. El sistema debe permitir filtrar la bitácora por rango de fechas, reactivo o responsable del consumo.
  4. La bitácora debe ser de solo lectura para los usuarios estándar; no se debe permitir editar ni eliminar registros históricos para garantizar la integridad de los datos.

### HU07 - Alertas Visuales de Stock Mínimo
* **Descripción:** Como Analista de Laboratorio, quiero que el sistema emita alertas visuales automáticas cuando la cantidad de un reactivo descienda de su umbral mínimo, para solicitar reposición a tiempo y evitar desabastecimiento.
* **Criterios de Aceptación:**
  1. El sistema debe evaluar de manera automática en la base de datos si la cantidad actual de un reactivo en stock es menor o igual al umbral mínimo definido para ese reactivo.
  2. En el panel principal (Dashboard) o vista de inventario, se deben destacar visualmente los reactivos en estado de escasez (ej. color de alerta rojo/naranja o icono de advertencia).
  3. Debe existir una sección específica de "Reactivos por Agotar" o "Alertas de Stock" de fácil acceso.
  4. La alerta debe desaparecer automáticamente cuando se registre un reabastecimiento que supere el umbral mínimo configurado.

### HU08 - Alertas de Vencimiento de Reactivos
* **Descripción:** Como Analista de Laboratorio, quiero recibir notificaciones visuales sobre los reactivos que estén próximos a vencer, para priorizar su uso o descartar insumos vencidos de forma segura.
* **Criterios de Aceptación:**
  1. El sistema debe buscar en el inventario todos los reactivos que tengan una fecha de vencimiento configurada.
  2. Se debe mostrar una advertencia visual (ej. amarillo para "próximo a vencer" a 30 días o menos, rojo para "vencido") en la lista de inventario y panel de alertas.
  3. La fecha de vencimiento debe validarse en la interfaz: no se debe permitir la carga de una fecha de vencimiento en el pasado al ingresar nuevo stock, a menos que sea una regularización de inventario histórico (con advertencia).
  4. En la ficha de stock físico, debe figurar claramente el estado del reactivo: "Vigente", "Próximo a Vencer" o "Vencido".

---

## Módulo 3: Préstamos Inter-Laboratorios (MVP - Crítico)

### HU09 - Registro de Préstamo de Reactivos (Origen)
* **Descripción:** Como Analista de Laboratorio, quiero registrar la salida de un reactivo en calidad de préstamo a otro laboratorio, para llevar el control físico de insumos transferidos temporalmente.
* **Criterios de Aceptación:**
  1. El sistema debe permitir registrar una transacción de préstamo saliente de un reactivo.
  2. Los campos requeridos son: Reactivo a prestar, Cantidad, Laboratorio destino (LEPA/LEM), Nombre del responsable que entrega y Nombre del responsable que recibe en el otro laboratorio.
  3. Al registrar el préstamo, la cantidad prestada debe ser deducida del stock actual del laboratorio origen y el estado del préstamo debe quedar en "Prestado - Activo".
  4. El sistema debe registrar esta transacción en la bitácora de movimientos bajo el tipo "Préstamo Saliente".

### HU10 - Recepción de Préstamos (Destino)
* **Descripción:** Como Analista de Laboratorio, quiero registrar la recepción de un reactivo que ha sido prestado por el otro laboratorio, para incorporarlo temporalmente al inventario disponible.
* **Criterios de Aceptación:**
  1. El usuario del laboratorio receptor debe poder registrar la entrada física de un préstamo recibido.
  2. Se debe seleccionar el reactivo (catálogo unificado), registrar la cantidad recibida, el laboratorio de origen y el responsable de recibir.
  3. El sistema debe incrementar el stock actual disponible del reactivo en el laboratorio receptor y marcar el préstamo localmente como "Recibido - Activo".
  4. Debe quedar trazabilidad en la bitácora del laboratorio destino como "Préstamo Entrante".

---

## Módulo 4: Control de Material de Vidrio (Baja Prioridad - Fuera del MVP)

### HU11 - Inventario de Material de Vidrio
* **Descripción:** Como Analista de Laboratorio, quiero registrar y controlar el inventario de material de vidrio de mi laboratorio, para conocer la disponibilidad cuantitativa de estos insumos.
* **Criterios de Aceptación:**
  1. El sistema debe permitir dar de alta materiales de vidrio (ej. vasos de precipitado, tubos de ensayo, matraces) por laboratorio.
  2. Los campos obligatorios son: Nombre o tipo de material, Cantidad disponible y Ubicación física (ej. estante, gaveta).
  3. El sistema debe permitir registrar retiros o adiciones en la cantidad de material de vidrio para actualizar la disponibilidad física.
  4. La visualización del inventario de vidrio debe estar claramente separada del catálogo de reactivos químicos para evitar confusiones operativas.

### HU12 - Control de Estado de Vidrio
* **Descripción:** Como Analista de Laboratorio, quiero registrar el estado cualitativo del material de vidrio, para saber qué cantidad está en condiciones de uso y qué cantidad está deteriorada.
* **Criterios de Aceptación:**
  1. En el inventario de material de vidrio, se debe poder clasificar la cantidad disponible según su estado físico (ej. "Buen Estado", "Desgastado/Agrietado" o "Dañado/Roto").
  2. Al reportar un material roto, el sistema debe darlo de baja automáticamente de la cantidad disponible y registrar el motivo de la pérdida.
  3. El sistema debe permitir visualizar un resumen cualitativo del estado del material de vidrio del laboratorio.

---

## Módulo 5: Gestión y Bitácoras de Equipos (Baja Prioridad - Fuera del MVP)

### HU13 - Inventario de Equipos de Medición
* **Descripción:** Como Investigador o Analista, quiero registrar y consultar los equipos de medición disponibles en el laboratorio, para tener un catálogo actualizado de los activos físicos y su marca/modelo.
* **Criterios de Aceptación:**
  1. Se debe permitir la creación de fichas de equipos de medición asignados al laboratorio.
  2. Campos obligatorios: Nombre del equipo, Marca y Modelo, Número de Serie (opcional) y Tipo de Mantenimiento requerido (opciones: "Calibración", "Limpieza" o "Ambos").
  3. Cada equipo debe tener un estado de disponibilidad operativo ("Operativo", "En Mantenimiento", "Fuera de Servicio").
  4. La ficha del equipo debe mostrar la fecha del próximo mantenimiento preventivo (calibración o limpieza).

### HU14 - Bitácora de Uso de Equipos
* **Descripción:** Como Investigador, quiero registrar cuándo y cómo uso un equipo de medición, para dejar un histórico de uso que ayude a planificar mantenimientos preventivos y asegurar la trazabilidad experimental.
* **Criterios de Aceptación:**
  1. El sistema debe proveer una bitácora digital de uso por cada equipo.
  2. Al iniciar o finalizar el uso de un equipo, el investigador debe registrar: Nombre del usuario, Fecha y hora, Experimento/Uso (descripción de cómo se usó) y observaciones del estado del equipo al finalizar.
  3. Esta bitácora debe ser de solo lectura una vez guardada, con listado ordenado cronológicamente de forma descendente.

### HU15 - Programación de Calibraciones y Limpiezas
* **Descripción:** Como Coordinador de Laboratorio, quiero visualizar las fechas programadas de próximas calibraciones y limpiezas de los equipos, para planificar las actividades del laboratorio sin interrumpir experimentos.
* **Criterios de Aceptación:**
  1. El sistema debe generar alertas visuales (ej. colores en el dashboard o calendario) de los equipos que requieren calibración o limpieza en un plazo menor a 15 días.
  2. Debe existir un listado ordenado por "Fecha de Próximo Mantenimiento" más cercana.
  3. Se debe diferenciar claramente si el mantenimiento requerido es una "Calibración" o una "Limpieza".

### HU16 - Registro de Mantenimiento Ejecutado
* **Descripción:** Como Técnico o Coordinador de Laboratorio, quiero registrar cuando se realiza un mantenimiento (calibración o limpieza) a un equipo, para actualizar su ficha técnica y reprogramar la fecha del siguiente mantenimiento.
* **Criterios de Aceptación:**
  1. El sistema debe permitir registrar una entrada en la bitácora de mantenimiento de un equipo.
  2. Campos obligatorios: Tipo de mantenimiento realizado (Calibración o Limpieza), Fecha de realización, Descripción detallada de las acciones realizadas, Técnico responsable y Nueva fecha de próximo mantenimiento.
  3. Al registrarse el mantenimiento con éxito, la fecha del próximo mantenimiento en la ficha principal del equipo debe actualizarse automáticamente con el nuevo valor provisto.

---

## Módulo 6: Reportes y Listados (Prioridad Media)

### HU17 - Exportación de Stock Crítico (PDF/CSV)
* **Descripción:** Como Coordinador de Laboratorio, quiero exportar listados de reactivos con existencias por debajo del mínimo o próximos a vencer, para utilizarlos como órdenes de compra o informes internos de insumos críticos.
* **Criterios de Aceptación:**
  1. El sistema debe proveer un botón para exportar reportes de inventario crítico.
  2. El reporte debe admitir filtros: reactivos por debajo del umbral mínimo, reactivos vencidos/próximos a vencer, o todo el stock consolidado del laboratorio.
  3. Formatos de salida obligatorios: PDF (apto para impresión) y CSV (para importación en hojas de cálculo).
  4. El documento exportado debe incluir un encabezado claro con el nombre del laboratorio, fecha de generación del reporte y número de página.
