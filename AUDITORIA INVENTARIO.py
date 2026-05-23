# ============================================================
# AUDITORÍA DE INVENTARIO
# Edgar Manuel Betancourt Ospina - C.C. 1.073.534.594
# Fundamentos de Programación - Código: 213022
# Universidad Nacional Abierta y a Distancia (UNAD)
# Fase 5 
# ============================================================

# -------------------------------------------------------
# 1. DATOS INICIALES   
# -------------------------------------------------------
inventario = [
    ["T001", "Teclado USB",          15,  20],
    ["T002", "Mouse Inalámbrico",     8,   8],
    ["T003", "Monitor 24 pulgadas",   2,  10],
    ["T004", "Cable HDMI",           30,  15],
    ["T005", "Auriculares",           0,   5],
    ["T006", "Webcam HD",             6,  12],
]
# -------------------------------------------------------
# 2. MÓDULO REQUERIDO (FUNCION)
# -------------------------------------------------------
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Calcula cuántas unidades se deben pedir de un artículo.

    Parámetros:
        stock_actual  (int): Unidades disponibles actualmente en bodega.
        stock_minimo  (int): Mínimo de unidades requeridas.

    Retorna:
        int: Cantidad a pedir. 
             - Si stock_actual < stock_minimo → retorna la diferencia.
             - Si stock_actual >= stock_minimo → retorna 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual  
    else:
        return 0                             
# -------------------------------------------------------
# 3. PROGRAMA PRINCIPAL
# -------------------------------------------------------
def main():
    print("=" * 60)
    print("        INFORME DE AUDITORÍA Y REABASTECIMIENTO")
    print("=" * 60)
    print(f"{'Código':<8} {'Nombre':<25} {'Stock':>7} {'Mínimo':>7} {'A Pedir':>9}")
    print("-" * 60)

    # Recorrido de matriz y muestra de estado de cada artículo
    for articulo in inventario:
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        print(f"{codigo:<8} {nombre:<25} {stock_actual:>7} {stock_minimo:>7} {cantidad_pedir:>9}")

    print("=" * 60)

    # --- LISTA FINAL DE PEDIDOS ---
    print("\n--- LISTA DE PEDIDOS (artículos que necesitan reabasto) ---\n")

    hay_pedidos = False
    for articulo in inventario:
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        if cantidad_pedir > 0:
            print(f"  Artículo : {nombre}")
            print(f"  Cantidad a pedir: {cantidad_pedir} unidades")
            print()
            hay_pedidos = True

    if not hay_pedidos:
        print("  ✔ Todos los artículos tienen stock suficiente.")

    print("=" * 60)
    print("  Fin del informe de inventario.")
    print("=" * 60)


# Punto de entrada del programa
if __name__ == "__main__":
    main()