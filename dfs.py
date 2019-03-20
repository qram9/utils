
class Node(object):
    def __init__(self):
        self.pre = 0
        self.rpost = 0
        self.succ = []
        self.n = 0
        
class DFS(object):
    def __init__(self):
        self.preorder = 1
        self.rpostorder = 100
        
    def do_dfs(self,inp):
        self.preorder = 1
        self.rpostorder = len(inp)
        for n in inp:
            n.pre = 0
            n.rpost = 0
    def DFS(self,n):
        n.pre = self.preorder
        self.preorder += 1
        for s in n.succ:
            if s.pre == 0:
                print "Tree Edge", n.n, s.n
                self.DFS(s)
            elif s.rpost == 0:
                print "Back Edge", n.n, s.n
            elif n.pre < s.pre:
                print "Forward Edge", n.n, s.n
            else:
                print "Cross Edge", n.n, s.n
        n.rpost = self.rpostorder
        rpostorder = self.rpostorder - 1

if __name__ == "__main__":
    inp = []
    n = Node()
    m = Node()
    p = Node()
    q = Node()
    r = Node()
    s = Node()
    
    n.n = 1
    m.n = 2
    p.n = 3
    q.n = 4
    r.n = 5
    s.n = 6
    
    n.succ = [m]
    m.succ = [p,q]
    p.succ = [m]
    q.succ = [m,r,s]

    inp.append(n)
    inp.append(m)
    inp.append(p)
    d = DFS()
    d.DFS(n)

        
    
