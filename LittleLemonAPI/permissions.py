from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()
    
class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery Crew').exists()
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        is_manager = user.groups.filter(name='Manager').exists()
        is_delivery = user.groups.filter(name='Delivery Crew').exists()

        return not (is_manager or is_delivery)
    
