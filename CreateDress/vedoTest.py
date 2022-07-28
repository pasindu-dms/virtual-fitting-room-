from vedo import *

mesh = Mesh("shirt.obj", "red")

mesh.texture("shirttexture.jpg", scale=0.1)
print(mesh.faces())
mesh.show()