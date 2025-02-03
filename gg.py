Program 3-10 (hit_the_target.py)

1  # Hit the Target Game
2  import turtle
3
4  # Named constants
5  SCREEN_WIDTH = 600    # Screen width
6  SCREEN_HEIGHT = 600   # Screen height
7  TARGET_LLEFT_X = 100  # Target's lower-left X
8  TARGET_LLEFT_Y = 250  # Target's lower-left Y
9  TARGET_WIDTH = 25     # Width of the target
10 FORCE_FACTOR = 30     # Arbitrary force factor
11 PROJECTILE_SPEED = 1  # Projectile's animation speed
12 NORTH = 90            # Angle of north direction
13 SOUTH = 270           # Angle of south direction
14 EAST = 0              # Angle of east direction
15 WEST = 180            # Angle of west direction
16
17  # Setup the window.
18  turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
19
20  # Draw the target.
 turtle.hideturtle()
22  turtle.speed(0)
23  turtle.penup()
24  turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
25  turtle.pendown()
26  turtle.setheading(EAST)
27  turtle.forward(TARGET_WIDTH)
28  turtle.setheading(NORTH)
29  turtle.forward(TARGET_WIDTH)
30  turtle.setheading(WEST)
31  turtle.forward(TARGET_WIDTH)
32  turtle.setheading(SOUTH)
33  turtle.forward(TARGET_WIDTH)
34  turtle.penup()
35
36  # Center the turtle.
37  turtle.goto(0, 0)
38  turtle.setheading(EAST)
39  turtle.showturtle()
40  turtle.speed(PROJECTILE_SPEED)
41
42  # Get the angle and force from the user.
43  angle = float(input("Enter the projectile's angle: "))
44  force = float(input("Enter the launch force (1−10): "))
45
46  # Calculate the distance.
47  distance = force * FORCE_FACTOR
48
49  # Set the heading.
50  turtle.setheading(angle)
51
52  # Launch the projectile.
53  turtle.pendown()
54  turtle.forward(distance)
55
56  # Did it hit the target?
57  if (turtle.xcor() >= TARGET_LLEFT_X and
58      turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
59      turtle.ycor() >= TARGET_LLEFT_Y and
60      turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
61          print('Target hit!')
62  else:
63          print('You missed the target.')
64
