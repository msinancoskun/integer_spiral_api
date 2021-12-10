class IntegerSpiral:

    def __init__(self, x, y):
        """
        Initializing x, y coordinates.
        Args:
            x (int): x coordinates
            y (int): y coordinates
        """
        self.x = x
        self.y = y
        self.layoutId_match = {}
        # this line creates the layout using basic matrix in math.
        self.layout = [[0 for _ in range(x)] for _ in range(y)]

    def create_layout(self):
        """ this method is created to add values to coordinates in the table to create spiral """
        # adding value to each coordinates
        m = self.x
        n = self.y
        spiral_value = 0
        left = 0
        up = 0
        right = m - 1
        down = n - 1
        direction = 'right'

        # ID created using x, y coordinates with '-0000' at the end of it.
        self.layoutId = str(m) + str(n) + "-0000" 

        while (left <= right and up <= down):
            if direction == 'right':
                for i in range(left, right + 1):
                    self.layout[up][i] = spiral_value
                    spiral_value += 1
                up += 1
                direction = 'down'

            if direction == 'down':
                for i in range(up, down + 1):
                    self.layout[i][right] = spiral_value
                    spiral_value += 1
                right -= 1
                direction = 'left'

            if direction == 'left':
                for i in range(right, left -1 , -1):
                    self.layout[down][i] = spiral_value
                    spiral_value += 1
                down -= 1
                direction = 'top'

            if direction == 'top':
                for i in range(down, up - 1, -1):
                    self.layout[i][left] = spiral_value
                    spiral_value += 1
                left += 1
                direction = 'right'

        self.layoutId_match[self.layoutId] = self.layout

        return self.layoutId

    def get_layouts(self):
        """
            this method is used to print the layout with layoutId.
        """
        return self.layoutId_match
        
    def get_layouts_by_value(self, layoutId, x_coor, y_coor):
        """
        This method is used to return a certain element using x,y coordinates.
        Args:
            x_coor (int): x coordinate of the return value
            y_coor (int): y coordinate of the return value

        Returns:
            str: the value of x, y coordinates with the statement.
        """
        if layoutId == self.layoutId:
            return "The value held by x: '{}', y: '{}' coordinates is '{}'".format(x_coor, y_coor, self.layout[y_coor][x_coor])


# Test cases
# spiral = IntegerSpiral(10, 6)
# print(spiral.create_layout())
# print(spiral.get_layouts())
# print(spiral.get_layouts_by_value("106-0000", 5, 2))


# spiral1 = IntegerSpiral(10, 8)
# spiral1.create_layout()
# spiral1.get_layouts()
# print(spiral1.get_layouts_by_value("108-0000", 4, 5))


# spiral2 = IntegerSpiral(3, 3)
# spiral2.create_layout()
# spiral2.get_layouts()
# print(spiral2.get_layouts_by_value("64-0000", 3, 2))


# spiral3 = IntegerSpiral(8, 10)
# spiral3.create_layout()
# spiral3.get_layouts()
# print(spiral3.get_layouts_by_value("810-0000", 1, 0))
