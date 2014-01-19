from p4treelib import Tree

t = Tree(typed=True)

class x():
    def __init__(self, binary):
        self.access = "x"
        self.binary = binary

t.create_node("x","x", path=True)

changed = True
while changed:
    import pdb; pdb.set_trace()
    changed = t.prune_no_access_leaves()

t.show(show_access=True)
