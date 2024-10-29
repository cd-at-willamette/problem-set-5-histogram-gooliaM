#Done with Addison Thompson
#made by julia martin
#and like one line from chatgpt

from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    counts = [0] * 10
    for value in data:
        if value == 0:
            counts[0]+=1
        elif value == 1:
            counts[1]+=1
        elif value == 2:
            counts[2]+=1
        elif value == 3:
            counts[3]+=1
        elif value == 4:
            counts[4]+=1
        elif value == 5:
            counts[5]+=1
        elif value == 6:
            counts[6]+=1
        elif value == 7:
            counts[7]+=1
        elif value == 8:
            counts[8]+=1
        elif value == 9:
            counts[9]+=1
        
    return counts
    pass

#1b
def print_histogram(hist:list[int]) -> None:
    for i in range(len(hist)):
        print('*' * hist[i])
    pass

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    gw = GWindow(width, height)

    max_count = max(hist)

    col_width = width / len(hist)
    
    for i in range(len(hist)): #This code was made by chatgpt
        count = hist[i]  # Get the count of occurrences for this index
        rect_height = (height / max_count) * count  # Scale height based on the count
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

