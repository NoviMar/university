from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("arial.ttf",24)
img = Image.new("RGB", (1000, 1000), "white")
i_draw = ImageDraw.Draw(img)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def draw_binary_tree(self, x, y, dx, dy, i_draw):
        if self.left is not None:
            new_x, new_y = x - dx, y + dy
            i_draw.line([(x, y), (new_x, new_y)], width=2, fill='black')
            self.left.draw_binary_tree(new_x, new_y, dx // 2, dy, i_draw)
     
        if self.right is not None:
            new_x, new_y = x + dx, y + dy
            i_draw.line([(x, y), (new_x, new_y)], width=2, fill='black')
            self.right.draw_binary_tree(new_x, new_y, dx // 2, dy, i_draw)
     
        i_draw.ellipse((x - 40, y - 40, x + 40, y + 40), fill='white', outline='black')
        if self.data < 0:
            i_draw.text((x, y), str(self.data), (0, 0, 0), font)
        else:
            i_draw.text((x - 11, y - 10), str(self.data), (0, 0, 0), font)

    def replace_negative_values(self):
        if self.data < 0:
            self.data = abs(self.data)
        if self.left is not None:
            self.left.replace_negative_values()
        if self.right is not None:
            self.right.replace_negative_values()

quantity = int(input("Введите количество элементов дерева: "))
if quantity != 0:
    first = float(input("Введите элемент дерева: "))
    root = Node(first)
    for top in range(quantity - 1):
        element = float(input("Введите элемент дерева: "))
        root.insert(element)
    root.replace_negative_values()
    root.draw_binary_tree(500, 50, 250, 100, i_draw)
    img.show()
else: 
    print("Дерево пустое.") 