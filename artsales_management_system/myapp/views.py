from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import User


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    import json
    try:
        data = json.loads(request.body)
        name = data.get('name')
        phone_number = data.get('phone_number')
        email = data.get('email')
        age = data.get('age')
        gender = data.get('gender')

        if not all([name, phone_number, email, age, gender]):
            return JsonResponse({'error': 'Missing fields'}, status=400)

        if not isinstance(age, int) or age < 0:
            return JsonResponse({'error': 'Invalid age'}, status=400)

        user = User.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            age=age,
            gender=gender
        )
        return JsonResponse({'id': user.id, 'name': user.name}, status=201)
    except (json.JSONDecodeError, ValueError) as e:
        return JsonResponse({'error': str(e)}, status=400)
