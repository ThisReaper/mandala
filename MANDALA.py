import turtle

# Erstelle die Schildkröte Leonardo
leonardo = turtle.Turtle()
leonardo.color("blue")
leonardo.screen.bgcolor("black")
leonardo.speed(0)  
# Funktion zum Zeichnen eines Quadrats
def zeichne_quadrat():
    for _ in range(4):
        leonardo.forward(100)
        leonardo.right(90)

for _ in range(32):
    zeichne_quadrat()
    leonardo.right(11.25)

# Halte das Fenster offen
turtle.done()
