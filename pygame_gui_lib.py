import pygame
from pygame.locals import *

# Basic color pallet
class colors:
    white   = (255,255,255)
    black   = (0,0,0)
    red     = (255,0,0)
    green   = (0,255,0)
    blue    = (0,0,255)

# Main class used for making objects to be rendered
class sprite():
    id      = None  # UID of the sprite
    x       = 0
    y       = 0
    width   = 0
    height  = 0
    visible = True
    name    = ""    # Name given to the sprite, Does not need to be unique.

    def __init__(self,name,x=0,y=0,width=0,height=0,visible=True):
        self.name       = name
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        self.visible    = visible

    # This method is called every game loop after the tick() method has ran
    def draw(self,display):
        pass

    # This method is called every game tick before objects are drawn
    def tick(self):
        pass

# default shape class, currently only for rectangles.
class shape(sprite):
    thickness   = 0
    color       = 0
    onclick     = None # This can be set to a custom method and is callled ever
                       # time the object is left clicked on.

    onDrag      = None # Similar to 'onclick' but is called every time the mouse
                       # cursor is moved ontop of the object while the left
                       # button is held.

    def __init__(self,name,x=0,y=0,width=0,height=0,thickness=0,
            color=colors.white,visible=True):
        super().__init__(name,x,y,width,height,visible)
        self.thickness  = thickness
        self.color      = color

    # called every game tick after the tick function
    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,
            self.width,self.height),self.thickness)

    # Called every game tick before the draw function
    def tick(self):
        pass

    # Called when the object has been clicked on,
    def clicked(self,mode):
        if mode == 1:   # Regular mouse click
            if self.onclick != None:
                self.onclick(self)
        if mode == 2:   # When the mouse button is down and cursor is moving.
            if self.onDrag != None:
                self.onDrag(self)

# Class for a game/window,
class python_GUI():
    FPS             = 60
    WINDOW_TITLE    = ""
    WINDOW_SIZE     = (800,600)
    BG_color        = colors.black

    sprites         = [] # Stores all the sprite objects
    sprite_count    = 0  # Keeps track of how many sprites have been created

    display         = None
    fpsClock        = None

    mouse_status    = 0 # Is set to 1 when the mouse button is pressed/held

    onclick = None

    def __init__(self,title,windowsize=(800,600),fps=60):
        self.WINDOW_TITLE   = title
        self.WINDOW_SIZE    = windowsize
        self.FPS            = fps

        pygame.init()
        pygame.font.init()

        self.fpsClock   = pygame.time.Clock()
        self.display    = pygame.display.set_mode(self.WINDOW_SIZE)

    # Default method for creating new sprites
    def add_sprite(self,name='',x=0,y=0,width=0,height=0,visible=True):
        return self.__append_sprite(sprite(name,x,y,width,height,visible))

    # used to add other sprite types to the game, such as shape classes
    def add_custom_sprite(self,spr):
        return self.__append_sprite(spr)

    def __append_sprite(self,spr):
        spr.id=(self.sprite_count)
        self.sprites.append(spr)
        uid=self.sprite_count
        self.sprite_count += 1
        return uid

    # Checks to see what sprite has been clicked on
    def __clicked_on(self,pos,mode):
        for i in self.sprites:
            x=i.x
            y=i.y
            width=i.width
            height=i.height

            # Checks mouse position with the object position & size
            # TODO refine this condition(s) to stop overlapping sprites
            if (pos[0] >= x and pos[0] <= x + width) and \
                (pos[1] >= y and pos[1] <= y + height):
                    i.clicked(mode)
    # Checks and actions any user events such as key presses or mouse movenent.
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Click and drag detection
            if(self.mouse_status == 1):
                if event.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    self.__clicked_on(mouse_position,2)

            # Regular mouse click detection
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self.__clicked_on(mouse_position,1)
                self.mouse_status = 1

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_status = 0

        # runs tick method in all sprites
        for i in self.sprites:
            i.tick()

    # calls draw method in all visible sprites
    def __draw_things(self):
        self.display.fill(self.BG_color)
        for i in self.sprites:
            if i.visible:
                i.draw(self.display)

    # Main game loop
    def tick(self):
        self.__check_events()
        self.__draw_things()
        pygame.display.update()
        self.fpsClock.tick(self.FPS)
