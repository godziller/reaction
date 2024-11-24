from model import Model
from controller import Controller
from view import View

if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    view = View(controller)