class OrderQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, order):
        if self.count == self.size:
            print("Queue is full. Cannot add new order.")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = order
        self.count += 1
        print(f"Order '{order}' added to the queue.")

    def dequeue(self):
        if self.count == 0:
            print("Queue is empty. No orders to process.")
            return
        order = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        print(f"Processed order: '{order}'")
        return order

    def display(self):
        if self.count == 0:
            print("Queue is empty. No orders to display.")
            return
        print("\nOrders in the queue:")
        index = self.front
        for _ in range(self.count):
            print(f"- {self.queue[index]}")
            index = (index + 1) % self.size

    def peek(self):
        if self.count == 0:
            print("Queue is empty. No orders to peek.")
            return
        print(f"Next order to process: '{self.queue[self.front]}'")


# Example Usage
if __name__ == "__main__":
    order_queue = OrderQueue(5)  

    # Adding orders
    order_queue.enqueue("Order 101")
    order_queue.enqueue("Order 102")
    order_queue.enqueue("Order 103")
    order_queue.enqueue("Order 104")
    order_queue.enqueue("Order 105")

    # Display orders
    order_queue.display()

    # Attempt to add when the queue is full
    order_queue.enqueue("Order 106")

    # Process orders (dequeue)
    order_queue.dequeue()
    order_queue.dequeue()

    # Display after processing
    order_queue.display()

    # Add more orders to demonstrate circular behavior
    order_queue.enqueue("Order 106")
    order_queue.enqueue("Order 107")

    # Final display of the queue
    order_queue.display()

    # Peek the next order
    order_queue.peek()
