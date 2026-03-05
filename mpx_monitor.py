"""
MPX System Monitor Module
Collects real-time system vitals and emotional vectors
"""
import psutil
import numpy as np
from typing import Dict, Any, Tuple, List
from datetime import datetime
import logging
from dataclasses import dataclass
import json
from sklearn.preprocessing import StandardScaler
import threading
from queue import Queue
import time

logger = logging.getLogger("MPX.monitor")

@dataclass
class SystemVitals:
    """Structured system telemetry data"""
    timestamp: datetime
    memory_usage_percent: float
    memory_used_gb: float
    memory_available_gb: float
    cpu_percent: float
    cpu_frequency_current: float
    cpu_cores: int
    load_average: Tuple[float, float, float]
    disk_io_read_mb: float
    disk_io_write_mb: float
    network_sent_mb: float
    network_recv_mb: float
    swap_usage_percent: float
    process_count: int