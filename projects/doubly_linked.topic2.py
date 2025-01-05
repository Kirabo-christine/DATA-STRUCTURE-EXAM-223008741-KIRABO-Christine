class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_feedback(self, feedback):
        print(f"Inserting feedback: {feedback}")  
        new_node = DoublyLinkedListNode(feedback)
        if not self.head:  
            self.head = new_node
        else:  
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        print(f"Feedback '{feedback}' added.")

    def display_feedbacks(self):
        print("Displaying feedbacks:") 
        if not self.head:
            print("No feedback available.")
            return
        current = self.head
        while current:
            print(f"- {current.data}")
            current = current.next

    def search_feedback(self, feedback):
        print(f"Searching for feedback: {feedback}")  
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
        print(f"Deleting feedback: {feedback}") 
        if not self.head:
            print("No feedback to delete.")
            return
        if self.head.data == feedback:  
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            print(f"Feedback '{feedback}' deleted.")
            return
        current = self.head
        while current:
            if current.data == feedback:
                if current.next:  
                    current.next.prev = current.prev
                if current.prev:  
                    current.prev.next = current.next
                print(f"Feedback '{feedback}' deleted.")
                return
            current = current.next
        print(f"Feedback '{feedback}' not found.")


# Example usage
if __name__ == "__main__":
    feedback_list = DoublyLinkedList()  

    # Insert feedback
    feedback_list.insert_feedback("Great customer service!")
    feedback_list.insert_feedback("Product quality is excellent.")
    feedback_list.insert_feedback("Fast delivery!")

    # Display feedbacks
    feedback_list.display_feedbacks()

    # Search for feedback
    feedback_list.search_feedback("Product quality is excellent.")
    feedback_list.search_feedback("Average experience.")

    # Delete feedback
    feedback_list.delete_feedback("Great customer service!")
    feedback_list.delete_feedback("Average experience.")

    # Display feedbacks after deletion
    feedback_list.display_feedbacks()





