from __future__ import annotations

import math
from dataclasses import dataclass


def _sigmoid(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


@dataclass
class StandardizedLogisticRegression:
    learning_rate: float = 0.05
    epochs: int = 500
    l2: float = 0.001

    def __post_init__(self) -> None:
        self.means: list[float] = []
        self.scales: list[float] = []
        self.weights: list[float] = []
        self.bias: float = 0.0
        self.is_fitted = False

    def _standardize(self, x: list[float]) -> list[float]:
        return [(v - m) / s for v, m, s in zip(x, self.means, self.scales)]

    def fit(self, X: list[list[float]], y: list[int]) -> "StandardizedLogisticRegression":
        if not X or len(X) != len(y):
            raise ValueError("non-empty equal-length X and y required")
        n_features = len(X[0])
        if n_features == 0 or any(len(row) != n_features for row in X):
            raise ValueError("X must be rectangular and non-empty")
        if any(label not in {0, 1} for label in y):
            raise ValueError("labels must be binary")

        n = len(X)
        self.means = [sum(row[j] for row in X) / n for j in range(n_features)]
        self.scales = []
        for j in range(n_features):
            var = sum((row[j] - self.means[j]) ** 2 for row in X) / n
            self.scales.append(max(math.sqrt(var), 1e-9))
        Z = [self._standardize(row) for row in X]
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            grad_w = [0.0] * n_features
            grad_b = 0.0
            for row, label in zip(Z, y):
                p = _sigmoid(self.bias + sum(w * v for w, v in zip(self.weights, row)))
                err = p - label
                grad_b += err
                for j, value in enumerate(row):
                    grad_w[j] += err * value
            grad_b /= n
            for j in range(n_features):
                grad_w[j] = grad_w[j] / n + self.l2 * self.weights[j]
                self.weights[j] -= self.learning_rate * grad_w[j]
            self.bias -= self.learning_rate * grad_b

        self.is_fitted = True
        return self

    def predict_proba_one(self, x: list[float]) -> float:
        if not self.is_fitted:
            raise ValueError("model is not fitted")
        if len(x) != len(self.weights):
            raise ValueError("feature length mismatch")
        z = self._standardize(x)
        return _sigmoid(self.bias + sum(w * v for w, v in zip(self.weights, z)))

    def predict_proba(self, X: list[list[float]]) -> list[float]:
        return [self.predict_proba_one(row) for row in X]


def binary_log_loss(forecasts: list[float], outcomes: list[int], eps: float = 1e-12) -> float:
    if not forecasts or len(forecasts) != len(outcomes):
        raise ValueError("non-empty equal-length inputs required")
    total = 0.0
    for p, y in zip(forecasts, outcomes):
        p = min(max(p, eps), 1.0 - eps)
        total += -(y * math.log(p) + (1 - y) * math.log(1 - p))
    return total / len(forecasts)
