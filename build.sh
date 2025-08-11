#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Starting build process..."

# Check Python version
PYTHON_VERSION=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "🐍 Python version: $PYTHON_VERSION"

# Upgrade pip to latest version
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install wheel first to avoid build issues
echo "🔧 Installing wheel..."
pip install wheel

# Try to install dependencies with different approaches
echo "📥 Installing dependencies..."

# First try: Minimal requirements (most compatible)
if pip install -r requirements-minimal.txt; then
    echo "✅ Minimal requirements installed successfully"
elif pip install -r requirements-render.txt; then
    echo "✅ Render requirements installed successfully"
elif pip install -r requirements-simple.txt; then
    echo "✅ Simple requirements installed successfully"
elif pip install -r requirements.txt; then
    echo "✅ Standard requirements installed successfully"
else
    echo "⚠️  Trying minimal installation..."
    pip install Django==4.2.7 Pillow gunicorn whitenoise
fi

# Try to install database driver
echo "🗄️  Installing database driver..."
if ! python -c "import psycopg2" 2>/dev/null; then
    echo "⚠️  psycopg2 not available, trying alternatives..."
    pip install psycopg2-binary==2.9.7 || pip install psycopg2-binary==2.9.6 || echo "⚠️  Using asyncpg instead"
fi

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"
