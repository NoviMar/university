from PIL import Image, ImageDraw, ImageFont
import math
from random import randint

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

def draw_graph(img, adjacency_matrix, square_size, p, start, end):
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

    current_vertex = end
    while current_vertex != start:
        previous_vertex = p[current_vertex]
        x1, y1 = vertex_coordinates[previous_vertex]
        x2, y2 = vertex_coordinates[current_vertex]
        draw.line([(x1, y1), (x2, y2)], fill='red', width=5)
        current_vertex = previous_vertex

def Dijkstra(adjacency_matrix, num_vertices, start, p):
    INF = 10**10
    F = [INF] * num_vertices
    F[start] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        min_R = INF
        min_v = None

        for i in range(num_vertices):
            if not visited[i] and F[i] < min_R:
                min_R = F[i]
                min_v = i

        if min_v is None:
            break

        visited[min_v] = True

        for j, weight in enumerate(adjacency_matrix[min_v]):
            if weight and not visited[j] and F[j] > F[min_v] + weight:
                F[j] = F[min_v] + weight
                p[j] = min_v

    return F

filename = 'graph.txt'
adjacency_matrix = read_graph(filename)
num_vertices = len(adjacency_matrix)
num_columns = math.ceil(math.sqrt(num_vertices))
start_vertex, end_vertex = 1, 10
p = [0] * num_vertices
F = Dijkstra(adjacency_matrix, num_vertices, start_vertex - 1, p)
img = create_img(num_vertices)
draw_graph(img, adjacency_matrix, 1000 // max(num_columns, math.ceil(num_vertices / num_columns)), p, start_vertex - 1, end_vertex - 1)
img.show()
