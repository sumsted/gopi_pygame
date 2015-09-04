import pygame
from gopigo import *

pygame.init()

last_direction = 'stop'
last_speed = 0

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

while not done:
    pygame.event.get()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    left_right_axis = joystick.get_axis(0)
    fwd_bwd_axis = joystick.get_axis(1)
    speed_axis = joystick.get_axis(5)
    direction_threshold = .8
    left_rot_button = joystick.get_button(2)
    right_rot_button = joystick.get_button(3)
    stop_button = joystick.get_button(12)
    quit_button = joystick.get_button(10)
    # axis 0  -1 left 1 right
    # axis 1  -1 up 1 down
    # axis 5  -1 stop 1 go
    if fwd_bwd_axis > -direction_threshold and left_right_axis < -direction_threshold and last_direction != 'left':
        last_direction = 'left'
        print('left')
        left()
    elif fwd_bwd_axis > -direction_threshold and left_right_axis > direction_threshold and last_direction != 'right':
        last_direction = 'right'
        print('right')
        right()
    elif fwd_bwd_axis < -direction_threshold and -direction_threshold < left_right_axis < direction_threshold and last_direction != 'fwd':
        last_direction = 'fwd'
        print('fwd')
        fwd()
    elif fwd_bwd_axis > direction_threshold and -direction_threshold < left_right_axis < direction_threshold and last_direction != 'bwd':
        last_direction = 'bwd'
        print('bwd')
        bwd()

    elif left_rot_button == 1 and last_direction != 'left_rot':
        print('left_rot')
        last_direction = 'left_rot'
        left_rot()
    elif right_rot_button == 1 and last_direction != 'right_rot':
        print('right_rot')
        last_direction = 'right_rot'
        right_rot()
    elif stop_button == 1 and last_direction != 'stop':
        print('stop')
        last_direction = 'stop'
        stop()
    elif quit_button == 1:
        print('quit')
        stop()
        done = True

    if speed_axis < -0.9 and last_speed != 0:
        last_speed = 0
        print('speed 0')
        set_speed(0)
    elif -.9 < speed_axis < .9 and last_speed != 100:
        last_speed = 100
        print('speed 100')
        set_speed(100)
    elif speed_axis > .9 and last_speed != 200:
        last_speed = 200
        print('speed 200')
        set_speed(200)

    # Limit to 20 frames per second
    clock.tick(20)

pygame.quit()
