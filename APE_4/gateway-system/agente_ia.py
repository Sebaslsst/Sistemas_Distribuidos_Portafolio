import os

import requests

OPEN_WEBUI_URL = os.getenv(
    "OPEN_WEBUI_URL", "http://ip_servidor:3000/api/chat/completions"
)
OPEN_WEBUI_API_KEY = os.getenv("OPEN_WEBUI_API_KEY")
OPEN_WEBUI_MODEL = os.getenv("OPEN_WEBUI_MODEL", "qwen3-coder:30b")


def decision_ia(data):
    prompt = (
        "Clasifica el siguiente pedido como CRITICO o NORMAL. "
        "Responde únicamente con una de esas dos palabras.\n"
        f"Pedido: {data}"
    )
    headers = {"Content-Type": "application/json"}
    if OPEN_WEBUI_API_KEY:
        headers["Authorization"] = f"Bearer {OPEN_WEBUI_API_KEY}"

    try:
        response = requests.post(
            OPEN_WEBUI_URL,
            headers=headers,
            json={
                "model": OPEN_WEBUI_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            },
            timeout=30,
        )
        response.raise_for_status()
        resultado = response.json()["choices"][0]["message"]["content"].upper()
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError) as error:
        print("[IA] Error, usando Round Robin:", error)
        return None

    if "CRITICO" in resultado:
        return 0
    if "NORMAL" in resultado:
        return 1
    print("[IA] Respuesta no reconocida, usando Round Robin")
    return None
