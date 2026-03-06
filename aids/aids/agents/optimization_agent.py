from memory.database import get_best_strategy


class OptimizationAgent:

    def suggest(self):
        best = get_best_strategy()

        if best:
            return {
                "message": "Learned optimal configuration",
                "optimal_action": best
            }

        return {
            "message": "Not enough data yet",
            "optimal_action": None
        }