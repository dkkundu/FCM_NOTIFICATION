# Generated by Django 3.2 on 2022-04-08 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import notification.models.fcm_settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMobileFcmToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated')),
                ('fcm_token', models.TextField(default='', verbose_name='FCM Token')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='token_mobile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFcmToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated')),
                ('fcm_token', models.TextField(default='', verbose_name='FCM Token')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='token_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FCMSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(help_text='FCM-00.1', max_length=255, unique=True, verbose_name='Version')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated')),
                ('api_key', models.CharField(help_text='AIzaSyA33PItbOMuAHiR-x4y7', max_length=255, verbose_name='apiKey')),
                ('auth_domain', models.CharField(help_text='f80.firebaseapp.com', max_length=255, verbose_name='authDomain')),
                ('database_URL', models.CharField(blank=True, help_text='https://f80.asia-southeast1.firebasedatabase.app', max_length=255, null=True, verbose_name='databaseURL')),
                ('project_id', models.CharField(help_text='sp-90f80', max_length=255, verbose_name='projectId')),
                ('storage_bucket', models.CharField(help_text='f80.appspot.com', max_length=255, verbose_name='storageBucket')),
                ('messaging_sender_id', models.CharField(help_text='6219890099', max_length=255, verbose_name='messagingSenderId')),
                ('app_id', models.CharField(help_text='1:62168752376:web:d92b54654b50414d', max_length=255, verbose_name='appId')),
                ('measurement_id', models.CharField(help_text='G-D5D0V879', max_length=255, verbose_name='measurementId')),
                ('server_key', models.CharField(help_text='key=AAAAkMzqN7g:APA91bFKF9NOhnZJWig..', max_length=255, verbose_name='serverKey')),
                ('use_public_vapid_key', models.CharField(help_text='BAelDrmFfEmTc1t2HHbU-4pABsf2rohKdRk9dtFY....', max_length=255, verbose_name='usePublicVapidKey')),
                ('action_domain', models.URLField(help_text='Application URL', verbose_name='actionDomain')),
                ('icon_image', models.ImageField(upload_to=notification.models.fcm_settings.media_upload_path, verbose_name='Icon Image')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_fcmsettings_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_fcmsettings_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
