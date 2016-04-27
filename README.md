For running the local CGI-server (from directory with cgi-bin)
* python3 -m http.server --cgi

* in browser : localhost:8000

* c правами что-то напутал автор http://pythonworld.ru/web/cgi-2.html
В первом случае пришлось ставить права
chmod go-w hello.py
а во втором уже на  выполнение (executable)
chmod a+x form.py 
