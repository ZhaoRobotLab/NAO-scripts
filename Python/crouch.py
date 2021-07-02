from naoqi import ALProxy
#import HearbeatDancesDemoV1 as HB

robotIP = "10.140.243.85"
PORT = 9559



posture_service = ALProxy("ALRobotPosture", robotIP, PORT)


def test():
    posture_service.goToPosture("Crouch", 1.0)

def Stest():
    posture_service.goToPosture("Stand", 1.0)


#HB.armsOut(60)

test()


