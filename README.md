# 🔐 Reset Password Code Brute-Forcer

Este script automatiza el proceso de recuperación de contraseña mediante el envío de códigos de recuperación comunes, usando múltiples hilos.

⚠️ **Este script es solo para fines educativos y debe utilizarse exclusivamente en entornos controlados como TryHackMe o laboratorios personales.**  
**Nunca lo utilices en sistemas sin autorización explícita.**

---

## ✅ Condiciones para usar este script

Este enfoque es ideal para escenarios tipo **"Beating the Auto-Logout Feature"**, en los que la aplicación te expulsa (te desloguea) tras uno o varios intentos fallidos de autenticación en 2FA o verificación de código OTP. Este comportamiento obliga a reiniciar todo el proceso desde el inicio (login o recuperación).

Este script resulta útil cuando se cumplen las siguientes condiciones:

1. 🔢 **El código OTP es predecible o tiene un espacio pequeño de combinaciones:**
   - Ejemplo: rangos como `1250` a `1350`.
   - En casos reales podría ir de `0000` a `9999`, pero si existe algún patrón, sigue siendo viable.

2. 🔄 **La aplicación revierte al login tras fallar el código:**
   - La sesión se invalida.
   - No permite seguir intentando directamente en el 2FA sin reiniciar el flujo.

3. 🚫 **No hay CAPTCHA, WAF o protecciones agresivas:**
   - No existen mecanismos que bloqueen tu IP por comportamiento sospechoso.
   - El tráfico automatizado no es detectado fácilmente.

---

Este tipo de lógica es común en entornos **CTF**, **TryHackMe**, **HackTheBox** o pruebas internas de pentesting.
  
---

## 🧠 ¿Cómo funciona?

1. Envía una solicitud para iniciar el proceso de recuperación con un correo predefinido.
2. Prueba múltiples códigos de recuperación en paralelo.
3. Detecta si alguno de los códigos es válido y detiene los demás hilos.
4. Muestra el `PHPSESSID` si tiene éxito.

---

## ⚙️ Requisitos

- Python 3.6+
- Librerías:
  - `requests`

Instalación:
```bash
pip install -r requirements.txt

