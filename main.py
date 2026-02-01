import pygame
import random
import sys

# Configuración inicial
pygame.init()
# USAMOS RESOLUCIÓN FIJA PARA QUE EL ROBOT NO SE LÍE
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores Neón
BLACK = (5, 5, 15)
NEON_BLUE = (0, 180, 255)
NEON_PINK = (255, 0, 120)
NEON_CYAN = (0, 255, 255)
GRID_COLOR = (20, 20, 40)

# Variables del juego - LAS DEFINIMOS DENTRO O CON NÚMEROS FIJOS
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_dir = "RIGHT"
food_pos = [400, 300] # Posición inicial fija para evitar errores
score = 0
clock = pygame.time.Clock()
start_pos = None

def show_score():
    font = pygame.font.SysFont('consolas', 40, bold=True)
    surface = font.render(f'SCORE: {score}', True, NEON_CYAN)
    screen.blit(surface, (20, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            
        if event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            dx = end_pos[0] - start_pos[0]
            dy = end_pos[1] - start_pos[1]
            if abs(dx) > abs(dy):
                if dx > 30 and snake_dir != "LEFT": snake_dir = "RIGHT"
                elif dx < -30 and snake_dir != "RIGHT": snake_dir = "LEFT"
            else:
                if dy > 30 and snake_dir != "UP": snake_dir = "DOWN"
                elif dy < -30 and snake_dir != "DOWN": snake_dir = "UP"
            start_pos = None

    # Lógica de movimiento
    if snake_dir == "UP": snake_pos[0][1] -= 10
    if snake_dir == "DOWN": snake_pos[0][1] += 10
    if snake_dir == "LEFT": snake_pos[0][0] -= 10
    if snake_dir == "RIGHT": snake_pos[0][0] += 10

    # Teletransporte
    if snake_pos[0][0] >= WIDTH: snake_pos[0][0] = 0
    if snake_pos[0][0] < 0: snake_pos[0][0] = WIDTH - 10
    if snake_pos[0][1] >= HEIGHT: snake_pos[0][1] = 0
    if snake_pos[0][1] < 0: snake_pos[0][1] = HEIGHT - 10

    # Crecimiento
    snake_pos.insert(0, list(snake_pos[0]))
    if snake_pos[0] == food_pos:
        score += 10
        food_pos = [random.randrange(1, 79) * 10, random.randrange(1, 59) * 10]
    else:
        snake_pos.pop()

    screen.fill(BLACK)
    pygame.draw.circle(screen, NEON_PINK, (food_pos[0]+5, food_pos[1]+5), 7)
    for pos in snake_pos:
        pygame.draw.rect(screen, NEON_BLUE, (pos[0], pos[1], 10, 10))
    
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            snake_pos = [[100, 50], [90, 50], [80, 50]]
            snake_dir = "RIGHT"
            score = 0

    show_score()
    pygame.display.flip()
    clock.tick(15)
