from turtle import *

speed(30)
bgcolor("black")

for i in range(5):

  h = 100

  penup()  
  goto(300*i, 0)
  pendown()

  for j in range(16):

    for k in range(18):

      color("yellow")
      h += 0.005  
      rt(90)   
      circle(100 - k * 6, 90)
      lt(90)
      circle(100 - k * 6, 90)
      rt(180)

    circle(30, 24)

    
  penup()     
#   write("TQM", font=("Arial", 100, "normal")) 
  goto(200*i, 300)
  
  pendown()

done()


# from turtle import *

# speed(100)
# bgcolor("black")

# for i in range(5):

#   h = 0

#   penup()
#   goto(-300*i, 0)  # Adjusted the initial x-coordinate to align to the right
#   pendown()

#   for j in range(16):

#     for k in range(18):

#       color("yellow")
#       h += 0.005
#       rt(90)
#       circle(100 - k * 6, 90)
#       lt(90)
#       circle(100 - k * 6, 90)
#       rt(180)

#     circle(30, 24)

#   penup()
#   goto(200*i, 0)  # Adjusted the initial x-coordinate to align to the right
#   pendown()

# done()

