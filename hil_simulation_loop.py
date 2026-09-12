import numpy as np
import time
import logging
from threat_injector import ThreatInjectionEngine

# Configure mock AXI4-Stream Interface
class AXI4StreamInterface:
    def send_data(self, payload):
        """Mocks the deterministic AXI-Stream transfer to the FPGA."""
        # In a physical HIL setup, this would utilize PYNQ or Xilinx DMA drivers
        # e.g., self.dma.sendchannel.transfer(payload)
        pass

def load_crcns_dataset():
    """Mocks loading the 60-channel CRCNS electrophysiological dataset."""
    logging.info("Loading CRCNS in vitro dataset...")
    # Generating 10 seconds of mock baseline neural noise at 25kHz
    return np.random.normal(0, 10, (60, 250000))

def run_hil_simulation():
    fs = 25000
    chunk_size = 250 # 10 ms chunks (STDP window compliance)
    
    # Initialize components
    plant_data = load_crcns_dataset()
    injector = ThreatInjectionEngine(sample_rate=fs, num_channels=60)
    axi_bus = AXI4StreamInterface()
    
    target_electrodes = [12, 14, 15, 22] # Spatial footprint of the attack
    
    logging.info("Starting closed-loop HIL simulation...")
    
    # Iterate through the dataset in 10ms chunks
    for i in range(0, plant_data.shape[1], chunk_size):
        chunk = plant_data[:, i:i+chunk_size]
        
        # Determine attack profile based on simulation time
        sim_time_ms = (i / fs) * 1000
        
        if 1000 < sim_time_ms < 1500:
            # Inject Naive Spoofing between 1s and 1.5s
            payload = injector.inject_naive_spoofing(chunk, target_electrodes)
        elif 3000 < sim_time_ms < 3500:
            # Inject Adaptive Evasion between 3s and 3.5s
            payload = injector.inject_adaptive_evasion(chunk, target_electrodes)
        elif 5000 < sim_time_ms < 5500:
            # Inject Faradaic Overdrive between 5s and 5.5s
            payload = injector.inject_dc_overdrive(chunk, target_electrodes)
        else:
            # Clean benign active inference
            payload = chunk
            
        # Stream data to the FPGA Device Under Test (DUT)
        start_time = time.perf_counter()
        axi_bus.send_data(payload)
        latency_us = (time.perf_counter() - start_time) * 1e6
        
        # Verify sub-10ms STDP constraint
        if latency_us > 10000:
            logging.warning(f"STDP Violation! Latency: {latency_us:.2f} us")

    logging.info("HIL Simulation complete.")

if __name__ == "__main__":
    run_hil_simulation()