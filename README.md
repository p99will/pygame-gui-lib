# pygame gui lib

 libiary to kick start the use of pygame

## Getting Started

download pygame-gui-lib.py to your local code directory.

```python
from pygame_gui_lib import *
```

### Prerequisites

Dependancies: 
 [pygame](https://www.pygame.org/wiki/GettingStarted) - How to install pygame

### Installing

Make sure the pygame-gui-lib.py is in your code directory

EG:
```
+-- myProject
|   +-- main.py
|   +-- pygame-gui-lib.py <-- HERE
```

Calling the python_GUI function should show your pygame window breifly, indicating it is working
```python
windowsize = (300,350)

# Creating new game window
window1 = python_GUI("example",windowsize)
```

Or calling printing colors.red should return the correct RGB value:
```python
print(colors.red)
# >>> (255,0,0)
```

## Example of code

```python
from pygame_gui_lib import *

windowsize = (300,350)

# Creating new game window
window1 = python_GUI("example",windowsize)

# list to store box sprites
boxes=[]

# Called when one of the boxes are clicked.
# The sprite object is passed back to this function to allow editing of the
# attributes.
def clicked_box(obj):       # Simply changes the color of a box to green and makes it
    obj.color=colors.green  # A solid shape (thickness=0)
    obj.thickness=0
    obj.highlighted=True    # Adds new attribute to the class instance

# This is called when the red button is pressed.
def reset_boxes(obj=None):
    for i in boxes:
        i.highlighted = 0
        i.color = colors.white
        i.thickness = 1

# Add new shape object, this is used as the reset button
#                name,[x],[y],[width],[height],[color],[visible]
button1 = shape("Reset",0,300,50,50,0,colors.red)

# Sets the onclick to link to a method we have defined in this py script.
# Alows the instance that was created in the calss to call methods in this
# script
button1.onclick=reset_boxes # NOTE: we have not used 'reset_boxes()'
                            # we just set it equal the function object

# Adds our newly made button to the game/window
window1.add_custom_sprite(button1)

# Creates a 10x10 matrix of square shape sprites
box_size = 30 # Box size; Both width and height will equal 30px
for y in range(10): # x and y are in reverse order to look like a 2d list when
                    # the list is printed / echoed
    for x in range(10):
        box=shape("Box"+str(x)+':'+str(y),box_size*x,box_size*y,box_size,
            box_size,1)
        box.onDrag=clicked_box # sets the onclick to the local method
                               # clicked_box
        boxes.append(box) # Adds the shape object to our locally defined list

# Adds all our box sprites into the window/game,
# This is actually allowing us to have the object to be reffered to either by
# boxes[x] or window1.sprites[x], they are linked to the same instance.
        # I didn't think this was possible in python, it is kind of bootstrapped
        # object pointers, or accessing the same object instance from
        # two different places.
for i in boxes:
    window1.add_custom_sprite(i)

# Main game loop
while 1:
    window1.tick()
```

## Contributing

Feel free to branch and recoomend changes, I will add extra parts to this from time to time when I need it.


## Authors

* **William Clelland** 
