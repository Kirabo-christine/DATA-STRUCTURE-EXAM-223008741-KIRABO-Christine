class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, feedback):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full. Cannot add new feedback.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = feedback
        print(f"Feedback '{feedback}' added to the queue.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty. No feedback to process.")
            return
        feedback = self.queue[self.front]
        if self.front == self.rear: 
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Processed feedback: '{feedback}'")
        return feedback

    def display(self):
        if self.front == -1:
            print("Queue is empty. No feedback to display.")
            return
        print("\nFeedback in the queue:")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(f"- {self.queue[i]}")
        else:  
            for i in range(self.front, self.size):
                print(f"- {self.queue[i]}")
            for i in range(0, self.rear + 1):
                print(f"- {self.queue[i]}")

    def peek(self):
        if self.front == -1:
            print("Queue is empty. No feedback to peek.")
            return
        print(f"Next feedback to process: '{self.queue[self.front]}'")


# Example Usage
if __name__ == "__main__":
    feedback_queue = CircularQueue(5) 

    # Adding feedback
    feedback_queue.enqueue("Excellent service!")
    feedback_queue.enqueue("Product quality is great.")
    feedback_queue.enqueue("Fast checkout process.")
    feedback_queue.enqueue("Staff was very friendly.")
    feedback_queue.enqueue("Loved the ambiance!")

    # Display feedbacks
    feedback_queue.display()

    # Attempt to add when the queue is full
    feedback_queue.enqueue("Parking needs improvement.")

    # Process feedback (dequeue)
    feedback_queue.dequeue()
    feedback_queue.dequeue()

    # Display after processing
    feedback_queue.display()

    # Add feedback after processing (to demonstrate wrap-around)
    feedback_queue.enqueue("Mobile app is user-friendly.")
    feedback_queue.enqueue("Great return policy.")

    # Final display of the queue
    feedback_queue.display()
