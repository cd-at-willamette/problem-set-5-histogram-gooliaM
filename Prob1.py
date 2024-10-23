from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    counts = [[] for _ in range(10)]
    for i in range(len(data)):
        for value in PI_DIGITS:
            if value == i:
                new_list = []
                counts[i].append(value)
    return counts

    pass

#1b
def print_histogram(hist:list[int]) -> None:
    for i in range(len(hist)):
        print('*' * len(hist[i]))
    pass

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    gw = GWindow(width, height)

    max = 0
    for i in range(len(hist)):
        for j in range(len(hist[i])):  
            if hist[i][j] > max: 
                max = hist[i][j]

    col_width = width / len(hist)
    
    for i in range(len(hist)): #This code was made by chatgpt
        
        count = len(hist[i])  # Get the count of occurrences for this index
        rect_height = (height / max) * count  # Scale height based on the count
        x = col_width * i  # Calculate x position for each column
        y = height - rect_height  # Position from the bottom

        color = 'red'  # Example color
        my_rect(x, y, col_width, rect_height, color)

    pass

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test

