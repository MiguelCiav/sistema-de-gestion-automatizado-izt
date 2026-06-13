# HU01 - Configuración de Laboratorio Local

## Summary
Inicializar la aplicación seleccionando el laboratorio físico (LEPA o LEM) para la operación independiente en la red local de cada máquina.

## Description
As a Técnico de Laboratorio / Administrador, I want to seleccionar el laboratorio al que pertenece la máquina durante el primer inicio, so that la aplicación filtre automáticamente el inventario y equipos correspondientes a esa ubicación y funcione de forma offline.

## Acceptance Criteria
1. Al iniciar la aplicación por primera vez en una máquina, debe mostrarse una pantalla de configuración inicial para seleccionar el laboratorio (LEPA o LEM).
2. La selección del laboratorio debe persistir localmente en la máquina (localStorage, SQLite o archivo de configuración).
3. Toda la interfaz del sistema (inventarios, bitácoras) debe estar pre-filtrada por defecto para el laboratorio seleccionado en el primer inicio.
4. Debe existir un panel de configuración protegido por contraseña de administrador para poder reconfigurar el laboratorio de la máquina en caso de ser necesario.
5. El sistema no debe requerir conexión a internet para esta configuración ni para el funcionamiento general local.
