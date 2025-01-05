class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)


# Example Usage
if __name__ == "__main__":
    # Create root node
    root = TreeNode("Customer Feedback")

    # Add categories as children
    service_feedback = TreeNode("Service Feedback")
    product_feedback = TreeNode("Product Feedback")
    delivery_feedback = TreeNode("Delivery Feedback")

    root.add_child(service_feedback)
    root.add_child(product_feedback)
    root.add_child(delivery_feedback)

    # Add subcategories and feedbacks
    service_feedback.add_child(TreeNode("Staff was polite"))
    service_feedback.add_child(TreeNode("Quick resolution of issues"))

    product_feedback.add_child(TreeNode("High product quality"))
    product_feedback.add_child(TreeNode("Affordable prices"))

    delivery_feedback.add_child(TreeNode("On-time delivery"))
    delivery_feedback.add_child(TreeNode("Packaging was excellent"))

    # Display the hierarchical data
    print("Hierarchical Representation of Feedback:")
    root.display()
