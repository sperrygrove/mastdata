from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

@dataclass
class PhoneMast:
    """
    Dataclass to represent Phone Mast data
    """
    prop_name: str
    prop_addr1: str
    prop_addr2: str
    prop_addr3: str
    prop_addr4: str
    unit_name: str
    tenant: str
    lease_start_date: date
    lease_end_date: date
    lease_years: int
    current_rent: Decimal
