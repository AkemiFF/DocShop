from django.shortcuts import render, get_object_or_404, redirect, reverse
from store.models import Product, Cart, Order


def index(request):
    title = "AkemiShop"
    product = Product.objects.all()
    context = {"products": product, "title": title}
    return render(request, 'store/index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    title = f"{product.name} from AkemiShop"
    return render(request, "store/detail.html", {"product": product, "title": title})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    c = get_object_or_404(Cart, user=request.user)
    context = {"title": "Panier",
               "orders": c.orders.all()
               }
    return render(request, "store/cart.html", context)


def delete_cart(request):
    if c := request.user.cart:
        # c.orders.all().delete()
        c.delete()

    return redirect('index')
