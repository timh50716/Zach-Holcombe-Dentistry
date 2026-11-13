"""Generator for the static site. Output is plain HTML/TXT/XML committed to the repo.

Usage: python3 tools/build.py .
"""
import html as htmllib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from service_content import SERVICE_CONTENT  # noqa: E402

OUT = Path(sys.argv[1])

# Production domain used for canonical URLs, schema, sitemap and llms.txt.
SITE = "https://dentalasheville.com"
UPDATED_ISO = "2026-10-28"
UPDATED_TEXT = "October 2026"
PRACTICE = "Zachary Holcombe D.M.D. General Dentistry"

PHONE = "828-684-3839"
EMAIL = "office@dentalasheville.com"
REQUEST = "contact.html#request"
TEL = "tel:+18286843839"
ADDR1 = "1944 Hendersonville Rd., Suite B-2"
ADDR2 = "Asheville, NC 28803"
FB = "https://www.facebook.com/dentalasheville/"
MAPS = "https://www.google.com/maps/search/?api=1&query=1944+Hendersonville+Rd+Suite+B-2+Asheville+NC+28803"
MAP_EMBED = "https://www.google.com/maps?q=1944+Hendersonville+Rd+Suite+B-2+Asheville+NC+28803&output=embed"

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
ICON_CAL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 4h-1V2h-2v2H8V2H6v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 16H5V10h14zm0-12H5V6h14z"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8V6.2c0-.8.2-1.2 1.4-1.2H17V2h-2.6C11.3 2 10 3.4 10 6v2H8v3h2v11h4V11h2.7l.3-3z"/></svg>'
ICON_DOC = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm-1 7V3.5L18.5 9zM8 13h8v2H8zm0 4h8v2H8z"/></svg>'
# Two-peak mountain mark echoing the practice logo.
MARK = ('<svg viewBox="0 0 120 50" aria-hidden="true"><path d="M2 46 L40 10 L58 28 L78 4 L118 46 Z" fill="#12a39a" opacity=".9"/>'
        '<path d="M2 46 L40 10 L70 46 Z" fill="#2f8fd8"/></svg>')
SUNBURST = ('<svg class="review__mark" viewBox="0 0 120 50" aria-hidden="true"><path d="M10 46 L46 18 L62 32 L80 12 L110 46 Z" fill="#c99a3d"/></svg>')

# (page slug, name, photo or None, one-line summary used on cards and in meta descriptions)
SERVICES = [
    ("preventive-care", "Diagnostic & Preventative Care", "diagnostic.jpg",
     "Regular exams, X-rays and professional cleanings to keep your teeth healthy and stop gum disease before it starts."),
    ("childrens-dentistry", "Children’s Dentistry", None,
     "Gentle checkups, cleanings, fluoride and sealants that help kids build healthy habits for life."),
    ("crowns-bridges", "Crowns, Bridges & Fillings", None,
     "Natural-looking crowns, bridges and tooth-colored fillings that restore strength and function."),
    ("cosmetic-dentistry", "Cosmetic Dentistry", "cosmetic.jpg",
     "Teeth whitening, veneers and tooth-colored restorations to help you smile with confidence."),
    ("emergency-dentistry", "Emergency Dentistry", None,
     "Toothache, broken tooth or lost crown? Call us and we’ll see you as quickly as possible."),
    ("dental-implants", "Implant Restorations", "implants.jpg",
     "Implant crowns, bridges, snap-in dentures and fixed hybrids to replace missing teeth."),
    ("dentures", "Complete & Partial Dentures", "dentures.jpg",
     "Complete and partial dentures, including implant-supported options, so you can chew and smile again."),
    ("root-canals", "Root Canals", "rootcanal.jpg",
     "Relieve tooth pain, remove infection and save your natural tooth."),
    ("oral-surgery", "Tooth Extractions", "oral.jpg",
     "Gentle tooth extractions, surgical root tip extractions and alveoloplasty."),
    ("periodontics", "Gum Disease Treatment", "periodontics.jpg",
     "Scaling and root planing and other periodontal treatments to protect your gums and bone."),
    ("tmj-night-guards", "TMJ Treatment & Night Guards", None,
     "Relief for jaw pain and custom night guards that protect your teeth from grinding."),
]
SERVICE_PAGES = {f"{slug}.html" for slug, _, _, _ in SERVICES}

HOURS = [("Monday", "8:00am – 5:00pm"), ("Tuesday", "8:00am – 5:00pm"), ("Wednesday", "8:00am – 5:00pm"),
         ("Thursday", "8:00am – 5:00pm"), ("Friday", "Closed"), ("Saturday", "Closed"), ("Sunday", "Closed")]


def abs_url(filename):
    return f"{SITE}/" if filename == "index.html" else f"{SITE}/{filename}"


def plain(text):
    """Strip tags and decode entities for schema / txt output."""
    return htmllib.unescape(re.sub(r"<[^>]+>", "", text)).strip()


DENTIST_ID = f"{SITE}/#dentist"
DOCTOR_ID = f"{SITE}/#dr-holcombe"
WEBSITE_ID = f"{SITE}/#website"

DENTIST = {
    "@type": "Dentist",
    "@id": DENTIST_ID,
    "name": PRACTICE,
    "url": f"{SITE}/",
    "logo": f"{SITE}/assets/img/logo.png",
    "image": f"{SITE}/assets/video/hero-poster.jpg",
    "alternateName": "Dental Asheville",
    "telephone": "+1-828-684-3839",
    "email": EMAIL,
    "paymentAccepted": "Dental insurance (we file all plans; out-of-network), CareCredit, Cherry",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "1944 Hendersonville Rd., Suite B-2",
        "addressLocality": "Asheville",
        "addressRegion": "NC",
        "postalCode": "28803",
        "addressCountry": "US",
    },
    "hasMap": MAPS,
    "areaServed": {"@type": "City", "name": "Asheville", "containedInPlace": {"@type": "State", "name": "North Carolina"}},
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
        "opens": "08:00",
        "closes": "17:00",
    }],
    "medicalSpecialty": "https://schema.org/Dentistry",
    "isAcceptingNewPatients": True,
    "employee": {"@id": DOCTOR_ID},
    "knowsAbout": [plain(name) for _, name, _, _ in SERVICES],
    "sameAs": [FB],
}

