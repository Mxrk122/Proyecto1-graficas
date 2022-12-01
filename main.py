import gl
import texture
from vector3 import *
import camera
import math
import Obj


filename = 'bread.bmp'


nvidia = gl.gl(filename)

nvidia.glCreateWindow(1000, 1000)

nvidia.glClearColor(0.5, 0.5, 0.5)

nvidia.glClear()

# Definir las propiedades de la camara - Viewport y angulos de vision
# El viewport debe ser mas pequeño que el tamaño de imagen jeje
Camera = camera.Camera()

Camera.loadViewportMatrix(100, 100, 100, 100)


#table
scale = (3, 3, 3)
translate = (2, 1, 0)
rotate = (math.pi/5, 0, 0)
object_color = (0, 1, 1)
face = Obj.Obj("table.obj")
Camera.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))
t = texture.Texture("wood.bmp")
#Correr textura
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)

# nutella
scale = (0.2, 0.2, 0.2)
translate = (0, 2, 1)
rotate = (math.pi/4, 0, 0)
object_color = (0, 1, 1)
face = Obj.Obj("Nutella_Milkshake.obj")
Camera.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))
t = texture.Texture("Nutella-milkshake.bmp")
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)


# Setear el shader
shader = [(1, 100/255, 230/255), (130/255, 77/255, 51/255)]
nvidia.setShader(shader)
#dona
scale = (15, 15, 15)
translate = (1.5, 3, 0)
rotate = (math.pi/4, 0, 0)
object_color = (0, 1, 1)
face = Obj.Obj("Doughnut_OBJ.obj")
Camera.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color)

#cinamon_roll_1k
scale = (15, 15, 15)
translate = (3, 2, 0)
rotate = (math.pi/4, 0, 0)
object_color = (0, 1, 1)
face = Obj.Obj("cinamon_roll_1k.obj")
t = texture.Texture("crtexture.bmp")
Camera.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)


#pan
scale = (0.1, 0.1, 0.1)
translate = (4, 1, 2)
rotate = (math.pi/3, 0, 0)
object_color = (1, 0.5, 1)
face = Obj.Obj("pan.obj")
t = texture.Texture("pt.bmp")
Camera.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))
nvidia.glObjectMode(face, Camera, scale, translate, rotate, object_color, t)


# Se escribio en prueba.bmp
nvidia.glFinish()
