# HU16 - Registro de Mantenimiento Ejecutado

## Summary
Registrar la realización de calibraciones o limpiezas en la bitácora de mantenimiento (fecha, observaciones del técnico, responsable y reprogramación automática del próximo ciclo).

## Description
As a Técnico de Laboratorio / Técnico de Mantenimiento, I want to registrar un evento de mantenimiento completado sobre un equipo, so that la fecha de próxima calibración se actualice automáticamente y el histórico quede registrado de forma inmutable.

## Acceptance Criteria
1. El usuario debe poder registrar un evento de mantenimiento completado sobre un equipo de medición.
2. Los campos obligatorios son: fecha de ejecución, tipo de evento (Calibración o Limpieza), descripción del trabajo realizado, observaciones del técnico y nombre del técnico responsable.
3. Al registrar el mantenimiento, el sistema debe actualizar de forma automática la fecha del último mantenimiento del equipo y recalcular la fecha del próximo mantenimiento según su frecuencia.
4. La entrada debe quedar guardada de forma inmutable en la `BitacoraMantenimiento` asociada al equipo para auditorías de calidad.