DOCTOR = {
    "@type": "Person",
    "@id": DOCTOR_ID,
    "name": "Zachary S. Holcombe",
    "honorificPrefix": "Dr.",
    "honorificSuffix": "DMD",
    "jobTitle": "General Dentist",
    "image": f"{SITE}/assets/img/dr-holcombe.jpg",
    "url": f"{SITE}/about.html#dr-holcombe",
    "worksFor": {"@id": DENTIST_ID},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "East Carolina University"},
        {"@type": "CollegeOrUniversity", "name": "North Carolina State University"},
    ],
    "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "degree",
        "name": "Doctor of Dental Medicine (DMD)",
        "recognizedBy": {"@type": "CollegeOrUniversity", "name": "East Carolina University"},
    },
    "memberOf": [
        {"@type": "Organization", "name": "American Dental Association"},
        {"@type": "Organization", "name": "Academy of General Dentistry"},
        {"@type": "Organization", "name": "North Carolina Dental Society"},
        {"@type": "Organization", "name": "Buncombe County Dental Society"},
    ],
}

WEBSITE = {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    "url": f"{SITE}/",
    "name": PRACTICE,
    "publisher": {"@id": DENTIST_ID},
    "inLanguage": "en-US",
}

SITEMAP = []  # (filename, priority) of every indexable page, filled by page()


def hours_list():
    return '<ul class="hours">' + "".join(f"<li><span>{d}</span><span>{h}</span></li>" for d, h in HOURS) + "</ul>"


def nav_link(href, label, page):
    active = href == page or (href == "services.html" and page in SERVICE_PAGES)
    cur = ' aria-current="page"' if active else ""
    return f'<a href="{href}"{cur}>{label}</a>'


def header(page):
    svc = "".join(f'<li><a href="{slug}.html">{name}</a></li>' for slug, name, _, _ in SERVICES)
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar">
  <div class="container">
    <div class="topbar__info">
      <a href="{TEL}">{ICON_PHONE}{PHONE}</a>
      <a class="topbar__address" href="{MAPS}" target="_blank" rel="noopener">{ICON_PIN}{ADDR1}, {ADDR2}</a>
    </div>
    <div class="topbar__social"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ICON_FB}</a></div>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="logo" href="index.html"><img src="assets/img/logo.png" alt="Zachary Holcombe D.M.D. General Dentistry" width="242" height="81"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav"><span class="sr-only">Menu</span><span></span><span></span><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav__list">
        <li>{nav_link("index.html", "Home", page)}</li>
        <li class="has-sub">{nav_link("about.html", "About Us", page)}
          <ul class="sub">
            <li><a href="about.html#dr-holcombe">Meet Dr. Holcombe</a></li>
            <li><a href="about.html#team">Our Team</a></li>
          </ul>
        </li>
        <li class="has-sub">{nav_link("services.html", "Services", page)}
          <ul class="sub sub--wide">{svc}</ul>
        </li>
        <li>{nav_link("new-patients.html", "New Patients", page)}</li>
        <li>{nav_link("contact.html", "Contact", page)}</li>
      </ul>
      <a class="btn" href="{REQUEST}">Request an Appointment</a>
    </nav>
  </div>
</header>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <a class="footer-logo" href="index.html"><img src="assets/img/logo.png" alt="Zachary Holcombe D.M.D. General Dentistry" width="242" height="81"></a>
    <p>{ADDR1}, {ADDR2} &nbsp;|&nbsp; <a href="{TEL}" style="color:#fff">{PHONE}</a> &nbsp;|&nbsp; <a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a></p>
    <ul class="footer-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About Us</a></li>
      <li><a href="services.html">Services</a></li>
      <li><a href="new-patients.html">New Patients</a></li>
      <li><a href="contact.html">Contact Us</a></li>
      <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
    </ul>
    <small>&copy; <span id="year">2026</span> Zachary Holcombe D.M.D. General Dentistry. All rights reserved.</small>
  </div>
</footer>
<nav class="action-bar" aria-label="Quick actions">
  <a href="{TEL}">{ICON_PHONE}Call</a>
  <a href="{REQUEST}">{ICON_CAL}Request</a>
  <a href="{MAPS}" target="_blank" rel="noopener">{ICON_PIN}Find Us</a>
</nav>
<script src="assets/js/main.js"></script>
"""


def page(filename, title, description, body, crumbs=(), page_type="WebPage", nodes=(), webpage_extra=None,
         priority="0.7", noindex=False):
    """Write one page. crumbs: (name, filename) pairs after Home, used for BreadcrumbList schema."""
    url = abs_url(filename)
    webpage = {
        "@type": page_type,
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "description": description,
        "isPartOf": {"@id": WEBSITE_ID},
        "publisher": {"@id": DENTIST_ID},
        "inLanguage": "en-US",
        "dateModified": UPDATED_ISO,
    }
    graph = [DENTIST, DOCTOR, WEBSITE, webpage]
    if crumbs:
        trail = [("Home", "index.html"), *crumbs]
        webpage["breadcrumb"] = {"@id": f"{url}#breadcrumb"}
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": i, "name": plain(n), "item": abs_url(f)}
                for i, (n, f) in enumerate(trail, 1)
            ],
        })
    webpage.update(webpage_extra or {})
    graph.extend(nodes)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    t, d = htmllib.escape(title), htmllib.escape(description)
    if noindex:
        seo = '<meta name="robots" content="noindex, follow">'
    else:
        SITEMAP.append((filename, priority))
        seo = f"""<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{PRACTICE}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/video/hero-poster.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}/assets/video/hero-poster.jpg">"""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
{seo}
<meta name="theme-color" content="#0f2e40">
<link rel="icon" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Vollkorn:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(filename)}<main id="main">
{body}
</main>
{footer()}</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")


