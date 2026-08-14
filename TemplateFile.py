from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor,ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()                                              #setting the hub to PrimeHub

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)        #Left Motor is A
right_motor = Motor(Port.D)                                   #Right Motor is D


robot = DriveBase(                                            #Setting robot parameters
    left_motor,
    right_motor,
    wheel_diameter = 56,
    axle_track = 112
)
