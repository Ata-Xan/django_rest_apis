from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     # its better to be more picky in here to give permissions to users
    #     # the purpose is to give the least amount of permissions at first.
    #     user = request.user        
    #     print(user.get_all_permissions())
    #     # to make the permissions granting more picky we will do this:
    #     if user.is_staff:
    #         # products => app name
    #         # view.model_name => type of CRUD (here just view)
    #         # so all in all ===> app_name.verb(add, delete, change, view)_model_name
    #         if user.has_perm("procuts.add_product"):
    #             return True
    #         if user.has_perm("procuts.delete_product"):
    #             return True
    #         if user.has_perm("procuts.change_product"):
    #             return True
    #         if user.has_perm("procuts.view_product"):
    #             return True
    #     # if request.user.is_staff:
    #     #     return True

    #     return False
        
    # For the time that obj has its own owner
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user