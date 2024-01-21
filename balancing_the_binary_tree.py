from random import randint
from PIL import Image, ImageDraw, ImageFont

class Node:
    def __init__(self, val, name):
        self.data:int = val
        self.left: Node 
        self.right: Node 
        self.id: int = name
        self.high: int = 0

    def __repr__(self):
        return "\n".join([f'Data = {self.data}',
                          f'Right = {None if self.right is None else self.right.data}',
                          f'Left = {None if self.left is None else self.left.data}'])

class BinaryTree:
    def __init__(self):
        self.root: Node 
        self.count: int = 0

    def __str__(self):
        if self.root is not None:
            return " ".join(self._get_tree(self.root))
        return ''

    def __len__(self):
        if self.root is not None:
            return len(self._get_tree(self.root))
        return 0

    # region Public

    def insert(self, val: int, name: int):
        if self.root is not None:
            self._insert(val, self.root, name)
        else:
            self.root = Node(val, name)
        self.count += 1

    def delete_tree(self,node: Node):
        if node is not None :
            self.delete_tree(node.left)
            self.delete_tree(node.right)
            del node
            self.count -= 1

    def paint_tree(self):
        img = Image.new("RGB", (1000, 1000), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf",20)

        if self.root is not None:
            self._drawTree(self.root,500,25,250,50,draw,font)

        return img

    def balans_tree(self, node,pred,predLR):
        if node == None :
            return False

        self._high_tree(self.root)
        f1,f2 = False, False
        if node.left :
            f1 = self.balans_tree(node.left,node,'L')
        self._high_tree(self.root)
        if node.right:
            f2 = self.balans_tree(node.right,node,'R')
        self._high_tree(self.root)

        f3 = self._rotate_not_balans_node(node,pred,predLR)
        return f1 or f2 or f3

    # endregion

    # region Private

    def _rotate_not_balans_node(self,node,pred, predLR):

        if not node or node and not node.left and not node.right: 
            return False

        f = False
        if node and node.left and node.right and node.left.high - node.right.high <=-2 :
            self._big_left_rotate(node,pred,predLR)
            f = True
            print(node.data)
        elif node and node.left and node.right and node.left.high - node.right.high >= 2 :
            self._big_right_rotate(node,pred,predLR)
            f = True
            print(node.data)
        elif node and not node.left and node.right and node.right.high > 1 :
            self._big_left_rotate(node,pred, predLR)
            f = True
            print(node.data)
        elif node and node.left and not node.right and node.left.high > 1 :
            self._big_right_rotate(node,pred,predLR)
            f = True
            print(node.data)
        return f
    
                
    def _drawTree(self,node,x,y,dx,dy,draw,font):
        if node.left is not None :
            newx,newy = x-dx,y+dy
            draw.line([(x,y),(newx,newy)],width=2,fill = 'black')
            self._drawTree(node.left,newx,newy,dx//2,dy,draw,font)
        if node.right is not None:    
            newx,newy = x+dx,y+dy
            draw.line([(x,y),(newx,newy)],width=2,fill = 'black')
            self._drawTree(node.right,newx,newy,dx//2,dy,draw,font)
       
        draw.ellipse( (x-25,y-25,x+25,y+25),fill = 'white', outline = "black"  )
        if node.data < 10 :
            draw.text((x-7,y-7),str(node.data),(0,0,0),font)
        else:    
            draw.text((x-10,y-7),str(node.data),(0,0,0),font)

    def _insert(self, value: int, node: Node, name: int):
        if value < node.data:
            if node.left is not None:
                self._insert(value, node.left, name)
            else:
                node.left = Node(value,name)
        else:
            if node.right is not None:
                self._insert(value, node.right, name)
            else:
                node.right = Node(value,name)
                
    def _get_tree(self, node: Node):
        if node is not None:
            return self._get_tree(node.left) + [str(node.data)] \
                   + self._get_tree(node.right)
        return []

    def _high_tree(self, node):
        if not node :
            return 0
        node.high = 1 + max ( self._high_tree(node.left), self._high_tree(node.right) )
        return node.high

    def _small_left_rotate(self,node, pred , predLR):
        RL = node.right.left
        node.right.left = node
        if node == self.root :
            self.root = node.right
        else:        
            if predLR == 'L' :
                pred.left = node.right
            else:
                pred.right = node.right
        node.right = RL

    def _small_right_rotate(self,node, pred , predLR):
        LR = node.left.right
        node.left.right = node
        if node == self.root :
            self.root = node.left
        else:        
            if predLR == 'L' :
                pred.left = node.left
            else:
                pred.right = node.left
        node.left = LR

    def _big_left_rotate(self, node, pred, predLR):
        print('L',end='')
        print(pred)
        print('L',end='')
        print(node)
        if node.right.left :
            self._small_right_rotate(node.right, node, 'R')
        self._small_left_rotate(node,pred,predLR)

    def _big_right_rotate(self, node, pred, predLR):
        print('R',end='')
        print(pred)
        print('R',end='')
        print(node)
        if node.left.right:
            self._small_left_rotate(node.left, node, 'L')
        self._small_right_rotate(node,pred,predLR)        

    # endregion

def main():
    tree = BinaryTree()
    for i in range(20):
        tree.insert(randint(1, 20), i)
    print(tree._get_tree(tree.root))
    print(f'Вывод по порядку: {tree}\nРазмер дерева: {len(tree)}')
    img = tree.paint_tree()
    img.show()

    while tree.balans_tree(tree.root,None,''):
        img1 = tree.paint_tree()
        img1.show()    

        
    tree.delete_tree(tree.root)
    tree = None


if __name__ == "__main__":
    main()