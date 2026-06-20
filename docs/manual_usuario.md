# 📘 Manual de Usuario - Chatbot de Gestión de Vacaciones

Este manual describe el funcionamiento, comandos y flujos conversacionales del asistente virtual automatizado para la solicitud de licencias ordinarias, desarrollado para el Trabajo Práctico Integrador (TPI).

---

## 🚀 1. Inicio del Sistema y Comandos Globales

El chatbot opera bajo una estructura de **Máquina de Estados Finitos (FSM)**. Esto significa que el bot siempre sabe en qué paso te encuentras y espera un dato específico.

### 📌 Comando de Emergencia
* **`salir`**: Puede ser ingresado en **cualquier momento** del flujo conversacional. 
  * **Acción**: Aborta inmediatamente el trámite actual, borra la memoria caché de la sesión y reinicia el bot al estado `INICIO`.

---

## 🗺️ 2. Flujo Secuencial de Operación (Paso a Paso)

### Paso 1: Inicialización del Trámite
* **Acción del Usuario**: Enviar el comando `/vacaciones` o iniciar el simulador.
* **Respuesta del Bot**: El sistema solicitará la identificación del empleado.
  * *Ejemplo*: `"👤 Bot: Por favor, introduce tu Número de Legajo:"`

### Paso 2: Autenticación (Gateway Legajo)
* **Acción del Usuario**: Ingresar el número de legajo numérico (Ej: `1001`).
* **Respuesta del Bot**: El sistema valida la existencia en la base de datos `mock_database.json`.
  * Si existe: Muestra un saludo personalizado y el saldo de días disponibles.
  * Si NO existe: Entra en el *Camino Infeliz* (Ver Sección 3).

### Paso 3: Solicitud de Período (Gateway Saldo)
* **Acción del Usuario**: Ingresar la cantidad de días enteros que desea tomarse (Ej: `5`).
* **Respuesta del Bot**: El sistema procesa las reglas de negocio en tiempo real.
  * Si el saldo es suficiente: Descuenta los días, registra la solicitud como `APROBADA` con un mensaje de éxito y finaliza.

---

## ⚠️ 3. Guía de Manejo de Errores (Caminos Infelices)

El software es robusto ante equivocaciones comunes del usuario, garantizando estabilidad (Criterio de Calidad de la TUP):

### Caso A: El usuario ingresa texto en lugar de números en los días
* **Qué hace el usuario**: Escribe `"cinco"`, `"cinco días"` o `"5a"`.
* **Reacción del Bot**: El bot detecta el error de tipo de datos, lanza una alerta de robustez y mantiene la sesión en el mismo paso sin colgarse.
  * *Mensaje*: `⚠️ [ERROR] Entrada inválida. Debes ingresar un número entero positivo.`

### Caso B: El usuario ingresa un legajo que no existe
* **Qué hace el usuario**: Escribe `9999` (id inexistente).
* **Reacción del Bot**: Deniega el acceso para proteger la persistencia de datos. Solicita nuevamente el ingreso correcto.
  * *Mensaje*: `⚠️ [ERROR] Legajo no encontrado en la base de datos. Inténtalo de nuevo.`

### Caso C: El usuario solicita más días de los que tiene disponibles
* **Qué hace el usuario**: Su saldo es de 14 días y solicita `20`.
* **Reacción del Bot**: La compuerta lógica del saldo deniega la operación, aborta el trámite por seguridad para no generar saldos negativos y resetea el contexto.
  * *Mensaje*: `❌ [RECHAZO SALDO] Saldo insuficiente. Trámite abortado por reglas de negocio.`

---

## 💻 4. Credenciales de Prueba Incluidas en el Simulador

Para evaluar los diferentes escenarios lógicos en tu defensa del TPI, utiliza los siguientes perfiles de prueba precargados:

1. **Legajo `1001` (Juan Pérez)**: Saldo amplio (14 días). Ideal para probar el **Camino Feliz**.
2. **Legajo `1002` (María López)**: Saldo ajustado (5 días). Ideal para probar el **Rechazo por Exceso de Días**.
3. **Legajo `1003` (Carlos Gómez)**: Sin saldo (0 días). Prueba inmediata de **Bloqueo de Negocio**.
