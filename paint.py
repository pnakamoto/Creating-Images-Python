import numpy as np
import matplotlib.pyplot as plt

# Define o tamanho da imagem
altura, largura = 500, 500
canvas = np.zeros((altura, largura))

# Número de manchas (blobs) a serem adicionadas
num_mancha = 1000

# Loop para criar várias manchas gaussianas
for _ in range(num_mancha):
    # Escolhe aleatoriamente a posição da mancha
    x0 = np.random.randint(0, largura)
    y0 = np.random.randint(0, altura)
    # Define o desvio padrão (tamanho) e a intensidade da mancha
    sigma = np.random.uniform(5, 30)
    amplitude = np.random.uniform(0.5, 1.5)

    # Cria uma malha de coordenadas para toda a imagem
    x = np.arange(largura)
    y = np.arange(altura)
    X, Y = np.meshgrid(x, y)

    # Calcula a distribuição gaussiana centrada em (x0, y0)
    gauss = amplitude * np.exp(-((X - x0)**2 + (Y - y0)**2) / (2 * sigma**2))
    # Adiciona a mancha ao canvas
    canvas += gauss

# Normaliza os valores da imagem para o intervalo [0, 1]
canvas = canvas - canvas.min()
canvas = canvas / canvas.max()

# Exibe a imagem com uma coloração que remete a tons de fogo/galáxia
plt.figure(figsize=(6,6))
plt.imshow(canvas, cmap='inferno')
plt.axis('off')
plt.show()
##################################################################################

import numpy as np
import matplotlib.pyplot as plt

# Dimensões da imagem
H, W = 500, 500

# Cria o fundo com um degradê de azul:
# Do topo (cor clara – sky blue) para a base (tom mais escuro – steel blue)
top_color = np.array([0.53, 0.81, 0.92])    # Sky blue (aproximado)
bottom_color = np.array([0.27, 0.51, 0.71]) # Steel blue (aproximado)
canvas = np.zeros((H, W, 3))
for i in range(H):
    t = i / (H - 1)
    canvas[i, :] = top_color * (1 - t) + bottom_color * t

