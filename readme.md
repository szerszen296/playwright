By uruchomić serwer python w wsl ubuntu trzeba:
pobrać python - apt install python3
by uruchomić serwer - python3 -m http.server

UWAGI DO PYTHON HTTP SERVER:
Warning http.server is not recommended for production. It only implements basic security checks.
Warning CGIHTTPRequestHandler and the --cgi command-line option are not intended for use by untrusted clients and may be vulnerable to exploitation. Always use within a secure environment.
Nie da sie uploadowac plikow na serwer