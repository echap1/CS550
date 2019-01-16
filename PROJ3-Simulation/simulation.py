"""
CS550 Project: Simulation
Due January 16, 2019

@author: Ethan Chapman

Dependencies:
    Pillow - Creating and drawing on images (pip3 install Pillow)

"""

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt
import imageio
import numpy as np

def get_background_image():
    """Generates the background image for the gif

    Args:
        None

    Returns:
        Image.Image: the background image

    """

    background = Image.new("RGB", (600, 200))  # Create a new image
    draw = ImageDraw.Draw(background)  # Create an ImageDraw object so that the program can draw shapes on the image
    draw.rectangle((0, 0, 10, 200), (128, 128, 128))  # Draw the wall

    return background


def gen_image(x1, x2, rect_size, background: Image.Image, collisions=0, finished=False, m1=1, m2=1, v1=0, v2=0, still=False):
    """Generates a frame of a gif (or a still image)

    Args:
        x1 (int): the x position of the first rectangle
        x2 (int): the x position of the second rectangle

        rect_size (int): the size of the rectangles (measured from center to edge)

        background (Image.Image): the background image

        collisions (int): the number of collisions that have happened (displayed in the text), default value 0
        finished (bool): if there are no more collisions going to happen (displayed in the text), default value False
        m1 (int): the mass of the first rectangle (displayed in the text), default value 1
        m2 (int): the mass of the second rectangle (displayed in the text), default value 1
        v1 (int): the velocity of the first rectangle (displayed in the text), default value 0
        v2 (int): the velocity of the second rectangle (displayed in the text), default value 0

        still (bool): if the image generated is part of a gif (won't display m1 m2 v1 v2 or finished if true)

    Returns:
        Image.Image: the frame of the gif (or still image)

    """

    new = background.copy()  # Make a copy of the background

    draw = ImageDraw.Draw(new)  # Allow drawing on the image

    draw.rectangle((x1 - rect_size, new.height - (2 * rect_size), x1 + rect_size, new.height), (0, 0, 255))  # Square 1
    draw.rectangle((x2 - rect_size, new.height - (2 * rect_size), x2 + rect_size, new.height), (0, 255, 0))  # Square 2

    # Draw the numbers on the squares
    s = draw.textsize("1")
    draw.text((x1 - s[0] / 2, new.height - rect_size - s[1] / 2), "1", (255, 255, 0))
    draw.text((x2 - s[0] / 2, new.height - rect_size - s[1] / 2), "2", (255, 0, 255))

    # Draw the number of collisions and the velocities if there
    if not still:
        draw.multiline_text((20, 10),
                            f"Collisions: {collisions} {f'(Finished)' if finished else ''}\n"
                            f"m1={m1}, m2={m2}\n"
                            f"v1={round(v1 * 100) / 100}, v2={round(v2 * 100) / 100}", spacing=0)
    else:
        draw.text((20, 10), f"m1={m1}, m2={m2}\n")

    return new


def generate_gif(m1=1, m2=1, rect_size=10, fps=60, x1=100, x2=200, v1=0, v2=-60, frames=800, filename=None):
    """Generates a gif of the collisions between the objects

    Args:
        m1 (int): the mass of the first rectangle, default value 1
        m2 (int): the mass of the second rectangle, default value 1

        rect_size (int): the size of the rectangles (measured from center to edge), default value 10

        fps (int): the fps of the gif, default value 60

        x1 (int): the x position of the first rectangle, default value 100
        x2 (int): the x position of the second rectangle, default value 200

        v1 (int): the velocity of the first rectangle, default value 0
        v2 (int): the velocity of the second rectangle, default value -60

        frames (int): the amount of frames to generate

        filename (str): the name of the file to save, default value f"{m2}.gif"

    Returns:
        None

    """

    background = get_background_image()  # Get the background image

    cpf = 1000  # The number of calculations per frame (in case there are multiple collisions)

    frame_buff = []  # The frame buffer to write to the gif

    collisions = 0  # The number of collisions so far

    for i in range(frames):  # For each frame
        for j in range(cpf):  # For each calculation per frame
            if x1 + (v1 / fps) + rect_size > x2 + (v2 / fps) - rect_size:  # If the rectangles are going to collide
                # Solves x1 + y(v1 / fps) + rect_size = x2 + y(v2 / fps) - rect_size
                # y is the coefficient multiplied to v1 and v2 so that they are touching but not colliding
                y = fps * ((x1 - x2) + 2 * rect_size) / (v2 - v1)

                # Add the velocities
                x1 += y * v1 / fps
                x2 += y * v2 / fps

                v1, v2 = do_collision(m1, m2, v1, v2)  # Change the velocities based on the collision

                collisions += 1  # Increase collisions by 1

            if x1 + (v1 / fps) - rect_size < 10:  # If box 1 is going to hit the wall
                x1 = 10 + rect_size  # Set box 1's position to the edge of the wall
                v1 = abs(v1)  # Make v1 positive (going toward v2)

                collisions += 1  # Increase collisions by 1

        # Append the frame to the buffer
        frame_buff.append(gen_image(x1, x2, rect_size, background, collisions, 0 <= abs(v1) < v2, m1, m2, v1 / fps, v2 / fps))

        # Increase the positions by their velocity
        x1 += v1 / fps
        x2 += v2 / fps

    # Set filename to the default value if there is no name given
    if filename is None:
        filename = f"{m2}.gif"

    # Write the buffer to the gif and save
    with imageio.get_writer(filename, mode='I', duration=1/fps) as writer:
        for frame in frame_buff:
            writer.append_data(np.asarray(frame))


