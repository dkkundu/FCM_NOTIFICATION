# DJANGO IMPORTS
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# PROJECT IMPORTS
from notification.models import UserFcmToken, FCMSettings


@csrf_exempt
def save_user_fcm_token(request):
    try:
        token = request.POST.get('token')
        user, created = UserFcmToken.objects.get_or_create(user=request.user)
        if created:
            print("Token object created", user)
        user.fcm_token = token
        user.save()
        return HttpResponse("TOKEN SAVED")
    except Exception as e:
        print("user-not found", e)
        return HttpResponse("UNABLE TO SAVED TOKEN")


def showFirebaseJS(request):
    fcm = get_object_or_404(FCMSettings, is_active=True)
    fcm_config = 'var firebaseConfig = { apiKey: "' + f"{fcm.api_key}" + '",authDomain:"' + f"{fcm.auth_domain}" + '",databaseURL: "' + f"{fcm.database_URL}" + '",projectId:"' + f"{fcm.project_id}"+'" ,storageBucket:"' + f"{fcm.storage_bucket}"+'",messagingSenderId:"' + f"{fcm.messaging_sender_id}"+'",appId:"' + f"{fcm.app_id}"+'",measurementId:"' + f"{fcm.measurement_id}"+'"};'

    data = \
        'importScripts(' \
        '"https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
        'importScripts(' \
        '"https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js");' \
        f'{fcm_config}' \
        'firebase.initializeApp(firebaseConfig);' \
        'const messaging=firebase.messaging();' \
        'messaging.setBackgroundMessageHandler(function (payload) {' \
        '    console.log(payload);' \
        '    const notification=JSON.parse(payload);' \
        '    const notificationOption={' \
        '        body:notification.body,' \
        '        icon:notification.icon' \
        '    };' \
        '    return ' \
        'self.registration.showNotification(payload.notification.' \
        'title,notificationOption);' \
        '});'

    return HttpResponse(data, content_type="text/javascript")


def showFirebaseJS2(request):
    data = \
        'importScripts(' \
        '"https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
        'importScripts(' \
        '"https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js");' \
        'var firebaseConfig = {' \
        '        apiKey: "AIzaSyA33PItbOMuAHiR-x4y7rY9oLFRIbkNJZg",' \
        '        authDomain: "bksp-90f80.firebaseapp.com",' \
        '        databaseURL: "https://bksp-90f80-default-rtdb.' \
        'asia-southeast1.firebasedatabase.app",' \
        '        projectId: "bksp-90f80",' \
        '        storageBucket: "bksp-90f80.appspot.com",' \
        '        messagingSenderId: "621913192376",' \
        '        appId: "1:621913192376:web:d92bb676b86ecd5b50414d",' \
        '        measurementId: "G-D5D0VDWQWD"' \
        ' };' \
        'firebase.initializeApp(firebaseConfig);' \
        'const messaging=firebase.messaging();' \
        'messaging.setBackgroundMessageHandler(function (payload) {' \
        '    console.log(payload);' \
        '    const notification=JSON.parse(payload);' \
        '    const notificationOption={' \
        '        body:notification.body,' \
        '        icon:notification.icon' \
        '    };' \
        '    return ' \
        'self.registration.showNotification(payload.notification.' \
        'title,notificationOption);' \
        '});'

    return HttpResponse(data, content_type="text/javascript")
