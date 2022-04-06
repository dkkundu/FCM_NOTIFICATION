# __FCM_NOTIFICATION__
[![django-version](https://img.shields.io/badge/django-3.2-green)](https://www.djangoproject.com)
[![python-version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org)
[![postgresql-version](https://img.shields.io/badge/postgresql-12.3-orange)](https://www.postgresql.org)
[![Coverage](https://jenkins.tiger-park.com/coverage/FCM_NOTIFICATION)](https://jenkins.tiger-park.com/job/FCM_NOTIFICATION/cobertura)
[![GH-Actions](https://github.com/Tiger-Park-Limited/FCM_NOTIFICATION/workflows/FCM_NOTIFICATION_CI/badge.svg)](https://github.com/Tiger-Park-Limited/FCM_NOTIFICATION/actions)
[![Jenkins_CI](https://jenkins.tiger-park.com/buildStatus/icon?job=FCM_NOTIFICATION&subject=Jenkins)](https://jenkins.tiger-park.com/job/FCM_NOTIFICATION)

###### _A Django Project._

# __Template features:__
- User Model with Profile (using Email address as username)
- Local Settings (to separate Dev/Production environments)
- Logging enabled (timely rotated daily at midnight)
- Log entries viewable under Django Admin, reusable anywhere  
- Import_Export plug-in (csv,xls,xlsx,json,etc import/export)
- Django REST Framework with API endpoints and view sets
- Django-Cors-Headers to work with Cross Origin Resource Sharing in REST API
- Django-filter for dynamic queryset filtering from url parameters
- Django-cleanup (auto removal of unused/unlinked files and images)
- Celery integration using RabbitMQ (can also use Redis)
- Test Driven Development (TDD on all written codes)
- Testing using coverage, and linting with flake8
- GitHub Actions CI, as well as Jenkins CI/CD with Docker
- Prometheus Monitoring with Model / Middleware metrics
- ...more features will be added regularly, stay tuned!

# __Usage:__
> _This document will be using the following as an input variable: `<variable>`. Please input your own value, i.e. `<project_name>` --> My-Project_
>
> _Please make sure `git`, `python`, `postgresql` and `rabbitmq` is installed in the system._
>
> _NOTE for Windows users: Please use `Git Bash` for the following steps_

    ```
