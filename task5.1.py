import sys, site

print("ispolnyaemiy fayl:", sys.executable)
print("prefiks", sys.prefix)
print("bazoviy prefiks:", sys.base_prefix)
print("v virtualnom okruzhenii??", sys.prefix != sys.base_prefix)
print("site-packages :", site.getsitepackages())
