import tkinter as tk

# Question 1

# root = tk.Tk()
# root.title("Robot Control Panel")
# root.geometry("500x400")
# root.configure(bg="yellow")

# root.mainloop()


# Question 2

# root = tk.Tk()
# canvas = tk.Canvas(root, width=300, height=300)
# canvas.pack()

# # A point = tiny circle
# canvas.create_oval(100, 100, 103, 103, fill="black")

# root.mainloop()

# Question 3

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()

# points = [20,50, 100,120, 180,90, 250,150]

# canvas.create_line(points, fill="blue", width=3)

# root.mainloop()


# Question 4

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=200)
# canvas.pack()

# p = canvas.create_oval(10, 90, 30, 110, fill="red")

# x_speed = 2

# def move_point():
#     canvas.move(p, x_speed, 0)
#     root.after(20, move_point)

# move_point()
# root.mainloop()



# Question 5

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()

# # body
# canvas.create_rectangle(100, 100, 250, 150, fill="gray")

# # wheels
# canvas.create_oval(110, 150, 140, 180, fill="black")
# canvas.create_oval(210, 150, 240, 180, fill="black")

# root.mainloop()


# Question 6

# root = tk.Tk()

# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()

# robot = canvas.create_oval(150, 150, 170, 170, fill="red")

# def move(dx, dy):
#     canvas.move(robot, dx, dy)

# tk.Button(root, text="Up", command=lambda: move(0, -10)).pack()
# tk.Button(root, text="Down", command=lambda: move(0, 10)).pack()
# tk.Button(root, text="Left", command=lambda: move(-10, 0)).pack()
# tk.Button(root, text="Right", command=lambda: move(10, 0)).pack()

# root.mainloop()


# Question 7

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400)
# canvas.pack()

# ball = canvas.create_oval(200,150,230,180, fill="blue")

# dx = 3
# dy = 3

# def move_ball():
#     global dx, dy
#     canvas.move(ball, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(ball)

#     # reverse direction if touching walls
#     if x1 <= 0 or x2 >= 500:
#         dx = -dx
#     if y1 <= 0 or y2 >= 400:
#         dy = -dy

#     root.after(20, move_ball)

# move_ball()
# root.mainloop()


# Question 8

# root = tk.Tk()
# root.title("Robot Motion")
# root.geometry("500x400")

# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# x, y = 50, 200
# r = 10
# velocity = 5

# robot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

# def move_robot():
#     global x
#     if x < 450:
#         x += velocity
#         canvas.coords(robot, x-r, y-r, x+r, y+r)
#         root.after(50, move_robot)

# move_robot()
# root.mainloop()



# Question 9 

# import math

# root = tk.Tk()
# root.title("Four Bar Mechanism")
# root.geometry("600x500")

# canvas = tk.Canvas(root, width=600, height=500, bg="white")
# canvas.pack()

# A = (150, 300)
# D = (400, 300)
# L2, L3, L4 = 120, 150, 130
# theta = math.radians(30)

# Bx = A[0] + L2 * math.cos(theta)
# By = A[1] - L2 * math.sin(theta)
# B = (Bx, By)

# # Approximate C (static drawing)
# C = (B[0] + 120, B[1] + 40)

# canvas.create_line(A, D, width=4, fill="black")     # Ground
# canvas.create_line(A, B, width=4, fill="red")       # Crank
# canvas.create_line(B, C, width=4, fill="blue")      # Coupler
# canvas.create_line(C, D, width=4, fill="green")     # Rocker

# for p in [A, B, C, D]:
#     canvas.create_oval(p[0]-5, p[1]-5, p[0]+5, p[1]+5, fill="black")

# root.mainloop()



# Question 10 

# root = tk.Tk()
# root.title("Keyboard Controlled Robot")
# root.geometry("500x400")

# canvas = tk.Canvas(root, width=500, height=350, bg="white")
# canvas.pack()

# x, y = 250, 175
# r = 8

# robot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

# def move(dx, dy):
#     global x, y
#     x += dx
#     y += dy
#     canvas.create_line(x-dx, y-dy, x, y, fill="gray")
#     canvas.coords(robot, x-r, y-r, x+r, y+r)

# def up(event): move(0, -5)
# def down(event): move(0, 5)
# def left(event): move(-5, 0)
# def right(event): move(5, 0)

# def reset():
#     canvas.delete("all")
#     global x, y, robot
#     x, y = 250, 175
#     robot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

# root.bind("<Up>", up)
# root.bind("<Down>", down)
# root.bind("<Left>", left)
# root.bind("<Right>", right)

# tk.Button(root, text="RESET", command=reset).pack()

# root.mainloop()

















