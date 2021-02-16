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
        self.consOf = ""
        self.prevCons = ""
        self.nextCons = ""
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

    def setConsof(self,consOf):
        self.consOf = consOf

    def getConsof(self):
        return self.consOf

    def setPrevcons(self,prevCons):
        self.prevCons = prevCons

    def getPrevcons(self):
        return self.prevCons

    def setNextcons(self,nextCons):
        self.nextCons = nextCons

    def getNextcons(self):
        return self.nextCons

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "%s\n isa: %s\n name: %s\n role: %s\n consOf: %s\n prevCons: %s\n nextCons: %s\n parent: %s" % \
               (self.ID, self.isa, self.name, self.role, self.consOf, self.prevCons, self.nextCons, self.parent)

class EdgeChunk:

    isa = 'edge'

    def __init__(self,ID):
        self.role = ""
        self.source = ""
        self.dest = ""
        self.envStateType = ""
        self.actionType = ""
        self.state = ""
        self.consOf = ""
        self.prevCons = ""
        self.nextCons = ""
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

    def setEnvironmentstatetype(self,envStateType):
        self.envStateType = envStateType

    def getEnvironmentstatetype(self):
        return self.envStateType

    def setActiontype(self,actionType):
        self.actionType = actionType

    def getActiontype(self):
        return self.actionType

    def setState(self,state):
        self.state = state

    def getState(self):
        return self.state

    def setConsof(self,consOf):
        self.consOf = consOf

    def getConsof(self):
        return self.consOf

    def setPrevcons(self,prevCons):
        self.prevCons = prevCons

    def getPrevcons(self):
        return self.prevCons

    def setNextcons(self,nextCons):
        self.nextCons = nextCons

    def getNextcons(self):
        return self.nextCons

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "%s\n isa: %s\n role: %s\n source: %s\n dest: %s\n environmentStateType: %s\n actionType: %s\n" \
               "state: %s\n consOf: %s\n prevCons: %s\n nextCons: %s\n parent: %s" % \
               (self.ID, self.isa, self.role, self.source, self.dest, self.envStateType, self.actionType,
                self.state, self.consOf, self.prevCons, self.nextCons, self.parent)

class ConditionChunk:

    isa = 'condition'

    def __init__(self,ID):
        #self.subj = ""
        self.pred = ""
        #self.target = ""
        #self.cons = ""
        self.desiredStatePred = ""
        self.firstCons = ""
        self.consequenceState = ""
        self.processed = ""
        self.parent = ""
        self.ID = ID

    def getID(self):
        return self.ID

    #def setSubj(self,subj):
    #    self.subj = subj

    #def getSubj(self):
    #    return self.subj

    def setPred(self,pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def setDesiredstatepred(self,desiredStatePred):
        self.desiredStatePred = desiredStatePred

    def getDesiredstatepred(self):
        return self.desiredStatePred

    def setFirstcons(self,firstCons):
        self.firstCons = firstCons

    def getFirstcons(self):
        return self.firstCons

    def setConsequencestate(self,consequenceState):
        self.consequenceState = consequenceState

    def getConsequencestate(self):
        return self.consequenceState

    def setProcessed(self,processed):
        self.processed = processed

    def getProcessed(self):
        return self.processed

    #def setTarget(self,target):
    #    self.target = target

    #def getTarget(self):
    #    return self.target

    #def setCons(self,cons):
    #    self.cons = cons

    #def getCons(self):
    #    return self.cons

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "%s\n isa: %s\n pred: %s\n desiredStatePred: %s\n firstCons: %s\n " \
               "consequenceState: %s\n processed: %s\n parent: %s" % \
               (self.ID, self.isa, self.pred, self.desiredStatePred, self.firstCons, self.consequenceState,
                self.processed, self.parent)
