from turtle import *

# speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for index, value in enumerate(colors):
    color(value)

    begin_fill()
    for j in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)   
    end_fill() 

mainloop()