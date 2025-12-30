def evaluar_acceso(usuario_activo, clave_correcta):
    if not usuario_activo and not clave_correcta:
        return "Sistema Bloqueado"
    if not usuario_activo:
        return "Usuario inactivo"
    if not clave_correcta:
        return "Clave incorrecta"
    return "Acceso Concedido"

evaluar = evaluar_acceso(True, True)
print(evaluar)
        