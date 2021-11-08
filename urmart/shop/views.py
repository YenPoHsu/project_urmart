from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.conf import settings
from django.contrib.auth.models import User

from shop.models import Product, Order

# Create your views here.


class ShopMainView(LoginRequiredMixin, View):
    def get(self, request):
        pl = Product.objects.all()
        ol = Order.objects.all()

        ctx = {'product_list': pl, 'order_list': ol}
        return render(request, 'shop/shop_main.html', ctx)

# ...


def OrderCreate2(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # check stock
    if product.stock_pcs <= 0:
        ctx = {'out_of_stock_message': 'Out of Product Stock!'}
        return render(request, 'shop/out_of_stock.html', ctx)

    user = get_object_or_404(User, pk=request.user.id)

    # check vip
    if (product.vip) and not (user.groups.filter(name='vip').exists()):
        ctx = {'not_vip_message': 'This product is vip custom only.'}
        return render(request, 'shop/vip_required.html', ctx)

    order_instance = Order.objects.create(
        product_id=product,
        gty=1,
        price=product.price,
        shop_id=product.shop_id,
        user_id=request.user)
    order_instance.save()
    ctx = {'product': product, 'user': user, 'order': order_instance}
    return render(request, 'shop/order_create_2.html', ctx)


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('shopmain')


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('shopmain')
