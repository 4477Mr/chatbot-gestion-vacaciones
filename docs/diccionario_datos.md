
# Diccionario de Datos - Sistema de Gestión de Vacaciones

Este documento detalla la estructura y restricciones de la persistencia simulada utilizada por el Chatbot de Recursos Humanos.

## 1. Entidad: Empleados (`BD_EMPLEADOS`)
Representa el registro maestro del personal activo habilitado para solicitar licencias.

| Campo | Tipo de Datos | Descripción | Restricciones / Reglas de Negocio |
| :--- | :--- | :--- | :--- |
| `ID (Clave)` | `Integer` | Número de legajo único del empleado (ej. 101, 102). | Llave primaria. |
| `nombre` | `String` | Nombre y apellido completo del trabajador. | Campo obligatorio. |
| `area` | `String` | Departamento organizacional al que pertenece. | Filtro de estructura interna. |
| `Saldo_vacaciones` | `Integer` | Días de vacaciones disponibles acumulados. | No puede ser menor a 0 tras confirmación. |

## 2. Entidad: Solicitudes (`BD_SOLICITUDES`)
Colección histórica que almacena las transacciones procesadas por el Chatbot para auditoría interna.

| Campo | Tipo de Datos | Descripción | Restricciones / Reglas de Negocio |
| :--- | :--- | :--- | :--- |
| `id_solicitud` | `Integer` | Identificador autoincremental de la transacción. | Llave primaria única. |
| `legajo` | `Integer` | Legajo del empleado que realiza la solicitud. | Llave foránea vinculada a `BD_EMPLEADOS`. |
| `dias_solicitados`| `Integer` | Cantidad de días requeridos en la sesión. | Debe ser menor o igual al saldo actual. |
| `estado` | `String` | Estado final del ciclo de vida de la transacción. | Valores: `APROBADO`, `RECHAZADO_SALDO`. |

