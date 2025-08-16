from django.shortcuts import render,redirect
from .models import Product,Profile,Category,FlowerStories,Color
from .forms import SignUpForm, UpdateUserForm,ChangePasswordForm, UserInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.shortcuts import render, redirect
from django.shortcuts import redirect
# image according to month
from datetime import datetime
from django.template.loader import render_to_string

def home_en(request):
    current_month = datetime.now().strftime("%B")  # Get current month name (e.g., "March")

    context = {
        'products': Product.objects.all(),
        'current_month': current_month,  # Add this to context
    }
    return render(request, 'en/home.html')

def home_mm(request):
    current_month = datetime.now().strftime("%B")  # Get current month name (e.g., "March")

    context = {
        'products': Product.objects.all(),
        'current_month': current_month,  # Add this to context
    }
    return render(request, 'mm/home.html')

def navbar_en(request):
   return render(request, 'en/navbar.html')

def navbar_mm(request):
   return render(request, 'mm/navbar.html')

def base_en(request):
   return render(request, 'en/base.html')

def base_mm(request):
   return render(request, 'mm/base.html')

def suggestion_en(request):
    # any context you want to pass
    return render(request, 'en/suggestion.html')

def suggestion_mm(request):
    # any context you want to pass
    return render(request, 'mm/suggestion.html')

def about_us_en(request):
   return render(request, 'en/about_us.html')

def about_us_mm(request):
   return render(request, 'mm/about_us.html') 

 #coming
def coming_soon_mm(request):
    return render(request, 'mm/coming.html')

def coming_soon_en(request):
    return render(request, 'en/coming.html')

from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import Product

