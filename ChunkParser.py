from Constants import *
from ChunkClasses import *
from GraphGenerator import *
import string
import networkx


# Utility function pulled from https://stackoverflow.com/questions/26987222/checking-whitespace-in-a-string-python
def contains_whitespace(s: string):
    return True in [c in s for c in string.whitespace]


# Read in chunks, convert to networkx
def readInputFile():
    # Open the input file
    inputFile = open(CONST_INPUT_FILE_NAME, "r")

    # Set up variable for chunk IDs which will be updated over time
    # Also set up list of chunks which will be created
    currentChunkID = ""
    currentChunk = None
    chunkList = []

    # Read in each line
    for line in inputFile:
        # Strip unneeded whitespace
        line = line.strip()
        # If the line is not blank, continue processing
        if line:
            # If line only has one block of characters, then it's a new chunk
            if not contains_whitespace(line):
                # New Chunk ID - create generic chunk
                if currentChunk is not None:
                    chunkList.append(currentChunk)
                    currentChunk = None
                currentChunkID = line
                currentChunk = GenericChunk(currentChunkID)
            else:
                # Chunk element - add attribute to list of attributes
                chunkAttributes = line.split()
                chunkAttributeType = chunkAttributes[0]
                chunkAttributeValue = chunkAttributes[1]
                currentChunk.addAttribute(chunkAttributeType,chunkAttributeValue)

    return chunkList


def processChunk(genericChunk: GenericChunk):
    # Set up a variable for the non-generic chunk
    typedChunk = None
    # Get the list of chunk attributes from the generic chunk
    chunkAttributes = genericChunk.getAttributes()
    # Get the chunk type
    chunkType = chunkAttributes.get(CONST_CHUNK_ATTR_ISA)
    # create the non-generic chunk
    if chunkType == CONST_CHUNK_TYPE_TASK:
        typedChunk = TaskChunk(genericChunk.getID())
    elif chunkType == CONST_CHUNK_TYPE_CONDITION:
        typedChunk = ConditionChunk(genericChunk.getID())
    elif chunkType == CONST_CHUNK_TYPE_NODE:
        typedChunk = NodeChunk(genericChunk.getID())
    elif chunkType == CONST_CHUNK_TYPE_EDGE:
        typedChunk = EdgeChunk(genericChunk.getID())
    # Populate the attributes for the newly typed chunk:
    for attributeType, attributeValue in chunkAttributes.items():
        if attributeType != CONST_CHUNK_ATTR_ISA:
            # Construct the method name to call
            # Attribute type is capitalized to match the camelCase format of the chunk methods
            methodName = 'set' + attributeType.capitalize()
            # Add the attribute to the chunk:
            getattr(typedChunk, methodName)(attributeValue)

    return typedChunk


def main():
    # Get list of chunks as generic chunks divorced from type
    genericChunkList = readInputFile()
    typedChunkList = []

    # Process the generic chunks into their actual chunk types
    for chunk in genericChunkList:
        newChunk = processChunk(chunk)
        typedChunkList.append(newChunk)

    # Clear the generic chunk list to free up memory
    genericChunkList.clear()

    # DEBUG: Print out the chunks
    for chunk in typedChunkList:
        print(chunk)

    # Generate graph based on chunks
    graph = generateGraph(typedChunkList)
    networkx.write_graphml_lxml(graph, CONST_INPUT_FILE_NAME + ".graphml")

main()