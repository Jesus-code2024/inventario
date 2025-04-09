# ...existing code...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Directorio global de plantillas
        ],
        'APP_DIRS': True,  
        'OPTIONS': {
            'context_processors': [
                # ...existing context processors...
            ],
        },
    },
]
# ...existing code...
