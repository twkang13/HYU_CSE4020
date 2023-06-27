import glfw
from OpenGL.GL import *
import numpy as np

primitiveType = GL_LINE_LOOP

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # draw dodecagon
    glBegin(primitiveType)
    th = np.radians(0)
    for i in range(12):
        glVertex2fv(T @ np.array([np.cos(th),np.sin(th)]))
        th += np.radians(30)
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global primitiveType
    
    if (key == glfw.KEY_0 and action == glfw.PRESS):
        primitiveType = GL_POLYGON
        
    elif (key == glfw.KEY_1 and action == glfw.PRESS):
        primitiveType = GL_POINTS
        
    elif (key == glfw.KEY_2 and action == glfw.PRESS):
        primitiveType = GL_LINES
        
    elif (key == glfw.KEY_3 and action == glfw.PRESS):
        primitiveType = GL_LINE_STRIP
        
    elif (key == glfw.KEY_4 and action == glfw.PRESS):
        primitiveType = GL_LINE_LOOP
        
    elif (key == glfw.KEY_5 and action == glfw.PRESS):
        primitiveType = GL_TRIANGLES
        
    elif (key == glfw.KEY_6 and action == glfw.PRESS):
        primitiveType = GL_TRIANGLE_STRIP
        
    elif (key == glfw.KEY_7 and action == glfw.PRESS):
        primitiveType = GL_TRIANGLE_FAN
        
    elif (key == glfw.KEY_8 and action == glfw.PRESS):
        primitiveType = GL_QUADS
        
    elif (key == glfw.KEY_9 and action == glfw.PRESS):
        primitiveType = GL_QUAD_STRIP

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480, 480, "2021025205-2-2", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.set_key_callback(window, key_callback)
    
    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll events
        glfw.poll_events()
        
        # Render here, e.g. using pyOpenGL
        T = np.array([[1.,0.], [0.,1.]])
        render(T)

        # Swap front and back buffers
        glfw.swap_buffers(window)
        
    glfw.terminate()


if __name__ == "__main__":
    main()
