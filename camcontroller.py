from amcrest import AmcrestCamera
import time

white_eye = AmcrestCamera('<IP_ADDRESS>', 80, '<USERNAME>', '<PASSWORD>').camera
black_eye = AmcrestCamera('<IP_ADDRESS>', 80, '<USERNAME>', '<PASSWORD>').camera

def camLoc(camera):

    try:
        cam_stats = camera.ptz_status().replace('\r', '').split('\n')
        currHori = float(cam_stats[2].split('=')[1])
        currVert = float(cam_stats[3].split('=')[1])
        return currHori, currVert
    except:
        print("An error has occured")
        pass

def inMotion(camera):
    cam_stats = camera.ptz_status().replace('\r', '').split('\n')
    return cam_stats[0].split('=')[1] != 'Idle'

def moveRight(camera):
    print("Moving Right...")
    camera.ptz_control_command(action="start", code="Right", arg1=0, arg2=0, arg3=0)
    time.sleep(0.5)
    camera.ptz_control_command(action="stop", code="Right")

def moveLeft(camera):
    print("Moving Left...")
    camera.ptz_control_command(action="start", code="Left", arg1=0, arg2=0, arg3=0)
    time.sleep(0.5)
    camera.ptz_control_command(action="stop", code="Left")

def moveUp(camera):
    print("Moving Up...")
    camera.ptz_control_command(action="start", code="Up", arg1=0, arg2=0, arg3=0)
    time.sleep(0.5)
    camera.ptz_control_command(action="stop", code="Up")

def moveDown(camera):
    print("Moving Down...")
    camera.ptz_control_command(action="start", code="Down", arg1=0, arg2=0, arg3=0)
    time.sleep(0.5)
    camera.ptz_control_command(action="stop", code="Down")  

def move(camera, targx, targy):
    while True:
        currLoc = camLoc(camera)
        if not currLoc is None:
            currx = currLoc[0]
            curry = currLoc[1]

            # Quick fix
            if currx == 180.0:
                moveLeft(camera)

            if ((currx > 180 and targx > 180) or (currx < 180 and targx < 180)) and abs(currx - targx) <= 5 and abs(curry - targy) <= 5:
                break
            else:
                # If both on left side
                if (currx > 180 and targx > 180) or (currx < 180 and targx < 180):
                    if abs(currx - targx) > 5:
                        if currx < targx:
                            moveRight(camera)
                        if currx > targx:
                            moveLeft(camera)
                else:
                    # If current on right side and targx is on left move left until current > 180
                    if currx < 180 and targx > 180:
                        moveLeft(camera)
                    # If current on left side and targx is on right move right until current < 180
                    if currx > 180 and targx < 180:
                        moveRight(camera)
                if abs(curry - targy) > 5:
                    if curry > targy:
                        moveUp(camera)
                    if curry < targy:
                        moveDown(camera)
            print("Current Position: " + str(currLoc) + "\nCurrent Target: (" + str(targx) + ", " + str(targy) + ")")

while True:
    # Moving the black amcrest camera to and back
    move(black_eye, 300, 20)
    move(black_eye, 70, 20)
    # Moving the white amcrest camera to and back
    move(white_eye, 2, 0)
    move(white_eye, 2, 50)