def visit_section():
    return f"""<section class="section" id="visit">
  <div class="container">
    <h2>Visit Us</h2>
    <div class="visit">
      <div class="visit__col">
        <p><strong>Zachary Holcombe D.M.D.</strong><br>{ADDR1}<br>{ADDR2}</p>
        <p><a href="{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><a href="{MAPS}" target="_blank" rel="noopener">Get directions &rarr;</a></p>
      </div>
      <div class="visit__col">
        <h3>Hours of Operation</h3>
        {hours_list()}
      </div>
      <div class="visit__map">
        <iframe class="map" title="Map to Zachary Holcombe D.M.D." src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </div>
</section>"""


REVIEWS = [
    ("I met Dr. Zack, What a nice guy! He made me feel very comfortable – thank you.", "Robin O."),
    ("This is the best possible dentist office in Asheville, in North Carolina, or anywhere else you want to go. Everyone is kind and as gentle as possible. I always feel that I have a clear understanding of what is going on and why. I feel both welcomed and respected as an active decision maker in my dental health.", "Michelle R."),
    ("Very friendly and helpful staff, got an appointment tremendously quick. Helped me acquire insurance info needed and were very on top of everything. Zach Holcombe along with reception staff are clearly very patient centered. Highly recommend.", "Andy B."),
    ("Met Dr. Holcombe, the new dentist…He did excellent work and was very friendly and personable", "Bill C."),
    ("Thankful to meet Dr. Zach and grateful that Glenn and Nancy have found someone to continue the legacy that they and their staff have built over the years.", "Cecelia C."),
    ("I have been a patient of Dr. Miller for 38 years and have had excellent care on each visit. I have really enjoyed Betty my hygienist. After that many years you feel like family here.", "Jo Wolfe"),
    ("I have always had a pleasant experience with Dr. Miller and his staff. Dr. Miller and Dr. Holcombe are very competent dentists and take great care in their work. I’m always treated well when I go in for an appointment.", "Max M."),
    ("Liked the new dentist and his assistant. Glad to see he gives the same friendly service.", "Jerry M."),
    ("Always a pleasure to visit your office-friendly staff and excellent care", "Dan M."),
    ("Always good to see you and your team… thanks for everything", "Brewster W."),
]


def reviews_section():
    items = "".join(
        f'<figure class="review{" is-active" if i == 0 else ""}">{SUNBURST}<blockquote>“{q}”</blockquote><figcaption><cite>{who}</cite></figcaption></figure>'
        for i, (q, who) in enumerate(REVIEWS))
    return f"""<section class="section section--mist" aria-labelledby="reviews-title">
  <div class="container">
    <h2 id="reviews-title" class="center">Patient Testimonials</h2>
    <p class="section__intro">What others are saying about Dr. Holcombe and our team.</p>
    <div class="reviews" aria-live="polite">{items}
      <div class="reviews__nav">
        <button type="button" data-review="prev" aria-label="Previous testimonial">&#10094;</button>
        <button type="button" data-review="next" aria-label="Next testimonial">&#10095;</button>
      </div>
    </div>
  </div>
</section>"""


def cta_band(title, text):
    return f"""<section class="band">
  <div class="container">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="{REQUEST}">Request an Appointment</a>
      <a class="btn btn--dark" href="{TEL}" style="border:1px solid rgba(255,255,255,.4)">Call {PHONE}</a>
    </div>
  </div>
</section>"""


