from django.shortcuts import redirect


def allowed_users(allowed_user=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if 'students' in allowed_user:
                if request.user.is_student:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('home')
            if 'teachers' in allowed_user:
                if request.user.is_staff:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('home')
            if 'institution' in allowed_user:
                if request.user.is_institution:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('home')
        return wrapper
    return decorator
