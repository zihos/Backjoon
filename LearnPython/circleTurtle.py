import turtle as t

n = 60

t.shape('turtle')
t.speed('fastest')
t.color('orange')
for i in range(n):
    t.circle(120)
    t.right(360/n)

t.mainloop()