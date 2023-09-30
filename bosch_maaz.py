import pygame
import pandas as pd
import math

pygame.init()

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

# Constants for braking
max_jerk = -30  # Max jerk in m/s^3
a_ego = -9  # Acceleration/deceleration of the vehicle in m/s^2
a_max = -9  # Maximum deceleration in m/s^2
v_ego = 0  # Initial speed of the vehicle in m/s

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for index, row in data.iterrows():
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0, 0, 255), ((x * 6) + 500, (y * 6) + 500), 10)
        x1_object = x + ((row['FirstObjectDistance_X'] * math.cos(theta)) - (row['FirstObjectDistance_Y'] * math.sin(theta)))
        y1_object = y + ((row['FirstObjectDistance_X'] * math.sin(theta)) - (row['FirstObjectDistance_Y'] * math.cos(theta)))
        x2_object = x + ((row['SecondObjectDistance_X'] * math.cos(theta)) - (row['SecondObjectDistance_Y'] * math.sin(theta)))
        y2_object = y + ((row['SecondObjectDistance_X'] * math.sin(theta)) - (row['SecondObjectDistance_Y'] * math.cos(theta)))
        x3_object = x + ((row['ThirdObjectDistance_X'] * math.cos(theta)) - (row['ThirdObjectDistance_Y'] * math.sin(theta)))
        y3_object = y + ((row['ThirdObjectDistance_X'] * math.sin(theta)) - (row['ThirdObjectDistance_Y'] * math.cos(theta)))
        x4_object = x + ((row['FourthObjectDistance_X'] * math.cos(theta)) - (row['FourthObjectDistance_Y'] * math.sin(theta)))
        y4_object = y + ((row['FourthObjectDistance_X'] * math.sin(theta)) - (row['FourthObjectDistance_Y'] * math.cos(theta)))
        pygame.draw.circle(screen, (0, 255, 0), (x1_object * 6 + 500, y1_object * 6 + 500), 5)
        pygame.draw.circle(screen, (255, 0, 0), (x2_object * 6 + 500, y2_object * 6 + 500), 5)
        pygame.draw.circle(screen, (0, 255, 255), (x3_object * 6 + 500, y3_object * 6 + 500), 5)
        pygame.draw.circle(screen, (255, 255, 0), (x4_object * 6 + 500, y4_object * 6 + 500), 5)

        if (index < (len(data) - 1)):
            delt = data.iloc[index + 1]['Timestamp'] - row['Timestamp']

        # Implement braking logic here
        t2 = (a_max - a_ego) / max_jerk
        t3 = (-v_ego) / a_max
        delta_v2 = (-max_jerk * t2 ** 3) / 6 + (a_ego / 2) * t2 ** 2 + v_ego * t2
        delta_v1 = (max_jerk / 2) * t2 ** 2 + a_ego * t2
        d1 = v_ego * t + (a_ego / 2) * t ** 2
        d2 = (max_jerk / 6) * t2 ** 3 + (a_ego / 2) * t2 ** 2 + v_ego * t2
        d3 = (-a_max / 2) * t3 ** 2 + v_ego * t3

        brake_distance = d1 + d2 + d3
        if delta_v2 < 0:
            brake_distance += delta_v2

        delx = row['VehicleSpeed'] * delt * math.cos(theta)
        dely = row['VehicleSpeed'] * delt * math.sin(theta)
        x = x + delx
        y = y + dely
        theta = theta + row['YawRate'] * delt
        v_ego = v_ego + delta_v1
        print(x, y, v_ego, brake_distance)
        pygame.time.delay(50)
        pygame.display.flip()

    screen.fill((255, 255, 255))
    x = 0
    y = 0
    theta = 0
    v_ego = 0
    print('game end')

# Done! Time to quit.
pygame.quit()
