adjArray = []
def buildTristrips( triangles ):

    count = 0
    for tri in triangles:
        adjArray.append(numValidAdj(tri))
    
    sortedTriangles = [x for _, x in sorted(zip(adjArray, triangles), key=lambda pair: pair[0])]


    for tri in sortedTriangles:
        if (tri.nextTri == None and tri.prevTri == None):
            count += 1
            findNext(tri)
            sortedTriangles.append(sortedTriangles.pop(sortedTriangles.index(tri)))
    print (count)

def findNext(triangle):
    possibleAdj = []
    validAdj = []
    for adj in triangle.adjTris:
        if (adj.nextTri == None and adj.prevTri == None):
            possibleAdj.append(numValidAdj(adj))
            validAdj.append(adj)
    sortedValid = [x for _, x in sorted(zip(possibleAdj, validAdj), key=lambda pair: pair[0])]
    if len(possibleAdj) == 0:
        return

    triangle.nextTri = sortedValid[0]
    sortedValid[0].prevTri = triangle
    findNext(sortedValid[0])



def numValidAdj(triangle):
    numTris = 0
    for adj in triangle.adjTris:
        if(adj.nextTri == None and adj.prevTri == None):
            numTris += 1
    return numTris