# ---------------- Home ----------------
home = f"""<section class="hero">
  <video class="hero__video" autoplay muted loop playsinline preload="auto" poster="assets/video/hero-poster.jpg" aria-hidden="true">
    <source src="assets/video/hero-mobile.mp4" type="video/mp4" media="(max-width: 860px)">
    <source src="assets/video/hero.mp4" type="video/mp4">
  </video>
  <button class="hero__toggle" type="button" aria-label="Pause background video">
    <svg class="icon-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h4v16H6zm8 0h4v16h-4z"/></svg>
    <svg class="icon-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4v16l13-8z"/></svg>
  </button>
  <div class="container">
    <h1 class="hero__kicker">Your Trusted Dentist in Asheville, NC</h1>
    <p class="hero__title">Quality, Patient-Centered Dental Care</p>
    <p class="hero__lede">Personalized, comfortable dental care for the whole family — from the same dentist every visit. New patients are always welcome!</p>
    <a class="btn" href="{REQUEST}">Request an Appointment</a>
  </div>
</section>

<section class="why" aria-label="Why choose us">
  <div class="why__title"><h2>Why Choose Us?</h2></div>
  <div class="why__stats">
    <div class="stat"><div class="stat__num">Family-Owned</div><div class="stat__label">Small, private practice</div></div>
    <div class="stat"><div class="stat__num">Same Dentist</div><div class="stat__label">Every visit</div></div>
    <div class="stat"><div class="stat__num">All Ages</div><div class="stat__label">Children to seniors</div></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media"><figure class="portrait"><img src="assets/img/dr-holcombe.jpg" srcset="assets/img/dr-holcombe-sm.jpg 480w, assets/img/dr-holcombe.jpg 800w" sizes="(max-width: 860px) 90vw, 460px" alt="Dr. Zachary Holcombe, DMD, general dentist in Asheville, NC" width="800" height="1000" loading="lazy"><figcaption>Dr. Zachary S. Holcombe, DMD</figcaption></figure></div>
    <div>
      <h2>Welcome to Our Practice</h2>
      <p>We believe great dental care starts with getting to know our patients. Our practice is focused on providing personalized, comfortable care for the whole family in a welcoming environment. We take the time to listen, answer questions and build lasting relationships with our patients while helping them maintain healthy, confident smiles for years to come.</p>
      <p>Dr. Holcombe took ownership of the practice in 2018, continuing the legacy of care built by Dr. Glenn Miller. As a small, family-owned practice, you’ll see the same dentist at every visit.</p>
      <div class="btn-row">
        <a class="btn" href="{REQUEST}">Request an Appointment</a>
        <a class="btn" href="about.html#dr-holcombe">Meet Dr. Holcombe</a>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <h2>Insurance &amp; Financing Made Simple</h2>
    <p>We file all dental insurance claims for you. We’re an out-of-network provider for every plan, and many patients still use their benefits with us. Flexible financing is available through CareCredit and Cherry.</p>
    <ul class="band__points">
      <li>We file all insurance for you</li>
      <li>Financing with CareCredit</li>
      <li>Financing with Cherry</li>
    </ul>
    <a class="btn" href="new-patients.html#insurance">Insurance &amp; Financing Details</a>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="center">New Patients Welcome</h2>
    <p class="section__intro"><strong>New to our practice? We’d love to meet you.</strong><br>Your first visit includes an exam, X-rays and a cleaning, so we can get a complete picture of your dental health.</p>
    <div class="cards">
      <div class="card"><div class="card__head">New Patient Special</div><p class="card__price">$225</p><p>Adult comprehensive exam for new patients.</p><a class="btn" href="{REQUEST}">Request an Appointment</a></div>
      <div class="card"><div class="card__head">Dental Emergency?</div><p>Toothache, broken tooth or lost crown? New and current patients are welcome — call and we’ll see you as quickly as possible.</p><a class="btn" href="emergency-dentistry.html">Emergency Care</a></div>
      <div class="card"><div class="card__head">Forms Ready to Go</div><p>Save time at your first visit by downloading and completing your patient information form at home.</p><a class="btn" href="new-patients.html#forms">Patient Forms</a></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <h2 class="center">Our Services</h2>
    <p class="section__intro">A wide range of services to help you achieve oral health and the smile you want, all in a comfortable and friendly environment.</p>
    <div class="tiles">
      <a class="tile tile--lg" href="cosmetic-dentistry.html" style="background-image:url(assets/img/cosmetic.jpg)"><span class="tile__label">Cosmetic Dentistry</span></a>
      <a class="tile" href="preventive-care.html" style="background-image:url(assets/img/diagnostic.jpg)"><span class="tile__label">Cleanings &amp; Checkups</span></a>
      <a class="tile tile--plain" href="crowns-bridges.html"><span class="tile__label">Crowns &amp; Bridges</span></a>
      <a class="tile tile--plain" href="childrens-dentistry.html"><span class="tile__label">Children’s Dentistry</span></a>
      <a class="tile tile--plain" href="emergency-dentistry.html"><span class="tile__label">Emergency Dentistry</span></a>
      <a class="tile" href="dental-implants.html" style="background-image:url(assets/img/implants.jpg)"><span class="tile__label">Implant Restorations</span></a>
      <a class="tile" href="dentures.html" style="background-image:url(assets/img/dentures.jpg)"><span class="tile__label">Dentures</span></a>
      <a class="tile tile--wide" href="services.html"><span class="tile__label">View All Services &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--reverse">
    <div class="split__media"><img src="assets/img/diagnostic.jpg" alt="Dental hygienist providing a professional cleaning" loading="lazy" width="600" height="400"></div>
    <div>
      <h2>A Dental Office Where You Feel Like Family</h2>
      <p>We strive to make each appointment the best experience possible in a comfortable, family-friendly atmosphere. Many of our patients have trusted this practice for decades, and as a small private practice, our team takes the time to get to know every patient who walks through our door.</p>
      <p>We take the time to make sure you have a clear understanding of what is going on and why, so you can be an active decision maker in your dental health.</p>
      <a class="btn" href="about.html">Learn More</a>
    </div>
  </div>
</section>

{reviews_section()}

{visit_section()}"""
page("index.html", "Asheville Dentist | Zachary Holcombe D.M.D. General Dentistry",
     "Family dentist in Asheville, NC. Dr. Zachary Holcombe offers cleanings, crowns, cosmetic and emergency dentistry and children’s care. New patients welcome.",
     home, priority="1.0", webpage_extra={"about": {"@id": DENTIST_ID}})

# ---------------- About ----------------
# (first name shown, photo file in assets/img, role or "" if not known yet, bio html or "")
TEAM = [
    ("Marija Mintz", "team-marija.jpg", "Dental Assistant",
     "<p>Marija joined our practice in 2016. She was born and raised in Macedonia where she attended dental school. She graduated from AB-Tech’s Dental Assisting program in 2006 and has been a dental assistant ever since. Being able to interact, educate, and comfort patients is the most rewarding experience to her. Marija has two boys and enjoys spending time with family and friends, cooking, traveling and outdoor activities — especially when it is warm!</p>"),
    ("Kelly", "team-kelly.jpg", "", ""),
    ("Tonia", "team-tonia.jpg", "", ""),
]


def team_cards():
    return "".join(
        f"""
      <article class="member">
        <img class="member__photo" src="assets/img/{img}" alt="{name}{', ' + role if role else ''} at {PRACTICE}" width="480" height="600" loading="lazy">
        <div class="member__body">
          <h3>{name}</h3>{f'<div class="member__role">{role}</div>' if role else ''}{bio}
        </div>
      </article>""" for name, img, role, bio in TEAM)


