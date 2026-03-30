import pygame
from Sprite import Sprite
from Colors import COLORS

class Environment:
    def __init__(self, screen, SW, SH):
        self.screen = screen

        self.ground_width = SW
        self.ground_height = 200

        self.ground_position = [0, SH - self.ground_height]

        self.sprite1 = Sprite(screen, SW, SH, self.ground_position, 'right', COLORS["SPRITE1"])
        self.sprite2 = Sprite(screen, SW, SH, self.ground_position, 'left', COLORS["SPRITE2"])

        self.ground_color = COLORS["GROUND"] 

        self.sprite1_attack = False
        self.sprite2_attack = False

        self.before_health_sprite1 = self.sprite1.health
        self.before_health_sprite2 = self.sprite2.health

    def reset(self):
        self.sprite1.reset()
        self.sprite2.reset()

    def step(self, action_sprite1, action_sprite2):
        sword1 = self.sprite1.sword
        sword2 = self.sprite2.sword
        sprite1 = self.sprite1
        sprite2 = self.sprite2

        self.sprite1.step(action_sprite1)
        self.sprite2.step(action_sprite2)

        done = False

        reward_sprite1 = 0
        reward_sprite2 = 0

        # sprite 1 attack sprite 2
        if sprite1.is_attacking:
            if self.sword_collision_detection(sword1, sprite2) and self.before_health_sprite2 == sprite2.health:
                if sprite2.health > 0:
                    sprite2.health -= 5

                    reward_sprite1 = 5
                    reward_sprite2 = -5
                
                if sprite2.health <= 0:
                    reward_sprite2 = 10
                    reward_sprite1 = -10

                    done = True

        if not sprite1.is_attacking:
            self.before_health_sprite2 = sprite2.health

        # sprite 2 attack sprite 1
        if sprite2.is_attacking:
            if self.sword_collision_detection(sword2, sprite1) and self.before_health_sprite1 == sprite1.health:
                if sprite1.health > 0:
                    sprite1.health -= 5

                    reward_sprite1 = -5
                    reward_sprite2 = 5

                if sprite1.health <= 0:
                    reward_sprite1 = 10
                    reward_sprite2 = -10

                    done = True

        if not sprite2.is_attacking:
            self.before_health_sprite1 = sprite1.health

        return reward_sprite1, reward_sprite2, done


    # def action(self, keys, events):
    #     self.sprite1.action(keys, events)
    #     self.sprite2.action(keys, events)

    def sword_collision_detection(self, sword, enemy):
        return (sword.position[0] < enemy.position[0] + enemy.width and
            sword.position[0] + sword.width > enemy.position[0] and
            sword.position[1] < enemy.position[1] + enemy.height and
            sword.position[1] + sword.height > enemy.position[1])

    # def handle_attack(self):
    #     sword1 = self.sprite1.sword
    #     sword2 = self.sprite2.sword

    #     sprite1 = self.sprite1
    #     sprite2 = self.sprite2

    #     # sprite 1 attack sprite 2
    #     if sprite1.is_attacking:
    #         if self.sword_collision_detection(sword1, sprite2) and self.before_health_sprite2 == sprite2.health:
    #             if sprite2.health > 0:
    #                 sprite2.health -= 5

    #     if not sprite1.is_attacking:
    #         self.before_health_sprite2 = sprite2.health

    #     # sprite 2 attack sprite 1
    #     if sprite2.is_attacking:
    #         if self.sword_collision_detection(sword2, sprite1) and self.before_health_sprite1 == sprite1.health:
    #             if sprite1.health > 0:
    #                 sprite1.health -= 5

    #     if not sprite2.is_attacking:
    #         self.before_health_sprite1 = sprite1.health

    def update(self):
        self.sprite1.render()
        self.sprite2.render()

        self.sprite1.sword_attack()
        self.sprite2.sword_attack()

        self.sprite1.jump()
        self.sprite2.jump()

        self.sprite1.check_boundary()
        self.sprite2.check_boundary()

    def render(self):
        pygame.draw.rect(self.screen, self.ground_color, (self.ground_position[0], self.ground_position[1], self.ground_width, self.ground_height))


