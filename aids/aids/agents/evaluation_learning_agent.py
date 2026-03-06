from memory.database import store_strategy


class EvaluationLearningAgent:

    def evaluate(self, world, action):
        efficiency = 1 - world["congestion"]
        store_strategy(action, efficiency)
        return efficiency