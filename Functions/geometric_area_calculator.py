def area(shape="rectangle", a=0, b=0, r=0, h=0):
    if shape == "square":
        return a * a
    elif shape == "rectangle":
        return a * b
    elif shape == "circle":
        return 3.14 * r * r
    elif shape == "triangle":
        return 0.5 * a * h
    else:
        return "Unknown shape"

print(area("square", a=5))         
print(area("rectangle", a=4, b=6)) 
print(area("circle", r=3))         
print(area("triangle", a=4, h=5))  
print(area(a=7, b=8))