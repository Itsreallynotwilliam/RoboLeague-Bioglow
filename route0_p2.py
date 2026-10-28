from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor,ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()                                              #setting the hub to PrimeHub

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)        #Left Motor is A
right_motor = Motor(Port.D)                                   #Right Motor is D
right_attach_motor = Motor(Port.F)
left_attach_motor = Motor(Port.B)

robot = DriveBase(                                            #Setting robot parameters
    left_motor,
    right_motor,
    wheel_diameter = 56,
    axle_track = 112
)

#setting speed for robot
robot.settings(
    straight_speed = 200,
    straight_acceleration=750,
    turn_acceleration=150,
    turn_rate=750,
)

robot.straight(40)
robot.turn(37)
robot.straight(400)
right_attach_motor.run_angle(150, 55)



robot.straight(-1000)

# move backwards (maybe keep lifting)

#hello this is a change make a change