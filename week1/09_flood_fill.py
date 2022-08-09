'''
Solution 1:
Let n = number of rows in the image.
Let m = number of columns in the image.
Time Complexity: O(n * m)
Space Complexity: O(max(n, m))
'''
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image
    return self.floodFillHelper(image, sr, sc, color, image[sr][sc])

def floodFillHelper(self, image: List[List[int]], sr: int, sc: int, color: int, fill_color):
    source_color = fill_color
    
    top_color = None
    if sr - 1 >= 0:
        top_color = image[sr - 1][sc]
    
    right_color = None
    if sc + 1 < len(image[sr]):
        right_color = image[sr][sc + 1]
    
    bottom_color = None
    if sr + 1 < len(image):
        bottom_color = image[sr + 1][sc]
    
    left_color = None
    if sc - 1 >= 0:
        left_color = image[sr][sc - 1]
    
    new_image = None
    
    if top_color is not None and top_color == source_color:
        image[sr - 1][sc] = color
        self.floodFillHelper(image, sr - 1, sc, color, fill_color)
        
    if right_color is not None and right_color == source_color:
        image[sr][sc + 1] = color
        self.floodFillHelper(image, sr, sc + 1, color, fill_color)
        
    if bottom_color is not None and bottom_color == source_color:
        image[sr + 1][sc] = color
        self.floodFillHelper(image, sr + 1, sc, color, fill_color)
        
    if left_color is not None and left_color == source_color:
        image[sr][sc - 1] = color
        self.floodFillHelper(image, sr, sc - 1, color, fill_color)
    
    image[sr][sc] = color
    
    return image

'''
Solution 2:
Let n = number of rows in the image.
Let m = number of columns in the image.
Time Complexity: O(n * m)
Space Complexity: O(n * m)
'''
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = Queue()
        seen = set()
        queue.put([sr, sc])
        color_to_fill = image[sr][sc]
        while not queue.empty():
            curr_row, curr_col = queue.get()
            if (curr_row, curr_col) in seen:
                continue
            seen.add((curr_row, curr_col))
            if image[curr_row][curr_col] != color_to_fill:
                continue

            image[curr_row][curr_col] = color

            if curr_row - 1 >= 0:
                queue.put((curr_row - 1, curr_col))

            if curr_col + 1 < len(image[curr_row]):
                queue.put((curr_row, curr_col + 1))

            if curr_row + 1 < len(image):
                queue.put((curr_row + 1, curr_col))

            if curr_col - 1 >= 0:
                queue.put((curr_row, curr_col - 1))

        return image