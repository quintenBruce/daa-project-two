class course:
    def __init__(self, _name, _prereqs):
        self.name = _name
        self.prereqs = _prereqs

    def printName(self):
        print(self.name)


#course initialization
cs3 = course("CS 3", [])
cs7 = course("CS 7", [])
cs6 = course("CS 6", [cs7])
cs4 = course("CS 4", [cs6, cs7])
cs0 = course("CS 0", [cs3, cs4])
cs5 = course("CS 5", [cs6])
cs1 = course("CS 1", [cs6])
cs2 = course("CS 2", [cs5])


topologicalOrdering = [];
visited = []; #contains the visited nodes for the current dfs recursive call


#modified depth first search algorithm to perform topological ordering
def dfs(crs: course): 
    return



courses = [cs0, cs1, cs2, cs3, cs4, cs5, cs6, cs7]

for course in courses: # run dfs on all courses
    if dfs(course) == False: print("Typological ordering not possible - cyclical graph")

for course in topologicalOrdering: course.printName() #print topological ordering