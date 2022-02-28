"""
Narit Trikasemsak
CS152A Final Project
December 1, 2021
File to make the multidimensional array for the icebreaker routing project. 
Does not need to be run from terminal, can be done using python3 arctic.py . 
eg. python3 arctic.py )
"""


import graphicsPlus as gr
import objects as pho
import array as arr

def visualize(array):
    """Function to create the basic window for the arctic ice field. Takes in an Map object array and returns a graphWin object """
    rows = array.rows
    columns = array.columns
    #since each block on map is 50 x 50, multiply the amount of blocks by 50 to get dimesnions of window
    width = 50 * rows
    height = 50 * columns
    #create window and return
    win = gr.GraphWin("Icebreaker", width, height, False)
    win.setBackground("white")
    return win


def addBlocks(win, array):
    """Function to turn the Map array into a visual version. Takes a GraphWin object and Map object array and returns a list of 
    block objects to be printed in main."""
    blocks = []
    #loop through each block in the array
    for i in range(len(array.array)):
        for j in range(len(array.array[i])):
            #if the current index is empty, insert a path block object
            if array.array[i][j] == 0:
                print(i,j)
                path = pho.Path(win, i*50, (j+1)*50)
                blocks.append(path)
            #if the current index has an obstacle, ie == 1, insert iceberg object.
            elif array.array[i][j] == 1:
                iceberg = pho.Iceberg(win, i*50, (j+1)*50)
                blocks.append(iceberg)
    return blocks


def setPoints(win, array):
    """Function to set the start and goal points of the map. Takes in a GraphWin object and map Object. Marks the start green on the map
    and marks the end red depending on where the user clicks. """
    #start / end points
    #wait for user to click
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    #convert it into the array's x and y coordinate system
    x = x//50
    y = y//50
    #insert a start block using the x and y conversion
    start = pho.Start(win, (x) * 50, (y+1)*50)
    #use setStart function to set x and y of start point
    array.setStart(int(x),int(y))
    #wait for user to click on endpoint 
    click = win.getMouse()
    #get x and y coordinates and convert it into the map's system.
    x = click.getX()
    y = click.getY()
    x = x//50
    y = y//50
    #use built in function to set x and y of goal and place End object block. 
    array.setGoal(int(x),int(y))
    end = pho.End(win, (x) * 50, (y+1)*50)
    
    
def moveShip(win, array):
    """Function that takes in a window object, and an Map called array. Returns a list of boat objects along the optimal route
    calculated by the wavefront algorithm"""
    #find the optimal route using wavefront function
    route = array.wavefront()
    boats = []
    #loop through the coordinates
    for i in range(len(route)):
        for j in range(len(route[i])):
            #add a boat object at each point in the route
            boat = pho.Boat(win, route[i][0]*50, (route[i][1]+1)*50)
            boats.append(boat)
    #return the list of boats created
    return boats


def main(obstacles):
    """Main function to make everything come together and create the map. Takes in obstacles, number of obstacles to create. 
    Creates a window of Zelle objects to represent the ice field and icebreaker. """
    #create the map
    map = arr.Map(30, 15)
    map.createArray()
    map.setObstacles(obstacles)
    #create the visual representation for the map and blcoks
    win = visualize(map)
    blocks = addBlocks(win, map)
    #draw the blocks onto the window
    for i in blocks:
        i.reshape()
    #let the user set start/end points
    setPoints(win, map)
    #find the optimal route for the ship
    route = moveShip(win, map)
    #draw the icebreakers going through the route
    for i in route:
        i.reshape()
    # completion message. Ask if the user wants to continue
    length = int(len(map.wavefront()))
    finish = gr.Text(gr.Point(750,290), "The wavefront algorithm found the shortest path for the Icebreaker to be %i blocks. Press r to restart. Press any other key to stop" %(length))
    finish.setStyle("bold")
    finish.setSize(20)
    finish.draw(win)
    #if the user presses r, recursively calls the main function and adds 10 o bstacles
    if win.getKey() == "r":
        win.close()
        main(obstacles+30)
    #else, closes the window. 
    else:
        win.close()


if __name__ == "__main__":
    main(50)
