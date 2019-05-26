import turtle  
import random
from tkinter import *
import LettersProbability as l


def drawPie(letter_angles, entry, canvas):
    
    n_angles = l.nAngles(int(float(entry.get())), letter_angles)
    pie = turtle.RawTurtle(canvas)
    
    #Sets starting point of drawing
    pie.up()
    pie.left(90)
    pie.backward(200)
    pie.right(90)
    pie.down()
    pie.speed(8)

    #Stores 55 random colors in list
    color = ["#"+''.join([random.choice('0123456789abcdef') for j in range(6)]) 
            for i in range(0, 55)]
    color_count = 0

    for i in n_angles:
    #Set color and draw part of pie slice
        pos1 = pie.pos()
        pie.pencolor(color[color_count])
        pie.fillcolor(color[color_count])
        pie.begin_fill()
        pie.circle(150, n_angles.get(i) / 2)
        pos2 = pie.position()

    #Draw Labels
        pie.up()
        pie.right(90)
        pie.forward(30)
        pie.down()
        pie.pencolor('black')
        pie.write(i + ', %s' % round(n_angles.get(i) / 360, 4), align = "center", font=("Arial", 7, "normal"))
        pie.pencolor(color[color_count])
        pie.up()
        pie.goto(pos2)
    #Back to drawing rest of pie slice
        pie.left(90)
        pie.circle(150, n_angles.get(i) / 2)
        pos3 = pie.pos()
        pie.left(90)
        pie.forward(150)
        pie.goto(pos1)
        pie.up()
        pie.goto(pos3)
        pie.right(90)
        pie.end_fill()
        pie.down()

        color_count += 1


letter_angles = l.letterAngles(l.letterCount("Words.txt"))

root = Tk()
canvas = Canvas(master = root, width = 500, height = 500) #Create canvas for drawings
canvas.pack()

root.title('Pie Chart') 
Label(root, text='Enter n').pack()
entry = Entry(root)
entry.pack() 

#Button which takes n input into drawpie function to draw the chart
enter_b = Button(root, text = "Enter", command = lambda: drawPie(letter_angles, entry, canvas))
enter_b.pack()

root.mainloop() 