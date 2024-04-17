from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

User = get_user_model()

@api_view(["POST"])
def create_user(request):
    if request.method == "POST":
        data = request.data
        email = data.get("email")
        password = data.get("password")
        if email and password:
            # Create user using create_user method
            user = User.objects.create_user(username=email, email=email, password=password)
            return Response({"message": "User created successfully"}, status=201)
        else:
            return Response({"error": "Email and password are required"}, status=400)

@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    user_data = [{"id": user.id, "email": user.email, "password": user.password} for user in users]
    return Response(user_data)

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid email or password"}, status=400)
        
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