about = f"""<section class="page-hero">
  <div class="container">
    <h1>About Us</h1>
    <p>Our entire team cares about getting to know you and building a relationship with you beyond simply fixing your teeth.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media"><div class="mark-card">{MARK}<span>Patient-centered since day one</span></div></div>
    <div>
      <h2>Our Practice</h2>
      <p>We believe great dental care starts with getting to know our patients. Our practice is focused on providing personalized, comfortable care for the whole family in a welcoming environment. We take the time to listen, answer questions and build lasting relationships with our patients while helping them maintain healthy, confident smiles for years to come.</p>
      <p>Dr. Holcombe took ownership of the practice in 2018, continuing the legacy of care built by Dr. Glenn Miller. As a small, family-owned practice, you’ll see the same dentist every visit. Our office provides everything from <a href="preventive-care.html">checkups and cleanings</a> and <a href="cosmetic-dentistry.html">cosmetic dentistry</a> to <a href="crowns-bridges.html">crowns and bridges</a>, <a href="dental-implants.html">implant restorations</a>, <a href="dentures.html">dentures</a>, <a href="root-canals.html">root canals</a>, <a href="childrens-dentistry.html">children’s dentistry</a> and <a href="emergency-dentistry.html">emergency care</a>.</p>
      <a class="btn" href="{REQUEST}">Request an Appointment</a>
    </div>
  </div>
</section>

<section class="section section--mist" id="dr-holcombe" style="scroll-margin-top:110px">
  <div class="container split split--reverse">
    <div class="split__media"><figure class="portrait"><img src="assets/img/dr-holcombe.jpg" srcset="assets/img/dr-holcombe-sm.jpg 480w, assets/img/dr-holcombe.jpg 800w" sizes="(max-width: 860px) 90vw, 460px" alt="Portrait of Dr. Zachary S. Holcombe, DMD" width="800" height="1000" loading="lazy"><figcaption>Dr. Zachary S. Holcombe, DMD</figcaption></figure></div>
    <div>
      <h2>Meet Dr. Holcombe</h2>
      <p>Dr. Holcombe is a Greenville, North Carolina, native who earned his undergraduate degree from North Carolina State University before receiving his Doctor of Dental Medicine degree from East Carolina University.</p>
      <p>He has been serving patients in his practice since taking ownership in 2018 and is grateful for the opportunity to build lasting relationships with his patients and their families. He enjoys getting to know each patient and helping them feel comfortable and confident in their dental care.</p>
      <p>Outside of the office, Dr. Holcombe enjoys spending time with his wife, Amy, and their three sons, Griffin, Turner and Hayes. When he’s not at the practice, you can find him gardening, woodworking, coaching his sons’ sports teams, or enjoying time with friends and family.</p>
      <p>Dr. Holcombe is an active member of:</p>
      <ul class="affil">
        <li>American Dental Association</li>
        <li>Academy of General Dentistry</li>
        <li>North Carolina Dental Society</li>
        <li>Buncombe County Dental Society</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="team" style="scroll-margin-top:110px">
  <div class="container">
    <h2 class="center">Our Team</h2>
    <p class="section__intro">Friendly, experienced and dedicated to making you feel at home.</p>
    <div class="team">{team_cards()}</div>
  </div>
</section>

{reviews_section()}

{cta_band("Ready to Meet Our Team?", "New patients are always welcome. Request an appointment and we’ll find a time that works for you.")}"""
page("about.html", "About Us | Zachary Holcombe D.M.D. – Asheville Dentist",
     "Meet Dr. Zachary Holcombe and the team at our Asheville, NC dental practice — patient-centered care for children to senior adults.",
     about, crumbs=[("About Us", "about.html")], page_type="AboutPage", priority="0.8",
     webpage_extra={"about": {"@id": DENTIST_ID}, "mainEntity": {"@id": DOCTOR_ID}})

# ---------------- Services ----------------
SERVICE_BY_SLUG = {slug: (name, img, summary) for slug, name, img, summary in SERVICES}


def service_aside(current):
    links = "".join(
        f'<li><a href="{slug}.html"{' aria-current="page"' if slug == current else ""}>{name}</a></li>'
        for slug, name, _, _ in SERVICES)
    return f"""<aside class="svc-aside" aria-label="Services and scheduling">
  <div class="svc-aside__box">
    <p class="svc-aside__title">Our Services</p>
    <ul class="svc-list">{links}</ul>
  </div>
  <div class="svc-aside__box svc-aside__box--ink">
    <p class="svc-aside__title">Schedule a Visit</p>
    <p>Monday–Thursday<br>8:00am – 5:00pm</p>
    <a class="btn" href="{REQUEST}">Request an Appointment</a>
    <p class="svc-aside__or">or call <a href="{TEL}">{PHONE}</a></p>
  </div>
  <div class="svc-aside__box">
    <p class="svc-aside__title">Insurance &amp; Financing</p>
    <p>We file all insurance for you. Financing available through CareCredit and Cherry.</p>
    <p><a href="new-patients.html#insurance">Learn more &rarr;</a></p>
  </div>
</aside>"""


def doctor_box(name):
    return f"""<section class="doctor-box" aria-labelledby="why-title">
  <img class="doctor-box__photo" src="assets/img/dr-holcombe-square.jpg" alt="Dr. Zachary S. Holcombe, DMD" width="320" height="320" loading="lazy">
  <div>
    <h2 id="why-title">Why Patients Choose Dr. Holcombe for {name}</h2>
    <ul class="checklist checklist--single">
      <li>Doctor of Dental Medicine (DMD) from East Carolina University; undergraduate studies at North Carolina State University</li>
      <li>Active member of the American Dental Association, Academy of General Dentistry, North Carolina Dental Society and Buncombe County Dental Society</li>
      <li>A small, family-owned practice where you see the same dentist every visit, led by Dr. Holcombe since 2018</li>
      <li>Personal care and long-term relationships: we take the time to listen, answer questions and explain your options</li>
    </ul>
    <p class="doctor-box__byline">Care provided by <a href="about.html#dr-holcombe">Dr. Zachary S. Holcombe, DMD</a>, general dentist at {PRACTICE}, {ADDR1}, {ADDR2}.</p>
  </div>
</section>"""


def related_block(slugs):
    cards = "".join(
        f'<a class="related__card" href="{s}.html"><strong>{SERVICE_BY_SLUG[s][0]}</strong><span>{SERVICE_BY_SLUG[s][2]}</span></a>'
        for s in slugs)
    return f"""<section class="svc-sec" aria-labelledby="related-title">
  <h2 id="related-title">Related Services</h2>
  <div class="related">{cards}</div>
  <p><a href="services.html">See all dental services &rarr;</a></p>
</section>"""


