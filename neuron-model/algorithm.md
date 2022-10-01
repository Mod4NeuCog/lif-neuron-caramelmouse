# Exercise: Algorithm for a neuron model

## no io
- **Input:** n/a
- **Output:** Membrane Potential
- **Result** : Change Membrane Potential in the Model Neuron
- **Parameters:**
  - Initial Potential       [mV] $V_i$
  - Spike threshold         [mV] $V_{th}$
  - Reset Potential         [mV] $V_{reset}$
  - Membrane Time Constant  [ms] $\tau_m$
  - Leak Reversal Potential [mV] $E_L$
- Function updateMembranePotential()
- Main():
    for time t (0,N)
      updateMembranePotential()
    end

## with io

### input as arg to a function
- **Input:** Input Current I
- **Output:** Membrane Potential
- **Result** : Change Membrane Potential in the Model Neuron
- **Parameters:**
  - Initial Potential       [mV] $V_i$
  - Spike threshold         [mV] $V_{th}$
  - Reset Potential         [mV] $V_{reset}$
  - Membrane Time Constant  [ms] $\tau_m$
  - Leak Reversal Potential [mV] $E_L$
- Function updateMembranePotential(I)
- Main():
    for time t (0,N)
      updateMembranePotential(I)
    end


### input as (python) console input
- **Input:** Input Current I
- **Output:** Membrane Potential
- **Result** : Change Membrane Potential in the Model Neuron
- **Parameters:**
  - Initial Potential       [mV] $V_i$
  - Spike threshold         [mV] $V_{th}$
  - Reset Potential         [mV] $V_{reset}$
  - Membrane Time Constant  [ms] $\tau_m$
  - Leak Reversal Potential [mV] $E_L$
- Function updateMembranePotential(I)
- Function getInputCurrent()
- Main():
    - getInputCurrent()
    - for time t (0,N)
      updateMembranePotential(I)
    end
