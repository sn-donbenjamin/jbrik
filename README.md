# JBRIK 
My adaptation of a Rubiks Cube solving robot. Intended as a hobby exercise in RaspberryPi, Python and GIT.

# Background/Components
Rubiks cube solving robot built from Legos, Raspberry Pi 3, Dexter BrickPi3, solved and controlled using libraries written in Python 2.7

The project is closely based on the original [BricKuber](https://www.dexterindustries.com/projects/brickuber-project-raspberry-pi-rubiks-cube-solving-robot-project/) project from Dexter Industries and has the following components:

- [Raspberry Pi](https://shop.dexterindustries.com/raspberry-pi-3/) - Will take pictures of the unsolved cube, process the solution and command the BrickPi.
- [BrickPi3](https://shop.dexterindustries.com/shop/robots/brickpi/brickpi-advanced-for-raspberry-pi) - Will controll the Lego motors.
- [Raspberr Pi Camera](https://shop.dexterindustries.com/raspberry-pi-camera/) - Will take pictures of the unsolved cube.
- [Raspbian for Robots](https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/) - Loaded onto an SD card, is the operating system for the Raspberry Pi.
- [LEGO Mindstorm](https://www.amazon.com/LEGO-6029291-Mindstorms-EV3-31313/dp/B00CWER3XY/ref=as_li_ss_tl?s=toys-and-games&ie=UTF8&qid=1477461771&sr=1-1&keywords=lego+mindstorms+ev3+31313&linkCode=sl1&tag=dexteindus-20&linkId=548432ea1fb981e344e36e80fb09b3fa) - Will be used to build the actual robot that solves the cube.
- [rubiks-color-tracker](https://github.com/dwalton76/rubiks-cube-tracker) - Python library used to convert an image of a cube into RGB values for each square.
- [BrickPi3](https://github.com/DexterInd/BrickPi3/tree/master/Projects/BricKuber) - BrickPi3 drivers (https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/brickpi3.py)
- JBRIK - Source code from this project written to solve the cube.
  - [motor_core](https://github.com/jdvcDev/jbrik/tree/dev/motor_core) - Wrapper library around Dexter Ind. LEGO motor drivers.  Controls articulation of the robot.
  - [solver_core](https://github.com/jdvcDev/jbrik/tree/dev/solver_core) - Routines to solve each phase of the cube.
  - [tracker_core](https://github.com/jdvcDev/jbrik/tree/dev/tracker_core)
    resolver - Routines used to convert RGB values corresponding to cube tiles into closest fit colors of the cube.
    tracker - Routines used to identify tiles on the cube faces and convert to RGB values.

Alogorithms used to solve the cube: https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/

# Setup/Installation
My prefered method of installation is using virtualenv.  You need only make sure that you have the dependencies listed in setup.py installed in order to run jbrik.  It's assumed that you're running on a RaspberryPi with Raspian for Robots with a BrickPi attached as well so there's an implied dependency on you having the BrickPi drivers to run the LEGO servos.

`git clone https://github.com/jdvcDev/jbrik.git`

`cd jbrik`

`virtualenv --python=<path to python version> ./venv`

`source venv/Scripts/activate`

`pip install .`


# Running/Example
![jbrk](https://github.com/jdvcDev/jbrik/blob/dev/resource/_MG_6751.JPG)

To run the solver:

`python jbrik.py`

The solver will perform the following sequence:

1. jbrik motor callibration.
2. A photo is take of each face of the cube.
3. The photos are interpreted by the tracker routines, each colored tile is extracted and converted to an RBG value.
4. The RGB values are input into the rosolver routines, the final output is a string colored tiles values representing the state of the cube.  For example:

`oogrwgwyrrgbwobyrygwbyyrwgwowowrobbyoggrgbwyrboyobyrbg`

5. The cube state string is input to the solver routines that will progress through 7 stages of solving the cube with each stage's solution represented by a list of movements required to solve that phase of the cube, each movement described by a face, a direction and the number of 90 degree movements.  For example:

`[3CW2],[1CC1],[4CW1]...`

5. The list of solution movements are then sent to the motor routines which execute the corresponding motor movements (flip, grab, rotate cube, rotate face) required to perform the movement.

The entire process takes roughly ten minutes depending on how many photos the solver is configured to take per face and how many movements are required to solve the cube.

#### Example Run 
[![jbrik video](https://github.com/jdvcDev/jbrik/blob/dev/resource/solver_thumb.png)](https://www.youtube.com/watch?v=4Z060QUFvyM)


# Challenges
#### Lighting 
Getting the tracker library to correctly resolve the face tiles to RGB values was difficult at times.  It would often fail to correctly identify colors, most often orange would be resolved as red and yellow as white.  At times the tracker would see reflections in the face of the cube and inaccurately identify these lighting transitions as unique tiles on the face.   
- I approached this with several different solutions beggining with lighting placement.  Ultimately, direct light makes the problem worse and I was unable to find a consistent lighting position that would produce consistent results.  
- I attempted to brute force the problem by taking an initial picture of the cube face, rotate the cube 90 degrees followed by another picture, etc. until I had 4 total pictures of the face.  I then converted each picture to the 9 unique RGB values correspong to the tiles on the given face, adjusted internal state representation of the individual tile locations to adjust for rotation, then used each of 4 unique RGB values for each tile to determine an aggregate average of the observed colors distance to each of the known cube colors... clear as mudd?  This worked, intermittently.  I found the tracker library was at times failing to identify an entire row of tiles (usually the top) which resulted in tiles being interpreted in the wrong order, or ultimately missing altogether.
- Eventually I decided on building a light box to operate the machine in.  This provided consistent non direct lighting and allowed me to revert to only one photo per cube face.

#### Nearest cube color match
Identifying the nearest cube known color for each RGB was challenging as well.  I initially attempted to use the color resolver library implemented by dwalton76 (author of the tracker lib) but found the implementation to be tightly coupled to the usage of the kociemba algorithm.  That is the majority of the implementation is built around converting the observed RGB values into a kociemba string.  Given I chose to implement my own solving algorithms it was more challenging to adopt the resolve code than to write my own resolver as well.  I experimented with various color math processes related to finding the lowest distance to the known cube colors, including an aggregate average across multiple picture as described above but ultimately I ended up using LAB color space and found lighting to be the primary issue.  Finally, it took some experimentation with how to set RGB values for the known cube colors as colors differ by cube implementation, a standard cube vs a speed cube being the two implementations I was using to prototype.

#### Cube flipping
I found that while running the solution set, that is, performing the motor movements to solve the cube, about 1 out of 100 moves would result in the machines grabber arm failing to flip the cube properly.  I experimented with several different speeds and movement ranges in an attempt to mitigate that but ulimately ended up resolving the issue by using a standard cube (vs a speed cube) due to its weight.  The machine seems to handle a heavier weighted cube better than a light one.
