import os

import pygame
import random
import sys

WIDTH = 800
HEIGHT = 900
FPS = 144 # khung hinh tren giay

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ground_y = 700

# Hàm chương trình
def VeNen():
    screen.blit(fl, (x_pos, 700))
    screen.blit(fl, (x_pos + 800, 700))
def creat_pipes():
    random_piles = random.choice(height_random)
    bottom_piles = piles_surface.get_rect(midtop=(900, random_piles))
    top_piles = piles_surface.get_rect(midtop = (900, random_piles - 750 ))
    return bottom_piles, top_piles
def piles_movement(piles):
    for pile in piles:
        pile.centerx -= 5
    return piles
def draw_piles(piles):
    for pile in piles:
        if pile.bottom >= 700:
            screen.blit(piles_surface, pile)
        else:
            flip_piles = pygame.transform.flip(piles_surface, False, True)
            screen.blit(flip_piles, pile)
def VACHAM(piles):
    for pile in piles:
        if bird_rect.colliderect(pile):
            music_hit_path.play()
            return False
        if bird_rect.centery < -50 or bird_rect.centery >750:
            return False
    return True
def Bird_Rotate(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement*3, 1.5)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return  new_bird, new_bird_rect
def score_display(game_state):
    if game_state == 'Main game':
        score_surface = game_font.render('Score ', True, (255, 255, 255))
        score_surface2 = game_font2.render(str(int(score)), True, (255,255,255))
        score_rect = score_surface.get_rect(center=(70, 30))
        score_rect2 = score_surface2.get_rect(center=(140, 30))
        screen.blit(score_surface, score_rect)
        screen.blit(score_surface2, score_rect2)
    if game_state == 'Game over':
        score_surface = game_font.render('Score ', True, (255, 255, 255))
        score_surface2 = game_font2.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(400, 30))
        score_rect2 = score_surface2.get_rect(center=(470, 30))
        screen.blit(score_surface, score_rect)
        screen.blit(score_surface2, score_rect2)

        high_score_surface = game_font.render('High score ', True, (255, 255, 255))
        high_score_surface2 = game_font2.render(str(int(Highest_score)), True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center=(390, 550))
        high_score_rect2 = score_surface2.get_rect(center=(410, 600))
        screen.blit(high_score_surface, high_score_rect)
        screen.blit(high_score_surface2, high_score_rect2)
def auto_update_HS(score, high_score):
    if score > high_score:
        high_score = score
    return high_score
# Cài đặt cơ bản
pygame.mixer.init(frequency= 44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump King By Kien")
clock = pygame.time.Clock()
game_font = pygame.font.Font(r"D:\Python\GameMaking\BEECH___.TTF", 40)
game_font2 = pygame.font.Font(r"D:\Python\GameMaking\BEECH___.TTF", 30)
# insert ảnh
bg = pygame.image.load(r"C:\Users\nguye\Downloads\Jennie.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

fl = pygame.image.load(r"E:\Pycharm\FileGame\assets\floor.png")
fl = pygame.transform.scale(fl, (WIDTH, 200))

bird = pygame.image.load(r"E:\Pycharm\FileGame\assets\yellowbird-midflap.png").convert_alpha()
bird = pygame.transform.scale2x(bird)
upfrag_bird = pygame.transform.scale2x(pygame.image.load(r"E:\Pycharm\FileGame\assets\yellowbird-upflap.png")).convert_alpha()
downfrag_bird = pygame.transform.scale2x(pygame.image.load(r"E:\Pycharm\FileGame\assets\yellowbird-downflap.png")).convert_alpha()
bird_list = [bird, upfrag_bird, downfrag_bird]
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center=(100, 450))
#TẠO MÀN HÌNH KẾT THÚC:
game_over_surface = pygame.transform.scale2x(pygame.image.load(r"E:\Pycharm\FileGame\assets\message.png"))
game_over_surface_rect = game_over_surface.get_rect(center = (400,280))
#Tạo âm thanh
music_wing_path = pygame.mixer.Sound(r"E:\Pycharm\FileGame\sound\sfx_wing.wav")
music_hit_path = pygame.mixer.Sound(r"E:\Pycharm\FileGame\sound\sfx_hit.wav")
music_die_path = pygame.mixer.Sound(r"E:\Pycharm\FileGame\sound\sfx_die.wav")
piles_surface = pygame.image.load(r"E:\Pycharm\FileGame\assets\pipe-green.png")
piles_surface = pygame.transform.scale2x(piles_surface)
# cài đặt cơ bản 2
game_active = True
x_pos = 0
bird_movement = 0
gravity = 0.1
score = 0
Highest_score = 0
piles_list = []
height_random = [300, 350, 400, 450, 500]
#tạo event
spawn_piles = pygame.USEREVENT
pygame.time.set_timer(spawn_piles, 800)
bird_frag = pygame.USEREVENT + 1
pygame.time.set_timer(bird_frag, 100)

# chương trình chạy
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 4
                music_wing_path.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                piles_list.clear()
                bird_rect = bird.get_rect(center=(100, 450))
                bird_movement = 0
                score = 0
        if event.type == spawn_piles:
            piles_list.extend(creat_pipes())
            print(creat_pipes())
        if event.type == bird_frag:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()

# ảnh nền
    screen.blit(bg, (0, 0))

    if game_active:
    # Vẽ cột
        piles_list = piles_movement(piles_list)
        draw_piles(piles_list)
        x_pos -= 1
    # chim
        game_active = VACHAM(piles_list)
        rotate_bird = Bird_Rotate(bird)
        screen.blit(rotate_bird, bird_rect)
        bird_movement += gravity
        bird_rect.centery += bird_movement
        score_display('Main game')
        score += 0.0065
    else:
        screen.blit(game_over_surface, game_over_surface_rect)
        Highest_score = auto_update_HS(score, Highest_score)
        score_display('Game over')

# vẽ mặt đất
    VeNen()
    if x_pos == -800:
        x_pos = 0


    pygame.display.flip()
pygame.quit()