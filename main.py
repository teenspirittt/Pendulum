import graphics as gr
import matplotlib.pyplot as plt
import numpy as np

size_x = 800
size_y = 800
start_angle = 90
angle_velocity = 0
wire_length = 300
a = 0.09
angle_acceleration = 0

window = gr.GraphWin("Mayatnik", size_x, size_y)
angle = start_angle * (3.14 / 180)
center_point = gr.Point(size_x / 2, size_y / 2)

coords = gr.Point(center_point.x + wire_length * np.sin(angle),
                  center_point.y + wire_length * np.cos(angle))

rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(size_x, size_y))
rectangle.setFill('white')
rectangle.draw(window)

center = gr.Rectangle(gr.Point(300, 400), gr.Point(500, 380))
center.setFill('grey')
center.draw(window)

ball = gr.Circle(gr.Point(coords.x, coords.y), 20)
ball.setFill('red')
ball.draw(window)


def update_coords(coords):
    new_point = gr.Point(center_point.x + wire_length * np.sin(angle),
                         center_point.y + wire_length * np.cos(angle))
    velocity = gr.Point(new_point.x - coords.x,
                        new_point.y - coords.y)
    return velocity


def get_angle(angle, angle_accelaration, angle_velocity):
    angle_accelaration = -a * np.sin(angle)
    angle += angle_velocity
    angle_velocity += angle_accelaration
    angle_velocity *= 0.9
    return angle, angle_accelaration, angle_velocity


while True:
    angle, angle_acceleration, angle_velocity = get_angle(angle, angle_acceleration, angle_velocity)
    velocity = update_coords(ball.getCenter())
    ball.move(velocity.x, velocity.y)
    line = gr.Line(center_point, ball.getCenter())
    line.setFill('brown')
    line.draw(window)
    gr.time.sleep(0.03)
    line.undraw()
    if window.checkMouse():
        break
window.close()
