from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

import math

import pickle
from punktgenerering import load_data
import datetime

time = 0
start_time = datetime.datetime.now()


def drawCylinder(punktA, punktB, radius):
    gluCylinder()


def cylinder_between(pointA, pointB, rad):
    v = [pointB[0] - pointA[0], pointB[1] - pointA[1], pointB[2] - pointA[2]]
    v = np.array(v, dtype=np.double)
    height = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    axis = (
        (1, 0, 0)
        if math.hypot(v[0], v[1]) < 0.001
        else np.cross(v, np.array([0, 0, 1]))
    )
    angle = -math.atan2(math.hypot(v[0], v[1]), v[2]) * 180 / math.pi

    glPushMatrix()
    glTranslate(pointA[0], pointA[1], pointA[2])
    glRotate(angle, *axis)
    glutSolidCylinder(rad, height, 32, 16)
    glPopMatrix()


def prepare():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, wnd_w / wnd_h, 0.1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, -2, 0, 0, 0, 0, 0, 0, 1)

    glClearColor(0.5, 0.5, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # causes wire frame
    glColor(1, 1, 0.5)

    #glRotatef(-30.0, 0.0, 0.0, 1.0)
    glRotatef(30.0, 1.0, 0.0, 0.0)
    glTranslatef(-2.0, 6.0, -3.0)
    glRotatef(-30.0, 0.0, 0.0, 1.0)


# x-rød
# y-grønn
# z-blå
def drawAxis():
    glPushMatrix()
    glColor(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1000.0, 0.0, 0.0)
    glEnd()
    glColor(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1000.0, 0.0)
    glEnd()
    glColor(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1000.0)
    glEnd()
    glPopMatrix()


def drawTHandle(W):
    W = W.T
    punktA = W[0]
    punktB = W[1]
    cylinder_between(punktA*0.3, punktA + (punktA*0.3), 0.3)
    cylinder_between(-punktB, punktB, 0.3)


def draw():
    prepare()
    drawAxis()
    end_time = datetime.datetime.now()
    time_index = (end_time - start_time).total_seconds() * 5
    glColor(1.0, 0.0, 0.0)
    drawTHandle(getWvalue(time_index, W_rk45))
    glTranslate(2.0, 0.0, 0.0)
    glColor(0.0, 1.0, 0.0)
    drawTHandle(getWvalue(time_index, W_rk4))
    glTranslate(2.0, 0.0, 0.0)
    glColor(0.0, 0.0, 1.0)
    drawTHandle(getWvalue(time_index, W_euler))
    glTranslate(2.0, 0.0, 0.0)
    glutSwapBuffers()
    glutPostRedisplay()


def getWvalue(time_index, W):
    return W[int((((time_index % int(t[-1])) / (t[-1] - t[0])) * len(W)))]


if __name__ == "__main__":
    oppgave = input("Oppgave nr [a, b, c]: ")
    W_rk45, W_rk4, W_euler, t, E = load_data(f"test{oppgave}.npy")
    wnd_w, wnd_h = 1920, 1080
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(wnd_w, wnd_h)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("cylinder")
    glutDisplayFunc(draw)
    glutMainLoop()