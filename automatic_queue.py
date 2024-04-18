import numpy as np
class Automatic_Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = np.full(max_size,None)
        
    def enqueue(self, new_item):
        """Adds a new item to the queue. Automatically 
        dequeues last item when queue is full

        Args:
            new_item (int): Item you want to add to the queu
        """
        new_queue = self.queue
        
        for i, item in enumerate(self.queue):
            if i == 0:
                new_queue[i] = new_item
            else:
                new_queue[i] = previous_item
                
            previous_item = item
            
        self.queue = new_queue
            





            
            
        