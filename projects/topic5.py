from collections import deque

class FeedbackDeque:
    def __init__(self):
        self.deque = deque()

    def add_feedback_front(self, feedback):
        self.deque.appendleft(feedback)
        print(f"Feedback '{feedback}' added to the front.")

    def add_feedback_rear(self, feedback):
        self.deque.append(feedback)
        print(f"Feedback '{feedback}' added to the rear.")

    def remove_feedback_front(self):
        if not self.deque:
            print("No feedback available to remove from the front.")
            return
        feedback = self.deque.popleft()
        print(f"Feedback '{feedback}' removed from the front.")
        return feedback

    def remove_feedback_rear(self):
        if not self.deque:
            print("No feedback available to remove from the rear.")
            return
        feedback = self.deque.pop()
        print(f"Feedback '{feedback}' removed from the rear.")
        return feedback

    def display_feedbacks(self):
        if not self.deque:
            print("No feedback available to display.")
            return
        print("\nCustomer Feedbacks (Front to Rear):")
        for feedback in self.deque:
            print(f"- {feedback}")

    def peek_front(self):
        if not self.deque:
            print("No feedback available at the front.")
            return
        print(f"Next feedback at the front: '{self.deque[0]}'")

    def peek_rear(self):
        if not self.deque:
            print("No feedback available at the rear.")
            return
        print(f"Next feedback at the rear: '{self.deque[-1]}'")


# Example Usage
if __name__ == "__main__":
    feedback_deque = FeedbackDeque()

    # Add feedback dynamically
    feedback_deque.add_feedback_rear("Loved the product quality!")
    feedback_deque.add_feedback_rear("Great customer service!")
    feedback_deque.add_feedback_front("Immediate assistance was appreciated.")
    feedback_deque.add_feedback_rear("Fast delivery service.")

    # Display all feedback
    feedback_deque.display_feedbacks()

    # Peek at both ends
    feedback_deque.peek_front()
    feedback_deque.peek_rear()

    # Remove feedback dynamically
    feedback_deque.remove_feedback_front()
    feedback_deque.remove_feedback_rear()

    # Display after removals
    feedback_deque.display_feedbacks()
