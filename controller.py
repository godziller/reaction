class Controller(object):

    def __init__(self, model):
        self._model = model

    def addTarget(self, topleftPoint, bottomrightPoint, color):
        self._model.addTarget(topleftPoint, bottomrightPoint, color)

    def updateColor(self, color):
        self._model.updateColor(color)

    def removeTarget(self):
        self._model.removeTarget()

    def getTarget(self):
        return self._model.getTarget()

    def gameStarted(self):
        return self._model.gameStarted()

    def isInside(self, point):
        return self._model.isInside(point)

