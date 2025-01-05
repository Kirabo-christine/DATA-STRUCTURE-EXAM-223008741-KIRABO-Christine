class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class SinglyLinkedList:
    def __init__(self):
        self.head = None  

    def insert_feedback(self, feedback):
        new_node = SinglyLinkedListNode(feedback)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Feedback '{feedback}' added.")

    def display_feedbacks(self):
        if not self.head:
            print("No feedback available.")
            return
        current = self.head
        print("Customer Feedbacks:")
        while current:
            print(f"- {current.data}")
            current = current.next

    def search_feedback(self, feedback):
        current = self.head
        position = 1
        while current:
            if current.data == feedback:
                print(f"Feedback '{feedback}' found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"Feedback '{feedback}' not found.")

    def delete_feedback(self, feedback):
        if not self.head:
            print("No feedback to delete.")
            return
        if self.head.data == feedback:
            self.head = self.head.next
            print(f"Feedback '{feedback}' deleted.")
            return
        current = self.head
        while current.next:
            if current.next.data == feedback:
                current.next = current.next.next
                print(f"Feedback '{feedback}' deleted.")
                return
            current = current.next
        print(f"Feedback '{feedback}' not found.")


# Example Usage
singly_list = SinglyLinkedList()
singly_list.insert_feedback("Great customer service!")
singly_list.insert_feedback("Product quality is excellent.")
singly_list.display_feedbacks()
singly_list.search_feedback("Product quality is excellent.")
singly_list.delete_feedback("Great customer service!")
singly_list.display_feedbacks()
