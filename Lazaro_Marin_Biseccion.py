import math
"""
Nombre y Apellidos: Lazaro Marin
Cédula: 27870547
"""

def error_relativo(vact, vant):
    """Implementación del error relativo.
    vact: valor actual.
    vant: valor anterior.
    return el error relativo de vact y vant.
    """
    pass

def biseccion(fx, inter, er, n):

    inter_a = inter[0] 
    inter_b = inter[1]
    it = 1 
    pnt_md_actual = 0 # punto medio actual
    pnt_md_anterior = 0 #punto medio anterior
    e = 1;

    if fx(inter_a) * fx(inter_b) < 0: #Sea menor a 0 hacer
        
        while (it < n) & (e > er):

            pnt_md_anterior = pnt_md_actual
            pnt_md_actual = (inter_a + inter_b) / 2 #se suma la tupla en la posicion a y b

            if fx( pnt_md_actual ) * fx( inter_b ) < 0:
                inter_a = pnt_md_actual
            else:
                inter_b = pnt_md_actual
            if it > 1:
                e = abs(pnt_md_actual - pnt_md_anterior / pnt_md_actual)
            it +=1 #incrementamos la iteracion

            #iteraciones
            print("\n")
            print(f"numero iteracion: {it}")
            print(f"punto medio actual: {pnt_md_actual}") 
            print(f"Error: {e}")

        return pnt_md_actual

if __name__ == "__main__":
    # Testing.

    # Datos.
    fx = lambda x: (x - 2)**2 - math.log(x)
    inter = (1, 2)
    er = 0.02
    n = 50

    biseccion(fx, inter, er, n)
