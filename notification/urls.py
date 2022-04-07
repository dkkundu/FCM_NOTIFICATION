from django.urls import path
from .views import (
    showFirebaseJS2,
    showFirebaseJS,
    save_user_fcm_token
)
app_name = 'notification'

urlpatterns = [
    # Firebase...........
    path('save_fcm_token/', save_user_fcm_token, name='save_fcm_token'),
    path(
        'firebase-messaging-sw.js',
        showFirebaseJS, name="show_firebase_js"
    ),
    # path(
    #     'firebase-messaging-sw2.js', showFirebaseJS2, name="show_firebase_js2"
    # ),
]
