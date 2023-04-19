from django.shortcuts import render,HttpResponse,redirect
from .models import Analyze
from .se import sentiment_analyzer
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
import csv, codecs
import json
from django.contrib import messages
# from django.http import JsonResponse
from collections import Counter
from .models import MyUser
@login_required(login_url='login')


def analyze_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        reader = csv.reader(codecs.iterdecode(uploaded_file, 'utf-8'))

        results = {}
        columns = next(reader) # get the header row
        selected_columns = ['رايك في تخصص الاعلام الالي', 'رايك في طريقة شرح  الدروس' , 'رايك في التدريس باللغة الفرنسية ', 'رايك في التدريس باللغة الانجليزية ', 'رايك في التدريس و التعلم عن بعد'] # replace with your desired column names
        selected_indices = [columns.index(col) for col in selected_columns]
        gender_counter = Counter() # initialize counter for gender
        academic_year_counter = Counter()
        favorite_method_counter = Counter()
        platform_counter = Counter()

        for row in reader:
            gender = row[columns.index('الجنس')]
            gender_counter[gender] += 1
            academic_year = row[columns.index('السنة الدراسية الحالية')]
            academic_year_counter[academic_year] += 1
            favorite_method = row[columns.index('في ايهم يكون مدى استعابك احسن ')]
            favorite_method_counter[favorite_method] += 1
            platform = row[columns.index('هل تتعامل مع المنصة التعليمية لتحميل الدروس المخصصة لك')]
            platform_counter[platform ] += 1
            
            for column in selected_columns:
                column_index = columns.index(column)
                sentiment = sentiment_analyzer(row[column_index])
                results.setdefault(column, []).append(sentiment)

        results_json = json.dumps(results) # convert results to JSON
        academic_year_counter_json = json.dumps(academic_year_counter) # convert results to JSON
        platform_counter_json = json.dumps(platform_counter)
        num_responders = sum(gender_counter.values())
        num_questions = len(columns) - 1
        male_count = gender_counter['ذكر']
        female_count = gender_counter['انثى']
        td_count = favorite_method_counter['TD'] + favorite_method_counter['TD;TP'] + favorite_method_counter['COURS;TD'] + favorite_method_counter['COURS;TD;TP']
        tp_count = favorite_method_counter['TP'] + favorite_method_counter['TD;TP'] + favorite_method_counter['COURS;TP'] + favorite_method_counter['COURS;TD;TP']
        cours_count = favorite_method_counter['COURS'] + favorite_method_counter['COURS;TP'] + favorite_method_counter['COURS;TD'] + favorite_method_counter['COURS;TD;TP']
        platform_yes_count = platform_counter['نعم']
        platform_no_count = platform_counter['لا']
        return render(request, 'dashboard.html', {
            'results_json': results_json,
            'academic_year_counter': academic_year_counter_json,
            'num_responders': num_responders,
            'num_questions': num_questions,
            'male_count': male_count,
            'female_count': female_count,
            'td_count': td_count,
            'tp_count': tp_count,
            'cours_count': cours_count,
            'platform_yes_count': platform_yes_count,
            'platform_no_count': platform_no_count,
            'platform_counter_json' : platform_counter_json
            # 'favorite_method_counter_json': favorite_method_counter_json
            
        })

    else:
        return render(request, 'upload_file.html')


def test(request):
    if request.method == 'POST':
        input_field = request.POST.get('input-field', '')
        sentiment = sentiment_analyzer(input_field)
        data = Analyze.objects.create(inputField=input_field, sentimentField=sentiment)
        return HttpResponseRedirect(reverse('result', kwargs={'sentiment': sentiment}))
    else:
        return render(request, 'test.html')

def home(request):
   return render(request , 'index.html')

def UploadFile(request):
   return render(request , 'Upload-File.html')

# def shareresult(request):
#    return render(request , 'share.html')

def contactus(request):
   return render(request , 'contact.html')

def result(request, sentiment):
    analyze = Analyze.objects.latest('id')
    inputField = analyze.inputField
    sentimentField = analyze.sentimentField
    return render(request, 'result.html', {'inputField': inputField, 'sentimentField': sentimentField, 'sentiment': sentiment})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        if MyUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('signup')
        
        if MyUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
            return redirect('signup')
        
        user = MyUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('login')
    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')



def logout(request):
    # logout(request)
    return redirect('login')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        MyUser = authenticate(request, username=username, password=password, backend='home.backend.MyBackend')
        if MyUser is not None:
            auth_login(request, MyUser)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, 'login.html')