from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from app_ts.subscriptions.forms import SubscriptionForm
from django.contrib import messages
from . models import Subscription


def subscription_list(request):
    subscription = Subscription.objects.all()[0:8]
    return render(request, 'subscription/subscription_list.html',
                  {'subscrition': subscription})


def added_subscription(request):
    form = SubscriptionForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Palestra registrada com sucesso')
            return redirect('subscription:subscription-detail', obj.pk)
    else:
        form = SubscriptionForm()

    return render(request, 'subscription/subscription_added.html',
                  {'form': form})


def update_subscription(request, pk):
    obj = get_object_or_404(Subscription, pk=pk)

    form = SubscriptionForm(request.POST, obj or None, instance=obj)
    if form.is_valid():
        form.save()

        return redirect("subscription:subscription-update', obj.pk")

    return render(request, "subscription/subscription_update.html",
                  {"form": form})


def subscription_detail(request, pk):
    template_name = 'subscription/detail_subscription.html'
    obj = Subscription.objects.get(pk=pk)
    return render(request, template_name, {'object': obj})


def delete_subscription(request, pk):
    Subscription.objects.get(pk=pk).delete()
    return redirect("home")
