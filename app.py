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
        self.x_axis = [i for i in range(x)]
        self.y_axis = [k for k in range(y)]
        self.len_x = len(self.x_axis)
        self.len_y = len(self.y_axis)
        self.final_number = ((x - 1) * (y - 1)) + (x - 1) + (y - 1)
        self.integer_list = [i for i in range(self.final_number + 1)]
        self.table = [[_ for _ in range(x)] for _ in range(y)]
        # matrix = 


    def create_table(self):
        """
        This function creates coordinates table for numbers resulting in a spiral to be placed.
        Then place the correct values to each coordinates to create a spiral.
        """
        # creating coordinates of numbers in the table
        for item_x in self.y_axis:
            for item_y in self.x_axis:
                self.table.append([item_x, item_y])

        
        # prettifying the table and its coordinates for presentation purposes
        count = 0
        for coordinates in self.table:
            # if x coordinates are the same, print them on the same line
            # else print them on a newline
            if self.table[count][0] <= self.table[self.len_x - count][0]:
                print(coordinates, end=' ')
            else:
                print('\n')
                print(coordinates, end=' ')
                count = 0
            count += 1

    def add_values(self):
        """ this method is created to add values to coordinates in the table to create spiral """
        # adding value to each coordinates
        m = 10
        n = 8
        value = 0
        left = 0
        top = 0
        right = m - 1
        bottom = n - 1
        direction = 'right'

        while (left <= right and top <= bottom):
            if direction == 'right':
                for i in range(left, right + 1):
                    self.table[top][i] = value
                    value += 1
                top += 1
                direction = 'down'

            if direction == 'down':
                for i in range(top, bottom + 1):
                    self.table[i][right] = value
                    value += 1
                right -= 1
                direction = 'left'

            if direction == 'left':
                for i in range(right, left -1 , -1):
                    self.table[bottom][i] = value
                    value += 1
                bottom -= 1
                direction = 'top'

            if direction == 'top':
                for i in range(bottom, top - 1, -1):
                    self.table[i][left] = value
                    value += 1
                left += 1
                direction = 'right'

        for item in self.table:
            print(item, end='\n')

    def get_layouts(self):
        "this method returns"
        for item in self.table:
            print(item)

    def get_value_layouts():
        pass


spiral = IntegerSpiral(4, 3)
spiral.create_table()
# spiral.add_values()
