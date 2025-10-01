import tkinter as tk
import winsound

root = None
canvas = None
logic = None  

sprites = []

keys = {
    "Left": False,
    "Right": False,
    "Up": False,
    "Down": False
}

def window(title : str, width : int, height : int, bg="black", resizable : bool=False):
    global root, canvas

    root = tk.Tk()
    root.title(title)        
    root.geometry(f"{str(width)}x{(str(height))}")
    root.resizable(resizable, resizable)
    root.focus_set()
    canvas = tk.Canvas(root, width=width, height=height, bg=bg)
    canvas.pack()

    return root, canvas

def draw_sprite(x : int, y : int, image_path):

    sprite = {
        "x" : x,
        "y" : y,
        "width" : 0,
        "height" : 0,
        "color" : None,
        "type" : "image"
    }

    sprite["image"] = tk.PhotoImage(file=image_path)
    sprite["width"] = sprite["image"].width()
    sprite["height"] = sprite["image"].height()

    sprites.append(sprite)
    return sprite

def draw_rect(x : int, y : int, width : int, height : int, color):
    sprite = {"x": x, "y": y, "width": width, "height": height, "color": color, "image" : None, "type" : "rect"}
    sprites.append(sprite)
    return sprite

def draw_text(x : int, y : int, text : str, size : int = 20, color="white", font : str ="Arial"):
    sprite = {
        "x": x,
        "y": y,
        "text": text,
        "size": size,
        "color": color,
        "font": font,
        "type": "text"
    }
    sprites.append(sprite) 
    return sprite 

def colliderect(sprite1, sprite2):
    x1, y1, w1, h1 = sprite1["x"], sprite1["y"], sprite1["width"], sprite1["height"]
    x2, y2, w2, h2 = sprite2["x"], sprite2["y"], sprite2["width"], sprite2["height"]
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2)

def get_keys():
    def tecla_presionada(event):
        keys[event.keysym] = True

    def tecla_suelta(event):
        keys[event.keysym] = False

    root.bind("<KeyPress>", tecla_presionada)
    root.bind("<KeyRelease>", tecla_suelta)

def is_key_pressed(key):
    return keys.get(key, False)

def set_logic(func):
    global logic
    logic = func

def update(ms=16):
    global root, canvas, logic

    if logic != None:
        logic()

    canvas.delete("all")

    for sprite in sprites:
        if sprite.get("image") is not None:  
            canvas.create_image(sprite["x"], sprite["y"], anchor="nw", image=sprite["image"])
        elif sprite["type"] == "text":
            canvas.create_text(
                sprite["x"], sprite["y"],
                text=sprite["text"],
                fill=sprite["color"],
                font=(sprite["font"], sprite["size"]),
                anchor="nw"
            )
        else:
            canvas.create_rectangle(
                sprite["x"], sprite["y"],
                sprite["x"] + sprite["width"],
                sprite["y"] + sprite["height"],
                fill=sprite["color"],
                outline=""
            )

    root.after(ms, update)

def start(ms):
    global root
    update(ms)
    root.mainloop()

def play_sound(path):
    winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_sound():
    winsound.PlaySound(None, winsound.SND_PURGE)