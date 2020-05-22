"""
Create an A* algorithm to check the shortest distance
"""
import heapq
import math

#Create a class node to store the data for each intersection
class Map_Node:
    def __init__(self, intersection,f_value = 0, distance = 0, path = []):
        self.inter = intersection
        self.f = f_value
        self.dist = distance
        self.path = path

#Euclidean distance
def dist(in1, in2, M):
    dist2  = 0
    in1 = M.intersections[in1]
    in2 = M.intersections[in2]
    for i in range(2):
        dist2 += (in1[i] - in2[i])**2
    return math.sqrt(dist2)

#Function to get the f value
def f(in2, in1, M, goal):
    g = dist(in1,in2.inter,M) + in2.dist #Distance between intersection + distance from start of in2
    h = dist(in1,goal, M) #Linera distance from goal
    return g+h
    
def shortest_path(M,start,goal):
    print("shortest path called")
    explored = set()               #Set for explored intersections
    frontier = []                  #List for frontier
    end_node = None
    node_dic = {}                  #Dictionary to look for the nodes in O(1)
    #f_value = dist(start, goal, M)
    start_node = Map_Node(start, 0 , 0,[start]) #Create the first node
    node_dic[start] = start_node
    heapq.heappush(frontier, [0, start_node]) #Make frontier a priority queue using the f_value
    

                          
    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1] #Pop node from min heap
        explored.add(node) #Explore the intersection
        #When goal intersection is explored, return it
        if node.inter == goal:
            end_node = node
            break
        for road in M.roads[node.inter]:
            if road not in explored:
                f_value = f(node, road, M, goal)
                if road not in node_dic:             #if the intersection hasn't been seen before
                    distance = dist(node.inter, road, M) + node.dist
                    new_node = Map_Node(road,f_value, distance, node.path + [road]) #Create a node adding the f_value, distance and path
                    heapq.heappush(frontier, [new_node.f, new_node])                #Push to heap  
                    node_dic[road] = new_node
                else:
                    if f_value < node_dic[road].f:   #if this path is shorter, update it
                        node_dic[road].path = node.path + [road]
                        node_dic[road].f = f_value
                    
                    
    if not end_node:       #If the intersection wasn't found
        return None
    else:
        return end_node.path  #return the path
    return




