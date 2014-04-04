import unittest
from p4treelib import Tree, Node
from test_outputs import *

class AClass(object):

    def __init__(self, data):
        self.data = data

    def __unicode__(self):
        return str(self.data)

    def __str__(self):
        return self.__unicode__()


class access():
    def __init__(self, binary):
        self.access = "an access"
        self.binary = binary

    def __str__(self):
        return self.access


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

    def test_prune_simplified(self):
        self.t.create_node("y","y", parent="x", access=access(binary=0))
        self.t.create_node("b","b", parent="x", access=access(binary=0))
        self.t.create_node("c","c", parent="b", access=access(binary=0))
        self.t.create_node("z","z", parent="y", access=access(binary=0))
        self.t.create_node("a","a", parent="y", access=access(binary=5))

        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves(simplified=True)
        self.assertEqual(self.t.size(), 3)
        self.t.show(show_access=True)

    def test_prune(self):
        self.t.create_node("y","y", parent="x", access=access(binary=0))
        self.t.create_node("b","b", parent="x", access=access(binary=0))
        self.t.create_node("c","c", parent="b", access=access(binary=0))
        self.t.create_node("z","z", parent="y", access=access(binary=0))
        self.t.create_node("a","a", parent="y", access=access(binary=5))

        changed = True
        while changed:
            changed = self.t.prune_no_access_leaves(simplified=False)
        self.assertEqual(self.t.size(), 6)
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

    def test_link_past_node_with_users(self):
        self.t.create_node("d","d", parent="y", path=True)
        self.t.create_node("e","e", parent="d", user=True, access=access(binary=5))
        self.t.create_node("f","f", parent="d", path=True)

        self.t.link_past_node("y")

        with self.assertRaises(KeyError):
            self.t['y']

        with self.assertRaises(KeyError):
            self.t['z']

        with self.assertRaises(KeyError):
            self.t['a']

        self.assertIn('d',self.t['x'].fpointer)
        self.assertIn('e',self.t['d'].fpointer)
        self.assertIn('f',self.t['d'].fpointer)

        self.assertEqual('x',self.t['d'].bpointer)
        self.assertEqual('d',self.t['e'].bpointer)
        self.assertEqual('d',self.t['f'].bpointer)

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


class StrTypedTreeCase(unittest.TestCase):

    def setUp(self):
        t = Tree(typed=True)
        t.create_node("//...","//...", path=True)
        t.create_node("u2//...","u2//...", parent="//...", user=True, access=access(binary=0))
        t.create_node("//two/...","//two/...", parent="//...", path=True)
        t.create_node("//one/...","//one/...", parent="//...", path=True)
        t.create_node("u1//...","u1//...", parent="//...", user=True, access=access(binary=0))
        self.t = t

    def test_to_str_user_path_alphabet_ordered(self):
        #Just to check it is not a fluke
        for x in range(50):
            users = []
            paths = []
            for node in self.t[self.t.root].fpointer:
                if self.t[node].user:
                    users.append(node)
                else:
                    paths.append(node)

            queue = sorted(users) + sorted(paths)

            self.assertSequenceEqual(queue, ("u1//...", "u2//...", "//one/...", "//two/..."))

    def test_to_str(self):
        for x in range(5000):
            self.assertEqual(self.t.to_str(), TO_STR_SIMPLE)


class ToDictTreeCase(unittest.TestCase):

    def setUp(self):
        t = Tree(typed=True)
        t.create_node(AClass("AC//..."), "//...", path=True)
        t.create_node(AClass("ACu1//..."), "u1//...", parent="//...", user=True, access=access(binary=0))
        t.create_node(AClass("ACu2//..."),"u2//...", parent="//...", user=True, access=access(binary=0))
        t.create_node(AClass("AC//one/..."),"//one/...", parent="//...", path=True)
        t.create_node(AClass("ACu1//one/..."),"u1//one/...", parent="//one/...", user=True, access=access(binary=0))
        t.create_node(AClass("ACu2//one/..."),"u2//one/...", parent="//one/...", user=True, access=access(binary=0))
        t.create_node(AClass("AC//one/red/..."),"//one/red/...", parent="//one/...", path=True)
        t.create_node(AClass("ACu1//one/red/..."),"u1//one/red/...", parent="//one/red/...",
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

    def test_to_dict_user_path_alphabet_ordered(self):
        for x in range(0, 500):
            d = self.t.to_dict()
            assert d == TO_DICT_USER_PATH_ALPHABET_ORDERED

    def test_typed_to_jstree_dict_user_path_alphabet_ordered(self):
        for x in range(0, 500):
            d = self.t.to_jstree_json(show_access=False)
            assert d == TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED

    def test_typed_to_jstree_dict_user_path_alphabet_ordered_expanded(self):
        for x in range(0, 500):
            d = self.t.to_jstree_json(show_access=True, expand_access=False)
            assert d == TYPED_TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED_EXPANDED

    def test_typed_to_jstree_dict_user_path_alphabet_ordered_expanded_all(self):
        for x in range(0, 500):
            d = self.t.to_jstree_json(show_access=True, expand_access=True, expand_all=True)
            assert d == TYPED_TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED_ACCESS_EXPANDED

    def test_typed_to_jstree_dict_user_path_alphabet_ordered_access(self):
        for x in range(0, 500):
            d = self.t.to_jstree_json(show_access=True)
            assert d == TYPED_TO_JSTREE_DICT_USER_PATH_ALPHABET_ORDERED_ACCESS

def suite():
    suites = [ToDictTreeCase, NodeCase, TreeCase,
            AccessTreeCase, TypedTreeCase, TypedPruningCase, StrTypedTreeCase, ToDictTreeCase, ToHtmlTreeCase]
    suite = unittest.TestSuite()
    for s in suites:
        suite.addTest(unittest.makeSuite(s))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
