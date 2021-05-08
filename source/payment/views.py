from payment.models import Payment
from django.shortcuts import render

# view function for make payment page
def make_payment(request):
    """
    This method functionality is conduct payment.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns make_payment page
    
    """
    return render(request, 'payments/make_payment.html')

# view function for confirming payment
def confirm_payment(request):
    """
    This method functionality is confirming payment.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns confirm_payment page
    
    """
    # getting form value
    phone = request.GET.get("phone")
    transaction_id = request.GET.get("transaction_id")

    context = {'confirm': False}

    # confirm payment
    payment = Payment.objects.filter(mobile_number=phone, transaction_id=transaction_id, verified=False)
    if len(payment) > 0:
        payment = payment[0]
        payment.verified = True
        payment.save()
        context['confirm'] = True

    return render(request, 'payments/confirm_payment.html', context)