# OOP

#%%

class Apple:
    def __init__(self, color='red', flavor='sweet'):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
new_apple = Apple()
print(honeycrisp.flavor)
print(fuji.flavor)
print(new_apple.color)

# %%

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        return self.area() + other.area()

triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
# %%
