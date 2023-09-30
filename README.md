# Autonomous Vehicle Collision Detection and Visualization
This Python project provides a solution for detecting objects in the path of an autonomous vehicle that may lead to collisions and visualizes the scenario using the Pygame library. It offers a real-time representation of an autonomous vehicle's environment, object distances, and potential collision detection.

## Table of Contents
Installation\
Usage\
Features\
Project Structure\
Future Enhancements\
License

### Installation
To use this project, follow these steps:

### Clone the repository:

git clone https://github.com/DanyaalMahmood/Bosch.git

cd autonomous-vehicle-collision
Ensure you have Python and Pygame installed on your system. You can install Pygame using pip:

pip install pygame

Run the project with the following command, providing the path to your input CSV file as an argument:

python main.py <input_file>

### Usage
Replace <input_file> with the name of your input CSV file containing object parameters and vehicle data. The csv file should be in the same directory.
The application will display an interactive visualization of the vehicle's movement and objects in its environment.
It calculates object distances, detects potential collisions, and provides case descriptions.
Features
Real-time visualization of an autonomous vehicle's environment.
Detection of objects in the vehicle's path.
Calculation of object distances and relative positions.
Potential collision detection and case descriptions.
Easy integration with custom datasets.
Project Structure
The project is organized as follows:

main.py: The main Python script for data processing and visualization.

### Future Enhancements
This project is continuously evolving, and future enhancements may include:

Advanced collision avoidance mechanisms.
Integration with sensor technologies for improved accuracy.
Machine learning algorithms for predictive collision avoidance.
Real-time communication with other vehicles and infrastructure.
Feel free to contribute to the project and help make autonomous vehicles safer and more reliable.




