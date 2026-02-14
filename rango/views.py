from unicodedata import category

from django.shortcuts import render, redirect
from django.http import HttpResponse


from rango.models import Category
from rango.forms import CategoryForm

from rango.models import Page
from rango.forms import PageForm
from django.urls import reverse

def index(request):
    # context_dict = {
    #     'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    # }
    #
    # return render(request, 'rango/index.html', context=context_dict)
    # # return render(request, 'rango/index.html')
    # # return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")

    category_list = Category.objects.order_by('-likes') [:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')
    # return HttpResponse("Rango says here is the about page.<a href='/rango'>Index</a>")

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form' : form })

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                # 如果 Page 添加成功 => 回到上ㄧ層的 Category 頁
                # 透過 rango:show_category 名稱在 urls.py 找到對應路徑
                # 因為 找到的路經需要執行的方法是 show_category() 所以需要提供必要參數放在 kwargs
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    # 其他情形都回到 添加 Page 頁
    return render(request, 'rango/add_page.html', context=context_dict)