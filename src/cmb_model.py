"""
CMB Spectrum and Foreground Modeling
Models:
- CMB blackbody spectrum (Planck law)
- Galactic synchrotron emission (power-law)
- Thermal dust emission (modified blackbody)

Author: Sipra Subhadarsini Sahoo
"""

import numpy as np
import matplotlib.pyplot as plt
import os   # <-- Added for automatic folder creation


# ----------------------------------------------------------
# Physical Constants (SI Units)
# ----------------------------------------------------------

h = 6.62607015e-34        # Planck constant (J s)
k = 1.380649e-23          # Boltzmann constant (J/K)
c = 2.99792458e8          # Speed of light (m/s)


# ----------------------------------------------------------
# Planck Blackbody Function
# ----------------------------------------------------------

def planck_spectrum(nu, T):
    """
    Compute blackbody spectral radiance B_nu(T).
    nu: frequency in Hz
    T: temperature in Kelvin
    """
    return (2*h*nu**3 / c**2) / (np.exp(h*nu/(k*T)) - 1)


# ----------------------------------------------------------
# Synchrotron Emission
# ----------------------------------------------------------

def synchrotron_spectrum(nu, A_sync, beta_sync):
    """
    Power-law synchrotron emission.
    A_sync: amplitude
    beta_sync: spectral index
    """
    return A_sync * (nu/1e9)**(-beta_sync)


# ----------------------------------------------------------
# Thermal Dust Emission
# ----------------------------------------------------------

def dust_spectrum(nu, A_dust, T_dust, beta_dust):
    """
    Modified blackbody dust emission.
    """
    return A_dust * (nu/1e11)**(beta_dust) * planck_spectrum(nu, T_dust)


# ----------------------------------------------------------
# Main Simulation
# ----------------------------------------------------------

def run_simulation():

    print("\n=== CMB Spectrum & Foreground Modeling ===\n")

    # Default parameters
    T_cmb_default = 2.725
    beta_sync_default = 2.9
    beta_dust_default = 1.7
    T_dust_default = 20.0

    try:
        T_cmb = float(input(f"CMB Temperature (K) [default {T_cmb_default}]: ") or T_cmb_default)
        beta_sync = float(input(f"Synchrotron spectral index β [default {beta_sync_default}]: ") or beta_sync_default)
        beta_dust = float(input(f"Dust emissivity index β_d [default {beta_dust_default}]: ") or beta_dust_default)
        T_dust = float(input(f"Dust Temperature (K) [default {T_dust_default}]: ") or T_dust_default)
    except ValueError:
        print("Invalid input detected. Using default parameters.")
        T_cmb = T_cmb_default
        beta_sync = beta_sync_default
        beta_dust = beta_dust_default
        T_dust = T_dust_default

    # Frequency range: 1 GHz to 1000 GHz
    freq_GHz = np.logspace(0, 3, 1000)
    freq_Hz = freq_GHz * 1e9

    # Compute components
    I_cmb = planck_spectrum(freq_Hz, T_cmb)

    # Normalize foreground amplitudes relative to CMB peak
    A_sync = np.max(I_cmb) * 1e-5
    A_dust = np.max(I_cmb) * 1e-6

    I_sync = synchrotron_spectrum(freq_Hz, A_sync, beta_sync)
    I_dust = dust_spectrum(freq_Hz, A_dust, T_dust, beta_dust)

    I_total = I_cmb + I_sync + I_dust

    # ------------------------------------------------------
    # Plotting
    # ------------------------------------------------------

    plt.figure(figsize=(8,6))
    plt.loglog(freq_GHz, I_cmb, label="CMB (Blackbody)")
    plt.loglog(freq_GHz, I_sync, label="Synchrotron")
    plt.loglog(freq_GHz, I_dust, label="Thermal Dust")
    plt.loglog(freq_GHz, I_total, label="Total Signal", linewidth=2)

    plt.xlabel("Frequency (GHz)")
    plt.ylabel(r"Spectral Radiance $B_\nu$ (W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$)")

    plt.title("CMB Spectrum with Astrophysical Foregrounds")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)

    # ------------------------------------------------------
    # Automatic Folder Creation 
    # ------------------------------------------------------

    os.makedirs("results", exist_ok=True)

    plt.savefig("results/cmb_spectrum.png", dpi=300)
    print("\nPlot saved to: results/cmb_spectrum.png")

    plt.show()


# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":
    run_simulation()

