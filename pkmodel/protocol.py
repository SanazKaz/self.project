# in protocol.py

class Protocol:
    def __init__(self, dose_times=[], dose_amounts=[]):
        """
        Initialize the dosing protocol with times and amounts.
        """
        self.dose_times = dose_times
        self.dose_amounts = dose_amounts

    def dose(self, t):
        """
        Default dose function. Returns the dose amount if t matches a dose time, 0 otherwise.
        """
        for i, dose_time in enumerate(self.dose_times):
            if t == dose_time:
                return self.dose_amounts[i]
        return 0

class Subcutaneous(Protocol):
    """
    Subcutaneous injection protocol.
    """
    def __init__(self, X=0.0, dose_times=[], dose_amounts=[]):
        super().__init__(dose_times, dose_amounts)
        self.X = X

    def dose(self, t):
        """
        Overrides the default dose function. 
        Adds a constant X to the dose value (if any) at time t.
        """
        return super().dose(t) + self.X

class IVBolus(Protocol):
    """
    IV bolus injection protocol.
    """
    def __init__(self, X=0.0, dose_times=[], dose_amounts=[]):
        super().__init__(dose_times, dose_amounts)
        self.X = X

    def dose(self, t):
        """
        Overrides the default dose function. 
        Adds a constant X to the dose value (if any) at time t.
        """
        return super().dose(t) + self.X