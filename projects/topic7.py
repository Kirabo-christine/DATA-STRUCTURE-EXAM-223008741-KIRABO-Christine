class Feedback:
    def __init__(self, feedback, priority):
        self.feedback = feedback
        self.priority = priority

    def __repr__(self):
        return f"[Priority: {self.priority}] {self.feedback}"


def bubble_sort_feedback(feedback_list):
    n = len(feedback_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if feedback_list[j].priority > feedback_list[j + 1].priority:
                feedback_list[j], feedback_list[j + 1] = feedback_list[j + 1], feedback_list[j]
                swapped = True
        if not swapped:
            break


# Example Usage
if __name__ == "__main__":
    # List of feedback with priorities
    feedbacks = [
        Feedback("Great product quality!", 3),
        Feedback("Fast delivery service.", 1),
        Feedback("Customer service was helpful.", 2),
        Feedback("Packaging could be better.", 4),
    ]

    print("Feedback before sorting:")
    for feedback in feedbacks:
        print(feedback)

    # Sort feedbacks by priority
    bubble_sort_feedback(feedbacks)

    print("\nFeedback after sorting by priority:")
    for feedback in feedbacks:
        print(feedback)
