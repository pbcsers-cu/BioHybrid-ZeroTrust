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

---

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
