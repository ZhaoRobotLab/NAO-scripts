#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import time
import qi
import argparse
import sys
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    animationPlayerProxy = ALProxy("ALAnimationPlayer", robotIP, PORT)
    posture_service = ALProxy("ALRobotPosture", robotIP, PORT)

    speech = ALProxy('ALTextToSpeech', robotIP, PORT)
    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    configuration = {"bodyLanguageMode":"contextual"}

    animatedSpeechProxy.say("\\rspd=80\\ \\vol=100\\ \\vct=75\\ Hello, I'm Nao. I'm going to lead you through some exercises. Lets start with three bouws.")

    animationPlayerProxy.run("animations/Stand/Gestures/BowShort_1")
    speech.say("One")
    time.sleep(1.75)

    animationPlayerProxy.run("animations/Stand/Gestures/BowShort_1")
    speech.say("Two")
    time.sleep(1.75)

    animationPlayerProxy.run("animations/Stand/Gestures/BowShort_1")
    speech.say("Three")
    time.sleep(1.75)
    
    animatedSpeechProxy.say("\\rspd=80\\ \\vol=100\\ \\vct=75\\ Ok, Now lets do three shoulder streches.")
    time.sleep(1)

    animationPlayerProxy.run("animations/Stand/Gestures/ShowSky_8")
    speech.say("One")
    time.sleep(2)

    animationPlayerProxy.run("animations/Stand/Gestures/ShowSky_8")
    speech.say("Two")
    time.sleep(2)

    animationPlayerProxy.run("animations/Stand/Gestures/ShowSky_8")
    speech.say("Three")
    time.sleep(2)

    animatedSpeechProxy.say("\\rspd=80\\ \\vol=100\\ \\vct=75\\ Greats, lets finish up with three squats.")

    posture_service.goToPosture("Crouch", 1.0)
    time.sleep(0.25)
    posture_service.goToPosture("Stand", 1.0)

    speech.say("One")
    time.sleep(1.75)

    posture_service.goToPosture("Crouch", 1.0)
    time.sleep(0.25)
    posture_service.goToPosture("Stand", 1.0)

    speech.say("Two")
    time.sleep(1.75)

    posture_service.goToPosture("Crouch", 1.0)
    time.sleep(0.25)
    posture_service.goToPosture("Stand", 1.0)

    speech.say("Three")

    animatedSpeechProxy.say("\\rspd=80\\ \\vol=100\\ \\vct=75\\ Thank you for working out with me, Goodbye")
  
main("169.254.156.191")
