import turtle
t=turtle.Turtle()

screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('cornflowerblue')

#introscreen
t.penup()
t.goto(0, 150)
t.pendown()
t.write("Welcome to my Turtle Presentation!", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(0, 50)
t.pendown()
screen.addshape('turtle.gif')
t.shape('turtle.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0, -150)
t.pendown()
screen.addshape('Welcome Pic.gif')
t.shape('Welcome Pic.gif')
t.stamp()
t.shape('classic')


turtle.penup()
turtle.goto(-200, -350)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
for _ in range(4): turtle.forward(50); turtle.left(90)
turtle.end_fill()



t.penup()
t.goto(90, -350)
t.pendown()
t.write("Press enter to go to next page", font=("Arial", 15, "bold italic"), align="center")

t.penup()
t.goto(250, 300)
t.write("Page 1", font=("Arial", 15, "bold italic"), align="center")
t.pendown()


page = input("Press Enter to Continue: ")
t.clear()
turtle.clear()


#2nd Page
screen.bgcolor('lightcoral')


t.penup()
t.goto(0, 170)
t.pendown()
t.write("My 3 favorite foods!", font=("Arial", 25, "bold italic"), align="center")



t.penup()
t.goto(-250, -100)
t.write("Tacos", font=("Arial", 25, "bold italic"), align="center")
t.penup()
t.goto(-250, -150)
screen.addshape('Taco.gif')
t.shape('Taco.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(-50, -100)
t.write("Fried Chicken", font=("Arial", 25, "bold italic"), align="center")
t.penup()
t.goto(-50, -150)
screen.addshape('KFC.gif')
t.shape('KFC.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(200, -95)
t.write("Bacon Cheese Fries", font=("Arial", 15, "bold italic"), align="center")
t.penup()
t.goto(200,-150)
screen.addshape('Fries.gif')
t.shape('Fries.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(-200,-350)
t.pendown()
turtle.color("red")
turtle.begin_fill()
for _ in range(3): turtle.forward(50); turtle.left(120)
turtle.end_fill()





t.penup()
t.goto(90, -350)
t.pendown()
t.write("Press enter to go to next page", font=("Arial", 15, "bold italic"), align="center")

t.penup()
t.goto(250, 300)
t.write("Page 2", font=("Arial", 15, "bold italic"), align="center")
t.pendown()

page = input("Press Enter to Continue: ")
t.clear()
turtle.clear()

#3rd page

screen.bgcolor('yellowgreen')


t.penup()
t.goto(0, 250)
t.pendown()
t.write("My Hobbies!", font=("Arial", 25, "bold italic"), align="center")



t.penup()
t.goto(-250, -85)
t.write("Playing Soccer", font=("Arial", 15, "bold italic"), align="center")
t.penup()
t.goto(-235, -150)
screen.addshape('soccer.gif')
t.shape('soccer.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(-50, -85)
t.write("Playing Volleyball", font=("Arial", 15, "bold italic"), align="center")
t.penup()
t.goto(-50, -150)
screen.addshape('vb.gif')
t.shape('vb.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(-50, -85)
t.write("Playing Volleyball", font=("Arial", 15, "bold italic"), align="center")
t.penup()
t.goto(-50, -150)
screen.addshape('vb.gif')
t.shape('vb.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(150, -65)
t.write("Playing Video Games", font=("Arial", 15, "bold italic"), align="center")
t.penup()
t.goto(150, -150)
screen.addshape('gc.gif')
t.shape('gc.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(0, 150)
t.write("Swimming", font=("Arial", 15, "bold italic"), align="center")
t.penup()
t.goto(0, 50)
screen.addshape('sw.gif')
t.shape('sw.gif')
t.stamp()
t.shape('classic')


circle = turtle.Turtle()
circle.penup()
circle.goto(-200, -350)
circle.pendown()
circle.color("green")
circle.begin_fill()
circle.circle(25)
circle.end_fill()




t.penup()
t.goto(90, -350)
t.pendown()
t.write("Press enter to go to next page", font=("Arial", 15, "bold italic"), align="center")

t.penup()
t.goto(250, 300)
t.write("Page 3", font=("Arial", 15, "bold italic"), align="center")
t.pendown()
page = input("Press Enter to Continue: ")
t.clear()
turtle.clear()
circle.clear()


#4th page

screen.bgcolor('darkviolet')


t.penup()
t.goto(0, 250)
t.pendown()
t.write("Favorite Movie", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(0, 100)
t.write("Lion King", font=("Arial", 20, "bold italic"), align="center")
t.penup()
t.goto(0, -100)
screen.addshape('lk.gif')
t.shape('lk.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(200, 0)
screen.addshape('s.gif')
t.shape('s.gif')
t.stamp()
t.shape('classic')

rhombus = turtle.Turtle()
rhombus.penup()
rhombus.goto(-200, -350)
rhombus.pendown()
rhombus.color("yellow")
rhombus.begin_fill()
for _ in range(2):
    rhombus.forward(60)
    rhombus.left(45)
    rhombus.forward(60)
    rhombus.left(135)
rhombus.end_fill()

t.penup()
t.goto(90, -350)
t.pendown()
t.write("Press enter to go to next page", font=("Arial", 15, "bold italic"), align="center")

t.penup()
t.goto(250, 300)
t.write("Page 4", font=("Arial", 15, "bold italic"), align="center")
t.pendown()


page = input("Press Enter to Continue: ")
rhombus.clear()
t.clear()

#5th page

screen.bgcolor('white')


t.penup()
t.goto(0, 250)
t.pendown()
t.write("My Favorite Sport!", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(0, -25)
screen.addshape('favsp.gif')
t.shape('favsp.gif')
t.stamp()
t.shape('classic')




t.penup()
t.goto(0, -350)
screen.addshape('wrdart.gif')
t.shape('wrdart.gif')
t.stamp()
t.shape('classic')







pent = turtle.Turtle()
pent.color("black")
pent.penup()
pent.goto(-200, -350)
pent.pendown()
pent.begin_fill()
for _ in range(5): pent.forward(50); pent.left(72)
pent.end_fill()










t.penup()
t.goto(90, -300)
t.pendown()
t.write("Last Page!", font=("Arial", 15, "bold italic"), align="center")

t.penup()
t.goto(250, 300)
t.write("Page 5", font=("Arial", 15, "bold italic"), align="center")
t.pendown()


turtle.done()
pent.clear()
t.clear()