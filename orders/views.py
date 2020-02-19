from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from items.models import Item
from .models import OrderItem,Order

@login_required
def add_item_to_cart(request,pk):
    item = get_object_or_404(Item,pk=pk)
    order_item,created = OrderItem.objects.get_or_create(user=request.user,item=item,ordered=False)
    qs = Order.objects.filter(user=request.user,ordered=False)

    if qs.exists():
        order= qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect('cart')
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user,ordered=False)
        order.items.add(order_item)
        order.save()
    return redirect('home')


@login_required
def remove_item_from_cart(request,pk):
    item = get_object_or_404(Item,pk=pk)
    qs = Order.objects.filter(user=request.user,ordered=False)

    if qs.exists():
        order = qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.get(item=item,user=request.user,ordered=False)
            order.items.remove(order_item)
            order_item.delete()
        else:
            pass #throw error
    else:
        pass #user has no order throw error
    return redirect('home')

@login_required
def reduce_item_quantity(request,pk):
    item = get_object_or_404(Item,pk=pk)
    qs = Order.objects.filter(user=request.user,ordered=False)

    if qs.exists():
        order = qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.get(item=item,user=request.user,ordered=False)
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('cart')
            else:
                order.items.remove(order_item)
                order_item.delete()
                return redirect('cart')
        else:
            pass #throw error
    else:
        pass #throw error
    return redirect('home')


class CartView(View):
    def get(self,*args,**kwargs):
        qs = Order.objects.filter(user=self.request.user,ordered=False)
        context = {}
        if qs.exists():
            order = qs[0]
            context = {"order":order}
        return render(self.request,'orders/cart.html',context=context)