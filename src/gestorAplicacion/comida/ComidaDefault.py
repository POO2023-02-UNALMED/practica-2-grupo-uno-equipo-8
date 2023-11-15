class ComidaDefault:
    """
    Interfaz que define las tarifas y métodos por defecto para una comida.
    """

    # Tarifa por defecto para el servicio a domicilio.
    tarifa_domicilio = 2000

    # Tarifa por defecto para las ganancias.
    tarifa_ganancias = 1.7

    # Tarifa por defecto para los impuestos.
    tarifa_impuestos = 0.19

    def get_descripcion(self):
        """
        Obtiene la descripción por defecto de la comida.
        """
        return "Ahora mismo no tenemos una descripcion para este producto, pero te invitamos a probarlo."

    def get_nutrientes(self, nombre):
        """
        Obtiene la información nutricional por porción de la comida.
        :param nombre: El nombre de la comida.
        :return: La información nutricional por porción de la comida.
        """
        m = (
            " _______________________________________________________ \n"
            f"|{'Producto: ' + nombre.center(48 - len(nombre))} |\n"
            "| Porcion: 30 g                                         |\n"
            "|_______________________________________________________| \n"
            "| Informacion nutricional por porcion                   |\n"
            "|______________________ ________ _______________________| \n"
            "| Energia              | 140 kcal| 7%% del valor diario  |\n"
            "|______________________ ________ _______________________|\n"
            "| Grasa total          | 6 g     | 9%% del valor diario  |\n"
            "| _ Grasa saturada     | 3 g     | 15%% del valor diario |\n"
            "| _ Grasa trans        | 0 g     |                      |\n"
            "|______________________ ________ _______________________| \n"
            "| Colesterol           | 0 mg    | 0%% del valor diario  |\n"
            "|______________________ ________ _______________________| \n"
            "| Sodio                | 75 mg   | 3%% del valor diario  |\n"
            "|______________________ ________ _______________________| \n"
            "| Carbohidratos totales| 20 g    | 7%% del valor diario  |\n"
            "| _ Fibra dietetica    | 1 g     | 4%% del valor diario  |\n"
            "| _ Azucares           | 10 g    |                      |\n"
            "|______________________ ________ _______________________| \n"
            "| Proteina             | 2 g     |                      |\n"
            "|______________________ ________ _______________________| \n"
            "| Vitamina A           | 0%% del valor diario            |\n"
            "| Vitamina C           | 0%% del valor diario            |\n"
            "| Calcio               | 2%% del valor diario            |\n"
            "| Hierro               | 6%% del valor diario            |\n"
            "|_______________________________________________________| \n"
        )
        return m