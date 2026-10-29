#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Marvel Slayer"
FPS = 30

# Оbjetos
fon = Actor('fon')
enemy = Actor('spider_man', (400, 230), size=(120,140))
moon_knight = Actor('moon_knight', (280, 80), size=(135,150))
jeff = Actor('jeff', (450, 80), size=(85,140))
venom = Actor('venom', (220, 230), size=(120,140))
thor = Actor('thor', (400, 230), size=(75,140))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 200))
button_menu = Actor("bonus", (300, 280))
button_game = Actor("bonus", (300, 180))
button_gallery = Actor("bonus", (300, 280))
win = Actor('win')

# Coleção
button_menu_2 = Actor('bonus', (300, 350))
enemy_gallery = Actor('spider_man', (150, 80), size=(120,140))


# Variáveis
count = 0
damage = 1
hp = 50
price1 = 15
price2 = 200
mode = 'menu'

# Desenhando os gráficos
def draw():
    global hp, mode
    if mode == 'game':
        fon.draw()
        enemy.draw()
        screen.draw.text(hp, center=(400, 130), color="#DC143C", fontsize = 30, background="#FFE4B5")
        screen.draw.text(count, center=(570, 30), color="black", fontsize = 30)
        # Bônus
        bonus_1.draw()
        screen.draw.text("1 de dano a cada 2s", center=(100, 80), color="black", fontsize = 20)
        screen.draw.text(price1, center=(100, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("5 pontos a cada 2s", center=(100, 180), color="black", fontsize = 20)
        screen.draw.text(price2, center=(100, 210), color="black", fontsize = 20)
        # Escrevendo as condições
        if  hp <= 0 and enemy.image == 'spider_man':
            hp = 100
            enemy.image = 'moon_knight'
        elif hp <= 0 and enemy.image == 'moon_knight':
            hp = 200
            enemy.image = 'jeff'
        elif hp <= 0 and enemy.image == 'jeff':
            hp = 350
            enemy.image = 'venom'
        elif hp <= 0 and enemy.image == 'venom':
            hp = 500
            enemy.image = 'thor'
        # Janela de vitória
        elif hp <= 0 and enemy.image == 'thor':
            win.draw()
            screen.draw.text("Você derrotou todos os monstros!", center=(300, 100), color="white", fontsize = 24)
            button_menu.draw()
            screen.draw.text("Voltar ao menu", center=(300, 270), color="black", fontsize = 20)
    
    elif mode == 'menu':
        win.draw()
        # Botões do menu
        button_game.draw()
        screen.draw.text("Jogar", center=(300, 170), color="black", fontsize = 20)
        button_gallery.draw()
        screen.draw.text("Coleção", center=(300, 270), color="black", fontsize = 20)
    
    elif mode == 'collection':
        win.draw()
        # Coleção de monstros
        enemy_gallery.draw()
        moon_knight.draw()
        jeff.draw()
        venom.draw()
        thor.draw()
        button_menu_2.draw()
        screen.draw.text("Voltar ao menu", center=(300,350), color="black", fontsize=20)
# Funções dos bônus
def for_bonus_1():
    global hp, count
    hp -= 1
    count += 1

def for_bonus_2():
    global count
    count += 5


# Processando os cliques
def on_mouse_down(button, pos):
    global count, damage, hp, price1, price2, mode
    if button == mouse.LEFT:
        # Clicando nos objetos
        if enemy.collidepoint(pos) and mode == 'game':
            count += 1
            hp -= damage
            enemy.y = 200
            animate(enemy, tween='bounce_end', duration=0.5, y=230)
        # Clicando no botão do bonus_1    
        elif bonus_1.collidepoint(pos):
            if count >= price1:
                schedule_interval(for_bonus_1, 1)
                count -= price1
                price1 *= 2
        # Clicando no botão do bonus_2
        elif bonus_2.collidepoint(pos):
            if count >= price2:
                schedule_interval(for_bonus_2, 3)
                count -= price2
                price2 *= 2 
        
        # Clicando no botão 'Jogar'
        elif button_game.collidepoint(pos):
            mode = 'game'
            
        # Clicando no botão 'Coleção'
        elif button_gallery.collidepoint(pos):
            mode = 'collection'
        # Clicando no botão 'Voltar ao menu'
        elif button_menu.collidepoint(pos):
            mode = 'menu'
        elif button_menu_2.collidepoint(pos):
            mode = 'menu'
