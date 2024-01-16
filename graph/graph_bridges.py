from random import randint
import math
from PIL import Image, ImageDraw, ImageFont


def read_graph(filename):
    with open(filename, 'r') as file:
        num_vertices = int(file.readline().strip())
        adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

        for line in file:
            vertex1, vertex2, weight = map(int, line.split())
            adjacency_matrix[vertex1 - 1][vertex2 - 1] = weight
            adjacency_matrix[vertex2 - 1][vertex1 - 1] = weight

    return adjacency_matrix

def create_img(num_vertices):
    num_columns = math.ceil(math.sqrt(num_vertices))
    num_rows = math.ceil(num_vertices / num_columns)
    square_size = 1000 // max(num_columns, num_rows)

    width = num_columns * square_size
    height = num_rows * square_size
    img = Image.new('RGB', (width, height), 'white')

    return img

def draw_graph(img, adjacency_matrix, square_size):
    draw = ImageDraw.Draw(img)
    num_vertices = len(adjacency_matrix)
    num_columns = math.ceil(math.sqrt(num_vertices))

    vertex_coordinates = {}

    for i in range(num_vertices):
        row, col = i // num_columns, i % num_columns

        x = col * square_size + randint(square_size // 4, square_size - square_size // 4)
        y = row * square_size + randint(square_size // 4, square_size - square_size // 4)

        vertex_coordinates[i] = (x, y)

    font = ImageFont.truetype('arial.ttf', 32)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = adjacency_matrix[i][j]
            if weight != 0:
                x1, y1 = vertex_coordinates[i]
                x2, y2 = vertex_coordinates[j]
                draw.line([(x1, y1), (x2, y2)], 'black', width=3)
                draw.ellipse([(x1 - 10, y1 - 10), (x1 + 10, y1 + 10)], fill='black', outline='black')

                text_x, text_y = x1 - 10, y1 - 50
                str_ = i + 1
                draw.text((text_x, text_y), str(str_), fill='black', font=font)

    text_x, text_y = x2 - 10, y2 - 50
    draw.ellipse([(x2 - 10, y2 - 10), (x2 + 10, y2 + 10)], fill='black', outline='black')
    draw.text((text_x, text_y), str(str_ +  1 ), fill='black', font=font)

def find_bridges(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    visited = [False] * num_vertices
    INF = 10**10
    disc = [INF] * num_vertices
    low = [INF] * num_vertices
    parent = [-1] * num_vertices

    bridges = []

    def bridge_util(u, time):
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1

        for v in range(num_vertices):
            if adjacency_matrix[u][v] != 0:
                if not visited[v]:
                    parent[v] = u
                    time = bridge_util(v, time)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        bridges.append((u + 1, v + 1))
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        return time

    time = 0

    for i in range(num_vertices):
        if not visited[i]:
            time = bridge_util(i, time)

    return bridges


filename = 'graph.txt'
adjacency_matrix = read_graph(filename)
num_vertices = len(adjacency_matrix)
num_columns = math.ceil(math.sqrt(num_vertices))

img = create_img(num_vertices)
draw_graph(img, adjacency_matrix, 1000 // max(num_columns, math.ceil(num_vertices / num_columns)))

bridges = find_bridges(adjacency_matrix)
print("Bridges in the graph:")


for bridge in bridges:
    print(bridge)

img.show()