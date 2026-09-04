# Desarrollo de una aplicación web con Django y panel de administración

La empresa necesita una aplicación web que permita a los usuarios registrarse, iniciar sesión y gestionar sus perfiles. Además, se requiere un panel de administración para que los administradores puedan ver y editar los perfiles de los usuarios. Los usuarios deben tener un nombre de usuario único y una contraseña segura. El panel de administración debe permitir la creación, edición y eliminación de perfiles de usuarios.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | aplicacion-web-con-django-y-admin-panel |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 10 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración inicial del proyecto

**Objetivo:** Configurar un proyecto de Django básico con autenticación de usuarios.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Crear un nuevo proyecto de Django.
- Configurar la autenticación de usuarios con registro y login.
- Asegurar que los nombres de usuario sean únicos y las contraseñas sean seguras.

**Entregable:** Proyecto de Django con autenticación de usuarios funcional.

<details>
<summary>Pistas de conocimiento</summary>

- Utilizar el sistema de autenticación incorporado de Django.
- Implementar validaciones en los formularios de registro y login.

</details>

### Fase 2: Creación del panel de administración

**Objetivo:** Desarrollar un panel de administración para gestionar perfiles de usuarios.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Crear un panel de administración en Django.
- Permitir la visualización, edición y eliminación de perfiles de usuarios.
- Asegurar que solo los administradores tengan acceso al panel.

**Entregable:** Panel de administración funcional para gestionar perfiles de usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Utilizar las vistas y templates de Django para crear el panel de administración.
- Implementar control de acceso para asegurar que solo los administradores puedan acceder al panel.

</details>

### Fase 3: Mejoras y pruebas

**Objetivo:** Realizar mejoras y pruebas para asegurar la calidad del proyecto.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Agregar mejoras al proyecto, como validaciones adicionales o mejoras en la interfaz de usuario.
- Realizar pruebas unitarias y de integración para asegurar que el proyecto funcione correctamente.
- Documentar el proyecto y proporcionar instrucciones de uso.

**Entregable:** Proyecto de Django mejorado y documentado, con pruebas unitarias y de integración.

<details>
<summary>Pistas de conocimiento</summary>

- Utilizar herramientas de testing de Django para realizar pruebas unitarias y de integración.
- Documentar el proyecto utilizando comentarios y un archivo README.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es Django y para qué se utiliza en el desarrollo de aplicaciones web?
- **paraQueSirve**: ¿Para qué sirve la autenticación de usuarios en una aplicación web y cómo se implementa en Django?
- **comoSeUsa**: ¿Cómo se utiliza el panel de administración en Django para gestionar perfiles de usuarios?
- **erroresComunes**: ¿Cuáles son los errores comunes al desarrollar una aplicación web con Django y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones de diseño implica el desarrollo de una aplicación web con Django y un panel de administración?

## Criterios de Evaluacion

- Configuración correcta del proyecto de Django con autenticación de usuarios.
- Desarrollo de un panel de administración funcional para gestionar perfiles de usuarios.
- Implementación de mejoras y pruebas para asegurar la calidad del proyecto.
- Documentación efectiva del proyecto y provisión de instrucciones de uso.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
