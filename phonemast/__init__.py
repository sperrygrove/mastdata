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

class PhoneMasts:
    """
    Class to implement data view methods
    """
    def __init__(self, masts):
        """
        masts: A list of PhoneMast objects
        """
        self.masts = masts

    def ordered_by_current_rent(self, asc=True, limit=5):
        """
        Return a list of phone masts ordered by current rent

        asc: order by current_rent ascending if True else descending
        limit: the number of results to limit to
        """
        # 1a: Produce a list sorted by “Current Rent” in ascending order
        by_rent = sorted(self.masts, key=lambda m: m.current_rent)
        # If we have multiple rows with the same value to be sorted, we may
        # wish to add another meaningful key to sort on e.g. lease_years e.g.:
        #by_rent = sorted(self.masts,
                #key=lambda m: (m.current_rent, m.lease_years))
        if not asc:
            by_rent = list(reversed(by_rent))
        if limit:
            by_rent = by_rent[:limit]
        return by_rent
