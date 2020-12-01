from pyglet.gl import *

# Direct OpenGL commands to this window.

image = pyglet.resource.image('dummy.png')  #import png file
texture = image.get_texture()   #prepare image to be used as texture


w, h = 480, 480  # setting pyglet window size
window = pyglet.window.Window(w, h)  # other parameters -> (w, h, "title", resizable=True)

#a random 2D vertex
vtx1 = [100.0,400.0]

#a list of vertices and also texture coords
vlist = pyglet.graphics.vertex_list(4, ('v2f', [10,10, 400, 0, 400,400, 100,400]), ('t2f', [0,0, 1,0, 1,1, 0,1]))

#not being used - but reserved to save key being pressed by user.
key = pyglet.window.key

#displays app fps to help debuging or visualizing performance
fps_display = pyglet.window.FPSDisplay(window=window)

#needs this enabled to allow textures to be depicted. Sometimes it needs to be disable/enabled inside a draw loop.
glEnable(GL_TEXTURE_2D)

#this loop repeats constantly similar to a movie "frame"
@window.event
def on_draw():
    #clears everything on buffer before drawing things again:
    glClear(GL_COLOR_BUFFER_BIT)

    ## matrix options
    #glLoadIdentity()
    #glMatrixMode(GL_PROJECTION)
    #glOrtho(0, w, 0, h, -1000.0, 1000.0)  # [near, far] = [-1000, 1000]
    #glMatrixMode(GL_MODELVIEW)


    ## simple triangle draw (no texture)
    """     glBegin(GL_TRIANGLES)
    
    glVertex2f(vtx1[0],vtx1[1])
    glVertex2f(w, 0)
    glVertex2f(w, window.height)
    
    glEnd() """

    

    ## draws a QUAD with glBegin method, so you have to give vertices and texture cords to be drawn:
    glBindTexture(texture.target, texture.id) #draw the folowing quad using this texture:
    glBegin(GL_QUADS)   #instruction to start drawing a QUAD using this 2D vtx and texture coords.
    #there is a sequence to place vertices on a quad, or it will draw something different than expected:
    glTexCoord2f(0.0, 0.0); glVertex2f(10.0, 10.0) # first corner at LEFT BOTTOM 
    glTexCoord2f(1.0, 0.0); glVertex2f(400.0, 0.0)  # second corner at RIGHT BOTTOM 
    glTexCoord2f(1.0, 1.0); glVertex2f(400.0,  400.0)
    glTexCoord2f(0.0, 1.0); glVertex2f(vtx1[0],  vtx1[1])   # last corner at LEFT TOP (testing mouse drag)
    glEnd()
   
    
    ## draws a quad using the information on the vlist instead of giving it on the fly.
    """
    glColor3f(1,1,1)
    glEnable(texture.target)  # texture.target -> GL_TEXTURE_2D
    glBindTexture(texture.target, texture.id)
    vlist.draw(GL_POLYGON) #vlist.draw(GL_QUADS)
    glDisable(texture.target)
    """


    #print (pyglet.clock.get_fps())
    fps_display.draw() #displays the fps

#window event that updates when mouse is pressed and moved
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & pyglet.window.mouse.LEFT:
        #simple test
        vtx1[0] = x
        vtx1[1] = y     
    pass


#def update(dx):
#   pass

#pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
pyglet.app.run()
