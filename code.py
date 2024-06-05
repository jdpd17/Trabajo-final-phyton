import re

def verificar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not re.search(r"[A-Z]", contraseña):
        return "La contraseña debe contener al menos una letra mayúscula."
    if not re.search(r"\d", contraseña):
        return "La contraseña debe contener al menos un número."
    return "La contraseña es válida."

def solicitar_contraseña():
    contraseña = input("Por favor, ingrese una contraseña: ")
    resultado = verificar_contraseña(contraseña)
    while resultado != "La contraseña es válida.":
        print(resultado)
        contraseña = input("Por favor, ingrese una contraseña: ")
        resultado = verificar_contraseña(contraseña)
    print("Contraseña aceptada.")

solicitar_contraseña()