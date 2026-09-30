import geometry2
from geometry2.flat import triangle_area
from geometry2.solid import sphere_volume
from geometry2.solid import hemishere_area

print('geometry2.__version__  =', geometry2.__version__)
print('geometry2.circle_area(3)     =', round(geometry2.circle_area(3), 4))
print('triangle_area(6, 4)          =', triangle_area(6, 4))
print('sphere_volume(3)             =', round(sphere_volume(3), 4))
print('hemishere_area(3)            =', round(hemishere_area(3), 4))
print('geometry2.__all__            =', geometry2.__all__)
print('geometry2.__file__           =', geometry2.__file__)