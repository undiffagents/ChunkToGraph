# Make classes for each type of chunk

class GenericChunk:

    isa = 'chunk'

    def __init__(self,ID):
        self.attributes = {}
        self.ID = ID

    def addAttribute(self,attributeType,attributeValue):
        self.attributes.update({attributeType: attributeValue})

    def getAttributes(self):
        return self.attributes

    def getID(self):
        return self.ID


class TaskChunk:

    isa = 'task'

    def __init__(self,ID):
        self.name = ""
        self.role = ""
        self.ID = ID

    def getID(self):
        return self.ID

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setRole(self,role):
        self.role = role

    def getRole(self):
        return self.role

    def __str__(self):
        return "%s\n isa: %s\n name: %s\n role: %s" % (self.ID, self.isa, self.name, self.role)

class NodeChunk:

    isa = 'node'

    def __init__(self,ID):
        self.role = ""
        self.name = ""
        self.parent = ""
        self.ID = ID

    def getID(self):
        return self.ID

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setRole(self,role):
        self.role = role

    def getRole(self):
        return self.role

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "%s\n isa: %s\n name: %s\n role: %s\n parent: %s" % \
               (self.ID, self.isa, self.name, self.role, self.parent)

class EdgeChunk:

    isa = 'edge'

    def __init__(self,ID):
        self.role = ""
        self.source = ""
        self.dest = ""
        self.parent = ""
        self.ID = ID

    def getID(self):
        return self.ID

    def setRole(self,role):
        self.role = role

    def getRole(self):
        return self.role

    def setSource(self,source):
        self.source = source

    def getSource(self):
        return self.source

    def setDest(self,dest):
        self.dest = dest

    def getDest(self):
        return self.dest

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "%s\n isa: %s\n role: %s\n source: %s\n dest: %s\n parent: %s" % \
               (self.ID, self.isa, self.role, self.source, self.dest, self.parent)

class ConditionChunk:

    isa = 'condition'

    def __init__(self,ID):
        self.subj = ""
        self.pred = ""
        self.target = ""
        self.cons = ""
        self.parent = ""
        self.ID = ID

    def getID(self):
        return self.ID

    def setSubj(self,subj):
        self.subj = subj

    def getSubj(self):
        return self.subj

    def setPred(self,pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def setTarget(self,target):
        self.target = target

    def getTarget(self):
        return self.target

    def setCons(self,cons):
        self.cons = cons

    def getCons(self):
        return self.cons

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "%s\n isa: %s\n subj: %s\n pred: %s\n target: %s\n cons: %s\n parent: %s" % \
               (self.ID, self.isa, self.subj, self.pred, self.target, self.cons, self.parent)
