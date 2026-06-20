# database.py
import json

# Base de datos simulada alineada estrictamente con el esquema del proyecto
BD_EMPLEADOS = {
    "1001": {"nombre": "Carlos Gomez", "area": "Desarrollo", "saldo_dias": 14, "estado_fsm": "INICIO"},
    "1002": {"nombre": "Ana Martínez", "area": "QA", "saldo_dias": 7, "estado_fsm": "INICIO"},
    "1003": {"nombre": "Luis Pérez", "area": "Soporte", "saldo_dias": 21, "estado_fsm": "INICIO"}
}

# Historial de solicitudes procesadas para auditoría
BD_SOLICITUDES = []

def obtener_empleado(legajo: str):
    """Busca un empleado por su número de legajo (String)."""
    return BD_EMPLEADOS.get(str(legajo).strip())

def actualizar_saldo_y_solicitud(legajo: str, dias: int, estado: str):
    """Modifica el saldo de días e impacta el historial histórico."""
    empleado = obtener_empleado(legajo)
    if empleado:
        if estado == "APROBADA":
            empleado["saldo_dias"] -= dias
        
        nueva_solicitud = {
            "legajo": str(legajo).strip(),
            "nombre": empleado["nombre"],
            "dias_solicitados": dias,
            "estado": estado
        }
        BD_SOLICITUDES.append(nueva_solicitud)
        return True
    return False
