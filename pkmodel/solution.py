import numpy as np
import scipy.integrate
import matplotlib.pylab as plt
from model import Model1, Model2
from protocol import Subcutaneous, IVBolus

def solve(model, protocol):
    """
    Solve the given PK model with the specified protocol.
    """
    model.dose = protocol.dose  # Override the model's dose function

    t_eval = np.linspace(0, 10, 1000)
    y0 = np.array([0.0, 0.0])
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: model.rhs(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )
    return sol

def plot_solution(solution, model_name):
    """
    Plot the solution.
    """
    plt.plot(solution.t, solution.y[0, :], label=model_name + ' central_comp')
    plt.plot(solution.t, solution.y[1, :], label=model_name + ' peripheral_comp')
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()


if __name__ == "__main__":
    # Specify the model
    model_instance = Model1()
    
    # Specify the protocol with dosing times and amounts
    protocol_instance = IVBolus(X=1.0, dose_times=[0.1, 0.5, 0.9], dose_amounts=[0.5, 0.3, 0.0])

    # Solve and plot
    solution = solve(model_instance, protocol_instance)
    plot_solution(solution, "Model1 with Specific Dosing Schedule")

    