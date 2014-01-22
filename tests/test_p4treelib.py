import unittest
from p4treelib import Tree, Node

class NodeCase(unittest.TestCase):
	def setUp(self):
		self.node1 = Node("Test One", "ide ntifier 1 ")

	def test_initialization(self):
		self.assertEqual(self.node1.tag, "Test One")
		self.assertEqual(self.node1.identifier, "ide_ntifier_1")
		self.assertEqual(self.node1.expanded, True)

	def test_set_fpointer(self):
		self.node1.update_fpointer(" identi fier 2")
		self.assertEqual(self.node1.fpointer, ['identi_fier_2'])

	def test_set_bpointer(self):
		self.node1.bpointer = " identi fier  1"
		self.assertEqual(self.node1.bpointer, 'identi_fier__1')

	def test_set_data(self):
		self.node1.data = {1:'hello', "two":'world'}
		self.assertEqual(self.node1.data, {1:'hello', "two":'world'})

	def tearDown(self):
		pass


class TreeCase(unittest.TestCase):
    def setUp(self):
        tree = Tree()
        tree.create_node("Harry", "harry")
        tree.create_node("Jane", "jane", parent="harry")
        tree.create_node("Bill", "bill", parent="harry")
        tree.create_node("Diane", "diane", parent="jane")
        tree.create_node("George", "george", parent="diane")
        tree.create_node("Mary", "mary", parent="diane")
        tree.create_node("Jill", "jill", parent="george")
        tree.create_node("Mark", "mark", parent="jane")
        self.tree = tree

    def test_tree(self):
        self.assertIsInstance(self.tree, Tree)

    def test_getitem(self):
        """Nodes can be accessed via getitem."""
        tree = Tree()
        tree.create_node("Harry", "harry")
        tree.create_node("Jane", "jane", parent="harry")

        for node_id in tree.nodes:
            try:
                tree[node_id]
            except KeyError:
                self.fail('Node access should be possible via getitem.')

        try:
            tree['root']
        except KeyError:
            pass
        else:
            self.fail('There should be no default fallback value for getitem.')

    def tearDown(self):
        pass

class access():
    def __init__(self, binary):
        self.access = "an access"
        self.binary = binary

class AccessTreeCase(unittest.TestCase):

    def setUp(self):
        #create root
        self.t = Tree()
        self.t.create_node("x","x", access=access(binary=0))

    def test_dont_prune_root(self):
        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves()
        self.assertRaises(CannotPruneException)
        self.t.show(show_access=True)

    def test_dont_prune_root(self):
        self.t['x'].access.binary = 1
        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves()
        self.assertEqual(self.t.size(), 1)
        self.t.show(show_access=True)

    def test_prune(self):
        self.t.create_node("y","y", parent="x", access=access(binary=0))
        self.t.create_node("b","b", parent="x", access=access(binary=0))
        self.t.create_node("c","c", parent="b", access=access(binary=0))
        self.t.create_node("z","z", parent="y", access=access(binary=0))
        self.t.create_node("a","a", parent="y", access=access(binary=5))

        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves()
        self.assertEqual(self.t.size(), 3)
        self.t.show(show_access=True)


class TypedTreeCase(unittest.TestCase):

    def setUp(self):
        t = Tree(typed=True)
        t.create_node("x","x", path=True)
        t.create_node("y","y", parent="x", path=True)
        t.create_node("b","b", parent="x", path=True)
        t.create_node("c","c", parent="b", path=True)
        t.create_node("z","z", parent="y", user=True, access=access(binary=0))
        t.create_node("a","a", parent="y", user=True, access=access(binary=5))
        self.t = t

    def test_prune_typed(self):
        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves()
        self.t.show(show_access=True)
        self.assertEqual(self.t.size(), 4)

class TypedPruningCase(unittest.TestCase):

    def setUp(self):
        t = Tree(typed=True)
        t.create_node("//...","//...", path=True)
        t.create_node("u1//...","u1//...", parent="//...", user=True, access=access(binary=0))
        t.create_node("u2//...","u2//...", parent="//...", user=True, access=access(binary=0))
        t.create_node("//one/...","//one/...", parent="//...", path=True)
        t.create_node("u1//one/...","u1//one/...", parent="//one/...", user=True, access=access(binary=0))
        t.create_node("u2//one/...","u2//one/...", parent="//one/...", user=True, access=access(binary=0))
        t.create_node("//one/red/...","//one/red/...", parent="//one/...", path=True)
        t.create_node("u1//one/red/...","u1//one/red/...", parent="//one/red/...",
                user=True, access=access(binary=0))
        t.create_node("u2//one/red/...","u2//one/red/...", parent="//one/red/...",
                user=True, access=access(binary=0))
        t.create_node("//one/red/old/...","//one/red/old/...", parent="//one/red/...", path=True)
        t.create_node("u1//one/red/old/...","u1//one/red/old/...", parent="//one/red/old/...",
                user=True, access=access(binary=0))
        t.create_node("u2//one/red/old/...","u2//one/red/old/...", parent="//one/red/old/...",
                user=True, access=access(binary=0))
        t.create_node("//one/red/new/...","//one/red/new/...", parent="//one/red/...", path=True)
        t.create_node("//one/blue/...","//one/blue/...", parent="//one/...", path=True)
        t.create_node("u1//one/blue/...","u1//one/blue/...", parent="//one/blue/...",
                user=True, access=access(binary=0))
        t.create_node("u2//one/blue/...","u2//one/blue/...", parent="//one/blue/...",
                user=True, access=access(binary=0))
        t.create_node("//two/...","//two/...", parent="//...", path=True)
        t.create_node("u1//two/...","u1//two/...", parent="//two/...", user=True, access=access(binary=0))
        t.create_node("u2//two/...","u2//two/...", parent="//two/...", user=True, access=access(binary=0))
        t.create_node("//two/black/...","//two/black/...", parent="//two/...", path=True)
        t.create_node("u1//two/black/...","u1//two/black/...", parent="//two/black/...",
                user=True, access=access(binary=0))
        t.create_node("u2//two/black/...","u2//two/black/...", parent="//two/black/...",
                user=True, access=access(binary=0))
        t.create_node("//two/blue/...","//two/blue/...", parent="//two/...", path=True)
        t.create_node("u1//two/blue/...","u1//two/blue/...", parent="//two/blue/...",
                user=True, access=access(binary=0))
        t.create_node("u2//two/blue/...","u2//two/blue/...", parent="//two/blue/...",
                user=True, access=access(binary=0))
        self.t = t

    def test_prune_typed_full(self):
        t2 = Tree(tree=self.t, deep=True)
        t2.remove_node("//one/red/new/...")

        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves()
        self.t.show(show_access=True)

        for node in t2.expand_tree():
            try:
                self.t[node]
            except:
                self.fail("couldn't find node {} on self.t".format(node))


def suite():
    suites = [NodeCase, TreeCase, AccessTreeCase, TypedTreeCase, TypedPruningCase]
    suite = unittest.TestSuite()
    for s in suites:
        suite.addTest(unittest.makeSuite(s))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
