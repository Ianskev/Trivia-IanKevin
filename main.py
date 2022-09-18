import time
import random

rojo = "\033[31m";
azul = "\033[34m";
reset = "\033[0m";
verde = "\033[32m";
amarillo = "\033[33m";
negrita = "\033[1m";
puntaje = random.randint(1,15);
print(negrita+rojo+"Bienvenido/a a mi trivia sobre Historia Universal\n"+reset);
nombre = input("Ingresa tú nombre: ");
print("\nBienvenido/a " + nombre + ", estas son las reglas:\n");

print(azul+"A) Por cada respuesta correcta se te sumaran entre 1 y 10 puntos"+reset);
print(azul+"B) Por cada respuesta incorrecta se te restaran entre 1 y 5 puntos"+reset);
print(azul+"C) Todos empiezan con un puntaje aleatorio y puedes terminar con puntos negativos"+reset);
print(azul+"D) Hay una pregunta que tiene una clave escondida que te otorga 10 puntos sí es que la encuentras y respondes correctamente ¡SUERTE!\n"+reset);
print(negrita+"Tú puntaje actual es: "+str(puntaje)+reset);

print("\nResponde las preguntas escribiendo la letra de la alternativa que creas correcta y \"Enter\" para enviar tú respuesta\n");
time.sleep(5)

print(negrita+amarillo+"1) ¿Cuándo finalizo la Segunda Guerra Mundial?"+reset);
print("a) 1943");
print("b) 1948");
print("c) 1945");
print("d) 1944");

respuesta_1 = input("\nTu respuesta: ");
while (respuesta_1.lower() not in ("a", "b", "c", "d")):
    respuesta_1 = input("Ingrese una de las claves de la lista: ");
if (respuesta_1.lower() == "c"):
    print(negrita+verde+"\nDiste en el blanco! Efectivamente fue en 1945\n"+reset);
    puntaje += random.randint(1,10);
else:
    print(negrita+rojo+"\nRespuesta incorrecta, estuviste muy pero muy cerca, la respuesta era: 1945\n"+reset);
    puntaje-=random.randint(1,5);
time.sleep(4)

print(negrita+amarillo+"2) ¿Cómo se llamaban los gobernantes del antiguo Egipto?"+reset);
print("a) Faraones");
print("b) Basileos");
print("c) Alcaldes");
print("d) Cónsules");

respuesta_2 = input("\nTu respuesta: ");
while (respuesta_2.lower() not in ("a", "b", "c", "d", "x")):
    respuesta_2 = input("Ingrese una de las claves de la lista: ");
if (respuesta_2.lower() == "a"):
    print(negrita+verde+"\n¡Exacto! Eran los depositarios del derecho divino, se le atribuían todos los poderes por mediación de Horus\n"+reset);
    puntaje += random.randint(1,10);
elif(respuesta_2.lower() == "x"):
    print(negrita+verde+"\nFelicidades encontraste la clave secreta, para reclamar tús 10 puntos extras responde correctamente la pregunta actual"+reset)
    secreto = input("Tú respuesta: ")
    while (secreto.lower() not in ("a","b","c","d")):
        secreto = input("Ingrese una de las claves de la lista: ");
    if (secreto.lower() == "a"):
        print(negrita+verde+"\n¡Exacto! Eran los depositarios del derecho divino, se le atribuían todos los poderes por mediación de Horus"+reset);
        print(negrita+verde+"\nGANASTE LOS PUNTOS POR RESPONDER BIEN Y 10 PUNTOS EXTRAS POR ENCONTRAR LA CLAVE SECRETA\n"+reset)
        puntaje+=random.randint(1,10)+10
    else:
        print(negrita+rojo+"\nLamentablemente respondiste mal :( pero descuida no te bajaremos puntos esta vez, la respuesta era: Faraones\n"+reset)
        puntaje+=0
else:
    print(negrita+rojo+"\nBuen intento pero no le diste al blanco, la respuesta era: Faraones\n"+reset);
    puntaje-=random.randint(1,5);
time.sleep(4)

print(negrita+amarillo+"3) ¿Dónde y cuándo se inventó la pólvora?"+reset);
print("a) Estados Unidos - siglo XIX.");
print("b) China - siglo IX.");
print("c) Francia - siglo XVII");
print("d) Inglaterra - siglo X");

respuesta_3 = input("\nTu respuesta: ");
while (respuesta_3.lower() not in ("a","b", "c", "d")):
    respuesta_3 = input("Ingrese una de las claves de la lista: ");
if (respuesta_3.lower() == "b"):
    print(negrita+verde+"\n¡¿Estás haciendo trampa?? Porque es CORRECTO. La pólvora fue inventada en China cuando curanderos y químicos estaban buscando crear una medicina que diera la inmortalidad.\n"+reset);
    puntaje += random.randint(1,10);
else:
    print(negrita+rojo+"\nLamento decirte esto pero... la respuesta correcta era: China - siglo IX\n"+reset);
    puntaje-=random.randint(1,5);
time.sleep(4)

print(negrita+amarillo+"4) ¿Por cuál otro nombre se conoce el Imperio Romano de Oriente?"+reset);
print("a) Imperio Mongol");
print("b) Imperio Otomano");
print("c) Imperio Bizantino");
print("d) Sacro Imperio Romano");

respuesta_4 = input("\nTu respuesta: ");
while (respuesta_4.lower() not in ("a", "b", "c", "d")):
    respuesta_4 = input("Ingrese una de las claves de la lista: ");
if (respuesta_4.lower() == "c"):
    print(negrita+verde+"\n¡Wow eres un GENIO! La capital del Imperio Romano de Oriente se construyó sobre la antigua población de Bizancio(luego llamada Constantinopla)\n"+reset);
    puntaje += random.randint(1,10);
else:
    print(negrita+rojo+"\nMi culpa por dejar una pregunta tan dificil, la respuesta correcta era: Imperio Bizantino\n"+reset);
    puntaje-=random.randint(1,5);
time.sleep(4)

print(negrita+amarillo+"5) ¿Cuándo comenzó la Revolución Francesa?"+reset);
print("a) 1810");
print("b) 1914");
print("c) 1790");
print("d) 1789");

respuesta_5 = input("\nTu respuesta: ");
while (respuesta_5.lower() not in ("a", "b", "c", "d")):
    respuesta_5 = input("Ingrese una de las claves de la lista: ");
if (respuesta_5.lower() == "d"):
    print(negrita+verde+"\nLa revolución empezó el 5 de mayo de 1789 con los debates de los Estados Generales (Asamblea) y tuvo un fuerte impulso el 14 de julio de 1789, con la toma de la Bastilla.\n"+reset);
    puntaje += random.randint(1,10);
else:
    print(negrita+rojo+"\nBuen intento, sera para la proxima! La respuesta era: 1789\n"+reset);
    puntaje-=random.randint(1,5);
time.sleep(4)

print(negrita+verde+"Bueno " + nombre + ", muchas gracias por participar en mí Trivia, este es tu puntaje obtenido: " + str(puntaje)+reset);
if (puntaje <=7):
  print(negrita+rojo+"Recuerda que siempre puedes volver a intentarlo!"+reset);
elif (puntaje>=8 and puntaje <=20):
  print(negrita+amarillo+"Eres muy bueno/a pero puedes ser mejor"+reset);
else:
  print(negrita+verde+"Eres un genio/a de pies a cabeza"+reset);