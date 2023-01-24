while true; do
    echo "Starting server..."
    python3 tango_with_django_project/manage.py runserver 5500
    echo "Server exited with code $?. Respawning.." >&2
    sleep 5
done