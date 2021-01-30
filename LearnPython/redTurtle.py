import turtle as t

n = 6

t.shape('turtle')
t.color('#7a7a7a')
t.begin_fill()

for i in range(n):
    t.fd(100)
    t.right(360/n)

t.circle(120)

t.end_fill()
t.mainloop()