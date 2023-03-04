from rest_framework.permissions import BasePermission
from users import  choices as user_choices


class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.user_type == user_choices.UserTypeChoices.Seller
        )
