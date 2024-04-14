from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    '''Чтение данных всем, остальное только Администраторам.'''

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)


class IsOwnerOrAdmin(permissions.BasePermission):
    '''Доступ только к данным пользователя или Администраторам.'''

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user) or bool(request.user and request.user.is_authenticated)
