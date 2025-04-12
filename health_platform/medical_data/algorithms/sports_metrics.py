# Fórmulas de nutrición deportiva

# Función para obtener el nivel de actividad física
def obtener_nivel_actividad():
    """
    Solicita al usuario que ingrese un nivel de actividad física válido.
    :return: Nivel de actividad física elegido.
    """
    niveles_validos = ["sedentario", "ligero", "moderado", "intenso"]
    while True:
        nivel = input("Ingresa tu nivel de actividad física (sedentario, ligero, moderado, intenso): ").lower()
        if nivel in niveles_validos:
            return nivel
        else:
            print("Entrada inválida. Por favor, elige una opción válida.")

# Función para calcular el factor de actividad física
def calcular_factor_actividad(nivel_actividad_fisica):
    """
    Calcula el factor de actividad física según el nivel de actividad física.
    :param nivel_actividad_fisica: Nivel de actividad física (sedentario, ligero, moderado, intenso)
    :return: Factor de actividad física
    """
    factores = {
        "sedentario": 1,
        "ligero": 1.2,
        "moderado": 1.5,
        "intenso": 1.8
    }
    return factores.get(nivel_actividad_fisica, 1)

# Función para calcular las calorías diarias para un deportista
def calcular_calorias_diarias_deportista(peso, altura, edad, sexo, nivel_actividad_fisica):
    """
    Calcula las calorías diarias que necesita un deportista en función de su peso, altura, edad, sexo y nivel de actividad física.
    :param peso: Peso del deportista en kilogramos
    :param altura: Altura del deportista en metros
    :param edad: Edad del deportista en años
    :param sexo: Sexo del deportista (Hombre o Mujer)
    :param nivel_actividad_fisica: Nivel de actividad física del deportista (sedentario, ligero, moderado, intenso)
    :return: Número de calorías diarias que necesita el deportista
    """
    factor_actividad = calcular_factor_actividad(nivel_actividad_fisica)
    if sexo == "Hombre":
        bmr = 66 + (6.2 * peso) + (12.7 * altura * 100) - (6.8 * edad)
    elif sexo == "Mujer":
        bmr = 655 + (4.35 * peso) + (4.7 * altura * 100) - (4.7 * edad)
    else:
        raise ValueError("Sexo inválido. Debe ser 'Hombre' o 'Mujer'.")
    return bmr * factor_actividad

# Función para calcular las grasas diarias para un deportista
def calcular_grasas_diarias_deportista(peso, altura, edad, sexo, nivel_actividad_fisica):
    """
    Calcula las grasas diarias que necesita un deportista en función de su peso, altura, edad, sexo y nivel de actividad física.
    :param peso: Peso del deportista en kilogramos
    :param altura: Altura del deportista en metros
    :param edad: Edad del deportista en años
    :param sexo: Sexo del deportista (Hombre o Mujer)
    :param nivel_actividad_fisica: Nivel de actividad física del deportista (sedentario, ligero, moderado, intenso)
    :return: Número de grasas diarias que necesita el deportista
    """
    calorias_diarias = calcular_calorias_diarias_deportista(peso, altura, edad, sexo, nivel_actividad_fisica)
    return calorias_diarias * 0.3

# Función para calcular las proteínas diarias para un deportista
def calcular_proteinas_diarias_deportista(peso, altura, edad, sexo, nivel_actividad_fisica):
    """
    Calcula las proteínas diarias que necesita un deportista en función de su peso, altura, edad, sexo y nivel de actividad física.
    :param peso: Peso del deportista en kilogramos
    :param altura: Altura del deportista en metros
    :param edad: Edad del deportista en años
    :param sexo: Sexo del deportista (Hombre o Mujer)
    :param nivel_actividad_fisica: Nivel de actividad física del deportista (sedentario, ligero, moderado, intenso)
    :return: Número de proteínas diarias que necesita el deportista
    """                    
    calorias_diarias = calcular_calorias_diarias_deportista(peso, altura, edad, sexo, nivel_actividad_fisica)
    return calorias_diarias * 0.3   

# Función para calcular requerimientos proteinicos diarios en deportistas
def calcular_proteinas_diarias_deportista(peso):
     """
        Calcula las proteínas diarias que necesita un deportista en función de su peso corporal.
        :param peso: Peso del deportista en kilogramos
        :return: Número de proteínas diarias que necesita el deportista
     """
     return 1.2 * peso
    
# Función para calcular requerimientos grasos diarios en deportistas
def calcular_grasas_diarias_deportista(peso):
        """
        Calcula las grasas diarias que necesita un deportista en función de su peso corporal.
        :param peso: Peso del deportista en kilogramos
        :return: Número de grasas diarias que necesita el deportista
        """
        return 0.5 * peso       

# Función para calcular requerimientos carbohidratos diarios en deportistas
def calcular_carbohidratos_diarias_deportista(peso):
            """
            Calcula los carbohidratos diarios que necesita un deportista en función de su peso corporal.
            :param peso: Peso del deportista en kilogramos
            :return: Número de carbohidratos diarios que necesita el deportista
            """
            return 2 * peso