def generate_still(m1=1, m2=1, rect_size=10, x1=100, x2=200, filename="still.gif"):
    """Generates a still image of the objects and the background at the given coordinates

    Args:
        m1 (int): the mass of the first rectangle, default value 1
        m2 (int): the mass of the second rectangle, default value 1

        rect_size (int): the size of the rectangles (measured from center to edge), default value 10

        x1 (int): the x position of the first rectangle, default value 100
        x2 (int): the x position of the second rectangle, default value 200

        v1 (int): the velocity of the first rectangle, default value 0
        v2 (int): the velocity of the second rectangle, default value -60

        filename (str): the name of the file to save, default value "still.gif"

    Returns:
        None

    """

    imageio.imsave("./" + filename, np.asarray(gen_image(x1, x2, rect_size, get_background_image(), m1=m1, m2=m2, still=True)))


def do_collision(m1, m2, v1, v2):
    """Calculates the new velocities

    Args:
        m1 (int): the mass of the first rectangle
        m2 (int): the mass of the second rectangle

        v1 (int): the velocity of the first rectangle
        v2 (int): the velocity of the second rectangle

    Returns:
        int: the first velocity after the collision
        int: the second velocity after the collision

    """

    # Implement the elastic collision equations
    v1, v2 = ((m1 - m2) / (m1 + m2)) * (v1 - v2) + v2, ((2 * m1) / (m1 + m2)) * (v1 - v2) + v2

    return v1, v2


def collide(m2):
    """Finds the number of collisions given m2

    Args:
        m2 (int): the mass of the second rectangle

    Returns:
        int: the number of collisions

    """

    # The starting velocities
    v1 = 0
    v2 = -1

    totalCollisions = 0  # The total number of collisions

    while not(0 <= abs(v1) < v2):  # While there are still more collisions
        # If v1 < 0, there are 2 more collisions (box 1 will bounce off the wall and then the box 2)
        if v1 < 0:
            collisions = 2

        # Otherwise, box 1 will just bounce off of box 2
        else:
            collisions = 1

        # Collision equations (v1 is abs(v1) because if it is negative, it will bounce off the wall and become positive)
        v1, v2 = ((1 - m2) / (1 + m2)) * (abs(v1) - v2) + v2, (2 / (1 + m2)) * (abs(v1) - v2) + v2

        # Add the number of collisions for this iteration to the total
        totalCollisions += collisions

    return totalCollisions


def collide_pi_estimate(n):
    """Uses collisions(m2) to estimate pi

    Args:
        n (int): the number of digits to calculate

    Returns:
        float: the pi estimate

    """

    return collide(10 ** (2 * n)) / 10 ** n


def gen_graph():
    """Plots the precision of the pi estimate for n from 0 to 4

    Args:
        None

    Returns:
        None, but shows and saves the graph

    """

    plt.bar(range(5), [abs(np.pi - collide_pi_estimate(10 ** (2 * i))) / np.pi * 100 for i in range(5)])
    plt.xlabel("n (m2=10 ** (2 * n))")
    plt.ylabel("% deviation from pi")
    plt.show()
    plt.savefig(fname="graph.png")
