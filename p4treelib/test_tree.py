from p4treelib import Tree

t = Tree(typed=True)

class x():
    def __init__(self, binary):
        self.access = "x"
        self.binary = binary

t.create_node("x","x", path=True)
t.create_node("y","y",parent="x", path=True)
t.create_node("b","b",parent="x", path=True)
t.create_node("c","c",parent="b", path=True)
t.create_node("z","z",parent="y", user=True, access=x(binary=0))
t.create_node("a","a",parent="y", user=True, access=x(binary=5))

changed = True
while changed:
    changed = t.prune_no_access_leaves()

t.show(show_access=True)
