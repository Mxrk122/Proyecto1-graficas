import gl
import texture
from vector3 import *
import camera
import Obj


filename = 'dutch_angle.bmp'


nvidia = gl.gl(filename)

nvidia.glCreateWindow(1000, 1000)

nvidia.glClearColor(1, 1, 1)

nvidia.glClear()


#Estas constantes se quedan asi
scale = (0.3, 0.3, 0.3)
translate = (0, 0, 0)
rotate = (0, 0, 0)
object_color = (0, 1, 1)

face = Obj.Obj("Nutella_Milkshake.obj")

#Correr textura
#t = texture.Texture("Nutella-Milkshake.bmp")

# Definir las propiedades de la camara - Viewport y angulos de vision
# El viewport debe ser mas pequeño que el tamaño de imagen jeje
Camera = camera.Camera()

Camera.loadViewportMatrix(100, 100, 100, 100)


#Medium angle
"""
Camera.lookAt(V3(0, 0, 30), V3(0, 0, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)
"""

#Low angle
"""
Camera.lookAt(V3(0, 0, 3), V3(0, 0, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)
"""

#High angle
"""
Camera.lookAt(V3(0, 10, 10), V3(0, 0, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)
"""

#Dutch angle
"""
rotate = (0, 0, 3.1416/3)
Camera.lookAt(V3(10, 10, 10), V3(-40, -10, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color)
"""

# Se escribio en prueba.bmp
nvidia.glFinish()
