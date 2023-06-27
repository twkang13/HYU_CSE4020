import glfw
from OpenGL.GL import *
import numpy as np

# global variable
currentTF = np.array([[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]])

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1] )
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global currentTF
    th = np.pi * 10 / 180
    
    if (action == glfw.PRESS or action == glfw.REPEAT):
        if (key == glfw.KEY_Q):
            currentTF = np.array([[1.,0.,-0.1], [0.,1.,0.], [0.,0.,1.]]) @ currentTF
        
        elif (key == glfw.KEY_E):
            currentTF = np.array([[1.,0.,.1], [0.,1.,0.], [0.,0.,1.]]) @ currentTF
        
        elif (key == glfw.KEY_A):
            currentTF = currentTF @ np.array([[np.cos(th),-np.sin(th),0.],[np.sin(th),np.cos(th),0.], [0.,0.,1.]])
        
        elif (key == glfw.KEY_D):
            currentTF = currentTF @ np.array([[np.cos(-th),-np.sin(-th),0.],[np.sin(-th),np.cos(-th),0.], [0.,0.,1.]])
        
        elif (key == glfw.KEY_1):
            currentTF = np.array([[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]])
        
        elif (key == glfw.KEY_W):
            currentTF = np.array([[0.9,0.,0.], [0.,1.,0.], [0.,0.,1.]]) @ currentTF
        
        elif (key == glfw.KEY_S):
            currentTF = np.array([[np.cos(th),-np.sin(th),0.],[np.sin(th),np.cos(th),0.], [0.,0.,1.]]) @ currentTF

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480, 480, "2021025205-3-1", None, None)
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
        render(currentTF)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
