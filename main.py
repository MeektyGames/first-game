import pygame
pygame.init()

#variables
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("game")
clock = pygame.time.Clock()
speed = 300
dt = 0

#player variables
player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)

#player functions
def draw_player():
    global radius
    global player_image
    global player_rect
    global player_circle

    radius = 40
    player_image = pygame.image.load('assets\images\chracters\player.png').convert_alpha()
    player_rect = player_image.get_rect()
    player_circle = pygame.draw.circle(screen, "pink", player_pos, radius)
    screen.blit(player_image, player_circle, player_rect)

def player_input():
    w = pygame.K_w
    s = pygame.K_s
    a = pygame.K_a
    d = pygame.K_d
    up = pygame.K_UP
    down = pygame.K_DOWN
    left = pygame.K_LEFT
    right = pygame.K_RIGHT

    keys = pygame.key.get_pressed()
    if keys[w] or keys[up]:
        player_pos.y -= speed * dt
    if keys[s] or keys[down]:
        player_pos.y += speed * dt
    if keys[a] or keys[left]:
        player_pos.x -= speed * dt
    if keys[d] or keys[right]:
        player_pos.x += speed * dt

def next_room():
    next_room = player_circle.right >= screen_width
    back_room = player_circle.left <= 0

    if next_room:
        print('next room')
        player_pos.x = 90

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("pink")

    draw_player()

    player_input()

    next_room()
    
    pygame.display.flip()

    dt = clock.tick(60) /1000

pygame.quit()