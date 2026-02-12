from rest_framework.permissions import BasePermission
from base.models import Shedule


class IsOwner(BasePermission):
    message = 'unauthorized'

    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        
        shedule_id = int(view.kwargs.get('id',0))

        if shedule_id==0:
            return False
        
        shedule = Shedule.objects.filter(id=id).first()
        if shedule is None:
            return False
        
        if shedule.user == request.user:
            return True
        
        return False
        
        
class IsAuthoenticated(BasePermission):
    message = 'unauthorized'

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        
        return False
    