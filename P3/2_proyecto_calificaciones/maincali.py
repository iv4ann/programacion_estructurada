import calificaciones

def main():
    datos = []

    opcion=True

    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menuPrincipal()

        match opcion:
            case "1":
                calificaciones.agregar_calif()
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrar_calif()
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcular_prom_calif()
                calificaciones.espereTecla()
            case "4":
                print("\n\t\t \U0001F6AATerminaste la ejecución del Sistema ... Gracias ...\U0001F6AA")
                opcion = False
            case _:
                print("\n\t\t \u274COpción Invalida, intenta de nuevo ...\u274C")
                opcion = True
                calificaciones.espereTecla()

if __name__=="__main__":
    main()