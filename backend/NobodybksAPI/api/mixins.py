from .permissions import IsStaffPermission
from rest_framework import permissions

class StaffEditorPermissionsMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]
    
class UserQuerrySetMixin():
    user_field = 'owner'
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query_data = {}
        query_data[self.user_field] = self.request.user
        return qs.filter(**query_data)    