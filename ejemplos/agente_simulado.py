"""Agente didáctico con herramienta ficticia y validación básica."""

def pronostico(ciudad):
    return {"ciudad": ciudad, "temperatura_c": 28, "condicion": "soleado"}

def ejecutar(plan):
    if plan.get("herramienta") != "pronostico":
        raise ValueError("herramienta no permitida")
    ciudad = plan.get("argumentos", {}).get("ciudad")
    if not isinstance(ciudad, str) or not ciudad.strip():
        raise ValueError("ciudad inválida")
    return pronostico(ciudad)

if __name__ == "__main__":
    plan = {"herramienta": "pronostico", "argumentos": {"ciudad": "Villahermosa"}}
    print(ejecutar(plan))
