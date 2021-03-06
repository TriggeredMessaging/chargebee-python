from chargebee.compat import json
from chargebee.models import Addon, Address, Card, Coupon, Customer, Event, HostedPage, Invoice,\
    Plan, Subscription, Transaction


class Result(object):

    def __init__(self, response):
        self._response = response
        self._response_obj = {}

    @property
    def subscription(self):
        return self._get('subscription', Subscription, {'addons': Subscription.Addon})

    @property
    def customer(self):
        return self._get('customer', Customer)

    @property
    def card(self):
        return self._get('card', Card)

    @property
    def address(self):
        return self._get('address', Address)

    @property
    def invoice(self):
        return self._get('invoice', Invoice, {
            'line_items': Invoice.LineItem,
            'discounts': Invoice.Discount,
        })

    @property
    def transaction(self):
        return self._get('transaction', Transaction)

    @property
    def event(self):
        return self._get('event', Event)

    @property
    def hosted_page(self):
        return self._get('hosted_page', HostedPage)

    @property
    def plan(self):
        return self._get('plan', Plan)

    @property
    def addon(self):
        return self._get('addon', Addon)

    @property
    def coupon(self):
        return self._get('coupon', Coupon)

    def _get(self, type, cls, sub_types=None):
        if not type in self._response:
            return None

        if not type in self._response_obj:
            self._response_obj[type] = cls.construct(self._response[type], sub_types)

        return self._response_obj[type]

    def __str__(self):
        return json.dumps(self._response, indent=4)


class Content(Result):
    pass
