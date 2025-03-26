graph = {
    'S' : [('A', 2) , ('B' , 3) , ('D' , 5)], 
    'A' : [('C' , 4)], 
    'B' : [('D' , 4)], 
    'C' : [('D' , 1), ('G' , 2)], 
    'D' : [('G' , 5)], 
    'G' : []
}

def pathCost (path) : 
    totalCost = 0 
    for(node , cost) in path:
        totalCost += cost 
    return totalCost  , path[-1][0]

def ucs(graph , start , goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=pathCost)# sorting by cost
        path = queue.pop(0) # choosing least cost
        node = path[-1][0]
        if node in visited : 
            continue
        visited.append(node)
        if node == goal: 
            return path 
        else: 
            adjacentNodes = graph.get(node , [])
            for (node2 , cost)in adjacentNodes: 
                newPath = path.copy()
                newPath.append((node2 , cost))
                queue.append(newPath)


solution = ucs(graph , 'S' , 'G')
print('solution is ', solution)
print('cost of solution is ' , pathCost(solution)[0])