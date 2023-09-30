import pygame
import pandas as pd
import math
import sys

pygame.init()

if len(sys.argv) != 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

file_name = sys.argv[1]
data = 0
try:
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_name)
    normalize_columns = [
    'FirstObjectDistance_X', 'FirstObjectDistance_Y',
    'SecondObjectDistance_X', 'SecondObjectDistance_Y',
    'ThirdObjectDistance_X', 'ThirdObjectDistance_Y',
    'FourthObjectDistance_X', 'FourthObjectDistance_Y',
    'VehicleSpeed', 'FirstObjectSpeed_X', 'FirstObjectSpeed_Y',
    'SecondObjectSpeed_X', 'SecondObjectSpeed_Y',
    'ThirdObjectSpeed_X', 'ThirdObjectSpeed_Y',
    'FourthObjectSpeed_X', 'FourthObjectSpeed_Y']

    # Divide the specified columns by the corresponding normalization factors
    data[normalize_columns] = data[normalize_columns] / [128, 128, 128, 128, 128, 128, 128, 128, 256, 256, 256, 256, 256, 256, 256, 256, 256]

    # Perform operations on the data as needed
    # For example, print the first few rows of the DataFrame
    print(data.head())

    # Your additional operations here

except FileNotFoundError:
    print(f"File not found: {file_name}")
except pd.errors.EmptyDataError:
    print(f"The file {file_name} is empty or not in CSV format.")
except Exception as e:
    print(f"An error occurred: {e}")



# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
offset = 500
scale = 4


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


d1 = 0
d2 = 0
d3 = 0 
d4 = 0


d1_hist = []
d2_hist = []
d3_hist = []
d4_hist = []

d1_xy = []
d2_xy = []
d3_xy = []
d4_xy = []
ego_xy = []


color1 = (52, 192, 235)
color2 = (52, 235, 147)
color3 = (165, 52, 235)
color4 = (235, 52, 76)


font = pygame.font.SysFont(None, 24)


collision = False
collision_object = None

check_case = False



