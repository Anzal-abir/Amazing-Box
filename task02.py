#task 02
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

winWidth, winHeight= 600, 600

Points=[]
Directions=[]
Colors=[]
speed= 2
blink_status='off'
should_blink='no'
Freeze=False

#Drawing The Points
def Draw_Point(x, y, color):
    glPointSize(7)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x,y) 
    glEnd()

#Defining Point pixels, Direction and Color
def Create_Point(x,y):
   global Points, Directions, Colors
   Points+=[[x,y]]
   Directions+=[[random.choice([-1,1]),random.choice([-1,1])]]
   Colors+=[list(float(random.random()) for _ in range(3))]


#Timer Blink
def Blink(value):
    global blink_status
    if blink_status=='off':
        blink_status='on'
    elif blink_status=='on':
        blink_status='off'
    if should_blink=='yes':
        glutTimerFunc(500, Blink, 0)

#Special Key Handler
def Speed_Control(key, x, y):
    global  Directions,speed, Freeze
    if Freeze==False:
        if key == GLUT_KEY_DOWN:
            for i in range (len(Directions)):
                if abs(Directions[i][0])>=0.25:
                    Directions[i][0]/=speed
                    Directions[i][1]/=speed
        elif key == GLUT_KEY_UP:
            for i in range (len(Directions)):
                if abs(Directions[i][0])<=1:
                    Directions[i][0]*=speed
                    Directions[i][1]*=speed
    
#Keyboard Handler
def Freeze_All(key, x, y):
    global Freeze
    if key==b" ":
        if Freeze==False:
            Freeze=True
        else:
            Freeze=False

#Mouse Handler
def convert_coordinate(x, y):
    global winWidth, winHeight
    a = x - (winWidth / 2)
    b = (winHeight / 2) - y
    return a, b

def mouseClick(button, state, x, y):
    global should_blink,blink_status, Freeze
    if Freeze==False:
        x, y = convert_coordinate(x, y)

        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                if should_blink== 'no':
                    should_blink='yes'
                    glutTimerFunc(1000, Blink, 0)
                    print("Points Started Blinking")
                else:
                    should_blink='no'
                    blink_status='on' 
                    print("Points Stopped Blinking")
                

        elif button == GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN:
                print(f"Point created at: {(x, y)} coordinate")
                Create_Point(x,y)
      
#Idle 
def animate():
    global Points ,Directions, winWidth, winHeight, Freeze
    if Freeze==False:
        for i in range (len(Points)):
            Points[i][0]+=Directions[i][0]
            Points[i][1]+=Directions[i][1]
            if Points[i][0] >= (winWidth/2) or Points[i][0] <= (-1*winWidth/2):
                Directions[i][0] *= -1
            if Points[i][1] >= (winHeight/2) or Points[i][1] <= (-1*winHeight/2):
                Directions[i][1] *= -1

        glutPostRedisplay()  


#Display
def showScreen():
    global Points, Colors , blink_status
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if blink_status=="off":
        for point in range(len(Points)):
            Draw_Point(Points[point][0],Points[point][1], Colors[point])
    else:
        for point in range(len(Points)):
            Draw_Point(Points[point][0],Points[point][1], [0,0,0])
    glutSwapBuffers()


#Main
def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 300, -300, 300, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) 
glutInitWindowPosition(600, 250)
wind = glutCreateWindow(b"Amazing Box") #window name

glutDisplayFunc(showScreen)
glutMouseFunc(mouseClick)
glutSpecialFunc(Speed_Control)
glutKeyboardFunc(Freeze_All)
glutIdleFunc(animate)
glutMainLoop()