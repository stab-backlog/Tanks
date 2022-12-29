import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, start_cords, color, k, k_names, info_lst, start_key, player, hp_amount):
        pygame.sprite.Sprite.__init__(self)
        self.start_cords = start_cords
        self.k = k
        self.k_names = k_names
        self.info_lst = info_lst
        self.start_key = start_key
        self.player = player
        self.hp = hp_amount
        self.rect_size = 25, 25
        self.image = pygame.Surface(self.rect_size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.start_cords

    def action(self, keys):
        if self.hp == 0:
            global run
            run = False

        self.rect.move_ip(
            (keys[self.k[0]] - keys[self.k[1]]) * player_speed,
            (keys[self.k[2]] - keys[self.k[3]]) * player_speed)

        if pygame.sprite.spritecollideany(self, bricks):
            self.rect.move_ip(
                -(keys[self.k[0]] - keys[self.k[1]]) * player_speed,
                -(keys[self.k[2]] - keys[self.k[3]]) * player_speed)

        if pygame.sprite.spritecollideany(self, bullets_2 if self.player == 1 else bullets_1):
            self.hp -= 1
            self.rect.x, self.rect.y = self.start_cords

        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

        if keys[self.k[4]]:

            global next_bullet_time

            if len(bullets_list[self.player]) < max_bullets and current_time >= next_bullet_time[-self.player]:

                info = self.start_key

                if not (len(self.info_lst) == 1 and self.info_lst[0] == self.k_names[4]):
                    for btn in range(len(self.info_lst) - 1, 0, -1):
                        if self.info_lst[btn] == self.k_names[4]:
                            info = self.info_lst[btn - 1]
                            break

                if info == self.k_names[0]:
                    x, y = self.rect.midright
                    direction = 0

                elif info == self.k_names[1]:
                    x, y = self.rect.midleft
                    direction = 2

                elif info == self.k_names[2]:
                    x, y = self.rect.midtop
                    direction = 3

                elif info == self.k_names[3]:
                    x, y = self.rect.midbottom
                    direction = 1

                else:
                    assert False, self.info_lst

                next_bullet_time[-self.player] = current_time + bullet_delta_time
                bullet = Bullet(x, y, self.player, direction)
                if self.player == 1:
                    bullets_1.add(bullet)
                    bullets_list[1].append(bullet)
                if self.player == 2:
                    bullets_2.add(bullet)
                    bullets_list[2].append(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, player, direction=0):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.direction = direction
        self.cords = x, y
        self.rect_size = 5, 5
        self.image = pygame.Surface(self.rect_size)
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.center = self.cords

    def move(self):
        x, y = None, None
        if self.direction == 0:
            self.rect.move_ip(bullet_speed, 0)
            x, y = self.rect.midleft

        elif self.direction == 1:
            self.rect.move_ip(0, bullet_speed)
            x, y = self.rect.midbottom

        elif self.direction == 2:
            self.rect.move_ip(-bullet_speed, 0)
            x, y = self.rect.midright

        elif self.direction == 3:
            self.rect.move_ip(0, -bullet_speed)
            x, y = self.rect.midtop

        # self.rect.clamp_ip(pygame.display.get_surface().get_rect())

        display_rect = pygame.display.get_surface().get_rect()

        if (x < display_rect[0] or x > display_rect[2]) or (y < display_rect[1] or y > display_rect[3]) or \
                pygame.sprite.spritecollideany(self, bricks):
            self.kill()
            bullets_list[self.player].remove(self)


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, rect_x, rect_y, wall_size):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.x, self.y = rect_x, rect_y
        self.rect_size = wall_size
        self.image = pygame.Surface(self.rect_size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y


board = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', ],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', ],
]


fps = 60

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

players = pygame.sprite.Group()
players_list = []

bullets_1 = pygame.sprite.Group()
bullets_2 = pygame.sprite.Group()

bullets_list = {
    1: [],
    2: [],
}

bricks = pygame.sprite.Group()
bricks_list = []

for board_y in range(len(board)):
    for board_x in range(len(board[board_y])):
        if board[board_y][board_x] == '1':
            brick = Wall('blue', board_x * 25, board_y * 25, (25, 25))
            bricks.add(brick)
            bricks_list.append(brick)

# length = (None, None)

first_info_direction_list = []
second_info_direction_list = []

info_direction_list = [first_info_direction_list, second_info_direction_list]

first_help_list = [[pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP, pygame.K_SPACE],
                   ['right', 'left', 'up', 'down', 'space'], 'right']
second_help_list = [[pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w, pygame.K_g],
                    ['d', 'a', 'w', 's', 'g'], 'a']

player_1 = Player((25, 25), 'red', first_help_list[0], first_help_list[1], first_info_direction_list,
                  first_help_list[2], 1, 3)
player_2 = Player((450, 450), 'green', second_help_list[0], second_help_list[1], second_info_direction_list,
                  second_help_list[2], 2, 3)

players.add(player_1, player_2)
players_list.append(player_1)
players_list.append(player_2)

player_speed = 5
bullet_speed = 10

max_bullets = 3
next_bullet_time = [0, 0]
bullet_delta_time = 100

run = True
while run:

    clock.tick(fps)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name in first_help_list[1]:
                first_info_direction_list.append(key_name)
            if key_name in second_help_list[1]:
                second_info_direction_list.append(key_name)

    key = pygame.key.get_pressed()

    for lst in info_direction_list:
        if lst:
            for i in range(len(lst) - 1, 0, -1):
                if lst[i] == lst[i - 1]:
                    del lst[i]

    for lst_len in info_direction_list:
        if len(lst_len) > 20:
            for lst_index in range(len(lst_len) - 1, -1, -1):
                if lst_len[lst_index] in ['g', 'space']:
                    last_key_1 = lst_len[lst_index]
                    last_key_2 = lst_len[lst_index - 1]
                    lst_len.clear()
                    lst_len.append(last_key_2)
                    lst_len.append(last_key_1)
                    break

    for pl in players_list:
        pl.action(key)

    for key in bullets_list:
        for bul in bullets_list[key]:
            bul.move()

    screen.fill('black')

    bricks.update()
    bricks.draw(screen)

    players.update()
    players.draw(screen)

    bullets_1.update()
    bullets_1.draw(screen)
    bullets_2.update()
    bullets_2.draw(screen)

    pygame.display.flip()

    # if length != (len(bullets), len(bullets_list)):
    #     print(length)
    #     length = len(bullets), len(bullets_list)

pygame.quit()
exit()