while running:

    # Did the user click the window close button?
    

    # Fill the background with white
    


    for index, row in data.iterrows():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((222, 222, 222))

        x1_object = x + ((row['FirstObjectDistance_X']* math.cos(theta)) - (row['FirstObjectDistance_Y'] * math.sin(theta)))
        y1_object = y + ((row['FirstObjectDistance_X']* math.sin(theta)) - (row['FirstObjectDistance_Y'] * math.cos(theta)))
        d1 = math.sqrt((row['FirstObjectDistance_X']**2) + (row['FirstObjectDistance_Y']**2))
        d1_hist.append(d1)
        d1_xy.append((x1_object, y1_object))
        

        x2_object = x + ((row['SecondObjectDistance_X']* math.cos(theta)) - (row['SecondObjectDistance_Y'] * math.sin(theta)))
        y2_object = y + ((row['SecondObjectDistance_X']* math.sin(theta)) - (row['SecondObjectDistance_Y'] * math.cos(theta)))
        d2 = math.sqrt((row['SecondObjectDistance_X']**2) + (row['SecondObjectDistance_Y']**2))
        d2_hist.append(d2)
        d2_xy.append((x2_object, y2_object))


        x3_object = x + ((row['ThirdObjectDistance_X']* math.cos(theta)) - (row['ThirdObjectDistance_Y'] * math.sin(theta)))
        y3_object = y + ((row['ThirdObjectDistance_X']* math.sin(theta)) - (row['ThirdObjectDistance_Y'] * math.cos(theta)))
        d3 = math.sqrt((row['ThirdObjectDistance_X']**2) + (row['ThirdObjectDistance_Y']**2))
        d3_hist.append(d3)
        d3_xy.append((x3_object, y3_object))


        x4_object = x + ((row['FourthObjectDistance_X']* math.cos(theta)) - (row['FourthObjectDistance_Y'] * math.sin(theta)))
        y4_object = y + ((row['FourthObjectDistance_X']* math.sin(theta)) - (row['FourthObjectDistance_Y'] * math.cos(theta)))
        d4 = math.sqrt((row['FourthObjectDistance_X']**2) + (row['FourthObjectDistance_Y']**2))
        d4_hist.append(d4)
        d4_xy.append((x4_object, y4_object))
        
        ego_xy.append((x, y))

        pygame.draw.circle(screen, (0, 0, 255), ((x*scale) + offset, (y*scale) + offset), 10)
        pygame.draw.circle(screen, color1, (x1_object*scale +offset, y1_object*scale + offset), 5)
        pygame.draw.circle(screen, color2, (x2_object*scale +offset, y2_object*scale + offset), 5)
        pygame.draw.circle(screen, color3, (x3_object*scale +offset, y3_object*scale + offset), 5)
        pygame.draw.circle(screen, color4, (x4_object*scale +offset, y4_object*scale + offset), 5)

        img1 = font.render(f'Object 1 Distance: {d1}', True, color1)
        screen.blit(img1, (20, 20))
        img2 = font.render(f'Object 2 Distance: {d2}', True, color2)
        screen.blit(img2, (20, 40))
        img3 = font.render(f'Object 3 Distance: {d3}', True, color3)
        screen.blit(img3, (20, 60))
        img4 = font.render(f'Object 4 Distance: {d4}', True, color4)
        screen.blit(img4, (20, 80))
        
        

        if(d1 < 8):
            temp = d1_hist[-40:][0] + 1
            check = True
            for i in d1_hist[-40:]:
                if abs(temp - i) > 5:
                    check = False
                    break
                if i >= temp:
                    check = False
                temp = i
            if check == True:
                collision = True
                collision_object = 1

        if(d2 < 8):
            temp = d2_hist[-40:][0] + 1
            check = True
            for i in d2_hist[-40:]:
                if abs(temp - i) > 5:
                    check = False
                    break
                if i >= temp:
                    check = False
                temp = i
            if check == True:
                collision = True
                collision_object = 2
        
        if(d3 < 8):
            temp = d3_hist[-40:][0] + 1
            check = True
            for i in d3_hist[-40:]:
                if abs(temp - i) > 5:
                    check = False
                    break
                if i >= temp:
                    check = False
                temp = i
            if check == True:
                collision = True
                collision_object = 3

        if(d4 < 8):
            temp = d4_hist[-40:][0] + 1
            check = True
            for i in d4_hist[-40:]:
                if abs(temp - i) > 5:
                    check = False
                    break
                if i >= temp:
                    check = False
                temp = i
            if check == True:
                print(d4_hist[-40:] , 'aa')
                collision = True
                collision_object = 4


        if collision:
            case = 0
            if collision_object == 1 and check_case == False:
                p1 = d1_xy[-40]
                p2 = d1_xy[-30]
                slope_line1 = (p1[1] - p2[1]) / (p1[0] - p2[0])
                slope_line2 = (ego_xy[-40][1] - ego_xy[-30][1]) / (ego_xy[-40][0] - ego_xy[-30][0])
                print(slope_line1, slope_line2)
                print(abs(slope_line2 - slope_line1) < 0.5)
                if (abs(slope_line2 - slope_line1) < 0.5):
                    angle_line1 = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
                    angle_line2 = math.atan2(ego_xy[-30][1] - ego_xy[-40][1], ego_xy[-30][0] - ego_xy[-40][0])
                    angular_difference = abs(angle_line1 - angle_line2)
                    # Check if the angular difference is close to 0 or pi (180 degrees)
                    tolerance = math.pi / 180  # You can adjust this tolerance as needed
                    if angular_difference < tolerance or abs(angular_difference - math.pi) < tolerance:
                        case = 'Car To Pedestrian Turn Adult'  # The lines are moving in the same direction or opposite directions
                        check_case = True
                    else:
                        case = 'Car to Pedestrian Longitudinal Adult'  # The lines are not moving in the same direction
                        check_case = True
            elif check == False:
                case = 'Car To Pedestrian Near Side Child Obstructed'
                check_case = True

            if collision_object == 2 and check_case == False:
                p1 = d2_xy[-40]
                p2 = d2_xy[-30]
                slope_line1 = (p1[1] - p2[1]) / (p1[0] - p2[0])
                slope_line2 = (ego_xy[-40][1] - ego_xy[-30][1]) / (ego_xy[-40][0] - ego_xy[-30][0])
                print(slope_line1, slope_line2)
                print(abs(slope_line2 - slope_line1) < 0.5)
                if (abs(slope_line2 - slope_line1) < 0.5):
                    angle_line1 = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
                    angle_line2 = math.atan2(ego_xy[-30][1] - ego_xy[-40][1], ego_xy[-30][0] - ego_xy[-40][0])
                    angular_difference = abs(angle_line1 - angle_line2)
                    # Check if the angular difference is close to 0 or pi (180 degrees)
                    tolerance = math.pi / 180  # You can adjust this tolerance as needed
                    if angular_difference < tolerance or abs(angular_difference - math.pi) < tolerance:
                        case = 'Car To Pedestrian Turn Adult'  # The lines are moving in the same direction or opposite directions
                        check_case = True
                    else:
                        case = 'Car to Pedestrian Longitudinal Adult'  # The lines are not moving in the same direction
                        check_case = True
            elif check == False:
                case = 'Car To Pedestrian Near Side Child Obstructed'
                check_case = True
            
            if collision_object == 3 and check_case == False:
                p1 = d3_xy[-40]
                p2 = d3_xy[-30]
                slope_line1 = (p1[1] - p2[1]) / (p1[0] - p2[0])
                slope_line2 = (ego_xy[-40][1] - ego_xy[-30][1]) / (ego_xy[-40][0] - ego_xy[-30][0])
                print(slope_line1, slope_line2)
                print(abs(slope_line2 - slope_line1) < 0.5)
                if (abs(slope_line2 - slope_line1) < 0.5):
                    angle_line1 = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
                    angle_line2 = math.atan2(ego_xy[-30][1] - ego_xy[-40][1], ego_xy[-30][0] - ego_xy[-40][0])
                    angular_difference = abs(angle_line1 - angle_line2)
                    # Check if the angular difference is close to 0 or pi (180 degrees)
                    tolerance = math.pi / 180  # You can adjust this tolerance as needed
                    if angular_difference < tolerance or abs(angular_difference - math.pi) < tolerance:
                        case = 'Car To Pedestrian Turn Adult'  # The lines are moving in the same direction or opposite directions
                        check_case = True
                    else:
                        case = 'Car to Pedestrian Longitudinal Adult'  # The lines are not moving in the same direction
                        check_case = True
            elif check == False:
                case = 'Car To Pedestrian Near Side Child Obstructed'
                check_case = True

            if collision_object == 4 and check_case == False:
                p1 = d4_xy[-40]
                p2 = d4_xy[-30]
                slope_line1 = (p1[1] - p2[1]) / (p1[0] - p2[0])
                slope_line2 = (ego_xy[-40][1] - ego_xy[-30][1]) / (ego_xy[-40][0] - ego_xy[-30][0])
                print(slope_line1, slope_line2)
                print(abs(slope_line2 - slope_line1) < 0.5)
                if (abs(slope_line2 - slope_line1) < 0.5):
                    angle_line1 = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
                    angle_line2 = math.atan2(ego_xy[-30][1] - ego_xy[-40][1], ego_xy[-30][0] - ego_xy[-40][0])
                    angular_difference = abs(angle_line1 - angle_line2)
                    # Check if the angular difference is close to 0 or pi (180 degrees)
                    tolerance = math.pi / 180  # You can adjust this tolerance as needed
                    if angular_difference < tolerance or abs(angular_difference - math.pi) < tolerance:
                        case = 'Car To Pedestrian Turn Adult'  # The lines are moving in the same direction or opposite directions
                        check_case = True
                    else:
                        case = 'Car to Pedestrian Longitudinal Adult'  # The lines are not moving in the same direction
                        check_case = True
            elif check == False:
                case = 'Car To Pedestrian Near Side Child Obstructed'
                check_case = True

                


            img5 = font.render(f'Collision Occurs With Object : {collision_object}', True, (0, 0, 0))
            screen.blit(img5, (450, 80))         
            if case != 0:
                img6 = font.render(f'Case : {case}', True, (0, 0, 0))
                screen.blit(img6, (450, 100))       
                

        if (index < (len(data) - 1)):
            delt = data.iloc[index + 1]['Timestamp'] - row['Timestamp']
        delx = row['VehicleSpeed'] * delt * math.cos(theta)
        dely = row['VehicleSpeed'] * delt * math.sin(theta)
        x = x + delx
        y = y + dely
        theta = theta + row['YawRate']*delt



        pygame.time.delay(10)
        pygame.display.flip()
    screen.fill((255, 255, 255))
    x = 0
    y = 0
    theta = 0
    d1_hist = []
    d2_hist = []
    d3_hist = []
    d4_hist = []
    collision = False
    # Draw a solid blue circle in the center

    # Flip the display
    

# Done! Time to quit.
pygame.quit()