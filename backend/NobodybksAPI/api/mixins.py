from .permissions import IsStaffPermission
from rest_framework import permissions

class StaffEditorPermissionsMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]