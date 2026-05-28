#!/usr/bin/env python3
"""
EcoAR · Generador de QRs

Uso:
    python generate_qr.py                    # genera con URL placeholder
    python generate_qr.py https://misitio.com/EcoAR   # genera con tu URL real

Requisitos:
    pip install "qrcode[pil]"
"""

import sys
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H

BASE_URL = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://YOUR-DOMAIN.com/EcoAR"

ITEMS = [
    {"key": "botella", "name": "Botella PET",          "color": "BLANCA"},
    {"key": "empaque", "name": "Empaque de domicilio", "color": "NEGRA"},
    {"key": "cascara", "name": "Cáscara de fruta",     "color": "VERDE"},
    {"key": "caja",    "name": "Caja de cartón",       "color": "BLANCA"},
]

out_dir = Path(__file__).parent / "qr"
out_dir.mkdir(exist_ok=True)

print(f"Generando QRs con base URL: {BASE_URL}")
print()
for item in ITEMS:
    url = f"{BASE_URL}/ar.html?item={item['key']}"
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,  # alta corrección de errores (más robusto)
        box_size=12,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    path = out_dir / f"qr-{item['key']}.png"
    img.save(path)
    print(f"  ✓ {item['name']:24s} → qr/{path.name}")
    print(f"    URL: {url}")

print()
print("Listo. Imprime las tarjetas en cards/cards.html (abre en navegador y usa Ctrl+P → guardar PDF).")
