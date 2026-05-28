#!/usr/bin/env python3
"""
EcoAR · Generador de QRs por caneca

Uso:
    python generate_qr.py                                    # con URL placeholder
    python generate_qr.py https://leoperez4.github.io/ecoar  # con tu URL real

Requisitos:
    pip install "qrcode[pil]"
"""

import sys
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H

BASE_URL = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://leoperez4.github.io/ecoar"

CANECAS = [
    {"key": "blanca", "name": "Caneca BLANCA · Aprovechables"},
    {"key": "negra",  "name": "Caneca NEGRA · No aprovechables"},
    {"key": "verde",  "name": "Caneca VERDE · Orgánicos"},
]

out_dir = Path(__file__).parent / "qr"
out_dir.mkdir(exist_ok=True)

print(f"Generando QRs con base URL: {BASE_URL}\n")
for c in CANECAS:
    url = f"{BASE_URL}/ar.html?caneca={c['key']}"
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=14,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    path = out_dir / f"qr-caneca-{c['key']}.png"
    img.save(path)
    print(f"  ✓ {c['name']}")
    print(f"    archivo: qr/{path.name}")
    print(f"    URL:     {url}\n")

print("Listo. Abre cards/cards.html para imprimir las tarjetas.")
