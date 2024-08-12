# CORS Error solution


![Django REST framework Logo](https://www.django-rest-framework.org/img/logo.png)


A Cross-Origin Resource Sharing (CORS) error typically occurs when your frontend is trying to access resources from a different origin (domain, protocol, or port) than the one it was served from. To fix this in a Django REST framework project, you need to set up CORS headers.

Here's how you can do it:

### 1. **Install django-cors-headers**:

First, install the __`django-cors-headers`__ package using pip:

```sh
pip install django-cors-headers
```

### 2. **Add to INSTALLED_APPS**:


Next, add __`corsheaders`__ to your __`INSTALLED_APPS`__ in __`settings.py`__:

```sh
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

### 3. **Add Middleware**:

Then, add __`CorsMiddleware`__ to your __`MIDDLEWARE`__ in __`settings.py`__. It should be placed above __`CommonMiddleware`__:

```sh
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```
### 4. **Configure CORS**:


Finally, configure your CORS settings. You can allow all origins (not recommended for production) or specify which origins are allowed.

- **To allow all origins**:
```sh
CORS_ALLOW_ALL_ORIGINS = True
```

- **To allow specific origins**:

```sh
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "https://yourfrontenddomain.com",
]
```

### 5. **Additional Settings**:

Depending on your needs, you may also want to configure other settings such as __`CORS_ALLOW_CREDENTIALS`__, __`CORS_ALLOW_METHODS`__, and __`CORS_ALLOW_HEADERS`__.

```sh
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
```
```sh
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "ngrok-skip-browser-warning",
]
```

After configuring these settings, your Django application should be able to handle CORS requests properly, and the CORS errors should be resolved.
