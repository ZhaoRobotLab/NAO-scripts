#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

'''Say a text with a local configuration'''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    configuration = {"bodyLanguageMode":"contextual"}
    
    animatedSpeechProxy.say(
        "\\rspd=75\\ \\vol=100\\ \\vct=75\\ To prepare for this exercise just take a few moments, whether you are sitting or standing to find a comfortable position. \
        You may choose to close your eyes or keep them open. \
        If you are feeling a bit tired, it may be useful to just let a little bit of light in to keep you alert.")

    animatedSpeechProxy.say(
        "\\rspd=75\\ \\vol=100\\ \\vct=75\\ \\pau=5000\\ Begin by gently moving your attention onto the process of breathing. \
        Simply observing each breath as it happens. \
        Whether you focus on the rise and fall of your chest. \
        Or perhaps the sensation of the breath as it moves in and out of the nostrils.")

    animatedSpeechProxy.say(
        "\\rspd=75\\ \\vol=100\\ \\vct=75\\ \\pau=5000\\ Are the breaths deep or shallow? \
        Long or short? \
        Really feel what it is like to breathe without the need to alter your breath, just observing it as it happens.")

    animatedSpeechProxy.say(
        "\\rspd=75\\ \\vol=100\\ \\vct=75\\ \\pau=5000\\ As you engage with this exercise you may find that your mind wanders. \
        Caught by thoughts or by noises around the room, or by bodily sensations. \
        When you notice that this happens, know that this is ok, and that our mind often wanders. \
        Simply notice what has caught your mind’s attention, then gently bring your focus back to the breath.")

    animatedSpeechProxy.say(
        "\\rspd=75\\ \\vol=100\\ \\vct=75\\ \\pau=5000\\ Now as you feel comfortable to do so you, can expand your awareness from your breath, onto the rest of your body, \
        and the room around you, and when you feel ready to do so,\\pau=500\\ you can open your eyes and bring the exercise to a close. \
        \\pau=2000\\ Thank you for participating, goodbye")
    
main("169.254.130.126")


    

