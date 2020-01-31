import unittest
from datetime import datetime

from decimal import Decimal

from phonemast import PhoneMasts, PhoneMast

class TestPhoneMasts(unittest.TestCase):
    """
    Test case for the PhoneMasts class
    """

    def test_ordered_by_current_rent(self):
        test_rents = list(map(Decimal,
                             ('79342.50', '7273.25', '72609', '41587',
                              '38815', '67601', '20142', '78165', '41468',
                              '87907'))
                          )
        # Demonstrate usage of a list comprehension for at least one of the
        # tasks
        phone_masts = PhoneMasts([PhoneMast(
                                   prop_name=f'name {i}',
                                   prop_addr1=f'addr1 {i}',
                                   prop_addr2=f'addr2 {i}',
                                   prop_addr3=f'addr3 {i}',
                                   prop_addr4=f'addr4 {i}',
                                   unit_name=f'unit {i}',
                                   tenant=f'tenant {i}',
                                   lease_start_date=datetime.now(),
                                   lease_end_date=datetime.now(),
                                   lease_years=i,
                                   current_rent=tr
                                  ) for i, tr in enumerate(test_rents)])

        sorted_test_rents = sorted(test_rents)
        limit = 5

        for ascending in (True, False):
            if not ascending:
                sorted_test_rents = list(reversed(sorted_test_rents))

            self.assertEqual(sorted_test_rents[:limit],
                            [mast.current_rent for mast in
                                phone_masts.ordered_by_current_rent(
                                    asc=ascending, limit=limit)])

if __name__ == '__main__':
    unittest.main()
