import pyautogui
import keyboard


# Define as coordenadas para o duplo clique
x1, y1 = 1218, 909
x2, y2 = 959, 807


# Loop para executar os cliques
while True:
    # Define a função que será executada quando a tecla F11 for pressionada
    def on_f11_press():

        # Move o cursor do mouse para as coordenadas do primeiro clique
        pyautogui.moveTo(x1, y1)

        # Executa o duplo clique
        pyautogui.doubleClick(button='left')

        # Move o cursor do mouse para as coordenadas do segundo clique
        pyautogui.moveTo(x2, y2)

        # Executa o duplo clique
        pyautogui.doubleClick(button='left')


    # Adiciona o listener de teclado para aguardar a tecla F11 ser pressionada
    keyboard.add_hotkey("F11", lambda: on_f11_press())
    
    # Aguarda indefinidamente
    keyboard.wait()
