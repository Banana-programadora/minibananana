import minibanana as mb

mb.window("Test", 500, 500, "white")

jugador = mb.draw_sprite(100, 100, "basic_human.png")
laser = mb.draw_rect(200, 100, 25, 25, "red")
texto = mb.draw_text(300, 300, "TUTORIAL", 30, "black")

mb.get_keys()

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
mb.start(10)