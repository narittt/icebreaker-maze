"""
Narit Trikasemsak
CS152A Final Project
December 1, 2021
File to make the multidimensional array for the icebreaker routing project. 
Cannot be run from terminal, part of the modular design. 
"""
import random
class Map:

    def __init__(self, rows = 10, columns = 10, obstacles = 10):
        """Initialization function for the map. Takes in rows, columns, and number of obstacles"""
        self.rows = rows
        self.columns = columns
        self.array = []
        self.obstacles = obstacles
        self.start = [0,0]
        self.goal = [rows-1, columns-1]

    def createArray(self):
        """Function to create the basic array, filling it up with zeros. Takes input for amount of rows and columns."""
        self.array = []
        fullList = self.array
        #loop through array and add each individual zero
        for i in range(self.rows):
            row = []                 
            for j in range(self.columns):
                row.append(0)
            fullList.append(row)
        self.array = fullList
    
    def getObstacles(self):
        """Getter function to return how many obstacles are in the array"""
        result = self.obstacles
        return result 

    def setObstacles(self, numObstacles):
        """Setter function to set obstacles. takes in number of obstacles and creates that many random ones and places it on the map"""
        #add a 1 to represent iceberg at each random x and y
        for i in range(numObstacles):
            randRow = random.randint(0, self.rows-1)
            randCol = random.randint(0, self.columns-1)
            self.array[randRow][randCol] = 1
    
    def getStart(self):
        """Getter function to return the coordinates of the starting point in a list"""
        result = self.start
        return result
    
    def getGoal(self):
        """Getter function to return the coordinates of the goal point in a list"""
        result = self.goal
        return result 
    
    def setStart(self, x, y):
        """Setter function to set the start coordinates of the map. Takes in x and y. sets the start point"""
        #removes old start coordinates (if any) and replaces it with an empty marker 0
        oldStart = self.start
        oldX = oldStart[0]
        oldY = oldStart[1]
        self.array[oldX][oldY] = 0 
        #sets the new start coordiante to have an S in the map
        self.start = [x,y]
        # self.array[x][y] = "S"
    
    def setGoal(self, x, y):
        """Setter function to set the goal coordinates of the map. takes in x and y. Sets the start point"""
        #removes old goal coordinates (if any) and replaces it with an empty marker 0
        oldGoal = self.goal
        oldX = oldGoal[0]
        oldY = oldGoal[1]
        self.array[oldX][oldY] = 0 
        #sets the new goal coordiante to have an S in the map
        self.goal = [x,y]
        # self.array[x][y] = "G"
    
    def wavefront(self):
        """Wavefront Algorithm borrowed from CS152 Team Design Challenge provided by Prof. Stephanie Doore"""
        
        '''Uses the wavefront algorithm to plan a path from the start position to the 
        goal position. Map must be a 2D list, goal should be a list of indices [row, col], and 
        start should be a list of indices [row, col]. Assumes obstacles have the value 1, and
        all empty cells have the value 0 within the 2D map list. Returns a nested list of 
        indices that can be followed from the start to the goal.'''

        # Create a COPY of the map so that we don't modify the original!
        #       Modifying the original would make it difficult to run the wavefront
        #       algorithm twice with different goal positions.
        mapOriginal = self.array
        map = []
        for r in range(len(mapOriginal)):
            map.append( mapOriginal[r][:] ) 

        # Initialize the goal's value to 2
        goal = self.goal
        rG = goal[0]
        cG = goal[1]
        map[rG][cG] = 2

        # Compute the shortest distance from the goal to each empty cell in the map.
        toDo = [ [rG, cG] ]
        while len(toDo) > 0:
            [ r, c ] = toDo.pop(0)
            # Check to see if the down, up, right, or left neighbors need to be updated
            for neighbor in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                rN = neighbor[0]
                cN = neighbor[1]
                if rN >= 0 and rN < len(map) and cN >= 0 and cN < len(map[0]):
                    # Only check the value of elements that exist
                    if (map[rN][cN] != 1) and ((map[r][c] + 1 < map[rN][cN]) or (map[rN][cN]==0)):
                        # This neighbor is not an obstacle and needs to be updated
                        map[rN][cN] = map[r][c] + 1     
                        # Now this neighbor's neighbors may need to be updated
                        if not( [rN,cN] in toDo ):
                            toDo.append( [rN,cN] )  
            #print("toDo:", toDo)     # uncomment this line if you want to see the toDo list grow and shrink   
            
        # Construct the shortest path from the start position to the goal.
        start = self.start
        r = start[0]
        c = start[1]
        path = [ [r, c] ]
        distance = map[r][c]
        rNext = r
        cNext = c
        while distance > 2:
            # Take a step in the direction with the minimum distance metric
            for neighbor in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                rN = neighbor[0]
                cN = neighbor[1]
                if rN >= 0 and rN < len(map) and cN >= 0 and cN < len(map[0]):
                    # Only check the value of elements that exist
                    if 1 <  map[rN][cN] and  map[rN][cN] < distance:
                        distance = map[rN][cN]
                        rNext = rN
                        cNext = cN
            r = rNext
            c = cNext
            path.append( [r, c] )

        return path
                


def test():
    """test code for the Map objects"""
    a = Map(10,10)
    a.createArray()
    a.setObstacles(20)
    a.setStart(0,4)
    a.setGoal(9,8)
    print(a.array)
    print(a.wavefront())

if __name__ == "__main__":
    test()