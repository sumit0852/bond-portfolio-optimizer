from fastapi import FastAPI
from pydantic import BaseModel
from optimizer import optimize_portfolio
import numpy as np
import uvicorn

app = FastAPI(title="Bond Portfolio Optimizer API")

class OptimizationInput(BaseModel):
    expected_returns: list[float]
    covariance_matrix: list[list[float]]
    durations: list[float]
    max_duration: float = 4.0

@app.get("/")
def root():
    return {"message": "Bond Portfolio Optimizer API is running 🚀"}

@app.post("/optimize")
def run_optimization(input_data: OptimizationInput):
    try:
        weights = optimize_portfolio(
            np.array(input_data.expected_returns),
            np.array(input_data.covariance_matrix),
            np.array(input_data.durations),
            input_data.max_duration
        )
        return {"success": True, "weights": list(weights)}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    # uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()


# {
#   "expected_returns": [0.03, 0.025, 0.04, 0.035, 0.028],
#   "covariance_matrix": [
#     [0.001, 0.0002, 0.0001, 0.0003, 0.0002],
#     [0.0002, 0.0012, 0.0003, 0.0002, 0.0001],
#     [0.0001, 0.0003, 0.0011, 0.0004, 0.0003],
#     [0.0003, 0.0002, 0.0004, 0.0013, 0.0004],
#     [0.0002, 0.0001, 0.0003, 0.0004, 0.0012]
#   ],
#   "durations": [2.1, 3.5, 4.0, 5.2, 2.8],
#   "max_duration": 4.0
# }


# To run the API, use the command:
# docker build -t bond-optimizer .
# docker run -p 8000:8000 bond-optimizer