def search_en(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        results = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not results.exists():
            messages.success(request, "The product doesn't exist. Please try again!")
        return render(request, "en/search.html", {"searched": results})
    return render(request, "en/search.html", {})

def search_mm(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        results = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not results.exists():
            messages.success(request, "ထုတ်ကုန်မတွေ့ပါ။ ထပ်မံစမ်းသပ်ပါ။")  # Myanmar message
        return render(request, "mm/search.html", {"searched": results})
    return render(request, "mm/search.html", {})

def update_info_en(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Your information has been updated!")
            return redirect('en:home_en')

        return render(request, "en/update_info.html", {'form': form, 'shipping_form': shipping_form})
    else:
        messages.warning(request, "You must be logged in.")
        return redirect('en:home_en')

def update_info_mm(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "သင့်အချက်အလက်များကိုပြင်ဆင်ပြီးပါပြီ။")
            return redirect('mm:home_mm')

        return render(request, "mm/update_info.html", {'form': form, 'shipping_form': shipping_form})
    else:
        messages.warning(request, "အကောင့်ဝင်ထားရပါမည်။")
        return redirect('mm:home_mm')


def flower_detail(request, name):
    language = request.session.get('language', 'eng')
    template_name = f'{name}_{language}.html'
    
    return render(request, template_name)


def category_en(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'en/category.html', {
            'products': products,
            'category': category
        })
    except Category.DoesNotExist:
        return redirect('en:home_en')

def category_mm(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'mm/category.html', {
            'products': products,
            'category': category
        })
    except Category.DoesNotExist:
        return redirect('mm:home_mm')

def product_detail_en(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, "en/product_detail.html", {'product_detail': product})

def product_detail_mm(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, "mm/product_detail.html", {'product_detail': product})


# About Us page view
def about_us(request):
    return render(request, 'about_us.html')


def filter_data_en(request):
    print("🔵 [EN] Received GET data:", request.GET)
    colors = request.GET.getlist('color[]')
    categories = request.GET.getlist('category[]')
    
    allProducts = Product.objects.all().distinct()
    
    if colors:
        allProducts = allProducts.filter(color_id__in=colors).distinct()
    if categories:
        allProducts = allProducts.filter(category_id__in=categories).distinct()

    rendered = render_to_string('en/product_list.html', {'data': allProducts})
    return JsonResponse({'data': rendered})

def filter_data_mm(request):
    colors = request.GET.getlist('color[]')
    categories = request.GET.getlist('category[]')
    
    allProducts = Product.objects.all().distinct()
    
    if colors:
        allProducts = allProducts.filter(color_id__in=colors).distinct()
    if categories:
        allProducts = allProducts.filter(category_id__in=categories).distinct()

    rendered = render_to_string('mm/product_list.html', {'data': allProducts})
    return JsonResponse({'data': rendered})

def products_en(request):
    products = Product.objects.all()
    colors = Color.objects.all()
    categories = Category.objects.all()
    return render(request, 'en/product.html', {
        'products': products,
        'colors': colors,
        'categories': categories
    })

def products_mm(request):
    products = Product.objects.all()
    colors = Color.objects.all()
    categories = Category.objects.all()
    return render(request, 'mm/product.html', {
        'products': products,
        'colors': colors,
        'categories': categories
    })

def update_password_en(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password1']
                current_user.set_password(new_password)
                current_user.save()
                # Save plaintext password to profile
                profile = Profile.objects.get(user=current_user)
                profile.plaintext_password = new_password
                profile.save()
                messages.success(request, "Your password has been updated.")
                login(request, current_user)
                return redirect('en:update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('en:update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'en/update_password.html', {'form': form})
    else:
        messages.warning(request, "You must be logged in.")
        return redirect('en:home_en')
    
def update_password_mm(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password1']
                current_user.set_password(new_password)
                current_user.save()
                # Save plaintext password to profile
                profile = Profile.objects.get(user=current_user)
                profile.plaintext_password = new_password
                profile.save()
                messages.success(request, "သင်၏စကားဝှက်ကိုပြောင်းပြီးပါပြီ။")
                login(request, current_user)
                return redirect('mm:update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('mm:update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'mm/update_password.html', {'form': form})
    else:
        messages.warning(request, "အကောင့်ဝင်ထားရပါမည်။")
        return redirect('mm:home_mm')


def update_user_en(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "User has been updated!")
            return redirect('en:home_en')  # Redirect to English home
        return render(request, "en/update_user.html", {'user_form': user_form})
    else:
        messages.warning(request, "You must be logged in.")
        return redirect('en/home_en')
    
def update_user_mm(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "သင့်အချက်အလက်ကို ပြင်ပြီးပါပြီ။")
            return redirect('mm:home_mm')  # Redirect to Myanmar home
        return render(request, "mm/update_user.html", {'user_form': user_form})
    else:
        messages.warning(request, "အကောင့်ဝင်ထားရပါမည်။")
        return redirect('mm:home_mm')



def login_user_en(request):
    return login_user_with_lang(request, lang='en')

def login_user_mm(request):
    return login_user_with_lang(request, lang='mm')

def login_user_with_lang(request, lang):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart

            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, 'You have been logged in')
            return redirect(f'/{lang}/home')
        else:
            messages.error(request, 'Invalid login, please try again')
            return redirect(f'/{lang}/login/')
    else:
        return render(request, f'{lang}/login.html', {})


def logout_user_en(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('en:home_en')  # Redirects to English home page

def logout_user_mm(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('mm:home_mm')  # Redirects to Myanmar home page


def register_user_en(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            plaintext_password = form.cleaned_data['password1']
            login(request, user)
            profile = Profile.objects.get(user=user)
            profile.plaintext_password = plaintext_password
            profile.save()
            messages.success(request, "Username Created! Please fill out the form.")
            return redirect('en:update_info')  # Redirect to English update info page
        else:
            messages.error(request, "Whoops! There was a problem Registering.")
            return redirect('en:register')  # Redirect back to English register page
    return render(request, 'en/signup.html', {'form': form})


def register_user_mm(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            plaintext_password = form.cleaned_data['password1']
            login(request, user)
            profile = Profile.objects.get(user=user)
            profile.plaintext_password = plaintext_password
            profile.save()
            messages.success(request, "Username Created! Please fill out the form.")
            return redirect('mm:update_info')  # Redirect to Myanmar update info page
        else:
            messages.error(request, "Whoops! There was a problem Registering.")
            return redirect('mm:register')  # Redirect back to Myanmar register page
    return render(request, 'mm/signup.html', {'form': form})

# # rose twy upgrade code for mm font
# def rose(request):
#     language = request.session.get('language', 'eng')  # Default to English
#     template_name = 'pages/rose_eng.html' if language == 'eng' else 'pages/rose_mm.html'
#     return render(request, template_name)

# def orchid(request):
#     language = request.session.get('language', 'eng')  # Default to English
#     template_name = 'pages/orchid_eng.html' if language == 'eng' else 'pages/orchid_mm.html'
#     return render(request, template_name)

# def tulip(request):
#     language = request.session.get('language', 'eng')  # Default to English
#     template_name = 'pages/tulip_eng.html' if language == 'eng' else 'pages/tulip_mm.html'
#     return render(request, template_name)

# def sunflower(request):
#     language = request.session.get('language', 'eng')  # Default to English
#     template_name = 'pages/sunflower_eng.html' if language == 'eng' else 'pages/sunflower_mm.html'
#     return render(request, template_name)

# def lotus(request):
#     language = request.session.get('language', 'eng')  # Default to English
#     template_name = 'pages/lotus_eng.html' if language == 'eng' else 'pages/lotus_mm.html'
#     return render(request, template_name)

# def daisy(request):
#     language = request.session.get('language', 'eng')  # Default to English
#     template_name = 'pages/daisy_eng.html' if language == 'eng' else 'pages/daisy_mm.html'
#     return render(request, template_name)


from django.http import Http404


def flower_detail_en(request, name):
    valid_flowers = ['rose', 'orchid', 'tulip', 'sunflower', 'lotus', 'daisy','kantkaw','jasmine']
    if name not in valid_flowers:
        raise Http404("Flower not found")
    return render(request, f'en/{name}.html')

def flower_detail_mm(request, name):
    valid_flowers = ['rose', 'orchid', 'tulip', 'sunflower', 'lotus', 'daisy','kantkaw','jasmine']
    if name not in valid_flowers:
        raise Http404("Flower not found")
    return render(request, f'mm/{name}.html')



def flowerlanding_en(request):
    flowers = FlowerStories.objects.all()
    return render(request, 'en/flowerlanding.html', {'flowers': flowers})

def flowerlanding_mm(request):
    flowers = FlowerStories.objects.all()
    return render(request, 'mm/flowerlanding.html', {'flowers': flowers})