def service_page(slug, name, img, summary):
    c = SERVICE_CONTENT[slug]
    url = abs_url(f"{slug}.html")
    lead = "".join(f'<p{" class=\"lead\"" if i == 0 else ""}>{t}</p>' for i, t in enumerate(c["lead"]))
    steps = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in c["steps"])
    steps_html = f"""<section class="svc-sec"><h2>{c["steps_title"]}</h2><ol class="timeline">{steps}</ol></section>"""
    secs = [f'<section class="svc-sec"><h2>{h}</h2>{body}</section>' for h, body in c["sections"]]
    # The numbered "what to expect" list reads best just before the final (aftercare) section.
    secs.insert(len(secs) - 1, steps_html)
    faqs = "".join(
        f'<details class="faq"><summary><h3>{q}</h3></summary><div class="faq__a"><p>{a}</p></div></details>'
        for q, a in c["faqs"])
    content = f"""<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / <span aria-current="page">{name}</span></nav>
    <h1>{c["h1"]}</h1>
    <p>{summary}</p>
  </div>
</section>

<section class="section">
  <div class="container svc-layout">
    <article class="svc-main">
      {f'<img class="svc-main__img" src="assets/img/{img}" alt="{name} at {PRACTICE} in Asheville, NC" width="600" height="400">' if img else ''}
      {lead}
      <div class="btn-row svc-cta"><a class="btn" href="{REQUEST}">Request an Appointment</a><a class="btn btn--dark" href="{TEL}">Call {PHONE}</a></div>
      {"".join(secs)}
      {doctor_box(name)}
      <section class="svc-sec" aria-labelledby="faq-title">
        <h2 id="faq-title">{name}: Frequently Asked Questions</h2>
        {faqs}
      </section>
      {related_block(c["related"])}
      <p class="page-meta">Last updated {UPDATED_TEXT}. This page is for general information and doesn’t replace an exam — call us to discuss your specific needs.</p>
    </article>
    {service_aside(slug)}
  </div>
</section>

{reviews_section()}

{cta_band("Have Questions About " + name + "?", "Dr. Holcombe will help you find the treatment best suited to your needs. Request an appointment or give us a call to get started.")}

{visit_section()}"""
    pc = c["procedure"]
    nodes = [
        {
            "@type": pc["type"],
            "@id": f"{url}#procedure",
            "name": plain(name),
            "description": summary,
            "bodyLocation": pc["body"],
            "howPerformed": pc["how"],
        },
        {
            "@type": "Service",
            "@id": f"{url}#service",
            "name": f"{plain(name)} in Asheville, NC",
            "serviceType": plain(name),
            "description": summary,
            "url": url,
            "provider": {"@id": DENTIST_ID},
            "areaServed": DENTIST["areaServed"],
        },
        {
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                for q, a in c["faqs"]
            ],
        },
    ]
    page(f"{slug}.html", c["title"], c["meta"], content,
         crumbs=[("Services", "services.html"), (name, f"{slug}.html")],
         page_type="MedicalWebPage", nodes=nodes, priority="0.9",
         webpage_extra={
             "about": {"@id": f"{url}#procedure"},
             "mainEntity": {"@id": f"{url}#service"},
             "specialty": "https://schema.org/Dentistry",
             "audience": "https://schema.org/Patient",
             **({"primaryImageOfPage": f"{SITE}/assets/img/{img}"} if img else {}),
         })


for slug, name, img, summary in SERVICES:
    service_page(slug, name, img, summary)

svc_cards = "".join(
    f"""<a class="svc-card" href="{slug}.html">
  {f'<img src="assets/img/{img}" alt="{name}" loading="lazy" width="600" height="400">' if img else f'<div class="svc-card__art">{MARK}</div>'}
  <div class="svc-card__body"><h3>{name}</h3><p>{summary}</p><span class="svc-card__more">Learn more about {name.lower()} &rarr;</span></div>
</a>""" for slug, name, img, summary in SERVICES)

services = f"""<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span aria-current="page">Services</span></nav>
    <h1>Dental Services in Asheville, NC</h1>
    <p>We offer a wide range of services to help you achieve a state of oral health and give you the smile you want — all in a comfortable and friendly environment.</p>
  </div>
</section>
<section class="section section--mist">
  <div class="container">
    <h2 class="center">Our Services &amp; Procedures</h2>
    <p class="section__intro">From routine checkups and children’s dentistry to crowns, implant restorations and emergency care, Dr. Holcombe and our team care for patients of all ages.</p>
    <div class="svc-grid">{svc_cards}</div>
  </div>
</section>

{cta_band("Not Sure What You Need?", "Dr. Holcombe will help you find the treatment best suited to your needs. Request an appointment or give us a call to get started.")}"""
page("services.html", "Dental Services in Asheville, NC | Zachary Holcombe D.M.D.",
     "Cleanings, children’s dentistry, crowns, cosmetic and emergency dentistry, implant restorations, dentures, root canals and TMJ care in Asheville, NC.",
     services, crumbs=[("Services", "services.html")], page_type="CollectionPage", priority="0.9",
     webpage_extra={"mainEntity": {
         "@type": "ItemList",
         "itemListElement": [
             {"@type": "ListItem", "position": i, "name": plain(name), "url": abs_url(f"{slug}.html")}
             for i, (slug, name, _, _) in enumerate(SERVICES, 1)
         ],
     }})

