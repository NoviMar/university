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

def find_max_leaf_value(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return node.data
    left_max = find_max_leaf_value(node.left)
    right_max = find_max_leaf_value(node.right)
    if left_max is None:
        return right_max
    elif right_max is None:
        return left_max
    else:
        return max(left_max, right_max)

def draw_binary_tree(node, x, y, dx, dy, i_draw):
    if node.left is not None:
        new_x, new_y = x - dx, y + dy
        i_draw.line([(x, y), (new_x, new_y)], width=2, fill='black')
        draw_binary_tree(node.left, new_x, new_y, dx // 2, dy, i_draw)
 
    if node.right is not None:
        new_x, new_y = x + dx, y + dy
        i_draw.line([(x, y), (new_x, new_y)], width=2, fill='black')
        draw_binary_tree(node.right, new_x, new_y, dx // 2, dy, i_draw)
 
    i_draw.ellipse((x - 25, y - 25, x + 35, y + 35), fill='white', outline='black')
    i_draw.text((x - 3, y - 10), str(node.data), (0, 0, 0), font)


quantity = int(input("Введите количество элементов дерева: "))

if quantity != 0:
    first = int(input("Введите элемент дерева: "))
    root = Node(first)

    for top in range(quantity - 1):
        element = int(input("Введите элемент дерева: "))
        root.insert(element)

    draw_binary_tree(root, 500, 50, 250, 100, i_draw)
    img.show()
    max_leaf_value = find_max_leaf_value(root)



print("Максимальное значение среди листьев дерева: ", end = "")
print("Его не существует" if quantity == 0 else max_leaf_value)