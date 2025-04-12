# Importar librerías necesarias
import math

# Antropometría básica e índices

# Indice de Masa Corporal (IMC) | peso en kg y altura en metros
def clasificar_IMC(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("El peso y la altura deben ser mayores a cero.")
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {round(imc, 2)} - Bajo peso"
    elif imc < 24.9:
        return f"IMC: {round(imc, 2)} - Normal"
    elif imc < 29.9:
        return f"IMC: {round(imc, 2)} - Sobrepeso"
    else:
        return f"IMC: {round(imc, 2)} - Obesidad"


# Peso Ideal Teórico 

# Fórmula de Broca | talla en m
def peso_broca(altura):
   if altura <= 0:
        raise ValueError("La altura debe ser mayor a cero.")
   peso_teorico_broca = (altura - 1) * 100
   return round(peso_teorico_broca, 2)


# Fórmula de Lorentz
def peso_lorentz(sexo, altura):
    if altura <= 0:
        raise ValueError("La altura debe ser mayor a cero.")
    
    if sexo == "Masculino":
        peso_teorico_lorentz = altura - 1 - ((altura - 1.5) / 4)
    elif sexo == "Femenino":
        peso_teorico_lorentz = altura - 1 - ((altura - 1.5) / 2)
    else:
        raise ValueError("Sexo inválido. Use 'Masculino' o 'Femenino'.")
    
    return round((peso_teorico_lorentz * 100), 2)

# Peso ajustado con peso ideal de Broca

def peso_ajustado(peso_actual, altura, factor_ajuste):
    # Función anidada
    def peso_broca(altura):
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero.")
        return round((altura - 1) * 100, 2)
    
    # Llamada a la función anidada
    peso_teorico_broca = peso_broca(altura)
    
    # Cálculo del peso ajustado
    peso_ajustado = ((peso_actual - peso_teorico_broca) * factor_ajuste) + peso_teorico_broca
    return round(peso_ajustado, 2)

# Índice Cintura-Cadera (cm)
def indice_cintura_cadera(circunferencia_cintura, circunferencia_cadera):
    if circunferencia_cintura <= 0 or circunferencia_cadera <= 0:
        raise ValueError("Los valores deben ser mayores a cero.")
    icc = circunferencia_cintura / circunferencia_cadera
    return round(icc, 2)  


# Calculo de Composición Corporal
# Conversión de unidades
def cm_a_pulgadas(cm):
    return cm / 2.54

# Fórmula para cálculo de Composición corporal
def composicion_corporal(sexo, peso, altura_cm, cintura_cm, cadera_cm, cuello_cm, abdomen_cm=None):
    """
    Calcula múltiples métricas corporales a partir de medidas en centímetros y peso en kg.
    
    Args:
        sexo (str): 'Masculino' o 'Femenino'
        peso (float): Peso corporal en kilogramos
        altura_cm (float): Altura en centímetros
        cintura_cm (float): Circunferencia de cintura en cm
        cadera_cm (float): Circunferencia de cadera en cm
        cuello_cm (float): Circunferencia de cuello en cm
        abdomen_cm (float): [Solo Mujeres] Circunferencia de abdomen en cm
    
    Returns:
        dict: Diccionario con las métricas calculadas
    """
    
    # Validaciones básicas
    if peso <= 0 or altura_cm <= 0 or cintura_cm <= 0 or cadera_cm <= 0 or cuello_cm <= 0:
        raise ValueError("Todos los valores numéricos deben ser mayores a cero.")
    
    if sexo not in ["Masculino", "Femenino"]:
        raise ValueError("El sexo debe ser 'Masculino' o 'Femenino'")
    
    # Conversión a pulgadas para fórmulas US Navy
    altura_pulg = cm_a_pulgadas(altura_cm)
    cuello_pulg = cm_a_pulgadas(cuello_cm)
    
    # Cálculo Índice Cintura-Cadera (ICC)
    icc = cintura_cm / cadera_cm
    
    # Cálculo Porcentaje de Grasa Corporal
    if sexo == "Masculino":
        abdomen_pulg = cm_a_pulgadas(cintura_cm)  # En hombres se usa la cintura como abdomen
        if abdomen_pulg <= cuello_pulg:
            raise ValueError("La circunferencia de cintura debe ser mayor que la del cuello en hombres.")
        
        grasa_corporal = 86.010 * math.log10(abdomen_pulg - cuello_pulg) - 70.041 * math.log10(altura_pulg) + 36.76
    
    else:  # Femenino
        if abdomen_cm is None or abdomen_cm <= 0:
            raise ValueError("En mujeres se requiere la circunferencia de abdomen.")
        
        abdomen_pulg = cm_a_pulgadas(abdomen_cm)
        cadera_pulg = cm_a_pulgadas(cadera_cm)
        suma = abdomen_pulg + cadera_pulg - cuello_pulg
        
        if suma <= 0:
            raise ValueError("Abdomen + cadera - cuello debe ser mayor a cero.")
        
        grasa_corporal = 163.205 * math.log10(suma) - 97.684 * math.log10(altura_pulg) - 78.387
    
    # Cálculo de masas
    masa_grasa = (grasa_corporal / 100) * peso
    masa_magra = peso - masa_grasa
    
    return {
        'Porcentaje Grasa': round(grasa_corporal, 2),
        'ICC': round(icc, 2),
        'Masa Grasa (kg)': round(masa_grasa, 2),
        'Masa Magra (kg)': round(masa_magra, 2)
    }

# Ejemplo de uso
resultado = composicion_corporal(
    sexo = "Femenino",
    peso = 65,
    altura_cm = 165,
    cintura_cm = 80,
    cadera_cm = 95,
    cuello_cm = 35,
    abdomen_cm = 85  # Requerido solo en mujeres
)

