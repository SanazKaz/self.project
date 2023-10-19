#
# Model class
#
import numpy as np

class PKModel:
    def __init__(self, Q_p1, V_c, V_p1, CL, X):
        """
        Initialize the pharmacokinetic model with given parameters.
        """
        self.Q_p1 = Q_p1
        self.V_c = V_c
        self.V_p1 = V_p1
        self.CL = CL
        self.X = X

    def rhs(self, t, y):
        """
        Define right-hand side of ODE for the model.
        """
        q_c, q_p1 = y
        transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
        dqc_dt = self.dose(t) - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    def dose(self, t):
        """
        Default dose function. Constant dose for demonstration.
        """
        return self.X

class Model1(PKModel):
    """
    Specific PKModel with predefined parameters.
    """
    def __init__(self):
        super().__init__(1.0, 1.0, 1.0, 10, 1.0)

class Model2(PKModel):
    """
    Another specific PKModel with a different set of parameters.
    """
    def __init__(self):
        super().__init__(2.0, 1.0, 1.0, 1.0, 1.0)
