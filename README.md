# EcoAR · Asistente Interactivo de Clasificación de Residuos en la Fuente

Proyecto final de **Diseño de Interfaces** — Universidad Manuela Beltrán, 2026.
WebAR que, al escanear el QR pegado en cada caneca, muestra en 3D los residuos
que corresponden a esa caneca según el código de colores oficial.

> Mateo Antonio Chica Parra · Andrés Felipe Hernández Suarez · Leonardo Andrés Pérez Márquez · Nicolas Daniel Saavedra Corredor
> Docente: Hernán Darío Cruz Bueno

**Sitio en vivo:** https://leoperez4.github.io/ecoar/

---

## Flujo del usuario

```
1. El residente se acerca a la caneca de su edificio
2. Saca el celular y abre la cámara
3. Apunta al QR pegado en la caneca
4. Toca la notificación que aparece (link)
5. Se abre el navegador con la experiencia AR de ESA caneca
6. Ve flotando en 3D los residuos que pueden ir ahí
```

**3 QRs, uno por caneca:**

| Caneca | Color | Residuos visualizados en AR |
|--------|-------|------------------------------|
| BLANCA | ⚪ blanco | Botella PET, Caja cartón, Papel, Lata aluminio |
| NEGRA  | ⚫ negro  | Empaque sucio, Papel higiénico, Servilleta usada, Icopor |
| VERDE  | 🟢 verde  | Cáscara banano, Cáscara naranja, Restos comida, Hojas/café |

---

## Tecnologías (todas gratuitas)

| Capa | Librería | Licencia |
|------|----------|----------|
| Motor 3D | A-Frame 1.5 | MIT |
| WebAR | AR.js | MIT |
| Modelos 3D | Primitivas A-Frame compuestas | — |
| QRs | python-qrcode | BSD |
| Hosting | GitHub Pages | Gratis |

**No requiere instalar apps.** Funciona en cualquier smartphone moderno (Android Chrome, iOS Safari 11+).

---

## Estructura

```
EcoAR/
├── index.html               ← Landing con las 3 canecas
├── ar.html                  ← Experiencia AR (?caneca=blanca|negra|verde)
├── generate_qr.py           ← Regenera los QRs
├── README.md
├── assets/
│   └── styles.css
├── qr/
│   ├── qr-caneca-blanca.png ← Para pegar en la caneca blanca
│   ├── qr-caneca-negra.png  ← Para pegar en la caneca negra
│   └── qr-caneca-verde.png  ← Para pegar en la caneca verde
└── cards/
    └── cards.html           ← Tarjetas A4 imprimibles
```

---

## Probar localmente

```bash
cd EcoAR/
python3 -m http.server 8000
# Abre http://localhost:8000/ en tu navegador
```

⚠️ Para probar en celular necesitas HTTPS. Por eso lo subimos a **GitHub Pages**.

---

## Personalización

| Quiero cambiar… | Editar |
|------------------|--------|
| Residuos de cada caneca | `ar.html` → constante `CANECAS` |
| Modelos 3D primitivos | `ar.html` → funciones `buildXxx()` |
| Textos / colores / chips | `ar.html` y `assets/styles.css` |
| URL base para QRs | `python generate_qr.py https://mi-url.com` |

---

## Cumplimiento con la propuesta original

| Objetivo de la propuesta | Implementación |
|--------------------------|----------------|
| Herramienta WebAR que escanee QRs | ✅ 3 QRs, uno por caneca, abren AR en navegador |
| Marcadores físicos sobre canecas | ✅ Tarjetas imprimibles con QR alto contraste |
| Flujos intuitivos en móvil | ✅ Escanear → ver, sin pasos intermedios |
| Gráficos, animaciones, mensajes en AR | ✅ Carrusel rotatorio + flotación + panel flotante + etiquetas |
| Código QR → información correcta | ✅ Parámetro `?caneca=...` configura toda la escena |
| Activos 3D de residuos | ✅ 12 modelos compuestos (4 por caneca) con primitivas |
| Caneca virtual blanca / negra / verde | ✅ Cilindro 3D coloreado con etiqueta destacada |

---

## Licencia

Código del proyecto: MIT — libre de usar, modificar, compartir.
