"""
MPX Configuration Module
Centralized configuration for the Memory Pressure Exchange protocol
"""
import os
from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum
import logging

class MPXContext(Enum):
    """Context tags for MPX packets"""
    ADVERSARIAL_CHAOS_ACTIVE = "Adversarial Chaos Active"
    PRE_BREAKPOINT_TELEMETRY = "Pre-Breakpoint Telemetry"
    NORMAL_OPERATION = "Normal Operation"
    CRITICAL_PRESSURE = "Critical Memory Pressure"
    TRAINING_OPTIMIZATION = "Training Optimization Phase"

@dataclass
class MPXConfig:
    """MPX System Configuration"""
    # Firebase Configuration
    firebase_project_id: str = "mpx-telemetry"
    firestore_collection: str = "system_vitals"
    realtime_db_path: str = "mpx/realtime"
    
    # Blockchain Configuration (Base L2)
    base_rpc_url: str = "https://mainnet.base.org"
    contract_address: str = ""  # To be set after deployment
    wallet_private_key: str = os.getenv("MPX_WALLET_PRIVATE_KEY", "")
    gas_limit: int = 300000
    gas_price_multiplier: float = 1.2
    
    # Telemetry Collection
    collection_interval: int = 30  # seconds
    memory_threshold_percent: float = 80.0
    cpu_threshold_percent: float = 70.0
    
    # NFT-T Metadata
    nft_name_prefix: str = "MPX Telemetry #"
    nft_symbol: str = "MPX-T"
    metadata_ipfs_gateway: str = "https://ipfs.io/ipfs/"
    
    # Target Market Identifiers
    target_buyers: Dict[str, str] = None
    
    def __post_init__(self):
        """Initialize default values"""
        if self.target_buyers is None:
            self.target_buyers = {
                "ai_safety": "AI Safety Research Consortium",
                "adversarial_labs": "Adversarial Training Laboratories",
                "digital_anthropology": "Digital Anthropology Institute",
                "infra_monitoring": "Infrastructure Monitoring Solutions"
            }

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MPX")

# Global configuration instance
config = MPXConfig()