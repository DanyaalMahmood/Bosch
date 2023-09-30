import pygame
import pandas as pd
import math
import pygame.mixer


pygame.init()
pygame.mixer.init()

data = pd.read_csv("data_normalized.csv")

# Set up the drawing window
screen = pygame.display.set_mode([1200, 1200])

# Run until the user asks to quit
running = True

x = 0
y = 0
theta = 0
x_translate = 500
y_translate = 500

delx = 0
dely = 0
t = 0
delt = 0

# Initial glow radius and color of objects
glow_radius = 5

glow_objects_1 = ('#1A5D1A')
glow_objects_2 = ('#1A5D1A')
glow_objects_3 = ('#1A5D1A')
glow_objects_4 = ('#1A5D1A')


# of car
glow_width = 5
glow_car = (255, 255, 255)  # White glow color

# Light of car
glow_enabled = True

# Sound of horn
sound_enabled = False
sound = pygame.mixer.Sound('horn.wav')


blue = (0, 0, 255)    # Blue
red = (255, 0, 0)    # Red
green = (0, 255, 0)    # Green
yellow = (255, 255, 0)  # Yellow

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(('#AEC3AE'))

    for index, row in data.iterrows():
        # Draw the square
        square_size = 20  # Size of the square
        square_color = (0, 0, 0)  # Blue square color
        square_x = (x * 6) + 500
        square_y = (y * 6) + 500
        pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

        # Draw the glow effect around the square using a rectangle
        if glow_enabled:
            glow_rect = pygame.Rect(square_x - glow_width, square_y - glow_width, square_size + 2 * glow_width, square_size + 2 * glow_width)
            pygame.draw.rect(screen, glow_car, glow_rect, 3) 
        
        if sound_enabled:
            sound.play()
        
        x1_object = x + ((row['FirstObjectDistance_X']* math.cos(theta)) - (row['FirstObjectDistance_Y'] * math.sin(theta)))
        y1_object = y + ((row['FirstObjectDistance_X']* math.sin(theta)) - (row['FirstObjectDistance_Y'] * math.cos(theta)))
        x2_object = x + ((row['SecondObjectDistance_X']* math.cos(theta)) - (row['SecondObjectDistance_Y'] * math.sin(theta)))
        y2_object = y + ((row['SecondObjectDistance_X']* math.sin(theta)) - (row['SecondObjectDistance_Y'] * math.cos(theta)))
        x3_object = x + ((row['ThirdObjectDistance_X']* math.cos(theta)) - (row['ThirdObjectDistance_Y'] * math.sin(theta)))
        y3_object = y + ((row['ThirdObjectDistance_X']* math.sin(theta)) - (row['ThirdObjectDistance_Y'] * math.cos(theta)))
        x4_object = x + ((row['FourthObjectDistance_X']* math.cos(theta)) - (row['FourthObjectDistance_Y'] * math.sin(theta)))
        y4_object = y + ((row['FourthObjectDistance_X']* math.sin(theta)) - (row['FourthObjectDistance_Y'] * math.cos(theta)))

        # Draw the objects with inner color and glow effect
        inner_circle_radius = 5
        pygame.draw.circle(screen, ('#CECE5A') , (x1_object*6 + 500, y1_object*6 + 500), inner_circle_radius)  # Inner circle
        pygame.draw.circle(screen, glow_objects_1, (x1_object*6 + 500, y1_object*6 + 500), inner_circle_radius + glow_radius, 3)  # Glow effect
        pygame.draw.circle(screen, ('#FFE17B') , (x2_object*6 + 500, y2_object*6 + 500), inner_circle_radius)  # Inner circle
        pygame.draw.circle(screen, glow_objects_2, (x2_object*6 + 500, y2_object*6 + 500), inner_circle_radius + glow_radius, 3)  # Glow effect
        pygame.draw.circle(screen, ('#FD8D14'), (x3_object*6 + 500, y3_object*6 + 500), inner_circle_radius)  # Inner circle
        pygame.draw.circle(screen, glow_objects_3, (x3_object*6 + 500, y3_object*6 + 500), inner_circle_radius + glow_radius, 3)  # Glow effect
        pygame.draw.circle(screen, ('#C51605'), (x4_object*6 + 500, y4_object*6 + 500), inner_circle_radius)  # Inner circle
        pygame.draw.circle(screen, glow_objects_4, (x4_object*6 + 500, y4_object*6 + 500), inner_circle_radius + glow_radius, 3)  # Glow effect

        # Repeat the same process for other objects (x2_object, x3_object, x4_object)

        if (index < (len(data) - 1)):
            delt = data.iloc[index + 1]['Timestamp'] - row['Timestamp']
        print('delt', delt)
        delx = row['VehicleSpeed'] * delt * math.cos(theta)
        dely = row['VehicleSpeed'] * delt * math.sin(theta)
        x = x + delx
        y = y + dely
        theta = theta + row['YawRate']*delt
        print(x, y)
        pygame.time.delay(50)
        pygame.display.flip()
        screen.fill(('#AEC3AE'))

    x = 0
    y = 0
    theta = 0
    # Draw a solid blue circle in the center
    print('game end')

    # Flip the display

# Done! Time to quit.
pygame.quit()
