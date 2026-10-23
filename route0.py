from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor,ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()                                              #setting the hub to PrimeHub

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)        #Left Motor is A
right_motor = Motor(Port.D)                                   #Right Motor is D
#right_attatch_motor = Motor(Port.)
left_attach_motor = Motor(Port.B)

robot = DriveBase(                                            #Setting robot parameters
    left_motor,
    right_motor,
    wheel_diameter = 56,
    axle_track = 112
)

#setting speed for robot
robot.settings(
    straight_speed = 400,
    straight_acceleration=750,
    turn_acceleration=150,
    turn_rate=750,
)


robot.straight(420)
left_attach_motor.run_angle(150,200)
robot.straight(-100)

left_attach_motor.run_angle(150,-135)
wait(200)
robot.straight(100)
left_attach_motor.run_angle(150,135)
robot.straight(-100)
left_attach_motor.run_angle(150,-200)
wait(200)
robot.straight(-310)
