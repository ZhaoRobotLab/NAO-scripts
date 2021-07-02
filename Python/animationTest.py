from naoqi import ALProxy

def main(robotIP, PORT=9559):
    animationPlayerProxy = ALProxy("ALAnimationPlayer", robotIP, PORT)
    posture_service = ALProxy("ALRobotPosture", robotIP, PORT)

    animationPlayerProxy.run("animations/Stand/Gestures/Hey_1")
    #animationPlayerProxy.run("animations/Stand/Gestures/YouKnowWhat_2") #Both arms in front of chest
    #animationPlayerProxy.run("animations/Stand/Gestures/Explain_1") #Small movement to put hands infront 
    #animationPlayerProxy.run("animations/Stand/Waiting/Stretch_3") #go on one leg
    #animationPlayerProxy.run("animations/Stand/Waiting/Stretch_1") #touch toes
    #animationPlayerProxy.run("animations/Stand/Waiting/Stretch_2") #bend one knee
    #animationPlayerProxy.run("animations/Stand/Waiting/Fitness_1") #crouch and do curles 
    #animationPlayerProxy.run("animations/Stand/Waiting/WalkInTheShit_1") #Lift foot and look (FEEL OVER)
    #animationPlayerProxy.run("animations/Stand/BodyTalk/Speaking/BodyTalk_11") #format for bodytalk
    #animationPlayerProxy.run("animations/Stand/Waiting/Relaxation_1") #yoga moves
    #animationPlayerProxy.run("animations/Stand/Waiting/FunnyDancer_1") #leg out big lean
    #animationPlayerProxy.run("animations/Stand/Waiting/MysticalPower_1") #arms up over head with sound
    #animationPlayerProxy.run("animations/Stand/Gestures/Freeze_2")

    #animationPlayerProxy.run("animations/Stand/Gestures/ShowSky_8")
    
    #posture_service.goToPosture("Stand", 1.0)
     
    
 
main("169.254.156.191")
