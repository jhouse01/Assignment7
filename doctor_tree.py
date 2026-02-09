class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        """
        Insert a new doctor under a specific parent on 'left' or 'right'.
        """
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        parent_node = self._find(self.root, parent_name)
        if parent_node is None:
            raise ValueError(f"Parent doctor '{parent_name}' not found.")

        if side == "left":
            if parent_node.left is not None:
                raise ValueError(f"{parent_name} already has a left report.")
            parent_node.left = DoctorNode(child_name)

        else:  # side == "right"
            if parent_node.right is not None:
                raise ValueError(f"{parent_name} already has a right report.")
            parent_node.right = DoctorNode(child_name)

    def _find(self, node, name):
        """Recursively search for a doctor by name."""
        if node is None:
            return None
        if node.name == name:
            return node

        left_search = self._find(node.left, name)
        if left_search:
            return left_search

        return self._find(node.right, name)

    # Traversals
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# -------- TESTING --------
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))

'''
The tree data structure is suitable to model the doctor reporting structure because it is natural to model one-to-many relationships. A doctor may have zero, one, or two direct reports, and those reports may, in turn, have direct reports of their own. This is a natural organizational chart, reflecting a natural hierarchy where authority flows downward from a single root. In addition, a binary tree admits efficient recursive traversal. Thus, a tree data structure makes it easy to print the tree structure in a variety of useful orders.

Each of these traversal strategies has a different real‑world purpose: Preorder traversal is appropriate when a supervisor‑first perspective is desired, for example generating a top‑down reporting list. Inorder traversal is useful when there is a need for the left‑to‑right ordering such as structures based on alphabetical or workflow‑based orders. Postorder traversal is best when the desire is to process subordinates before supervisors such as summarizing workloads or end‑of‑shift reports.

Heaps are also good in emergency situations since they facilitate fast retrieval of the patient in need. This is made possible by the min-heap, which allows fast retrieval of the root element. Moreover, this approach ensures efficiency in insertion and removal, especially in situations where the system might be loaded. This corresponds to emergency room occurrences since the emergency room operates in real-time. New emergency cases are presented at random times; therefore, heaps help in maintaining order according to priority without necessarily sorting them.
'''
