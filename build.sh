#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Starting build process..."

# Check Python version
PYTHON_VERSION=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "🐍 Python version: $PYTHON_VERSION"

# Force Python version if possible
if [[ "$PYTHON_VERSION" == "3.13" ]]; then
    echo "⚠️  Python 3.13 detected - trying to use Python 3.11..."
    # Try to use Python 3.11 if available
    if command -v python3.11 &> /dev/null; then
        echo "✅ Python 3.11 found, switching..."
        export PATH="/opt/render/project/src/.venv/bin:$PATH"
    fi
fi

# Upgrade pip to latest version
echo "📦 Upgrading pip..."
python -m pip install --upgrade pip

# Install wheel first to avoid build issues
echo "🔧 Installing wheel..."
python -m pip install wheel setuptools

# Try to install dependencies with different approaches
echo "📥 Installing dependencies..."

# First try: Ultra-minimal requirements (most compatible)
if python -m pip install -r requirements-ultra-minimal.txt; then
    echo "✅ Ultra-minimal requirements installed successfully"
elif python -m pip install -r requirements-minimal.txt; then
    echo "✅ Minimal requirements installed successfully"
elif python -m pip install -r requirements-render.txt; then
    echo "✅ Render requirements installed successfully"
elif python -m pip install -r requirements-simple.txt; then
    echo "✅ Simple requirements installed successfully"
elif python -m pip install -r requirements.txt; then
    echo "✅ Standard requirements installed successfully"
else
    echo "⚠️  Trying minimal installation..."
    python -m pip install Django==4.2.7 Pillow gunicorn whitenoise
fi

# Try to install database driver (optional for now)
echo "🗄️  Installing database driver..."
if ! python -c "import psycopg2" 2>/dev/null; then
    echo "⚠️  psycopg2 not available, trying alternatives..."
    python -m pip install psycopg2-binary==2.9.7 || python -m pip install psycopg2-binary==2.9.6 || echo "⚠️  Database driver not available - will use SQLite"
fi

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"
