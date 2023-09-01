# © ALM Solutions AB.
# Written by Tobias Alm
import json
import logging

import stripe as stripe
# Third Party
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from common.const import CONST_LOG_NAME

# Local
log = logging.getLogger(CONST_LOG_NAME)

'''
Events to handle for Subscription, paid:
charge.succeeded
checkout.session.completed
customer.created
customer.updated
invoice.created
invoice.finalized
customer.subscription.created (Last event for free trial) 
invoice.updated
invoice.paid
invoice.payment_succeeded
customer.subscription.updated
payment_intent.created

Unhandled event type customer.subscription.deleted (When customer subscription has ended or been cancelled.)
customer.deleted (when the customer is deleted, should be followed by a customer.subscription.deleted if it is active) 
'''

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    log.info('Got webhook')
    try:
        event = stripe.Event.construct_from(
                json.loads(payload), stripe.api_key
                )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=200)
    match event.type:
        case 'checkout.session.completed':
            log.info('Got checkout')
        case _:
            log.info(f'Unhandled event type {event.type}')
    return HttpResponse(status=200)
