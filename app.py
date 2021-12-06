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
        # this line creates the layout using basic matrix in math.
        self.layout = [[0 for _ in range(x)] for _ in range(y)]

    def add_values(self):
        """ this method is created to add values to coordinates in the table to create spiral """
        # adding value to each coordinates
        m = self.x
        n = self.y
        integer = 0
        left = 0
        up = 0
        right = m - 1
        down = n - 1
        direction = 'right'

        while (left <= right and up <= down):
            if direction == 'right':
                for i in range(left, right + 1):
                    self.layout[up][i] = integer
                    integer += 1
                up += 1
                direction = 'down'

            if direction == 'down':
                for i in range(up, down + 1):
                    self.layout[i][right] = integer
                    integer += 1
                right -= 1
                direction = 'left'

            if direction == 'left':
                for i in range(right, left -1 , -1):
                    self.layout[down][i] = integer
                    integer += 1
                down -= 1
                direction = 'top'

            if direction == 'top':
                for i in range(down, up - 1, -1):
                    self.layout[i][left] = integer
                    integer += 1
                left += 1
                direction = 'right'

    def get_layouts(self):
        " this method is used to print the layout inside the self.layout list. "
        for arr in self.layout:
            # print("index" , *[i for i in range(self.len_x)], sep=' | ')
            print(*arr, sep='\t')

    def get_layouts_by_value(self, x_coor, y_coor):
        return "The value held by x: '{}', y: '{}' coordinates is '{}'".format(x_coor, y_coor, self.layout[y_coor][x_coor])


spiral = IntegerSpiral(10, 8)
spiral.add_values()
spiral.get_layouts()
print(spiral.get_layouts_by_value(9, 7))
