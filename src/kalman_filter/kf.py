import numpy as np

class KF:
    def __init__(self, initial_x: float, initial_v: float) -> None:
        # mean of state Gaussian Random Variable
        self.x = np.array([initial_x, initial_v])
        # covariance of GRV
        self.P = np.eye(2)

    @property
    def pos(self) -> float:
        return self.x[0]

    @property
    def vel(self) -> float:
        return self.x[1]