from django.contrib.auth.models import Group
from registration.backends.simple.views import RegistrationView

#Class that inherits from Django-registartion-redux to create a user group and add the user to that group when newly registered
#We need to do this as registartion-redux does not create groups...
class userGroupRegistration(RegistrationView):
    def get_success_url(self, request, user):
        newgroup = Group.objects.create(name=user)

        addToGroup = Group.objects.get(name=user)
        addToGroup.user_set.add(user)

        return '/'
