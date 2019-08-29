import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.subaccount import SubAccount


class TestSubAccount(BaseTestCase):

    @httpretty.activate
    def test_subaccount_create(self):
        """Method defined to test subaccount creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/subaccount"),
            content_type='text/json',
            body='{"status": true, "message": "Subaccount created"}',
            status=201,
        )

        response = SubAccount.create(
            business_name="Test Biz 123", settlement_bank="Access Bank",
            account_number="xxxxxxxxx", percentage_charge="6.9"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_subaccount_list(self):
        """Function defined to test subaccount list method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/subaccount"),
            content_type='text/json',
            body='{"status": true, "message": "Subaccounts retrieved"}',
            status=201,
        )

        response = SubAccount.list(perPage=3, page=1)
        self.assertEqual(response['status'], True)
    
    @httpretty.activate
    def test_subaccount_fetch(self):
        """Function defined to test Product fetch method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/subaccount/ACCT_4hl4xenwpjy5wb"),
            content_type='text/json',
            body='{"status": true, "message": "Subaccount retrieved"}',
            status=201,
        )

        response = Product.fetch(id_or_slug="ACCT_4hl4xenwpjy5wb")
        self.assertEqual(response['status'], True)
