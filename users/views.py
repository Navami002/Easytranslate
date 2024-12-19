from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
import requests
import json



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user using username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'users/login.html')


def home_view(request):
    # Render the home page template
    return render(request, 'users/home.html') 


def quiz_page(request):
    return render(request, 'quizzes/quizzes.html')



def translate_text(request):
    if request.method == "POST":
        try:
            # Parse JSON data
            data = json.loads(request.body)
            
            input_text = data.get("input_text")
            source_lang = data.get("source_lang")
            target_lang = data.get("target_lang")

            # Print values for debugging
            print(f"Input Text: {input_text}")
            print(f"Source Language: {source_lang}")
            print(f"Target Language: {target_lang}")

            # Validate input
            if not input_text or not source_lang or not target_lang:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            api_key = "AIzaSyDZ1J360axOkYougg5DlUFO_6GnGST2zRk"
            url = "https://translation.googleapis.com/language/translate/v2"
            params = {
                "q": input_text,
                "source": source_lang,
                "target": target_lang,
                "format": "text",
                "key": api_key,
            }

            # Send the request to Google Translate API
            response = requests.post(url, params=params)
            
            # Log the full API response
            print("Google API Response Status:", response.status_code)
            print("Google API Response Content:", response.text)

            result = response.json()

            # Log the response JSON
            print("Google API JSON Response:", result)

            if "data" in result:
                translated_text = result["data"]["translations"][0]["translatedText"]
                return JsonResponse({"translated_text": translated_text})
            else:
                return JsonResponse({"error": "Translation failed. Check API Key."}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid Request"}, status=400)


# Home view (no login required)
def home(request):
    return render(request, 'home.html')

@login_required
def start_quiz(request, quiz_name):
    return render(request, f'quizzes/{quiz_name}.html')


def submit_quiz(request):
    if request.method == 'POST':
  
        
        return render(request, 'quizzes/submit.html')

    return redirect('quiz_page')

