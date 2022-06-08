# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.views.generic import FormView, TemplateView, View, CreateView
# from django.urls import reverse_lazy
# from django.contrib.auth.models import User

# from .forms import LoginForm, ProductForm, CategoryForm

# class AdminLoginView(FormView):
#     template_name = "admin/login.html"
#     form_class = LoginForm
#     success_url = reverse_lazy("store:home")

#     def form_valid(self, form):
#         uname = form.cleaned_data.get("username")
#         pword = form.cleaned_data["password"]
#         usr = authenticate(username=uname, password=pword)
        
#         if usr is not None and User.objects.filter(username=usr).values("is_superuser")[0]['is_superuser']:
#             login(self.request, usr)
#         else:
#             return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
#         return super().form_valid(form)


# class AdminLogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect("admin:login")


# class AdminRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             pass
#         else:
#             return redirect("admin:login")
#         return super().dispatch(request, *args, **kwargs)


# class AdminProductCreateView(AdminRequiredMixin, CreateView):
#     template_name = "admin/productcreate.html"
#     form_class = ProductForm
#     success_url = reverse_lazy("admin:home")

#     def form_valid(self, form):
#         # p = form.save()
#         images = self.request.FILES.getlist("more_images")
#         for i in images:
#             print(f'{i}\n{type(i)}')
#             # ProductImage.objects.create(product=p, image=i)
#         return HttpResponse('ok')
#         # return super().form_valid(form)


# class AdminCategoryCreateView(AdminRequiredMixin, CreateView):
#     template_name = "admin/categorycreate.html"
#     form_class = CategoryForm
#     success_url = reverse_lazy("admin:home")

#     def form_valid(self, form):
#         p = form.save()
#         return super().form_valid(form)
