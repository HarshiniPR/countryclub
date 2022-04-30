from django.contrib import admin

# Register your models here.
from .models import Login
from .models import FeedBack
from .models import RegisterEvent
from .models import MembershipRegistration

admin.site.register(Login)
admin.site.register(FeedBack)
admin.site.register(RegisterEvent)
admin.site.register(MembershipRegistration)
