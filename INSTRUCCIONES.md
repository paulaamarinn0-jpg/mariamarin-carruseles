# Carrusel automático de @mariamarin.ai

Guía que sigue la tarea programada cada vez que corre (día de por medio). Resultado: un carrusel nuevo guardado como **borrador** en Metricool para Instagram + Facebook, programado a las **11:00 a.m. (America/Santiago) del mismo día**, que Pau revisa y aprueba.

## La cuenta
- @mariamarin.ai: divulgadora de IA, español colombiano. Se presenta como "María".
- Colores: rosa y morado. La plantilla ya los trae; no cambiar el diseño.
- Su cara aparece **solo en la portada** (`plantilla/assets/portada.png`). Ninguna otra slide lleva fotos de ella.
- Prohibido: contenido tipo "convertí X en imagen con IA", filtros, glow-ups, fotos con IA de mamá/perro. Cada carrusel deja algo útil o sorprendente.

## 1. Buscar el tema
Temas: noticias de IA, apps, trucos y funciones ocultas **de cualquier herramienta** (no solo Claude). Prioriza lo que está **pegando esa semana**: lanzamientos virales, apps en tendencia, trucos que se están compartiendo.
- Busca con varias consultas en la web; verifica cada dato en la fuente original (blog oficial, nota de prensa, documentación).
- Solo cosas **reales, actuales y que la gente pueda probar hoy**. Nada de rumores ni filtraciones sin confirmar.
- Revisa la carpeta `publicados/` para **no repetir** temas o herramientas recientes.
- Un carrusel = un hilo: 4 o 5 ítems sobre un mismo ángulo (p. ej. "5 apps de IA que reemplazan a…", "Lo que lanzó Google esta semana y casi nadie vio", "Funciones ocultas de ChatGPT que…").

## 2. Escribir
- **Título de portada con gancho fuerte / clickbait que sí cumple**: curiosidad, número, contraste ("gratis", "en 5 minutos", "casi nadie sabe"). El tono puede ser exagerado, **el contenido nunca falso**: si el título promete algo, las slides lo entregan.
- Cada slide: título corto (máx. ~6 palabras, con una palabra en `<em>`), texto de 1–2 líneas (máx. ~120 caracteres, con un `<b>`), y una caja:
  - `caja_titulo`: "PÍDELE ASÍ", "CÓMO PROBARLO", "DÓNDE ENCONTRARLO" o "EL DATO".
  - `caja_texto`: el prompt exacto o los pasos/datos concretos (máx. ~110 caracteres). Resalta lo variable con `<span class=v>…</span>`.
- Español colombiano, cercano, sin tecnicismos innecesarios.
- Cierre: CTA de **"Comenta [PALABRA] y te mando [algo útil] por DM"** (los prompts, los links, la lista de apps…). PALABRA en mayúsculas, corta y relacionada (APPS, LINKS, PROMPTS, GRATIS…).

## 3. Diseñar
- Llena un `contenido.json` con la estructura de `plantilla/ejemplo.json` (portada, slides, cierre). `serie` es la etiqueta del encabezado (p. ej. "noticias IA", "apps de IA", "trucos de IA").
- `grafico` de cada slide: un mockup en HTML (420 px de alto, 952 px de ancho) que ilustre la idea, como en el ejemplo. Clases disponibles: `win` + `bar` (ventana de app), `note` (post-it amarillo), `sticker` (etiqueta rosa), `tag`. Variables de color: `--pink`, `--vio`, `--lila`, `--card`, `--line`, `--dk`. No usar logos ni imágenes de marcas; los nombres de apps van como texto. No uses emojis de color (la fuente no los tiene); ✦ ✓ → sí funcionan.
- Renderiza: `python3 plantilla/render.py contenido.json salida/` (necesita `pip install playwright --break-system-packages && python3 -m playwright install chromium` si no está).
- **Revisa cada slide visualmente** (ábrela con Read). Corrige texto cortado, solapado o desbordado antes de seguir.

## 4. Subir y programar
1. Copia las slides a `publicados/AAAA-MM-DD/` (`slide-1.jpg`…) junto con `contenido.json` y `descripcion.txt`. Commit y push a `main`.
2. Comprueba que `https://raw.githubusercontent.com/paulaamarinn0-jpg/mariamarin-carruseles/main/publicados/AAAA-MM-DD/slide-1.jpg` responde 200.
3. Metricool (`createScheduledPost`), brand **blogId 7455408**:
   - `providers`: instagram + facebook; `instagramData: {"type":"POST"}`, `facebookData: {"type":"POST"}`
   - `media`: las URLs raw de las slides en orden
   - `publicationDate`: hoy 11:00:00, timezone `America/Santiago`
   - **`draft: true`** — nunca publicar directo
   - `text`: descripción (gancho + resumen numerado de los ítems + CTA "Comenta PALABRA…" + 6–8 hashtags)
4. Si la hora 11:00 ya pasó o falla algo, programa para el día siguiente a las 11:00 y avisa.

## 5. Avisar a Pau
Envía un mensaje corto con: el título del carrusel, la palabra del CTA, qué tiene que mandar por DM a quien comente, y el `plannerUrl` del borrador para aprobarlo.
