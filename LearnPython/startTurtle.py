import turtle as t

n = 5
t.shape('turtle')
t.color('gold')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right((360/n)*2)
    t.forward(100)
    t.left(360/n)

t.end_fill()
t.mainloop()