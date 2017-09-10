""" Serpinski Triangle drawing function
Function is implemented in Python 3.
Function have three optional parametrs:
- Method: 1 = Iterative or 2 = Chaos methods. (Iterative is default)
- Depth of iterative method. (4 is default depth)
- Shift coordinats. ([0,0] is default)


"""
def serpinskiTriangle (method=1, depth=4, startCrd=[0,0]):

#Mode definition

#  ---- Iterate Mode Definition ----
    def iterateMode(depth):
        import turtle
        
        def drawTriangle(points,myTurtle):
            myTurtle.up()
            myTurtle.goto(points[0][0],points[0][1])
            myTurtle.down()
            myTurtle.goto(points[1][0],points[1][1])
            myTurtle.goto(points[2][0],points[2][1])
            myTurtle.goto(points[0][0],points[0][1])

        # Find middle coordinats between two points
        def getMid(p1,p2):
            return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

        # Recursive drawing function
        def sierpinski(points,degree,myTurtle):
            drawTriangle(points,myTurtle)
            if degree > 0:
                sierpinski([points[0],
                                getMid(points[0], points[1]),
                                getMid(points[0], points[2])],
                           degree-1, myTurtle)
                sierpinski([points[1],
                                getMid(points[0], points[1]),
                                getMid(points[1], points[2])],
                           degree-1, myTurtle)
                sierpinski([points[2],
                                getMid(points[2], points[1]),
                                getMid(points[0], points[2])],
                           degree-1, myTurtle)

        def main():
           myT = turtle.Turtle()
           # Set max speed of drawing
           myT.speed(0)
           myWindow = turtle.Screen()
           # Triangle coordinats
           myPoints = [[-200 + startCrd[0],-100 + startCrd[1]],[0 + startCrd[0],200 + startCrd[1]],[200 + startCrd[0],-100 + startCrd[1]]]
           sierpinski(myPoints,depth,myT)
           myWindow.exitonclick()

        main()
#  ---- END Iterate Mode Definition ----


#  ---- Chaos Mode Definition ----
    def chaosMode():
        import random, turtle

        def main():
            myT = turtle.Turtle()
            # Set max speed of drawing
            myT.speed(0)
            myT.up()
            myWindow = turtle.Screen()
            # Triangle coordinats
            myPoints = [[-200,-100],[0,200],[200,-100]]

            # Det random coordinats inside the triangle
            dot = [(random.randint(myPoints[0][0],myPoints[2][0])/2),(random.randint((myPoints[0][1]+myPoints[2][1])/2,myPoints[1][1]/2))]
            # print(dot)
            counter = 0
            
            # Random choice of active attractor and make math
            die = [1,2,3]

            while (counter < 10000):
                counter = counter + 1
                switch = random.choice(die)
                if switch == 1:
                    dot[0] = (dot[0] + myPoints[0][0])/2
                    dot[1] = (dot[1] + myPoints[0][1])/2
                if switch == 2:
                    dot[0] = (dot[0] + myPoints[1][0])/2
                    dot[1] = (dot[1] + myPoints[1][1])/2
                if switch == 3:
                    dot[0] = (dot[0] + myPoints[2][0])/2
                    dot[1] = (dot[1] + myPoints[2][1])/2

                # Go to address and draw the dot
                myT.goto(dot[0], dot[1])
                # Here you can change size of the dot
                myT.dot(2, 'black')
                
            myWindow.exitonclick()
            
        main()

#  ---- END Chaos Mode Definition ----



#Mode switch
    if method == 1:
        iterateMode(depth)
    elif method == 2:
        chaosMode()


#Lunch function
serpinskiTriangle(1)
