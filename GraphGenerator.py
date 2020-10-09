import networkx
from ChunkClasses import *
from Constants import *


def generateGraph(typedChunkList):
    # Create graph
    graph = networkx.MultiDiGraph()
    # Populate graph
    for chunk in typedChunkList:
        graph = handleChunk(chunk, graph)
    # Return graph
    return graph


def handleChunk(chunk, graph):
    if type(chunk) ==  TaskChunk:
        # Create task in graph
        graph = handleTask(chunk, graph)
    if type(chunk) == NodeChunk:
        # Create node in graph
        graph = handleNode(chunk, graph)
    if type(chunk) == EdgeChunk:
        # Create edge in graph
        graph = handleEdge(chunk, graph)
    if type(chunk) == ConditionChunk:
        # Create condition in graph (THIS WILL BE THE HARDEST PART)
        graph = handleCondition(chunk, graph)
    return graph


def handleTask(chunk: TaskChunk, graph):
    # Get task attributes
    taskID = chunk.getID()
    taskName = chunk.getName()
    taskRole = chunk.getRole()

    # Add task and its attributes to graph
    graph.add_node(taskID, value=taskID)
    graph = addName(graph, taskID, taskName)
    graph = addRole(graph, taskID, taskRole)

    # Return updated graph
    return graph


def handleNode(chunk: NodeChunk, graph):
    # Get node attributes
    nodeID = chunk.getID()
    nodeName = chunk.getName()
    nodeRole = chunk.getRole()
    nodeParent = chunk.getParent()

    # Add node and its attributes to the graph
    graph.add_node(nodeID, value=nodeID)
    graph = addName(graph, nodeID, nodeName)
    graph = addRole(graph, nodeID, nodeRole)
    if nodeParent != 'nil':
        graph.add_edge(nodeID, nodeParent, value=CONST_GRAPH_HAS_PARENT_EDGE)

    # Return updated graph
    return graph


def handleEdge(chunk: EdgeChunk, graph):
    # Get edge attributes
    edgeID = chunk.getID()
    edgeRole = chunk.getRole()
    edgeSource = chunk.getSource()
    edgeDest = chunk.getDest()
    edgeParent = chunk.getParent()

    # We can probably ignore edgeID and edgeParent
    # Add edge to graph
    graph.add_edge(edgeSource, edgeDest, value=edgeRole)

    # Return updated graph
    return graph


def handleCondition(chunk: ConditionChunk, graph):
    # Need to figure out how to handle conditions, as they can have edges as a consequence...
    return graph


def addName(graph, ID, name):
    graph.add_node(ID + "_name", value=name)
    graph.add_edge(ID, ID + "_name", value=CONST_GRAPH_HAS_NAME_EDGE)
    return graph


def addRole(graph, ID, role):
    graph.add_node(ID + "_role", value=role)
    graph.add_edge(ID, ID + "_role", value=CONST_GRAPH_HAS_ROLE_EDGE)
    return graph
