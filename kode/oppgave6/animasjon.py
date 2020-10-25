from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

import math

import pickle
from punktgenerering import load_data
from oppgave1.oppgave1_funksjoner import M, L, R
import datetime

time = 0
start_time = datetime.datetime.now()


def cylinder_between(pointA, pointB, rad):
    """
    Denne funksjonen tegner en sylinder som starter i pointA og slutter i PointB med radius radS
    :param pointA: punkt midt på starten av sylinderet
    :param pointB: punkt midt på enden av sylinderet
    :param rad: radiusen til sylinderet:
    :return: none
    """
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
    """
    denne funksjonen gjør noe nødvendig preprossesering i opengl
    med tanke på farger, perspektiv etc
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, wnd_w / wnd_h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, -2, 0, 0, 0, 0, 0, 0, 1)

    glClearColor(0.5, 0.5, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # causes wire frame
    glColor(1, 1, 0.5)

    # glRotatef(-30.0, 0.0, 0.0, 1.0)
    glRotatef(30.0, 1.0, 0.0, 0.0)
    glTranslatef(-12.0, 36.0, -18.0)
    glRotatef(-30.0, 0.0, 0.0, 1.0)


def drawAxis():
    """
    tegner de tre aksene i rommet
    x <-- rød
    y <-- grønn
    z <-- blå
    """
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
    """
    Denne funksjonen tegner selve tnøkkelen, forenklet til to sylindere
    :param W: punktene som definerer t-nøkkelen sin posisjon på et tidspunkt
    :return: none
    """
    W = W.T
    punktA = normalize(W[0])
    punktB = normalize(W[1])

    cylinder_between(
        punktA * R[0] - punktA * (center_of_mass),
        -punktA * (center_of_mass) + punktA * (L[1]) + (punktA * R[0]),
        R[1],
    )
    cylinder_between(
        -punktB * (L[0] / 2) - punktA * (center_of_mass),
        punktB * (L[0] / 2) - punktA * (center_of_mass),
        R[0],
    )


def draw():
    """
    denne funksjonen kaller på preprosseseringen og tegningen
    :return: none
    """
    prepare()
    drawAxis()
    end_time = datetime.datetime.now()
    time_index = (end_time - start_time).total_seconds() * 5
    glColor(1.0, 0.0, 0.0)
    drawTHandle(getWvalue(time_index, W_rk45, t_rk45))
    glTranslate(10.0, 0.0, 0.0)
    glColor(0.0, 1.0, 0.0)
    drawTHandle(getWvalue(time_index, W_rk4, t_rk4))
    glTranslate(10.0, 0.0, 0.0)
    glColor(0.0, 0.0, 1.0)
    drawTHandle(getWvalue(time_index, W_euler, t_euler))
    glTranslate(10.0, 0.0, 0.0)
    glutSwapBuffers()
    glutPostRedisplay()


def getWvalue(time_index, W, t):
    """
    :param time_index: indeksen til tidspunktet
    :param W: listen over punktene til de ulike tidspunktene
    :param t: listen over timestamps som tilhører punkter
    :return: punktene som definerer t-nøkkelen ved et gitt tidspunkt
    """
    return W[int((((time_index % int(t[-1])) / (t[-1] - t[0])) * len(W)))]


def normalize(vector):
    """
    :param vector: inputvektoren
    :return: inputvektoren normalisert til å ha lengde 1
    """
    length = np.sqrt(sum(i ** 2 for i in vector))
    return vector / length


def calculate_center_of_mass(mass, radius, length):
    """
    :param mass: liste med massen til de to sylindrene
    :param radius: liste med radiusen til de to sylindrene
    :param length: lengden til de to sylindrene
    :return: massesenteret til t-nøkkelen
    """
    return (mass[1] * (R[0] + L[1] / 2)) / (sum(i for i in mass))


if __name__ == "__main__":
    oppgave = input("Oppgave nr [a, b, c]: ")
    W_rk45, W_rk4, W_euler, t_rk45, t_rk4, t_euler, E = load_data(
        f"oppgave{oppgave}.npy"
    )
    wnd_w, wnd_h = 1920, 1080
    center_of_mass = calculate_center_of_mass(M, R, L)
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(wnd_w, wnd_h)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(f"Oppgave {oppgave}")
    glutDisplayFunc(draw)
    glutMainLoop()
