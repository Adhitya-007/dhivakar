from memory.database import load_world, save_world


class TrafficWorldStateAgent:

    def load(self):
        world = load_world()

        if not world:
            world = {
                "lanes": 3,
                "signal_time": 60,
                "vehicle_density": 100,
                "congestion": 0.5
            }
            save_world(world)

        return world

    def update(self, world):
        save_world(world)