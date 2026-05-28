# EcoAR · Asistente Interactivo de Clasificación de Residuos en la Fuente

Proyecto final de **Diseño de Interfaces** — Universidad Manuela Beltrán, 2026.
Aplicación WebAR (Realidad Aumentada basada en marcadores) que guía a los residentes a
clasificar correctamente sus residuos sólidos según el código de colores oficial de Bogotá
(blanca, negra, verde).

> Mateo Antonio Chica Parra · Andrés Felipe Hernández Suarez · Leonardo Andrés Pérez Márquez · Nicolas Daniel Saavedra Corredor
> Docente: Hernán Darío Cruz Bueno

---

## Tecnologías (todas gratuitas / open source)

| Capa | Librería | Licencia |
|------|----------|----------|
| Motor 3D / VR | [A-Frame 1.5](https://aframe.io) | MIT |
| WebAR | [AR.js](https://github.com/AR-js-org/AR.js) | MIT |
| Modelos 3D | [Khronos glTF Sample Models](https://github.com/KhronosGroup/glTF-Sample-Models) | CC BY 4.0 |
| Generación de QR | [python-qrcode](https://github.com/lincolnloop/python-qrcode) | BSD |
| Hosting | GitHub Pages / Netlify | Plan gratuito |

**No requiere instalación de apps.** Funciona en el navegador de cualquier smartphone moderno
con cámara (Android Chrome, iOS Safari 11+).

---

## Estructura del proyecto

```
EcoAR/
├── index.html               ← Landing page (menú principal)
├── ar.html                  ← Experiencia AR (param ?item=...)
├── marker.html              ← Marcador HIRO en pantalla (para pruebas)
├── README.md                ← Este archivo
├── generate_qr.py           ← Script para regenerar QRs con tu URL real
├── assets/
│   ├── styles.css
│   └── marker-hiro.png      ← Marcador HIRO (referencia visual)
├── qr/
│   ├── qr-botella.png
│   ├── qr-empaque.png
│   ├── qr-cascara.png
│   └── qr-caja.png
└── cards/
    └── cards.html           ← Tarjetas imprimibles A4 con QR + marcador
```

---

## Cómo probarlo

### Opción 1 · Hosting gratuito (RECOMENDADO, funciona en celular)

WebAR requiere **HTTPS** para que el navegador permita acceso a la cámara. Por eso necesitas
hosting (en `localhost` también funciona, pero no se puede escanear con otro dispositivo).

#### A. GitHub Pages (más fácil)

1. Crea una cuenta en [github.com](https://github.com) (gratis).
2. Crea un repositorio nuevo, por ejemplo `ecoar`.
3. Sube esta carpeta completa al repositorio (botón "Add file → Upload files").
4. En el repositorio, ve a **Settings → Pages**.
5. En "Source", selecciona la rama `main` y carpeta `/ (root)`. Guarda.
6. Espera 1–2 minutos. Tu sitio quedará en:
   `https://TU-USUARIO.github.io/ecoar/`
7. Regenera los QRs con tu URL real:
   ```bash
   pip install "qrcode[pil]"
   python generate_qr.py https://TU-USUARIO.github.io/ecoar
   ```
8. Vuelve a subir la carpeta `qr/` actualizada y `cards/cards.html`.

#### B. Netlify (sin necesidad de Git)

1. Entra a [app.netlify.com](https://app.netlify.com) (gratis con email).
2. Arrastra la carpeta `EcoAR/` completa al área "Want to deploy a new site without connecting to Git?"
3. Netlify te asignará una URL del tipo `https://random-name.netlify.app`.
4. Regenera los QRs con esa URL como en el paso A.7.

#### C. Cloudflare Pages, Vercel, Surge — también gratis, mismo principio.

### Opción 2 · Pruebas locales (solo en el computador)

```bash
cd EcoAR/
python3 -m http.server 8000
# Abre http://localhost:8000/ en tu navegador
```

Para probar en el celular dentro de la misma red Wi-Fi:
```bash
# Encuentra tu IP local
ip addr | grep inet    # Linux/macOS
ipconfig               # Windows

python3 -m http.server 8000
# En el celular abre http://192.168.X.X:8000/
```

> ⚠️ El navegador del celular **bloqueará la cámara** porque no es HTTPS. Para vencer esto
> usa una de las opciones de hosting (sección 1) o herramientas como `ngrok http 8000`.

---

## Uso (flujo del residente)

1. Se acerca a la caneca del edificio.
2. Escanea el QR pegado en la tarjeta (ver `cards/cards.html`) con la cámara de su celular.
3. El navegador abre `ar.html` con el residuo correspondiente.
4. Acepta el permiso de cámara.
5. Apunta al marcador HIRO impreso. El modelo 3D del residuo aparece flotando.
6. Toca el botón **"Mostrar destino"** para ver la animación que lleva el residuo a la
   caneca del color correcto, mientras un panel flotante explica la indicación clave.

### Modo sin marcador (vista previa 3D)

Si el usuario aún no tiene el marcador impreso, puede tocar **"Vista previa 3D"** en la
esquina superior derecha. La escena se mostrará en un visor 3D normal, arrastrable, sin
necesidad de cámara ni marcador.

---

## Imprimir las tarjetas

1. Abre `cards/cards.html` en el navegador.
2. Toca el botón "🖨️ Imprimir / Guardar PDF" o usa `Ctrl + P` / `Cmd + P`.
3. Configura: tamaño A4, margen reducido, en color.
4. Recorta y pega cada tarjeta junto a la caneca correspondiente del cuarto de basura.

> El bloque "HIRO" en cada tarjeta es una representación visual. Para máxima precisión de
> tracking, descarga el [marcador HIRO oficial](https://raw.githack.com/AR-js-org/AR.js/master/data/images/HIRO.jpg)
> y reemplaza la imagen. En la versión productiva del proyecto, cada caneca tendría un
> marcador único (barcode markers de AR.js, 0–63) para experiencias diferenciadas.

---

## Personalización rápida

| Quiero cambiar… | Editar |
|------------------|--------|
| Textos, colores, indicaciones de cada residuo | `ar.html` → constante `ITEMS` |
| Modelos 3D | `ar.html` → `<a-assets>` (urls GLB) |
| Estilos visuales de la landing | `assets/styles.css` |
| Lista de residuos en menú | `index.html` |
| URL base para QRs | `python generate_qr.py https://mi-url.com` |

---

## Cumplimiento con la propuesta original

| Objetivo de la propuesta | Implementación |
|--------------------------|----------------|
| Herramienta WebAR basada en marcadores que escanee QRs | ✅ AR.js + marcador HIRO; QRs llevan al navegador automáticamente |
| Flujos de navegación intuitivos en móvil | ✅ Landing → QR → AR; HUD táctil con botones grandes |
| Gráficos, animaciones y mensajes sobre cámara | ✅ Modelo 3D + animación de caída en caneca + panel flotante + UI overlay |
| Código que conecte QR ↔ información correcta | ✅ Parámetro `?item=...` configura modelo, caneca, mensaje y color |
| Activos 3D de residuos representativos | ✅ Botella PET, empaque, cáscara (avocado), caja de cartón |
| Caneca virtual blanca / negra / verde | ✅ Cilindro 3D con color y etiqueta según residuo |
| Paneles UI flotantes con instrucciones | ✅ `a-plane` + `a-text` con tip de manejo del residuo |

---

## Licencia

Código del proyecto: MIT (libre de usar, modificar, compartir).
Modelos 3D externos: CC BY 4.0 (Khronos).

---

¿Dudas o mejoras? Cada componente está comentado en el código para facilitar su edición.
