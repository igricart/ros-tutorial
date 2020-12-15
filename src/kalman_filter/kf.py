# Example doing a Kalman Filter for a system composed of position, velocity and acceleration

# S = So + V*dt + (a*t^2)/2
# V = Vo + a*dt

import numpy as np

class KF:
    def __init__(self, initial_x: float,
                       initial_v: float,
                       accel_variance: float) -> None:
        # mean of state Gaussian Random Variable
        self._x = np.array([initial_x, initial_v])
        self._accel_variance = accel_variance
        # covariance of GRV
        self._P = np.eye(2)

    def predict(self, dt: float) -> None:
        # x = F x
        # P = F P F^t + G a G^t
        F = np.array([[1, dt], [0, 1]])
        new_x = F.dot(self._x)

        G = np.array([0.5 * dt**2, dt]).reshape((2, 1))
        new_P = F.dot(self._P).dot(F.T) + G.dot(G.T) * self._accel_variance
        
        self._P = new_P
        self._x = new_x

    @property
    def cov(self) -> np.array:
        return self._P

    @property
    def mean(self) -> np.array:
        return self._x

    @property
    def pos(self) -> float:
        return self._x[0]

    @property
    def vel(self) -> float:
        return self._x[1]