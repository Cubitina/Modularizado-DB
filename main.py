import sys
print(sys.path)
from frontend.frontend import *

# Función principal que inicia el programa
def main():
    """
    Función principal que inicia la app.
    """
    # Llama a la función para que se ejecute y se inicie el programa
    menu_de_bienvenida(menu)

if __name__ == "__main__":
    main()