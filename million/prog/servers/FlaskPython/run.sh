procs=`nproc`
gunicorn -w $procs -k gthread --threads $procs --bind localhost:8080 main:app
