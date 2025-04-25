# 🔐 Reset Password Code Brute-Forcer

Este script automatiza el proceso de recuperación de contraseña mediante el envío de códigos de recuperación comunes, usando múltiples hilos.

⚠️ **Este script es solo para fines educativos y debe utilizarse exclusivamente en entornos controlados como TryHackMe o laboratorios personales.**  
**Nunca lo utilices en sistemas sin autorización explícita.**

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
`bash`
`pip install requests`

---

## 🚀 Uso

`python3 reset_code_bruter.py`

---

## ⚙️ Configuración
Puedes personalizar los siguientes campos dentro del script:
- URL: Ruta del endpoint (reset_password.php).
- EMAIL: Correo objetivo de la recuperación.
- CODES: Lista de códigos que se probarán (1 por hilo).

---

## 📚 Notas

- Se usan threads para probar múltiples códigos en paralelo.
- Si un código es válido, el programa se detiene.
- Incluye headers que simulan un navegador real.
