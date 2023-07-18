# %% IMPORTS
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# %% Lotka-Volterra equations:

def lotkavolterra(t, z, a, b, c, d):
    x, y = z    # z: INPUT, initial or current number of Prey and Predator
                # x=x(t) is the number of prey
                # y=y(t) is the number of predator
    # Calculate the temporal evolution of x and y, i.e., dx/dt and dy/dt:
    return [a * x - b * x * y, c * x * y - d * y] #[a * x - b * x * y, -c * y + d * x * y]

a = 0.4   # Reproduction rate of pray
b = 0.001   # Predator feeding rate per prey creature = prey mortality rate per predator.
c = 0.003   # Predator mortality rate when prey is not available.
d = 0.6   # Reproduction rate of predators per prey species

x0 = 600   # Initial population of the prey
y0 = 500    # Initial population of the predator
time_span = [0, 50] # in years

sol = solve_ivp(lotkavolterra, time_span, [x0, y0], args=(a, b, c, d), dense_output=True)

t     = np.linspace(0, time_span[1], 300)
y_Sol = sol.sol(t)

fig = plt.figure(figsize=(6, 4))
plt.plot(t, y_Sol[0,].T, alpha=1, lw=2, label='prey')
plt.plot(t, y_Sol[1,].T, alpha=1, lw=2, label='predator')
plt.xlabel('time')
plt.ylabel('population')
plt.title('Lotka-Volterra System')
plt.ylim(0, 2000)
plt.legend()
plt.tight_layout()
plt.savefig('Lotka_Volterra_System.png', dpi=200)
plt.show()

fig = plt.figure(figsize=(6, 4))
plt.plot(y_Sol[0,:], y_Sol[1,:], alpha=1, lw=2)
plt.xlabel('Population of prey')
plt.ylabel('Population of predators')
plt.title('Lotka-Volterra System (phase space)')
plt.xlim(0, 1000)
plt.ylim(0, 2000)
plt.legend()
plt.tight_layout()
plt.savefig('Lotka_Volterra_System_phase_space.png', dpi=200)
plt.show()
# %% END