# ---------------- New patients / forms ----------------
new_patients = f"""<section class="page-hero">
  <div class="container">
    <h1>New Patients</h1>
    <p>New smiles are always welcome! Here’s how to get ready for your first visit.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="center">Your First Visit</h2>
    <p class="section__intro">Your first visit includes a comprehensive <a href="preventive-care.html">exam, X-rays and a cleaning</a>. We’ll get to know you, review your health history and answer your questions. Explore all of our <a href="services.html">dental services</a>.</p>
    <div class="special">
      <p class="special__label">New Patient Special</p>
      <p class="special__price">$225</p>
      <p>Adult comprehensive exam for new patients. Call or request an appointment to schedule.</p>
    </div>
    <ol class="steps">
      <li><h3>Request an Appointment</h3><p><a href="{REQUEST}">Request an appointment online</a> or call <a href="{TEL}">{PHONE}</a>, Monday–Thursday, 8:00am–5:00pm.</p></li>
      <li><h3>Complete Your Forms</h3><p>Download the patient information form below and fill it out at home to save time when you arrive.</p></li>
      <li><h3>Visit Our Office</h3><p>Find us at {ADDR1}, {ADDR2}. We look forward to getting to know you!</p></li>
    </ol>
  </div>
</section>

<section class="section section--mist" id="forms">
  <div class="container">
    <h2 class="center">Patient Forms</h2>
    <p class="section__intro">Download, print and complete these forms before your visit.</p>
    <div class="downloads">
      <a class="download" href="assets/forms/patient-information-form.pdf" target="_blank" rel="noopener">{ICON_DOC}<span><strong>Patient Information Form</strong>PDF download</span></a>
      <a class="download" href="assets/forms/authorization-release-of-information.pdf" target="_blank" rel="noopener">{ICON_DOC}<span><strong>Authorization Release of Information</strong>PDF download</span></a>
    </div>
  </div>
</section>

<section class="section" id="insurance" style="scroll-margin-top:110px">
  <div class="container">
    <h2 class="center">Insurance &amp; Financing</h2>
    <p class="section__intro">We want cost to be one less thing to worry about.</p>
    <div class="cards cards--two">
      <div class="card"><div class="card__head">Dental Insurance</div><p>We file all dental insurance claims for you. We’re an out-of-network provider for every insurance plan, and many patients with dental benefits still choose to see us. Call our office with your plan information and we’ll be glad to help you understand your coverage.</p></div>
      <div class="card"><div class="card__head">Financing</div><p>Flexible payment options are available through <strong>CareCredit</strong> and <strong>Cherry</strong>, so you can get the care you need now and pay over time.</p></div>
    </div>
  </div>
</section>

{reviews_section()}

{visit_section()}"""
page("new-patients.html", "New Patients & Forms | Asheville Dentist Dr. Holcombe",
     "New patients welcome: $225 adult comprehensive exam. We file all insurance and offer CareCredit and Cherry financing. Dr. Zachary Holcombe, Asheville, NC.",
     new_patients, crumbs=[("New Patients", "new-patients.html")], priority="0.8",
     nodes=[{
         "@type": "Offer",
         "@id": f"{abs_url('new-patients.html')}#new-patient-special",
         "name": "New Patient Special: Adult Comprehensive Exam",
         "price": "225",
         "priceCurrency": "USD",
         "offeredBy": {"@id": DENTIST_ID},
         "url": abs_url("new-patients.html"),
     }])

# ---------------- Contact ----------------
contact = f"""<section class="page-hero">
  <div class="container">
    <h1>Request an Appointment</h1>
    <p>Send us a request below or give us a call — we’ll be glad to help.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cards">
      <div class="card"><div class="card__head">Call</div><p>The fastest way to schedule or ask a question.</p><a class="btn" href="{TEL}">{PHONE}</a></div>
      <div class="card"><div class="card__head">Email</div><p>For general questions. For urgent needs, please call.</p><a class="btn" href="mailto:{EMAIL}">Email Us</a></div>
      <div class="card"><div class="card__head">Visit</div><p>{ADDR1}<br>{ADDR2}</p><a class="btn" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a></div>
    </div>
  </div>
</section>

<section class="section section--mist" id="request" style="scroll-margin-top:110px">
  <div class="container">
    <h2 class="center">Appointment Request</h2>
    <p class="section__intro">Tell us a little about what you need and when you’re available, and our office will call you to confirm a time. This is a request — your appointment isn’t booked until we confirm it with you. For a dental emergency, please call <a href="{TEL}">{PHONE}</a>.</p>
    <form class="request-form" name="appointment-request" method="POST" action="/thank-you.html" data-netlify="true" netlify-honeypot="company">
      <input type="hidden" name="form-name" value="appointment-request">
      <p class="hp"><label>Leave this empty <input name="company" tabindex="-1" autocomplete="off"></label></p>
      <div class="form-grid">
        <label>First and last name *<input name="name" autocomplete="name" required></label>
        <label>Phone *<input name="phone" type="tel" autocomplete="tel" required></label>
        <label>Email<input name="email" type="email" autocomplete="email"></label>
        <label>I am a…<select name="patient-type"><option>New patient</option><option>Current patient</option></select></label>
        <label>Reason for visit<select name="reason">
          <option>Checkup &amp; cleaning</option><option>Toothache or emergency</option><option>Crown, bridge or filling</option>
          <option>Cosmetic dentistry</option><option>Child’s visit</option><option>Dentures or implant restoration</option><option>Other</option>
        </select></label>
        <label>Preferred days &amp; times<input name="availability" placeholder="e.g. Tuesday or Wednesday mornings"></label>
      </div>
      <label>Anything else we should know?<textarea name="message" rows="4" placeholder="Please don’t include detailed medical information."></textarea></label>
      <button class="btn" type="submit">Send Request</button>
    </form>
  </div>
</section>

{visit_section()}"""
page("contact.html", "Request an Appointment | Asheville Dentist Dr. Holcombe",
     "Request an appointment with Dr. Zachary Holcombe online or call 828-684-3839. 1944 Hendersonville Rd., Suite B-2, Asheville, NC 28803.",
     contact, crumbs=[("Contact", "contact.html")], page_type="ContactPage", priority="0.8")

