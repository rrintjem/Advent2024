'''


'''
import sys
from queue import Queue
from heapq import heapify, heappop, heappush

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
class GraphNode:
    def __init__(self, id,loc,paths):
       self.id = id
       self.loc = loc
       self.paths=paths
       self.neighbours = []
    
    def add_neighbour(self, node):
        self.neighbours.append(node)

class Graph:
    def __init__(self, graph: dict = {}):
       self.graph = graph  # A dictionary for the adjacency list

    def add_node(self,node):
        if node not in self.graph:  # Check if the node is already added
           self.graph[node] = {} 
    def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
        
       self.graph[node1][node2] = weight  # Else, add a connection to its neighbor
   
    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()
        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(
               pq
            )  # Get the node with the min distance

            if current_node in visited:
               continue  # Skip already visited nodes
            visited.add(current_node)  # Else, add the node to visited set
            for neighbor, weight in self.graph[current_node].items():
                # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
        predecessors = {node: None for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors
    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()

        return path

def getFilename():
    argc = len(sys.argv)
    filename = 'input16.txt'
    if argc > 1:
        filename = 'test_input16.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    rows = []
    for line in f:
        data = list(line.strip())
        rows.append(data)

    return rows

def isNode(data,row,col):
    res = False
    touchPoints = 4

    coords = []
    for d in dirs:
        try:
            val = data[row+d[0]][col+d[1]]
            if val != '#':
                coords.append(d)
        except:
            val = '#'
        if val == '#':
            touchPoints-=1

    if data[row][col] == 'S' or data[row][col] == 'E':
        res = True
    else:
        if touchPoints == 2:
            #print(coords)
            if coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]:
                res = False
            else: 
                res = True
        elif touchPoints > 2:
            res = True

    return res,coords

def findLocation(data,val):
    max_rows = len(data)
    max_cols = len(data[0])
    x = 0
    for y in range(max_rows):
        row = data[y]
        if val in row:
            x = row.index(val)
            break
    return (y,x)

def getIntersectID(coord):
    for n in intersections:
        if n.loc == coord:
            return n.id
    return None
def getIntersectCoord(id):
    for n in intersections:
        if n.id == id:
            return n.loc
    return None
def getNodeID(coord):
    for n in nodes:
        if n.loc == coord:
            return n.id
    return None

def getNodeCoord(id):
    for n in nodes:
        if n.id == id:
            return n.loc
    return None

def getNodePaths(id=None,coord=None):
    for n in nodes:
        if n.id == id or n.loc == coord:
            return n.paths
    return None

def calcPathCost(path):
    cost = 0
    dir = '>'
    prev_val =''
    for n in path:
        movement = ''
        if n == 'S':
            prev_val = n
            prev= getNodeCoord(n)
            continue
        curr = getNodeCoord(n)
        if curr[0] < prev[0]:#moving up
            movement = '^'
        if curr[0] > prev[0]:#moving down
            movement = 'v'
        if curr[1] < prev[1]:#moving left
            movement = '<'
        if curr[1] > prev[1]:#moving right
            movement = '>'
        
        n_dist = G.graph[prev_val][n]
        if movement != dir and n_dist < 1000 and n != 'E':
            dir = movement
            cost += 1000
            print('Turn + 1000')
        print('+'+str(n_dist))
        cost+=n_dist
        prev_val = n
        prev= getNodeCoord(n)
    return cost

def findIntersectNeighbours(node,data):
    for d in node.paths:
        distance = 0
        curr = node.loc

        while True:
            distance +=1
            curr = (curr[0]+d[0],curr[1]+d[1])
            if data[curr[0]][curr[1]] == '#':
                break
            if curr in node_coords:
                n_id = getNodeID(curr)
                node.add_neighbour(n_id)
                if len(getNodePaths(id=n_id)) == 2 and n_id != 'E' and n_id != 'S':
                    distance += 1000
                

                G.add_edge(node.id, n_id, distance)
                #print('{} to {} = {}'.format(node.id,n_id,distance))
                break
    return node,G

def findNeighbours(node,data):
    for d in node.paths:
        distance = 0
        curr = node.loc

       # print(node.id,d)
        while True:
            distance +=1
            curr = (curr[0]+d[0],curr[1]+d[1])
            if data[curr[0]][curr[1]] == '#':
                break
            if curr in node_coords:
                n_id = getNodeID(curr)
                node.add_neighbour(n_id)
                if len(getNodePaths(id=n_id)) == 2 and n_id != 'E' and n_id != 'S':
                    distance += 1000
                

                G.add_edge(node.id, n_id, distance)
                #print('{} to {} = {}'.format(node.id,n_id,distance))
                break
            if curr in intersect_coords:
                n_id = getIntersectID(curr)
                intersect_neighbours = findIntersectNeighbours(n_id,data)



    return node,G


def part1(data):
    global G 
    global nodes
    global node_coords
    global intersections
    global intersect_coords

    G = Graph()
    nodes = []
    node_coords = []
    intersections = []
    intersect_coords = []
    result = 0
   
    i = 0
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            if col == '#':
                print(col,end='')
                continue
            checkNode, pathDirs=isNode(data,y,x)
            
            if checkNode:
                if col =='S' or col == 'E':
                    nodes.append(GraphNode(col,(y,x),pathDirs))
                    G.add_node(col)
                    print(col,end='')
                    node_coords.append((y,x))
                else:
                    num_paths = len(pathDirs)
                    if num_paths > 2:
                        intersect_coords.append((y,x))
                        intersections.append(GraphNode(str(i),(y,x),pathDirs))
                        print('+',end='')
                    else:
                        nodes.append(GraphNode(str(i),(y,x),pathDirs))
                        print('X',end='')
                        G.add_node(str(i))
                        i+=1
                        node_coords.append((y,x))
                
            else:
                print(col,end='')
            
        print('')
    
    for i,n in enumerate(nodes):
        #print(n.id,end=': ')
        nodes[i],G = findNeighbours(n,data)
        #print(nodes[i].neighbours)

    

    
    
    maze_path = G.shortest_path('S', 'E')
   # print(maze_path)
    result = calcPathCost(maze_path)

    '''if result <= 93449:
        result = 'too low'
    elif result >= 94448:
        result = 'too high'
    '''
    return result

def part2(data):
    result = 0
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    part1_result =part1(data)
    print(part1_result)

    #part2_result = part2(data)
    #print(part2_result)

main()
