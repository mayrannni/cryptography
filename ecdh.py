# Elabora un programa que se ejecute correctamente 
# El programa elaborado valida que las entradas de datos sean validas y resuelve el problema seleccionado 
# El programa debe seguir las buenas prácticas de desarrollo

from tinyec import registry
import secrets

def validate_msg(msg):
    if not msg.strip():
        print("advertencia: el mensaje no debe estar vacío.")
        return False
    return True

def main():
    print("=== Elliptic Curve Diffie-Hellman ===")
    curve = registry.get_curve("brainpoolP256r1") # curva brainpool de 256 bits

    # claves para alice
    alice_priv = secrets.randbelow(curve.field.n)
    alice_pub = alice_priv * curve.g

    # claves para bob
    bob_priv = secrets.randbelow(curve.field.n)
    bob_pub = bob_priv * curve.g

    # derivar las claves compartidas
    alice_shared = alice_priv * bob_pub
    bob_shared = bob_priv * alice_pub

    print("claves generadas exitosamente :D")
    print("coincidencia de las claves compartidas ->", alice_shared == bob_shared)

    msg = input("mensaje a intercambiar: ")
    if validate_msg(msg):
        print("**el mensaje está listo para cifrarse.")

if __name__ == "__main__":
    main()
