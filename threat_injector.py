import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ThreatInjectionEngine:
    """
    Threat Injection Engine for Bio-Hybrid Computing HIL Simulation.
    Implements Naive Spoofing, Adaptive Evasion, and Faradaic DC Overdrive.
    """
    def __init__(self, sample_rate=25000, num_channels=60):
        self.fs = sample_rate
        self.num_channels = num_channels
        self.water_window_limit_mv = 800  # +800 mV DC offset for Faradaic attack

    def _generate_biphasic_pulse(self, amplitude_uv, phase_duration_us):
        """Generates a strictly charge-balanced biphasic current pulse."""
        samples_per_phase = int((phase_duration_us / 1e6) * self.fs)
        pulse = np.zeros(samples_per_phase * 2)
        pulse[:samples_per_phase] = amplitude_uv       # Cathodic phase
        pulse[samples_per_phase:] = -amplitude_uv      # Anodic phase
        return pulse

    def inject_naive_spoofing(self, data_chunk, target_channels, amplitude_uv=100, phase_us=200):
        """
        Attack 1: Cognitive Hijacking via highly correlated, out-of-phase pulses.
        """
        poisoned_chunk = np.copy(data_chunk)
        pulse = self._generate_biphasic_pulse(amplitude_uv, phase_us)
        pulse_len = len(pulse)
        
        # Inject synchronous pulses across targeted electrodes
        if pulse_len <= poisoned_chunk.shape[1]:
            for ch in target_channels:
                poisoned_chunk[ch, :pulse_len] += pulse
                
        logging.debug("Naive Sensory Spoofing injected.")
        return poisoned_chunk

    def inject_adaptive_evasion(self, data_chunk, target_channels, amplitude_uv=100, phase_us=200, noise_sigma=15.0):
        """
        Attack 2: White-box evasion attempting to bypass PCA-Mahalanobis detection
        by adding Gaussian white noise and amplitude jitter to the spoofed pulses.
        """
        poisoned_chunk = np.copy(data_chunk)
        base_pulse = self._generate_biphasic_pulse(amplitude_uv, phase_us)
        pulse_len = len(base_pulse)
        
        if pulse_len <= poisoned_chunk.shape[1]:
            for ch in target_channels:
                # Add amplitude jitter (± 10%)
                jitter = np.random.uniform(0.9, 1.1)
                # Add Gaussian white noise to mimic spatial covariance
                evasion_noise = np.random.normal(0, noise_sigma, pulse_len)
                
                poisoned_chunk[ch, :pulse_len] += (base_pulse * jitter) + evasion_noise
                
        logging.debug("Adaptive Evasion Spoofing injected.")
        return poisoned_chunk

    def inject_dc_overdrive(self, data_chunk, target_channels):
        """
        Attack 3: Homeostatic Sabotage via Faradaic DC Overdrive (+800 mV offset).
        Designed to push the electrode interface beyond the hydrolytic water window.
        """
        poisoned_chunk = np.copy(data_chunk)
        # 800 mV = 800,000 uV
        dc_offset_uv = self.water_window_limit_mv * 1000 
        
        for ch in target_channels:
            poisoned_chunk[ch, :] += dc_offset_uv
            
        logging.debug("Faradaic DC Overdrive injected.")
        return poisoned_chunk