#!/bin/sh

# -----------------------------
# Script de démarrage pour Docker
# -----------------------------

# Fonction pour vérifier que la DB est prête
echo "⏳ Waiting for database..."
until python manage.py showmigrations >/dev/null 2>&1; do
    echo "⏳ Database not ready yet. Waiting 2 seconds..."
    sleep 2
done
echo "✅ Database is ready!"

# Appliquer les migrations
echo "🗃 Applying migrations..."
python manage.py migrate --noinput

# Créer un superuser s'il n'existe pas
echo "👤 Creating superuser if not exists..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "abdou"
email = "admin@example.com"
password = "admin123"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("✅ Superuser created")
else:
    print("ℹ️ Superuser already exists")
EOF

# Collecter les fichiers statiques
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Lancer Gunicorn
echo "🚀 Starting Gunicorn..."
exec gunicorn museum_api.wsgi:application --bind 0.0.0.0:8080 --workers 3 --timeout 120
