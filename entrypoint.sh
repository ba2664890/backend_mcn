#!/bin/sh

# Attendre que la DB soit prête
echo "⏳ Waiting for database..."
sleep 5

# Appliquer les migrations
echo "🗃 Applying migrations..."
python manage.py migrate --noinput

# Créer un superuser s'il n'existe pas
echo "👤 Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("adminba", "admin@example.com", "admin123")
    print("✅ Superuser created")
else:
    print("ℹ️ Superuser already exists")
EOF

# Collecter les fichiers statiques
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Lancer Gunicorn
echo "🚀 Starting Gunicorn..."
exec gunicorn museum_api.wsgi:application --bind 0.0.0.0:8080
