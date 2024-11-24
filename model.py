import shelve
from datetime import datetime
import math
import unittest


class Model(object):

    def __init__(self):

        self._target = None
        self._gameState = 0

    def addTarget(self, topleftPoint, bottomrightPoint, color):
        '''
        This will simply create a new circle - a target - and update the game state

        The gameState is a simple 1/0 to indicate if there is a target to hit or not.
        When we add a target, we move the gameState to 1
        :param topleftPoint: top left x,y of box for circle
        :param bottomrightPoint: bottom right x,y point of box for circle
        :param color:
        :return:
        '''
        self._gameState = 1
        self._target = Circle(topleftPoint, bottomrightPoint, color)

    def removeTarget(self):
        '''
        Simple operation to remove the target and reset the game state so we can game again.
        :return:
        '''
        self._gameState = 0
        del(self._target)

    def getTarget(self):
        return self._target

    def updateColor(self, color):
        self._target.updateColor(color)

    def gameStarted(self):
        '''
        simple helper function to return what the game state is in.
        :return: True/False
        '''
        if self._gameState == 0:
            return False
        else:
            return True

    def isInside(self, point):
        '''
        THis function is called to check if a Point is inside the Circle's boundary

        We calculate the distance using simple pythagorous from the center of the circle to the Point.
        If that distance is less than the circle radius, then the point is inside , otherwise outside.
        :param point:
        :return:
        '''
        if self._target is None:
            raise ValueError("No target available.")

        centre = self._target.centre
        print('Center x:' +  str(centre.x))
        print('Center y:' + str(centre.y))
        distance = math.sqrt((centre.x - point.x) ** 2 + (centre.y - point.y) ** 2)
        print(distance)
        print(self._target.radius)
        if distance < self._target.radius:
            print("inside")
            return True
        else:
            print("outside")
            return False

class Point(object):
    '''
    Reusing the Point class from Labs

    '''
    def __init__(self, xval, yval):
        self._x = xval
        self._y = yval

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, xval):
        self._x = xval

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

class Circle(object):
    '''
    We simplify our code from the Lab examples.

    The CA is only about circles, so we don't need the generic Shape Class from the Labs.
    THe object creation time - date of birth (dob) is recorded when the object is created.
    This can be used for calculating the reaction time later in the game.
    Less code = Less bugs.
    '''
    def __init__(self, tlPoint, brPoint, colour):
        self._color = colour
        self._radius = (brPoint.x - tlPoint.x) / 2
        self._centre = Point(brPoint.x - self._radius, brPoint.y - self._radius)
        self._dob = datetime.now()  # record when the shape was created.
        print("printing circle creation")
        print(brPoint.x)
        print(brPoint.y)
        print(tlPoint.x)
        print(tlPoint.y)
        print(self._centre.x)
        print(self._centre.y)
        print(self._radius)
        print(self._dob)

    @property
    def radius(self):
        return self._radius
    @property
    def centre(self):
        return self._centre
    @property
    def dob(self):
        return self._dob
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color


