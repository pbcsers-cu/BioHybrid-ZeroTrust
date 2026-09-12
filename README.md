# Zero-Trust Architectures for Bio-Hybrid Computing

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![SystemVerilog](https://img.shields.io/badge/SystemVerilog-IEEE%201800--2017-brightgreen.svg)](https://ieeexplore.ieee.org/document/8299595)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the Hardware-in-the-Loop (HIL) simulation scripts and SystemVerilog Register-Transfer Level (RTL) logic for the paper: **"Zero-Trust Architectures for Bio-Hybrid Computing: Mitigating Cyber-Physical Threats in Organoid Intelligence,"** submitted to *IEEE Transactions on Information Forensics & Security (T-IFS)*.

## Overview

Biological computing substrates, such as 3D cortical organoids (Organoid Intelligence), offer immense computational efficiency but introduce severe cyber-physical vulnerabilities. This repository provides the tools to simulate, test, and synthesize a **hardware-anchored zero-trust defense framework** designed to protect living neural tissue from cognitive hijacking and homeostatic sabotage.

### Key Features
1. **Threat Injection Engine (Python):** Dynamically intercepts and manipulates authentic `in vitro` multi-electrode array (MEA) data to simulate three specific attack vectors from the Bio-STRIDE threat taxonomy.
2. **Hardware-in-the-Loop (HIL) Simulator (Python):** Emulates the deterministic AXI4-Stream data transfer between the biological plant and the digital hardware.
3. **Deterministic Air-Gap & Safe-Mode Logic (SystemVerilog):** The synthesizable RTL code enforcing the sub-25 $\mu$s stimulation window, the 2 ms biological refractory interlock, and the PCA-Mahalanobis anomaly tripwire.

## Repository Structure

```text
biohybrid-zerotrust/
│
├── python_sim/
│   ├── threat_injector.py        # Implements Naive Spoofing, Adaptive Evasion, and DC Overdrive
│   ├── hil_simulation_loop.py    # Main HIL testbed script and AXI-Stream mock
│   └── data/                     # Directory for placing the CRCNS .mat/.npy datasets
│
├── rtl/
│   ├── bio_zero_trust_top.sv     # Top-level integration of security primitives
│   └── air_gap_fsm.sv            # Finite State Machine for hardware air-gapping
│
├── requirements.txt              # Python dependencies
└── README.md


```

## Threat Models Implemented

The `threat_injector.py` module evaluates the architecture against three distinct threat profiles:

* **Naive Sensory Spoofing (Cognitive Hijacking):** Injects highly correlated, out-of-phase biphasic current pulses ($100\ \mu A$, $200\ \mu s$) to maliciously drive structural plasticity.
* **Adaptive Evasion Spoofing:** Simulates a "white-box" adversary attempting to bypass the PCA-Mahalanobis detector by adding Gaussian white noise ($\mathcal{N}(0, \sigma^2)$) and amplitude jitter to spoofed pulses.
* **Faradaic DC Overdrive (Tampering):** Introduces a sustained $+800\text{ mV}$ DC offset to push the electrode-electrolyte interface beyond the hydrolytic water window, inducing localized cytotoxicity.

---

## Getting Started

### Prerequisites

* **Python:** Version 3.8 or higher.
* **Hardware Synthesis:** AMD/Xilinx Vivado Design Suite 2021.2 (or newer) is recommended to synthesize the `.sv` files for the Zynq UltraScale+ MPSoC target.

### 1. Installation

Clone the repository and install the required Python packages:

git clone [https://github.com/pbcsers-cu/BioHybrid-ZeroTrust.git](https://github.com/pbcsers-cu/BioHybrid-ZeroTrust.git)
cd BioHybrid-ZeroTrust
pip install -r requirements.txt



*(The `requirements.txt` includes `numpy` and `scipy`)*

### 2. Sourcing the Biological Dataset

To ensure the cryptographic neural biomarker algorithm is tested against authentic biological stochasticity, this framework utilizes genuine neurophysiological recordings.

1. Download the mammalian cortical network MEA recordings from the **[CRCNS (Collaborative Research in Computational Neuroscience) open repository](https://crcns.org/)**.
2. Place the downloaded `.mat` or `.npy` files into the `python_sim/data/` directory.
*(Note: The provided `hil_simulation_loop.py` script generates mock baseline neural noise by default if the real dataset is not detected).*

### 3. Running the HIL Simulation

Execute the primary simulation loop to observe the dynamic threat injection and sub-10 ms latency verification:

```bash
cd python_sim
python hil_simulation_loop.py

```

Expected output will log the timeline of injected attacks (Naive, Adaptive, Overdrive) and verify STDP constraint compliance for the mock AXI4-Stream transfer.

---

## RTL Synthesis & Hardware Deployment

The files located in the `rtl/` directory are written in synthesizable SystemVerilog.

* `bio_zero_trust_top.sv` is designed to be instantiated directly onto the Programmable Logic (PL) of an FPGA fabric (e.g., Zynq UltraScale+).
* It operates at a target core clock of **200 MHz**.
* The `air_gap_fsm.sv` specifically maps to the *Biological Safe-Mode* protocol, physically enforcing Trust Boundary B via the `mux_en` and `safe_mode` output signals.

---

## Citation

If you use this framework or code in your research, please cite our paper:

```bibtex
@article{barman2026zerotrust,
  author={Barman, Prokash},
  title={Zero-Trust Architectures for Bio-Hybrid Computing: Mitigating Cyber-Physical Threats in Organoid Intelligence},
  journal={IEEE Transactions on Information Forensics and Security},
  year={2026},
  publisher={IEEE}
}

```

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

```

```
