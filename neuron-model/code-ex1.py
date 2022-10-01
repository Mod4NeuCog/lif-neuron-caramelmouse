# Simulate an LIF neuron for 100s with dt = 0.1s
class Neuron():
    def __init__(self):
        self.V_th = -65.
        self V_reset = -75.
        self tau_m = 5.
        self.V_init = -75.
        self.g_L = 10.
        self.E_L = -75.

    def updateMembranePotential(self, I, V_before, dt, V_mem):
        dV = (-(V_mem - V_reset) + (I/self.g_L))/self.tau_m
        self.V_mem = V_before + (dV*dt)
        return self.V_mem

neuron = Neuron()

T = 100.
dt = 0.1
I = 200
V_mem = -75.
V_before = -75.
V_mem_hist = [V_mem]

for t in range(0,T,dt):
    V_mem = updateMembranePotential(I, V_before, dt, V_mem)
    V_mem_hist.append(V_mem)

