"""Narit Trikasemsak
CS152 A 
Final Project
December 10, 2021
File for the object classes to be used in the simulations. 
Cannot be run from terminal. 
"""


import graphicsPlus as gr 

class Thing:
    def __init__(self, win, the_type):
        """Initialization for the parent function win. Takes in graphiwn object and string the type. """
        self.type = the_type
        self.win = win
        self.vis = []
        self.color = (0,0,0)
        

    def getColor(self):
        """Getter function, returns tuple for rgb color"""
        return self.color
    

    def setColor(self,c):
        """Setter functino for color. Takes in tuple c"""
        self.color = c
        if self.color != None:
            for item in self.vis:
                item.setFill(gr.color_rgb(c[0],c[1],c[2]))
    

    def getPosition(self):
        """getter function for position that returbs a tuple."""
        return (self.position[0],self.position[1])


    def draw(self):
        """Function to draw object in self.vis"""
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True


    def undraw(self):
        """Function to undraw object in self.vis"""
        for item in self.vis:
            item.undraw()
        self.drawn = False

class Path(Thing):
    def __init__(self, win, x0, y0, color = (0, 105, 148)):
        """Initialization function for child class Path block.Takes in win, and x and y coordinates and color"""
        Thing.__init__(self, win, "path")
        self.x = x0
        self.y = y0
        self.setColor(color)
        self.reshape()
    

    def reshape(self):
        """Function to draw/update the object"""
        upperCorn = gr.Point(self.x, self.y)
        lowerCorn = gr.Point(self.x + 50, self.y - 50)	
        self.vis = [gr.Rectangle(upperCorn,lowerCorn)]
        for i in self.vis:
            i.setFill("lightblue")
        self.draw()


class Iceberg (Thing):
    def __init__(self, win, x0, y0, color = (112,128,144)):
        """Initialization function for child class block. Takes in win, and x and y coordinates and color"""
        Thing.__init__(self, win, "path")
        self.x = x0
        self.y = y0
        self.setColor(color)
        self.reshape()
    

    def reshape(self):
        upperCorn = gr.Point(self.x, self.y)
        lowerCorn = gr.Point(self.x + 50, self.y - 50)	
        self.vis = [gr.Rectangle(upperCorn,lowerCorn)]
        for i in self.vis:
            i.setFill("slategray")
        self.draw()


class Start (Thing):
    def __init__(self, win, x0, y0, color = (112,128,144)):
        """Initialization function for child class block.Takes in win, and x and y coordinates and color"""
        Thing.__init__(self, win, "path")
        self.x = x0
        self.y = y0
        self.setColor(color)
        self.reshape()
    
    def reshape(self):
        """Function to draw/update the object"""
        upperCorn = gr.Point(self.x, self.y)
        lowerCorn = gr.Point(self.x + 50, self.y - 50)	
        self.vis = [gr.Rectangle(upperCorn,lowerCorn)]
        for i in self.vis:
            i.setFill("green")
        self.draw()
        
class End (Thing):
    def __init__(self, win, x0, y0, color = (112,128,144)):
        """Initialization function for child class block"""
        Thing.__init__(self, win, "path")
        self.x = x0
        self.y = y0

        self.setColor(color)
        self.reshape()
    
    def reshape(self):
        """Function to draw/update the object"""
        upperCorn = gr.Point(self.x, self.y)
        lowerCorn = gr.Point(self.x + 50, self.y - 50)	
        self.vis = [gr.Rectangle(upperCorn,lowerCorn)]
        for i in self.vis:
            i.setFill("red")
        self.draw()

class Boat(Thing):
    def __init__(self, win, x0, y0):
        """Initilization functino for the boat object. Takes in win, and x and y coordinates."""
        Thing.__init__(self, win, "path")
        self.x = x0
        self.y = y0
        self.reshape()
    

    def reshape(self):
        """Function to draw/update the object"""
        #undraw the obj if it is drawn
        upperCorn = gr.Point(self.x + 15, self.y - 30)
        lowerCorn = gr.Point(self.x + 30, self.y - 20)
        frontVer = gr.Point(self.x + 30, self.y - 30)
        frontTip = gr.Point(self.x + 35, self.y - 25)
        backVer = gr.Point(self.x + 15, self.y - 20)
        backTip = gr.Point (self.x+10, self.y - 25)
        self.vis = [gr.Rectangle(upperCorn,lowerCorn), gr.Polygon(lowerCorn, frontTip, frontVer), gr.Polygon(upperCorn, backTip, backVer)]
        for i in self.vis:
            i.setFill("red")
        self.draw()
        #     draw the object


# def test():
#     """Test functino for the Zelle objects. Creates a window and calls each of the objects. """
#     win = gr.GraphWin('Icebreaker', 1000, 500, False)
#     win.setBackground("white")
#     path1 = Path(win, 0,50)
#     path2 = Path(win, 50, 50)
#     path1.reshape()
#     path2.reshape()
#     # path3 = pho.Path(win, 0, 100)
#     # path3.reshape()
#     iceberg1 = Iceberg(win, 200, 250)
#     iceberg1.reshape()
#     boat1 = Boat(win, 0, 50)
#     boat1.reshape()
#     win.getKey()
#     boat1.undraw()
#     win.getMouse()
#     win.close()

# if __name__ == "__main__":
#     test()


