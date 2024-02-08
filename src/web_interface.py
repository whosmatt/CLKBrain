from core import CLKBrain

class WebInterface:
    def __init__(self):
        self.clk_brain = CLKBrain()
    
    def receive_task(self, task):
        print(f"Received task: '{task}'")
        best_network = self.clk_brain.select_best_network(task)
        optimized_network = self.clk_brain.optimize_network(best_network)
        return optimized_network
    
    def train_and_predict(self, network, data):
        self.clk_brain.train_network(network, data)
        predictions = self.clk_brain.predict(network, data)
        return predictions
