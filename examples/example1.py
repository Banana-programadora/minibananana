import minibanana as mb

mb.window("Test", 500, 500, "white")

jugador = mb.draw_sprite(100, 100, "basic_human.png") #POSICION X, POSICION Y, ARCHIVO DE LA IMAGEN
laser = mb.draw_rect(200, 100, 25, 25, "red") #POSICION X, POSICION Y, TAMAÑO X, TAMAÑO Y, COLOR
texto = mb.draw_text(300, 300, "TUTORIAL", 30, "black"), #POSICION X, POSICION Y, TEXTO, TAMAÑO DE LETRA, COLOR, FUENTE

mb.get_keys() #DETECTA LEFT, RIGHT, UP Y DOWN

def logica():
    if mb.is_key_pressed("Left"):
        jugador["x"] -= 5
    if mb.is_key_pressed("Right"):
        jugador["x"] += 5
    if mb.is_key_pressed("Up"):
        jugador["y"] -= 5
    if mb.is_key_pressed("Down"):
        jugador["y"] += 5
    if mb.colliderect(jugador, laser):
        quit()

mb.set_logic(logica)
mb.start(10) # 10 REPRESENTA LOS MS POR FRAME, UN 16 SON UNOS 60 FPS
