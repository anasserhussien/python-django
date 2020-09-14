from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):


    # def has_permission(self, request, view):
    #     my_safe_methods = ['GET', 'PUT', 'Delete']
    #     if request.method in my_safe_methods:
    #         return True
    #     return False

   
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True 
        return request.user == obj.user

