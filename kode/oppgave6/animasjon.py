from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

import math

import pickle
from punktgenerering import load_data


def drawCylinder(punktA, punktB, radius):
    gluCylinder()


def cylinder_between(pointA, pointB, rad):
    v = [pointB[0] - pointA[0], pointB[1] - pointA[1], pointB[2] - pointA[2]]
    v = np.array(v, dtype=np.double)
    print(v)
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


def draw():

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

    W, t, E = load_data("big.npy")

    punktA = W[0].T[0]
    punktB = W[0].T[1]
    print(punktA)
    print(punktB)
    cylinder_between(punktA, punktB, 0.3)

    glutSwapBuffers()
    glutPostRedisplay()


wnd_w, wnd_h = 300, 300
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(wnd_w, wnd_h)
glutInitWindowPosition(50, 50)
glutCreateWindow("cylinder")
glutDisplayFunc(draw)
glutMainLoop()