from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import LoginForm


def home(request):
    return render(request, 'store/store.html', {})


class AdminLoginView(FormView):
    template_name = "admin/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("store:adminhome")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)

        print(usr)
        
        if usr is not None:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
        
        return super().form_valid(form)


class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("store:home")


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/admin/login/")
        return super().dispatch(request, *args, **kwargs)


class AdminHomeView(AdminRequiredMixin, TemplateView):
    template_name = "admin/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["pendingorders"] = Order.objects.filter(
        #     order_status="Order Received").order_by("-id")
        return context
