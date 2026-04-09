import random

def trivia():
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "respuesta": "París"
        },
        {
            "pregunta": "¿En qué año llegó Cristóbal Colón a América?",
            "respuesta": "1492"
        }
    ]

    pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
    respuesta = input(f"{preguntas[pregunta_aleatoria]['pregunta']}\n")

    if respuesta.lower() == preguntas[pregunta_aleatoria]['respuesta'].lower():
        print("¡FELICIDADES! Ganaste el juego")
        return False
    else:
        print("Upsi, sigue intentando")
        return True


juega = True

nombre = input("¿Cuál es tu nombre? \n")

print(f"¡Hola {nombre}! Bienvenido a la trivia, te daremos una serie de preguntas, si contestas una de ellas correctamente ganas el juego.\n¡COMENCEMOS!")

while juega:
    juega = trivia()

print("Gracias por jugar, ¡hasta la próxima!")

