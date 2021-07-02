from naoqi import ALProxy
from threading import Thread
import argparse
import sys
import time

robotIP = "169.254.10.14"
PORT = 9559

animationPlayerProxy = ALProxy("ALAnimationPlayer", robotIP, PORT)
posture_service = ALProxy("ALRobotPosture", robotIP, PORT)
motion_service = ALProxy("ALMotion", robotIP, PORT)

fractionMaxSpeed  = 0.2

shoulderNames = ["LShoulderRoll", "RShoulderRoll"]
shoulderOutAngles = [1.3, -1.3]

#shoulderPitchNames = ["LShoulderPitch", "RShoulderPitch"]
#shoulderHighPitchAangles[
#shoulderLowPitchAangles[

elbowNames = ["LElbowRoll", "RElbowRoll"]
elbowBentAngles = [-1.54, 1.54]
elbowStraightAngles = [-0.0349, 0.0349]

legNames = ["LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll", "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"]
legCrouchAngles = [-0.08126, -0.70253, 2.1138, -1.182756, 0.0798099, 0.08126, -0.70253, 2.1138, -1.82756, -0.0798099]
legStandAngles = [0.108955, 0.1365, -0.09208, 0.08126, -0.1042, -0.1119, 0.13188, -0.08586, 0.082877, 0.105887]

#Start Dance Moves
def armsOut(secs):
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed)
        motion_service.setAngles(elbowNames, elbowStraightAngles, fractionMaxSpeed)

def armsOutElbowsBent(secs):
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed) 
        motion_service.setAngles(elbowNames, elbowBentAngles, fractionMaxSpeed)

def leftElbowBent(secs):
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed) 
        motion_service.setAngles("LElbowRoll", -1.54, fractionMaxSpeed)
        motion_service.setAngles("RElbowRoll", 0.0349, fractionMaxSpeed)

def rightElbowBent(secs):
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed) 
        motion_service.setAngles("RElbowRoll", 1.54, fractionMaxSpeed)
        motion_service.setAngles("LElbowRoll", -0.0349, fractionMaxSpeed)
        
def squatDownArmsOut(secs):
    motion_service.post.angleInterpolationWithSpeed(legNames, legCrouchAngles, fractionMaxSpeed) 
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed) 
        motion_service.setAngles(elbowNames, elbowStraightAngles, fractionMaxSpeed)

def squatDownLeftBent(secs):
    motion_service.post.angleInterpolationWithSpeed(legNames, legCrouchAngles, fractionMaxSpeed) 
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed) 
        motion_service.setAngles("LElbowRoll", -1.54, fractionMaxSpeed)
        motion_service.setAngles("RElbowRoll", 0.0349, fractionMaxSpeed)

def standUpRightBent(secs):
    motion_service.post.angleInterpolationWithSpeed(legNames, legCrouchAngles, fractionMaxSpeed) 
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed)
        motion_service.setAngles("RElbowRoll", 1.54, fractionMaxSpeed)
        motion_service.setAngles("LElbowRoll", -0.0349, fractionMaxSpeed)

def standUpArmsOut(secs):
    motion_service.post.angleInterpolationWithSpeed(legNames, legStandAngles, fractionMaxSpeed) 
    t_end = time.time() + secs
    while time.time() < t_end:
        motion_service.post.setAngles(shoulderNames, shoulderOutAngles, fractionMaxSpeed) 
        motion_service.setAngles(elbowNames, elbowStraightAngles, fractionMaxSpeed)

#def flapArms(secs):
    

#Start Full Dances        
def normSinusRhythm():
    posture_service.goToPosture("Stand", 1.0)
    i = 0
    while i < 4:
        armsOut(2)
        armsOutElbowsBent(2)
        armsOut(2)
        squatDownArmsOut(2)
        standUpArmsOut(2)
        i += 1
        
def secondDegreeAVB():
    posture_service.goToPosture("Stand", 1.0)
    i = 0
    while i < 4:
        armsOut(2)
        armsOutElbowsBent(2)
        armsOut(2+i)
        squatDownArmsOut(2)
        standUpArmsOut(2)
        i += 1

def junctionalRythm():
    posture_service.goToPosture("Stand", 1.0)
    armsOut(2)
    i = 0
    while i < 4:
        squatDownArmsOut(2)
        time.sleep(0.2)
        standUpArmsOut(2)
        time.sleep(0.75)
        i += 1

def atrailFib():
    posture_service.goToPosture("Stand", 1.0)
    armsOut(2)
    i = 0
    while i < 4:
        leftElbowBent(2)
        rightElbowBent(2)
        squatDownLeftBent(2)
        standUpRightBent(2)
        i += 1
    
    
normSinusRhythm()
atrailFib()

