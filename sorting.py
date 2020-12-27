from tkinter import *
from tkinter import ttk
import random
import time

# Plotting the UI
origin=Tk()
origin.title('Sorting Algorithm Visualizer')
origin.maxsize(1000,600)
origin.config(bg='black')

# Variables
selected_alg = StringVar()

# Plotting array
def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 980
    x_width = c_width / (len(data) + 1)
    offset = 5
    spacing = 3
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    origin.update_idletasks()

# Bubble Sort
def bubble_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else '#dface8' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, ['#81e075' for x in range(len(data))])

# Selection Sort
def selection_sort(data,drawData,timeTick):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
                drawData(data, ['blue' if x == j or x == i else '#dface8' for x in range(len(data))] )
        data[i], data[min_idx] = data[min_idx], data[i]
    time.sleep(timeTick)
    drawData(data, ['#81e075' for x in range(len(data))])

# Merge Sort
def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getcolor_array(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

# Quick Sort
def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)

# Insertion Sort
def insertion_sort(data, drawData, timeTick):
    colorarray=[]
    for x in range (len(data)):
        colorarray.append('#dface8')
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        colorarray[i]='red'
        while j >= 0 and key < data[j] :
                data[j + 1] = data[j]
                j -= 1
                colorarray[j+1]='blue'
                drawData(data, colorarray )
        data[j + 1] = key
        time.sleep(timeTick)
        drawData(data, ['#81e075' for x in range(len(data))])


def getcolor_array(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

# Generates Array
def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['#FFFF00' for x in range(len(data))])

# Choosing the alogrithm and running the respective sorting code
def StartAlgorithm():
    global data
    if not data: return

    if alg_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())

    elif alg_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif alg_menu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    elif alg_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, speedScale.get())
    elif alg_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])

# Base Layout
ui_frame = Frame(origin, width=1000, height=200,bg='grey')
ui_frame.grid(row=0,column=0,padx=10,pady=10)

canvas= Canvas(origin,width=1000,height=380,bg='black')
canvas.grid(row=1,column=0,padx=10,pady=10)

#User Interface
#Row:0 (Algorithm,speed)
Label(ui_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
alg_menu = ttk.Combobox(ui_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort','Insertion Sort','Merge Sort','Quick Sort'])
alg_menu.grid(row=0,column=1, padx=5, pady=5)
alg_menu.current(0)

speedScale = Scale(ui_frame, from_=0.001, to=0.2,  resolution=0.002,length=200, orient=HORIZONTAL, label="Select Speed [s]", width=5)
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(ui_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row:1 (Size, min, max)
sizeEntry = Scale(ui_frame, from_=1, to=200, resolution=1, orient=HORIZONTAL, label="Data Size", width=5)
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(ui_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, label="Min Value", width=5)
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(ui_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", width=5)
maxEntry.grid(row=1, column=2, padx=5, pady=5)
Button(ui_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

origin.mainloop()
