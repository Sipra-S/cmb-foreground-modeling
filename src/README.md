# CMB Spectrum Simulation Module

This folder contains the Python implementation for modeling the Cosmic Microwave Background (CMB) spectrum along with astrophysical foreground components.
# Files in This Folder

- `cmb_model.py`  
  Main simulation script for modeling:
  - CMB blackbody spectrum (Planck’s law)
  - Galactic synchrotron emission (power-law)
  - Thermal dust emission (modified blackbody)

- `requirements.txt`  
  Lists required Python dependencies to run the simulation.

# Physical Model Implemented
The script computes spectral radiance using:
# 1. Planck Blackbody Law
\[
B_\nu(T) =
\frac{2h\nu^3}{c^2}
\frac{1}{e^{h\nu/kT} - 1}
\]

CMB temperature used by default:
T = 2.725 K

Units:
W m⁻² Hz⁻¹ sr⁻¹
# 2. Synchrotron Emission

Power-law model:

\[
I_\nu^{sync} \propto \nu^{-\beta}
\]
# 3. Thermal Dust Emission

Modified blackbody:

\[
I_\nu^{dust} \propto \nu^{\beta_d} B_\nu(T_{dust})
\]

# Installation
Install dependencies using:
pip install -r requirements.txt









