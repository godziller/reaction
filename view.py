from tkinter import Tk, Frame, Label, Canvas
from model import Point
import random
import time
from datetime import datetime


class View(object):

    def __init__(self, controller):
        '''
        A simple view. A canvas and a label for game results.

        The CA calls for printing to terminal. But I decided to use the terminal for verbose output, and then
        use the label for a simpler game result.
        :param controller:
        '''
        self._controller = controller
        self._targetColor = 'Red'
        self._targetRadius = 30
        self._currentTarget = None

        root = Tk()
        root.title("Test Your reaction!!")
        root.maxsize(930, 620)

        canvas_frame = Frame(root, width=800, height=700, bg='red')
        canvas_frame.grid(row=0, column=1)
        canvas_frame.grid_propagate(False)

        # A label to display the results
        self._result_label = Label(root, text="Click to start!", font=("Arial", 14))
        self._result_label.grid(row=2, column=1)

        self._canvas = Canvas(canvas_frame, bg="white", width=600, height=600)
        self._canvas.bind("<Button-1>", self.mouseClicked)
        self._canvas.pack()



        root.mainloop()

    def mouseClicked(self, event):
        clickTime = datetime.now()

        '''
        The gameState will determine if a target has already been displayed and gmae is on ... or not
        
        If this is the first click, then we need to create a random circle.
        We have to do some funky scoping of randint to prevent the circle partially being drawn of the boundaries.
        
        '''

        if not self._controller.gameStarted():
            randx = random.randint(self._targetRadius, (self._canvas.winfo_width() - (self._targetRadius*2)))
            randy = random.randint(self._targetRadius, (self._canvas.winfo_height() - (self._targetRadius*2)))

            tlPoint = Point(randx, randy)
            brPoint = Point(randx + (self._targetRadius*2), randy + (self._targetRadius*2))

            time.sleep(random.randint(5, 10))

            self._controller.addTarget(tlPoint, brPoint, self._targetColor)
            # saving the created circle just so we can delete is later in the game.
            self._currentTarget = self._canvas.create_oval(randx, randy, brPoint.x, brPoint.y, fill=self._targetColor)
        else:
            x, y = event.x, event.y
            point = Point(x, y)
            print(f"Mouse clicked at: ({x}, {y})")
            dob = self._controller.getTarget().dob
            reaction_time = (clickTime - dob).total_seconds()

            # Check if the click was inside the target
            if self._controller.isInside(point):
                result_text = f"Reaction time: {reaction_time:.3f} seconds - HIT!:  Click to go again"
            else:
                result_text = f"Reaction time: {reaction_time:.3f} seconds - Miss: Click to go again"
            self._result_label.config(text=result_text)

            self._canvas.delete(self._currentTarget)
            self._controller.removeTarget()



