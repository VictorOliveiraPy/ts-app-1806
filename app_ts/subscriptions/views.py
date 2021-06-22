from django.shortcuts import get_object_or_404, render, redirect
from app_ts.subscriptions.forms import SubscriptionForm
from django.contrib import messages
from . models import Subscription
from django.db.models import Q


def search(request):
    query = request.GET.get('query', '')
    subscription = Subscription.objects.filter(
        Q(name__icontains=query)
        | Q(cpf__icontains=query)
        | Q(email__icontains=query)
        | Q(phone__icontains=query)
        | Q(lecture_theme__icontains=query)
    )
    return render(
        request,
        'subscription/subscription_list.html',
        {'subscription': subscription, 'query': query}
    )


def subscription_list(request):
    subscription = Subscription.objects.all()[0:8]
    return render(
        request,
        'subscription/subscription_list.html',
        {'subscription': subscription},
    )


def added_subscription(request):
    form = SubscriptionForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            obj = form.save()
            messages.success(
                request,
                'Palestra registrada com sucesso'
            )

            return redirect(
                'subscription:subscription-detail',
                obj.pk
            )
    else:
        form = SubscriptionForm()

    return render(
        request,
        'subscription/subscription_added.html',
        {'form': form},
    )


def update_subscription(request, pk):
    obj = get_object_or_404(
        Subscription,
        pk=pk
    )

    form = SubscriptionForm(
        request.POST,
        obj or None,
        instance=obj
    )
    if form.is_valid():
        form.save()

        return redirect(
            "subscription:subscription-update', obj.pk"
        )

    return render(
        request,
        "subscription/subscription_added.html",
        {"form": form}
    )


def subscription_detail(request, pk):
    template_name = 'subscription/detail_subscription.html'
    obj = Subscription.objects.get(pk=pk)
    return render(
        request,
        template_name,
        {'object': obj},
    )


def delete_subscription(request, pk):
    Subscription.objects.get(pk=pk).delete()
    return redirect(
        "subscription:subscription-list"
    )
