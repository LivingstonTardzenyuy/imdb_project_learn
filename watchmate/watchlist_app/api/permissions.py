from rest_framework import permissions

class IsAdminOrReadOnlyPermission(permissions.IsAdminUser):
    def has_permission(self, request, view):   #for complete object all
        admin_permission =bool(request.user and request.user.is_staff)
        if request.method in permissions.SAFE_METHODS:
            return True 
        return bool(request.method == 'GET' or admin_permission)
        
    
    
    #Allowing only users who added a permission to edit it
class IsReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):            #we use has_object_permission when we want to do a particular operation on the object
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user 