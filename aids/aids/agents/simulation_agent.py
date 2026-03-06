import random


class SimulationAgent:

    def apply_action(self, world, action):

        if "lanes" in action:
            world["lanes"] = max(1, action["lanes"])

        if "signal_time" in action:
            world["signal_time"] = max(10, action["signal_time"])

        congestion = world["vehicle_density"] / (
            world["lanes"] * world["signal_time"]
        )

        congestion = min(congestion, 1)
        congestion += random.uniform(-0.05, 0.05)

        world["congestion"] = max(0, min(congestion, 1))

        return world