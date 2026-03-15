from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from memory.database import init_db
from agents.world_state_agent import TrafficWorldStateAgent
from agents.simulation_agent import SimulationAgent
from agents.evaluation_learning_agent import EvaluationLearningAgent
from agents.optimization_agent import OptimizationAgent

app = FastAPI()

init_db()

world_agent = TrafficWorldStateAgent()
simulation_agent = SimulationAgent()
evaluation_agent = EvaluationLearningAgent()
optimization_agent = OptimizationAgent()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Traffic Agentic Simulation Running 🚦"}


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/world")
def get_world():
    return world_agent.load()


@app.post("/play")
def play(lanes: int = None, signal_time: int = None):

    world = world_agent.load()

    action = {}

    if lanes is not None:
        action["lanes"] = lanes

    if signal_time is not None:
        action["signal_time"] = signal_time

    world = simulation_agent.apply_action(world, action)

    efficiency = evaluation_agent.evaluate(world, action)

    world_agent.update(world)

    return {
        "updated_world": world,
        "efficiency_reward": efficiency
    }



@app.get("/optimal")
def optimal():
    return optimization_agent.suggest()
