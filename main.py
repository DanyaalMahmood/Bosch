import pygame
import pandas as pd
import math

pygame.init()

data = pd.read_csv("data_normalized.csv")

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])



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

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    


    for index, row in data.iterrows():
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), ((x*6) + 500, (y*6) + 500), 20)
        if (index < (len(data) - 1)):
            delt = data.iloc[index + 1]['Timestamp'] - row['Timestamp']
        print('delt', delt)
        delx = row['VehicleSpeed'] * delt * math.cos(theta)
        dely = row['VehicleSpeed'] * delt * math.sin(theta)
        x = x + delx
        y = y + dely
        theta = theta + row['YawRate']*delt
        print(x, y)
        pygame.time.delay(2)
        pygame.display.flip()
    x = 0
    y = 0
    theta = 0
    # Draw a solid blue circle in the center
    print('game end')

    # Flip the display
    

# Done! Time to quit.
pygame.quit()