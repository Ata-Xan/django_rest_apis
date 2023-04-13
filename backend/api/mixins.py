from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_class = [permissions.IsAdminUser, IsStaffEditorPermission]