# Adiciona nuvens: manchas gaussianas em branco
num_clouds = 30  # número de nuvens
x = np.arange(W)
y = np.arange(H)
X, Y = np.meshgrid(x, y)
for _ in range(num_clouds):
    # Centro aleatório para a nuvem (preferencialmente na parte superior)
    cx = np.random.randint(0, W)
    cy = np.random.randint(0, H // 2)
    sigma = np.random.uniform(20, 50)
    amplitude = np.random.uniform(0.3, 0.7)

    # Cria a "nuvem" usando uma função gaussiana
    cloud = amplitude * np.exp(-(((X - cx)**2 + (Y - cy)**2) / (2 * sigma**2)))

    # Adiciona a nuvem aos canais R, G e B (branco)
    canvas[:, :, 0] += cloud
    canvas[:, :, 1] += cloud
    canvas[:, :, 2] += cloud

# Garante que os valores estejam no intervalo [0, 1]
canvas = np.clip(canvas, 0, 1)

plt.figure(figsize=(6, 6))
plt.imshow(canvas)
plt.axis('off')
plt.title("Céu com Nuvens", fontsize=16)
plt.show()

#####################################################################################

import numpy as np
import matplotlib.pyplot as plt
import random

def scene_sky():
    # Céu com nuvens: fundo degradê de azul com manchas gaussianas que simulam nuvens.
    H, W = 500, 500
    # Definindo cores para o fundo
    top_color = np.array([0.53, 0.81, 0.92])    # azul-claro (sky blue)
    bottom_color = np.array([0.27, 0.51, 0.71]) # azul-acinzentado (steel blue)
    canvas = np.zeros((H, W, 3))
    for i in range(H):
        t = i / (H - 1)
        canvas[i, :] = top_color*(1-t) + bottom_color*t

    # Adiciona nuvens na metade superior da imagem
    num_clouds = random.randint(20, 40)
    x = np.arange(W)
    y = np.arange(H)
    X, Y = np.meshgrid(x, y)
    for _ in range(num_clouds):
        cx = np.random.randint(0, W)
        cy = np.random.randint(0, H//2)
        sigma = np.random.uniform(20, 50)
        amplitude = np.random.uniform(0.3, 0.7)
        cloud = amplitude * np.exp(-(((X-cx)**2 + (Y-cy)**2) / (2*sigma**2)))
        # Adiciona a nuvem aos três canais (resultando em branco)
        canvas[:, :, 0] += cloud
        canvas[:, :, 1] += cloud
        canvas[:, :, 2] += cloud

    canvas = np.clip(canvas, 0, 1)
    plt.imshow(canvas)
    plt.title("Céu com Nuvens", fontsize=16)
    plt.axis('off')
    plt.show()

def scene_galaxy():
    # Galáxia abstrata: fundo preto com um brilho radial no centro e estrelas espalhadas.
    H, W = 500, 500
    canvas = np.zeros((H, W, 3))

    # Cria um brilho radial (glow) com centro ligeiramente deslocado
    y = np.linspace(0, H-1, H)
    x = np.linspace(0, W-1, W)
    X, Y = np.meshgrid(x, y)
    center = (W/2 + np.random.uniform(-20,20), H/2 + np.random.uniform(-20,20))
    distance = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
    sigma = np.random.uniform(50, 100)
    glow = np.exp(-distance**2 / (2 * sigma**2))

    # Escolhe uma cor para o brilho (tons que lembram galáxias)
    color_choice = random.choice([
        np.array([0.8, 0.5, 1.0]),
        np.array([0.5, 0.8, 1.0]),
        np.array([1.0, 0.8, 0.5])
    ])
    for c in range(3):
        canvas[:,:,c] += glow * color_choice[c]

    # Adiciona estrelas brancas aleatórias
    num_stars = random.randint(300, 600)
    for _ in range(num_stars):
        star_x = np.random.randint(0, W)
        star_y = np.random.randint(0, H)
        brightness = np.random.uniform(0.8, 1.0)
        size = random.choice([1, 2])
        if size == 1:
            canvas[star_y, star_x, :] = brightness
        else:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if 0 <= star_y+dy < H and 0 <= star_x+dx < W:
                        canvas[star_y+dy, star_x+dx, :] = brightness

    canvas = np.clip(canvas, 0, 1)
    plt.imshow(canvas)
    plt.title("Galáxia Abstrata", fontsize=16)
    plt.axis('off')
    plt.show()

def scene_mountains():
    # Montanhas abstratas: céu degradê com uma silhueta de montanhas formada por uma função senoidal com ruído.
    H, W = 500, 500
    # Fundo: degradê do azul claro ao azul escuro
    top_color = np.array([0.7, 0.85, 1.0])
    bottom_color = np.array([0.4, 0.6, 0.8])
    canvas = np.zeros((H, W, 3))
    for i in range(H):
        t = i / (H - 1)
        canvas[i, :] = top_color*(1-t) + bottom_color*t

    # Gera a silhueta das montanhas usando uma combinação de seno e ruído
    x = np.linspace(0, 4*np.pi, W)
    mountain = 200 + 50*np.sin(x + np.random.uniform(0, 2*np.pi)) + 30*np.random.randn(W)
    mountain = np.clip(mountain, 0, H).astype(int)
    # Preenche a área abaixo da curva com uma cor escura (silhueta)
    for i in range(W):
        y_val = mountain[i]
        canvas[y_val:H, i, :] = np.array([0.2, 0.2, 0.2])

    plt.imshow(canvas)
    plt.title("Montanhas Abstratas", fontsize=16)
    plt.axis('off')
    plt.show()

# Escolhe aleatoriamente um dos cenários
scenes = [scene_sky, scene_galaxy, scene_mountains]
random.choice(scenes)()
