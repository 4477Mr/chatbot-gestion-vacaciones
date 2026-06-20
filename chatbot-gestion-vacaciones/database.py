# database.py
import json

# Base de datos simulada (Simulación de Persistencia)
BD_EMPLEADOS = {
    101: {"nombre": "Carlos Gomez",  "area": "Desarrollo", "Saldo_vacaciones": 14},
    102: {"nombre": "Ana Martínez",  "area": "QA", "Saldo_vacaciones": 7},
    103: {"nombre": "Luis Pérez ",  "area": "Soporte", "Saldo_vacaciones": 21}
}

# Historial de solicitudes procesadas para auditoría
BD_SOLICITUDES = []

def obtener_empleado(legajo: int):
    """Busca un empleado por su número de legajo."""
    return BD_EMPLEADOS.get(legajo)

def actualizar_saldo_y_solicitud(legajo: int, dias: int, estado: str):
    """Modifica el saldo del empleado y registra la auditoría."""
    if legajo in BD_EMPLEADOS:
        if estado == "APROBADO":
            BD_EMPLEADOS[legajo]["Saldo_vacaciones"] -= dias
        
        nueva_solicitud = {
            "id_solicitud": len(BD_SOLICITUDES) + 1,
            "legajo": legajo,
            "dias_solicitados": dias,
            "estado": estado
        }
        BD_SOLICITUDES.append(nueva_solicitud)
        return True
    return False
