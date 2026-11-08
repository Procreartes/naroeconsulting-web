#!/usr/bin/env python3
"""Genera la web de Naroe Consulting (naroeconsulting.com) y su especial de ROI e impacto económico (/roi/).

Uso:  python3 scripts/generar.py
Datos editables (Gestor de webs del portal o a mano): data/servicios.json
No edites los .html a mano: se sobrescriben.
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from web import RAIZ, Sitio, ICO, esc, datos, mailto  # noqa: E402

CORREO = "hola@naroeconsulting.com"
PALETA = ["#DB3E4C", "#F69178", "#F4CF70", "#36A693", "#3257A8", "#8B3D88", "#E5A9C9", "#937465", "#969696"]

S = Sitio(
    nombre="Naroe Consulting", nombre_corto="Naroe Consulting",
    dominio="https://naroeconsulting.com",
    titular="Naroe Consulting S.L.", nif="B22534804",
    domicilio="Hoya de Parrado, 4 · 35017 Las Palmas de Gran Canaria",
    correo=CORREO, correo_datos="protecciondatos@naroeconsulting.com",
    objeto="Esta web informa sobre los servicios de consultoría de Naroe Consulting S.L. y sobre la forma de contactar.",
    color_tema="#111111", color_fondo="#ffffff",
    precarga=["manrope-latin-800-normal.woff2", "manrope-latin-400-normal.woff2"],
    menu=[("/#servicios", "Servicios"), ("/roi/", "ROI e impacto"), ("/#nosotros", "Quiénes somos"), ("/#contacto", "Contacto")],
    marca='<span class="logo"><span class="logo-caja">NAROE</span><span class="logo-txt">CONSU<br>LTING</span></span>',
    pie_html='''<div class="pie-arriba">
      <div><span class="logo logo-pie"><span class="logo-caja">NAROE</span><span class="logo-txt">CONSU<br>LTING</span></span>
      <p>Consultoría especializada en proyectos culturales, eventos y valoración de patrocinios.</p></div>
      <div><p><a href="mailto:hola@naroeconsulting.com">hola@naroeconsulting.com</a></p>
      <p>Hoya de Parrado, 4 · Las Palmas de Gran Canaria</p><p class="pie-nota">Una empresa de Grupo Livon</p></div>
    </div>''',
)

SERVICIOS = datos("servicios.json", [])


def franja():
    return '<div class="franja" aria-hidden="true">' + "".join(f'<i style="background:{c}"></i>' for c in PALETA) + "</div>"


def inicio():
    servicios = ""
    for i, s in enumerate(SERVICIOS):
        color = PALETA[i % len(PALETA)]
        enlace = s.get("enlace") or ""
        externo = enlace.startswith("http")
        mas = (f'<a class="servicio-enlace" href="{esc(enlace)}">{"Ir a " + esc(enlace.split("//")[-1]) if externo else "Saber más"} {ICO["flecha"]}</a>'
               if enlace else "")
        servicios += f'''<article class="servicio aparece" style="--c:{color}">
      <h3>{esc(s.get("titulo"))}</h3><p>{esc(s.get("texto"))}</p>{mas}
    </article>'''

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "ProfessionalService", "name": "Naroe Consulting",
        "legalName": "Naroe Consulting S.L.", "url": S.dominio + "/", "email": CORREO, "taxID": "B22534804",
        "address": {"@type": "PostalAddress", "streetAddress": "Hoya de Parrado, 4", "postalCode": "35017",
                    "addressLocality": "Las Palmas de Gran Canaria", "addressCountry": "ES"},
        "areaServed": "Canarias",
    }, ensure_ascii=False)

    cuerpo = f'''<section class="portada">
  <div class="contenedor">
    <p class="antetitulo">Consultoría · Las Palmas de Gran Canaria</p>
    <h1>Datos que demuestran<br>lo que vale un <span class="subraya">evento</span>.</h1>
    <div class="portada-pie">
      <p class="entradilla">Consultoría especializada en proyectos culturales, organización de eventos y valoración de patrocinios para administraciones públicas y entidades privadas.</p>
      <div class="botones">
        <a class="boton boton-negro" href="/roi/">ROI e impacto económico {ICO["flecha"]}</a>
        <a class="boton boton-linea" href="{mailto(CORREO, "Consulta desde la web")}">Escríbannos</a>
      </div>
    </div>
  </div>
  {franja()}
</section>

<section class="seccion" id="servicios" aria-labelledby="t-servicios">
  <div class="contenedor">
    <div class="cabecera-seccion"><p class="antetitulo">Servicios</p><h2 id="t-servicios">En qué les podemos ayudar</h2></div>
    <div class="servicios">{servicios}</div>
  </div>
</section>

<section class="seccion seccion-negra" aria-labelledby="t-especial">
  <div class="contenedor especial">
    <div>
      <p class="antetitulo">Especial</p>
      <h2 id="t-especial">ROI para eventos y estudios de impacto económico</h2>
      <p>Pre-ROI para solicitar un patrocinio, informe de retorno publicitario para justificarlo y estudio de impacto económico para contar lo que el evento deja en el territorio. Con método, fuentes verificables y declaración de independencia.</p>
      <a class="boton boton-blanco" href="/roi/">Ver cómo trabajamos {ICO["flecha"]}</a>
    </div>
    <dl class="formula" aria-label="Indicadores del informe">
      <div><dt>VPE</dt><dd>Valor publicitario equivalente</dd></div>
      <div><dt>ROAS</dt><dd>Retorno ÷ inversión</dd></div>
      <div><dt>ROI</dt><dd>(Retorno − inversión) ÷ inversión</dd></div>
    </dl>
  </div>
</section>

<section class="seccion" id="nosotros" aria-labelledby="t-nosotros">
  <div class="contenedor nosotros">
    <div><p class="antetitulo">Quiénes somos</p><h2 id="t-nosotros">Gente de producción que habla el idioma de los datos</h2></div>
    <div>
      <p class="entradilla">Naroe Consulting nace de la experiencia de dirigir festivales y proyectos culturales de gran formato en Canarias.</p>
      <p>Su director técnico, Naroe Valls O’Shanahan, suma más de veinticinco años de trayectoria en la dirección de festivales y proyectos culturales, y ha elaborado, supervisado y certificado informes técnicos de ROI e impacto económico para administraciones públicas y promotores privados.</p>
      <p>Por eso sabemos qué pide cada convocatoria, qué documentación sirve de verdad y cómo presentar un proyecto para que se entienda a la primera.</p>
    </div>
  </div>
</section>

<section class="seccion contacto" id="contacto" aria-labelledby="t-contacto">
  <div class="contenedor contacto-caja">
    {franja()}
    <h2 id="t-contacto">¿Tienen un evento, un patrocinio o una convocatoria entre manos?</h2>
    <p>Cuéntennos el proyecto y les enviamos un presupuesto.</p>
    <a class="boton boton-negro" href="{mailto(CORREO, "Presupuesto")}">{ICO["mail"]} {CORREO}</a>
  </div>
</section>'''
    return S.pagina("Naroe Consulting · ROI de patrocinios, impacto económico y consultoría para eventos",
                    "Consultoría en Canarias para eventos y proyectos culturales: informes ROI de patrocinios, estudios de impacto económico, subvenciones y planes de juventud.",
                    "/", cuerpo, actual="", ld=ld)


INFORMES = [
    ("pre", "Pre-ROI", "Antes del evento",
     "Estima el retorno publicitario que puede generar un patrocinio a partir del plan de soportes y de difusión comprometido. Sirve para solicitar el patrocinio y para que la entidad que patrocina sepa qué obtiene a cambio.",
     ["Plan de soportes y contraprestaciones", "Valor publicitario equivalente estimado", "ROAS y ROI previstos"]),
    ("roi", "Informe ROI", "Después del evento",
     "Mide el retorno publicitario real con las pruebas de lo que se hizo: soportes, emisiones, prensa, redes y presencia de marca. Es el informe que acompaña la justificación del patrocinio.",
     ["Valoración soporte a soporte", "Verificación de la presencia de marca", "Resultado frente a lo comprometido"]),
    ("impacto", "Estudio de impacto económico", "Lo que el evento deja en el territorio",
     "Calcula el efecto económico del evento en el municipio o la isla: el gasto del público, de la organización y de los proveedores, y su efecto en el empleo y el turismo.",
     ["Gasto de asistentes y visitantes", "Gasto de la organización en proveedores locales", "Empleo y retorno turístico"]),
]

PASOS = [
    ("Encargo y presupuesto", "Nos cuentan el evento, el patrocinio y la convocatoria. Les enviamos un presupuesto cerrado antes de empezar."),
    ("Documentación", "Les pedimos solo lo imprescindible y les decimos exactamente qué sirve. Pueden enviarlo todo por una carpeta compartida o por WeTransfer."),
    ("Cálculo y verificación", "Valoramos cada soporte con su método y comprobamos que cada prueba acredita de verdad la presencia de la marca."),
    ("Informe firmado", "Entregamos el informe en PDF, firmado, con resumen ejecutivo, metodología, detalle por soporte y declaración de independencia."),
]

DOCUMENTOS = [
    ("Contraprestaciones comprometidas", "Más que el contrato de patrocinio, lo que se comprometió a cambio: soportes, menciones, presencia de marca."),
    ("Costes", "Lo que costó cada acción de comunicación. Con los costes basta; no hace falta enviar todas las facturas."),
    ("Certificados de emisión", "De radio, televisión o publicidad exterior, a nombre de quien contrató y con referencia al evento."),
    ("Clipping", "Entrevistas, crónicas y programas de radio o televisión donde aparezca la marca."),
    ("Redes sociales", "Estadísticas de las publicaciones: alcance, impresiones, reproducciones e interacciones."),
]

CRITERIOS = [
    "Cada soporte se valora con su método: la publicidad exterior por su coste de contratación, no por un CPM teórico.",
    "En redes sociales no se suman a la vez interacciones, impresiones y visualizaciones: se elige una base para no contar dos veces.",
    "Un certificado de emisión solo acredita si está a nombre de quien contrató y hace referencia al evento.",
    "El coste de campañas programáticas se justifica con el precio real de compra y una comparativa, no solo con la plataforma del proveedor.",
    "En televisión se comprueba que la pieza se emitió en las cadenas certificadas y que la marca aparece en ella.",
]


def roi():
    informes = "".join(f'''<article class="informe aparece" id="{k}" style="--c:{PALETA[[0, 4, 3][i]]}">
      <p class="informe-cuando">{esc(cuando)}</p><h3>{esc(t)}</h3><p>{esc(d)}</p>
      <ul>{"".join(f"<li>{esc(x)}</li>" for x in lis)}</ul>
    </article>''' for i, (k, t, cuando, d, lis) in enumerate(INFORMES))
    pasos = "".join(f'<li class="aparece"><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for t, d in PASOS)
    docs = "".join(f"<div><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>" for t, d in DOCUMENTOS)
    criterios = "".join(f"<li>{ICO['check']}<span>{esc(c)}</span></li>" for c in CRITERIOS)

    cuerpo = f'''<section class="portada portada-roi">
  <div class="contenedor">
    <p class="antetitulo">Especial · ROI e impacto económico</p>
    <h1>Cuánto vuelve de cada euro de patrocinio.</h1>
    <div class="portada-pie">
      <p class="entradilla">Informes de retorno publicitario y estudios de impacto económico para festivales, eventos deportivos, conciertos y proyectos culturales que reciben patrocinio público o privado.</p>
      <div class="botones"><a class="boton boton-negro" href="{mailto(CORREO, "Presupuesto de informe ROI")}">Pedir presupuesto {ICO["flecha"]}</a></div>
    </div>
  </div>
  {franja()}
</section>

<section class="seccion" aria-labelledby="t-informes">
  <div class="contenedor">
    <div class="cabecera-seccion"><p class="antetitulo">Tres informes</p><h2 id="t-informes">Antes, después y más allá del evento</h2></div>
    <div class="informes">{informes}</div>
  </div>
</section>

<section class="seccion seccion-gris" aria-labelledby="t-cifras">
  <div class="contenedor cifras-grid">
    <div><p class="antetitulo">Las cifras del informe</p><h2 id="t-cifras">Tres números que cualquiera entiende</h2>
    <p>El valor publicitario equivalente (VPE) es lo que habría costado conseguir esa misma visibilidad comprándola en cada medio. A partir de ahí, el ROAS y el ROI comparan ese retorno con lo que se aportó.</p></div>
    <div class="ejemplo" role="group" aria-label="Ejemplo ilustrativo">
      <p class="ejemplo-titulo">Ejemplo ilustrativo</p>
      <dl>
        <div><dt>Aportación del patrocinio</dt><dd>10.000 €</dd></div>
        <div><dt>Retorno total (VPE)</dt><dd>40.000 €</dd></div>
        <div class="destaca"><dt>ROAS = 40.000 ÷ 10.000</dt><dd>4,0x</dd></div>
        <div class="destaca"><dt>ROI = (40.000 − 10.000) ÷ 10.000</dt><dd>300 %</dd></div>
      </dl>
      <p class="ejemplo-nota">Cifras inventadas para explicar el cálculo; no corresponden a ningún cliente.</p>
    </div>
  </div>
</section>

<section class="seccion" aria-labelledby="t-proceso">
  <div class="contenedor">
    <div class="cabecera-seccion"><p class="antetitulo">Cómo trabajamos</p><h2 id="t-proceso">Cuatro pasos, sin papeleo de más</h2></div>
    <ol class="pasos">{pasos}</ol>
  </div>
</section>

<section class="seccion seccion-gris" aria-labelledby="t-docs">
  <div class="contenedor docs-grid">
    <div><p class="antetitulo">Qué necesitamos</p><h2 id="t-docs">Lo que sí sirve para justificar</h2>
    <p>Cuanto menos trabajo para ustedes, mejor. Esto es lo que pedimos para un informe ROI:</p></div>
    <dl class="docs">{docs}</dl>
  </div>
</section>

<section class="seccion" aria-labelledby="t-criterios">
  <div class="contenedor criterios">
    <div><p class="antetitulo">Rigor</p><h2 id="t-criterios">Criterios que aplicamos</h2>
    <p>Seguimos las guías de retorno publicitario de las administraciones y los criterios con los que se revisan estos informes. Así el informe aguanta la revisión.</p></div>
    <ul class="lista-check">{criterios}</ul>
  </div>
</section>

<section class="seccion seccion-negra" aria-labelledby="t-indep">
  <div class="contenedor estrecho indep">
    <h2 id="t-indep">Independencia</h2>
    <p>Cada informe incluye una declaración expresa de independencia: Naroe Consulting no mantiene vinculación societaria, laboral ni económica con el promotor del evento evaluado, y el informe se elabora de forma independiente y objetiva.</p>
  </div>
</section>

<section class="seccion contacto" aria-labelledby="t-contacto">
  <div class="contenedor contacto-caja">
    {franja()}
    <h2 id="t-contacto">¿Necesitan un Pre-ROI, un ROI o un estudio de impacto?</h2>
    <p>Envíennos el nombre del evento, las fechas, el patrocinio y la convocatoria, y les respondemos con un presupuesto.</p>
    <a class="boton boton-negro" href="{mailto(CORREO, "Presupuesto de informe ROI o impacto económico")}">{ICO["mail"]} {CORREO}</a>
  </div>
</section>'''
    return S.pagina("ROI de patrocinios y estudios de impacto económico · Naroe Consulting",
                    "Pre-ROI, informes de retorno publicitario y estudios de impacto económico para eventos y festivales en Canarias. Método verificable y declaración de independencia.",
                    "/roi/", cuerpo)


def main():
    css = (RAIZ / "css/base.css").read_text(encoding="utf-8") + "\n" + (RAIZ / "css/tema.css").read_text(encoding="utf-8")
    S.escribir("css/estilos.css", css)
    S.publicar({"index.html": inicio(), "roi/index.html": roi()})


if __name__ == "__main__":
    main()