# ---------------- Thank you (form confirmation) ----------------
thanks = f"""<section class="page-hero">
  <div class="container">
    <h1>Thank You!</h1>
    <p>We’ve received your appointment request. Our office will call you to confirm a time.</p>
  </div>
</section>
<section class="section">
  <div class="container center">
    <p>Our office is open Monday–Thursday, 8:00am–5:00pm. If you need to reach us sooner, please call <a href="{TEL}">{PHONE}</a>.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="new-patients.html#forms">Patient Forms</a>
      <a class="btn" href="index.html">Back to Home</a>
    </div>
  </div>
</section>"""
page("thank-you.html", "Thank You | Zachary Holcombe D.M.D.", "Your appointment request has been received.", thanks, noindex=True)

# ---------------- 404 ----------------
not_found = """<section class="page-hero">
  <div class="container">
    <h1>Page Not Found</h1>
    <p>Sorry, we couldn’t find that page. It may have moved when we updated our website.</p>
  </div>
</section>
<section class="section">
  <div class="container center">
    <p>Try one of these instead:</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="index.html">Home</a>
      <a class="btn" href="services.html">Services</a>
      <a class="btn" href="contact.html">Contact Us</a>
    </div>
  </div>
</section>"""
page("404.html", "Page Not Found | Zachary Holcombe D.M.D.", "The page you were looking for could not be found.",
     not_found, noindex=True)

# ---------------- robots.txt / sitemap.xml ----------------
(OUT / "robots.txt").write_text(f"""# {PRACTICE} — {SITE}
User-agent: *
Allow: /
Disallow: /tools/

Sitemap: {SITE}/sitemap.xml
""", encoding="utf-8")

urls = "".join(
    f"  <url>\n    <loc>{abs_url(f)}</loc>\n    <lastmod>{UPDATED_ISO}</lastmod>\n    <priority>{prio}</priority>\n  </url>\n"
    for f, prio in SITEMAP)
(OUT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n',
    encoding="utf-8")


# ---------------- llms.txt / llms-full.txt (https://llmstxt.org) ----------------
def md(fragment):
    """Very small HTML -> Markdown conversion for our own generated content."""
    t = re.sub(r'<a href="([^":]+\.html)">(.*?)</a>', lambda m: f"[{m.group(2)}]({abs_url(m.group(1))})", fragment)
    t = re.sub(r"<h3>(.*?)</h3>", r"\n#### \1\n", t)
    t = re.sub(r"<li>(.*?)</li>", r"- \1\n", t)
    t = re.sub(r"</p>", "\n\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = htmllib.unescape(t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


FACTS = f"""- Practice: {PRACTICE}
- Dentist: Dr. Zachary S. Holcombe, DMD (East Carolina University; undergraduate at North Carolina State University). Took over the practice in 2018.
- Memberships: American Dental Association, Academy of General Dentistry, North Carolina Dental Society, Buncombe County Dental Society
- Address: {ADDR1}, {ADDR2}
- Previous dentist: Dr. Glenn Miller, DDS (Dr. Holcombe took ownership in 2018)
- Phone: {PHONE}
- Email: {EMAIL}
- Hours: Monday–Thursday 8:00am–5:00pm; Friday–Sunday closed
- Patients: families, children to senior adults; new patients and emergency patients welcome
- Scheduling: call the office or request an appointment online at {abs_url('contact.html')}
- New patient special: $225 adult comprehensive exam; the first visit includes an exam, X-rays and a cleaning
- Insurance: files all dental insurance; out-of-network with all plans
- Financing: CareCredit and Cherry
- What sets the practice apart: small, private, family-owned; same dentist every visit; long-term patient relationships; comfortable atmosphere
- Facebook: {FB}"""

svc_lines = "\n".join(f"- [{plain(name)}]({abs_url(slug + '.html')}): {summary}" for slug, name, _, summary in SERVICES)
(OUT / "llms.txt").write_text(f"""# {PRACTICE}

> Small, family-owned general dental practice in Asheville, North Carolina, led by Dr. Zachary S. Holcombe, DMD. We provide preventive care, children's dentistry, crowns and bridges, cosmetic and emergency dentistry, implant restorations, dentures, root canals, extractions, gum disease treatment, and TMJ treatment and night guards for patients of all ages.

{FACTS}

## Services

{svc_lines}

## Practice

- [About Us]({abs_url('about.html')}): Dr. Holcombe's background and our team
- [New Patients & Forms]({abs_url('new-patients.html')}): first-visit steps and downloadable patient forms
- [Request an Appointment]({abs_url('contact.html')}): online appointment request, phone, email, address, hours and directions
- [Insurance & Financing]({abs_url('new-patients.html')}#insurance): insurance filing and CareCredit / Cherry financing
- [All Services]({abs_url('services.html')}): overview of every service

## Optional

- [Full text of service pages]({SITE}/llms-full.txt): complete service descriptions and FAQs in Markdown
""", encoding="utf-8")

full = [f"# {PRACTICE} — Full Service Information\n\n{FACTS}\n"]
for slug, name, _, summary in SERVICES:
    c = SERVICE_CONTENT[slug]
    parts = [f"## {plain(c['h1'])}\n\nURL: {abs_url(slug + '.html')}\n\n{summary}\n"]
    parts += [md(f"<p>{t}</p>") for t in c["lead"]]
    for h, body in c["sections"]:
        parts.append(f"### {plain(h)}\n\n{md(body)}")
    parts.append(f"### {plain(c['steps_title'])}\n\n" + "\n".join(
        f"{i}. **{plain(t)}** — {md(d)}" for i, (t, d) in enumerate(c["steps"], 1)))
    parts.append("### Frequently Asked Questions\n\n" + "\n\n".join(f"**{plain(q)}**\n{md(a)}" for q, a in c["faqs"]))
    full.append("\n\n".join(parts))
(OUT / "llms-full.txt").write_text("\n\n---\n\n".join(full) + "\n", encoding="utf-8")

print("built", sorted(p.name for p in OUT.glob("*.html")), "+ robots.txt, sitemap.xml, llms.txt, llms-full.txt")

