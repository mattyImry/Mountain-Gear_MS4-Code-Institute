from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle the webhooks for Stripe
    Code taken from Boutique Ado
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic webhook event
        """

        return HttpResponse(
            content=f'Webhook Receved: {event["type"]}',
            status=200)
