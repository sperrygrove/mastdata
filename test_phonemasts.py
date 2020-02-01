import unittest
from datetime import datetime, date

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

    def test_with_lease_years(self):
        lease_years = (10, 10, 15, 20, 20, 10, 40, 40)
        phone_masts = PhoneMasts([PhoneMast(
                                   prop_name=f'name {i}',
                                   prop_addr1=f'addr1 {i}',
                                   prop_addr2=f'addr2 {i}',
                                   prop_addr3=f'addr3 {i}',
                                   prop_addr4=f'addr4 {i}',
                                   unit_name=f'unit {i}',
                                   tenant=f'tenant {i}',
                                   lease_start_date=date.today(),
                                   lease_end_date=date.today(),
                                   lease_years=ly,
                                   current_rent=Decimal('10')
                                  ) for i, ly in enumerate(lease_years)])
        expectations = {10: ['name 0', 'name 1', 'name 5'],
                        15: ['name 2'],
                        40: ['name 6', 'name 7']}
        for lease_years, expected_mast_names in expectations.items():
            self.assertListEqual(expected_mast_names,
                                [mast.prop_name for mast in
                                    phone_masts.with_lease_years(lease_years)])

    def test_count_by_tenant(self):
        test_data = {'Tenant A': 22, 'Tenant B': 55, 'Tenant C': 101}
        masts = []
        for name, num_masts in test_data.items():
            for i in range(num_masts):
                masts.append(PhoneMast(prop_name=f'name {i}',
                                       prop_addr1=f'addr1 {i}',
                                       prop_addr2=f'addr2 {i}',
                                       prop_addr3=f'addr3 {i}',
                                       prop_addr4=f'addr4 {i}',
                                       unit_name=f'unit {i}',
                                       tenant=name,
                                       lease_start_date=date.today(),
                                       lease_end_date=date.today(),
                                       lease_years=20,
                                       current_rent=Decimal('10')
                                      )
                            )

        phone_masts = PhoneMasts(masts)
        for name, num_masts in test_data.items():
            self.assertEqual(num_masts, phone_masts.count_by_tenant()[name])

    def test_lease_start_between(self):
        test_data = {'Tenant A': date(1989, 2, 1),
                     'Tenant B': date(2001, 2, 1),
                     'Tenant C': date(2002, 2, 1),
                     'Tenant D': date(2005, 2, 1),
                     'Tenant E': date(2012, 2, 1),
                     'Tenant F': date(2012, 6, 1),
                     }
        masts = []
        for name, lease_start_date in test_data.items():
            masts.append(PhoneMast(prop_name='name',
                                   prop_addr1='addr1',
                                   prop_addr2='addr2',
                                   prop_addr3='addr3',
                                   prop_addr4='addr4',
                                   unit_name='unit',
                                   tenant=name,
                                   lease_start_date=lease_start_date,
                                   lease_end_date=date.today(),
                                   lease_years=20,
                                   current_rent=Decimal('10')
                                  )
                        )
        phone_masts = PhoneMasts(masts)
        expected_names = ['Tenant B', 'Tenant C', 'Tenant D']
        self.assertListEqual(expected_names,
                [mast.tenant for mast in
                    phone_masts.lease_start_between(
                        date(1999, 1, 1),
                        date(2005, 2, 1)
                        )],
            )

if __name__ == '__main__':
    unittest.main()
