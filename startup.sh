pip install -r requierments.txt
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app