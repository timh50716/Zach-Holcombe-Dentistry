"""One-off generator for the static pages. Output is plain HTML committed to the repo."""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

PHONE = "828-684-3839"
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

SERVICES = [
    ("preventive", "Diagnostic & Preventative Care", "diagnostic.jpg"),
    ("cosmetic", "Cosmetic Dentistry", "cosmetic.jpg"),
    ("implants", "Dental Implants", "implants.jpg"),
    ("dentures", "Complete & Partial Dentures", "dentures.jpg"),
    ("oral-surgery", "Oral Surgery", "oral.jpg"),
    ("periodontics", "Periodontics", "periodontics.jpg"),
    ("root-canals", "Root Canals", "rootcanal.jpg"),
]

HOURS = [("Monday", "8:00am – 5:00pm"), ("Tuesday", "8:00am – 5:00pm"), ("Wednesday", "8:00am – 5:00pm"),
         ("Thursday", "8:00am – 5:00pm"), ("Friday", "Closed"), ("Saturday", "Closed"), ("Sunday", "Closed")]


def hours_list():
    return '<ul class="hours">' + "".join(f"<li><span>{d}</span><span>{h}</span></li>" for d, h in HOURS) + "</ul>"


def nav_link(href, label, page):
    cur = ' aria-current="page"' if href == page else ""
    return f'<a href="{href}"{cur}>{label}</a>'


def header(page):
    svc = "".join(f'<li><a href="services.html#{sid}">{name}</a></li>' for sid, name, _ in SERVICES)
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
          <ul class="sub">{svc}</ul>
        </li>
        <li>{nav_link("new-patients.html", "New Patients", page)}</li>
        <li>{nav_link("contact.html", "Contact", page)}</li>
      </ul>
      <a class="btn" href="contact.html">Book an Appointment</a>
    </nav>
  </div>
</header>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <a class="footer-logo" href="index.html"><img src="assets/img/logo.png" alt="Zachary Holcombe D.M.D. General Dentistry" width="242" height="81"></a>
    <p>{ADDR1}, {ADDR2} &nbsp;|&nbsp; <a href="{TEL}" style="color:#fff">{PHONE}</a></p>
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
  <a href="contact.html">{ICON_CAL}Schedule</a>
  <a href="{MAPS}" target="_blank" rel="noopener">{ICON_PIN}Find Us</a>
</nav>
<script src="assets/js/main.js"></script>
"""


def page(filename, title, description, body, extra_head=""):
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Vollkorn:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
{extra_head}</head>
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
        <p><a href="{TEL}">{PHONE}</a></p>
        <p><a href="{MAPS}" target="_blank" rel="noopener">Get directions &rarr;</a></p>
      </div>
      <div class="visit__col">
        <h4>Hours of Operation</h4>
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
      <a class="btn" href="{TEL}">Call {PHONE}</a>
      <a class="btn btn--dark" href="new-patients.html" style="border:1px solid rgba(255,255,255,.4)">Patient Forms</a>
    </div>
  </div>
</section>"""


# ---------------- Home ----------------
schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "name": "Zachary Holcombe D.M.D. General Dentistry",
  "url": "https://dentalasheville.com/",
  "telephone": "+1-{PHONE}",
  "image": "https://dentalasheville.com/assets/img/logo.png",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "1944 Hendersonville Rd., Suite B-2",
    "addressLocality": "Asheville",
    "addressRegion": "NC",
    "postalCode": "28803",
    "addressCountry": "US"
  }},
  "openingHoursSpecification": [{{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
    "opens": "08:00",
    "closes": "17:00"
  }}],
  "sameAs": ["{FB}"]
}}
</script>
"""

tile_imgs = {sid: img for sid, _, img in SERVICES}
home = f"""<section class="hero">
  <div class="container">
    <p class="hero__kicker">Your Trusted Dentist in Asheville</p>
    <h1 class="hero__title">Quality, Patient-Centered Dental Care</h1>
    <p class="hero__lede">Whatever dentistry you're in need of, you'll feel comfortable with our team. New smiles are always welcome!</p>
    <a class="btn" href="contact.html">Book an Appointment</a>
  </div>
</section>

<section class="why" aria-label="Why choose us">
  <div class="why__title"><h2>Why Choose Us?</h2></div>
  <div class="why__stats">
    <div class="stat"><div class="stat__num">Since 1981</div><div class="stat__label">Caring for Asheville</div></div>
    <div class="stat"><div class="stat__num">7</div><div class="stat__label">Areas of care, one office</div></div>
    <div class="stat"><div class="stat__num">All Ages</div><div class="stat__label">Children to seniors</div></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media"><div class="mark-card">{MARK}<span>Zachary Holcombe D.M.D.</span>General Dentistry</div></div>
    <div>
      <h2>Welcome to Our Practice</h2>
      <p>Being patient-centered means that your positive experience, in every detail, is our primary concern. Our entire team cares about getting to know you and building a relationship with you beyond simply fixing your teeth.</p>
      <p>Dr. Holcombe took over the practice in 2018, carrying forward the legacy of care that Dr. Miller and our long-time team built over decades. We would love to take care of you and your entire family, from children to senior adults.</p>
      <div class="btn-row">
        <a class="btn" href="contact.html">Book an Appointment</a>
        <a class="btn" href="about.html#dr-holcombe">Meet Dr. Holcombe</a>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <h2>Questions About Insurance?</h2>
    <p>Our front office will help you gather the insurance information you need and understand your benefits before treatment begins.</p>
    <ul class="band__points">
      <li>Help with insurance information</li>
      <li>Clear explanations before treatment</li>
      <li>Quick appointment scheduling</li>
    </ul>
    <a class="btn" href="{TEL}">Call {PHONE}</a>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="center">New Patients Welcome</h2>
    <p class="section__intro"><strong>New to our practice? We’d love to meet you.</strong><br>Getting started is simple — give us a call, fill out your forms ahead of time, and we’ll take it from there.</p>
    <div class="cards">
      <div class="card"><div class="card__head">Call to Schedule</div><p>Reach our front office Monday–Thursday, 8:00am–5:00pm.</p><a class="btn" href="{TEL}">{PHONE}</a></div>
      <div class="card"><div class="card__head">Forms Ready to Go</div><p>Save time at your first visit by downloading and completing your patient information form at home.</p><a class="btn" href="new-patients.html">Patient Forms</a></div>
      <div class="card"><div class="card__head">Easy to Find</div><p>We’re on Hendersonville Road in Suite B-2, Asheville, NC 28803.</p><a class="btn" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <h2 class="center">Our Services</h2>
    <p class="section__intro">A wide range of services to help you achieve oral health and the smile you want, all in a comfortable and friendly environment.</p>
    <div class="tiles">
      <a class="tile tile--lg" href="services.html#cosmetic" style="background-image:url(assets/img/cosmetic.jpg)"><span class="tile__label">Cosmetic Dentistry</span></a>
      <a class="tile" href="services.html#preventive" style="background-image:url(assets/img/diagnostic.jpg)"><span class="tile__label">Preventive Care</span></a>
      <a class="tile" href="services.html#implants" style="background-image:url(assets/img/implants.jpg)"><span class="tile__label">Dental Implants</span></a>
      <a class="tile" href="services.html#dentures" style="background-image:url(assets/img/dentures.jpg)"><span class="tile__label">Dentures</span></a>
      <a class="tile" href="services.html#root-canals" style="background-image:url(assets/img/rootcanal.jpg)"><span class="tile__label">Root Canals</span></a>
      <a class="tile" href="services.html#oral-surgery" style="background-image:url(assets/img/oral.jpg)"><span class="tile__label">Oral Surgery</span></a>
      <a class="tile" href="services.html#periodontics" style="background-image:url(assets/img/periodontics.jpg)"><span class="tile__label">Periodontics</span></a>
      <a class="tile tile--wide" href="services.html"><span class="tile__label">View All Services &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--reverse">
    <div class="split__media"><img src="assets/img/diagnostic.jpg" alt="Dental hygienist providing a professional cleaning" loading="lazy" width="600" height="400"></div>
    <div>
      <h2>A Dental Office Where You Feel Like Family</h2>
      <p>We strive to do everything we can to make each appointment the best experience possible. Many of our patients have trusted this practice for decades — our business manager has been here since 1989 and our hygienist since 1981.</p>
      <p>We take the time to make sure you have a clear understanding of what is going on and why, so you can be an active decision maker in your dental health.</p>
      <a class="btn" href="about.html">Learn More</a>
    </div>
  </div>
</section>

{reviews_section()}

{visit_section()}"""
page("index.html", "Asheville Dentist | Zachary Holcombe D.M.D. General Dentistry",
     "Quality, patient-centered dental care in Asheville, NC. Dr. Zachary Holcombe offers preventive, cosmetic, implant, denture, oral surgery, periodontal and root canal care. Call 828-684-3839.",
     home, schema)

# ---------------- About ----------------
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
      <p>We strive to do everything we can to make each appointment the best experience possible. We would like to take care of you and your entire family, from children to senior adults.</p>
      <p>Dr. Holcombe took over the practice in 2018 and is proud to continue the legacy of friendly, excellent care our patients have counted on for years.</p>
      <a class="btn" href="contact.html">Book an Appointment</a>
    </div>
  </div>
</section>

<section class="section section--mist" id="dr-holcombe" style="scroll-margin-top:110px">
  <div class="container split split--reverse">
    <div class="split__media"><div class="mark-card">{MARK}<span>Zachary S. Holcombe, D.M.D.</span></div></div>
    <div>
      <h2>Meet Dr. Holcombe</h2>
      <p>Dr. Holcombe is a native of Greenville, NC who attended North Carolina State University for undergraduate studies before earning his DMD from East Carolina University. He is married to his wife Amy and they have one child. When not practicing dentistry he enjoys spending time outdoors with his friends and family.</p>
      <p>Dr. Holcombe enjoys working with his patients and is thankful for his practice that he took over in 2018. He is an active member of:</p>
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
    <div class="team">
      <article class="member">
        <h3>Cathy Matheson</h3>
        <div class="member__role">Business Manager &amp; Appointments Secretary</div>
        <span class="member__since">With the practice since 1989</span>
        <p>Cathy has worked at the practice since 1989 as the Business Manager. She is married with 2 grown sons and 3 granddaughters. She enjoys her job and the patients in the practice.</p>
      </article>
      <article class="member">
        <h3>Betty Abshire</h3>
        <div class="member__role">Registered Dental Hygienist</div>
        <span class="member__since">With the practice since 1981</span>
        <p>Betty graduated from the dental hygiene program at Asheville-Buncombe Technical Community College in 1980. She has been working at the practice since April 1981 and enjoys both her work and the patients! Betty has 2 children, Corey and Amy.</p>
      </article>
      <article class="member">
        <h3>Marija Mintz</h3>
        <div class="member__role">Dental Assistant</div>
        <span class="member__since">With the practice since 2016</span>
        <p>Marija was born and raised in Macedonia where she attended dental school. She graduated from AB-Tech’s Dental Assisting program in 2006 and has been a dental assistant ever since. Being able to interact, educate, and comfort patients is the most rewarding experience to her. Marija has two boys and enjoys spending time with family and friends, cooking, traveling and outdoor activities — especially when it is warm!</p>
      </article>
    </div>
  </div>
</section>

{reviews_section()}

{cta_band("Ready to Meet Our Team?", "New smiles are always welcome. Give us a call and we’ll find a time that works for you.")}"""
page("about.html", "About Us | Zachary Holcombe D.M.D. – Asheville Dentist",
     "Meet Dr. Zachary Holcombe and the team at our Asheville, NC dental practice — patient-centered care for children to senior adults.",
     about)

# ---------------- Services ----------------
svc_index = "".join(f'<a href="#{sid}">{name}</a>' for sid, name, _ in SERVICES)


def svc(sid, name, img, body):
    return f"""<article class="service" id="{sid}">
  <img src="assets/img/{img}" alt="{name}" loading="lazy">
  <div><h2>{name}</h2>{body}</div>
</article>"""


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


services_body = [
    svc("preventive", "Diagnostic & Preventative Care", "diagnostic.jpg",
        "<p>One of the easiest ways to prevent the decline of your oral health is to maintain a regular schedule of having your teeth cleaned by our dental hygienist. A professional cleaning will minimize the accumulation of harmful plaque and calculus on your teeth. Your hygienist will also provide you with instruction on personalized home care.</p>"
        "<p>By working together, we can prevent the advance of gum disease and ensure healthy teeth and a beautiful smile in the years ahead. Your doctor and hygienist can aid you in determining the treatment best suited to your specific needs.</p>"
        + checklist(["Dental radiographs", "Oral cancer screenings", "Examinations and consultations", "Dental cleanings", "Sealants", "Fluoride application"])),
    svc("cosmetic", "Cosmetic Dentistry", "cosmetic.jpg",
        "<p>We understand the importance of being able to smile with confidence. A great smile is one of the best ways to make a positive impression, which is why we offer a wide variety of treatments to help give you the smile you want.</p>"
        "<h4>Teeth Whitening</h4><p>This helps you have a brighter and whiter smile. Teeth naturally change color over time but also become discolored due to staining from coffee, tea, red wine and smoking. Whitening is not for all situations, but we would love to discuss whether it could benefit you.</p>"
        "<h4>Tooth-Colored Fillings</h4><p>We offer resin composite fillings that blend in with your natural tooth.</p>"
        "<h4>Veneers, Crowns and Bridges</h4><p>Veneers cover the front of your tooth to help change its shape or color. Crowns help protect a cracked or damaged tooth, restoring its strength and appearance. A bridge covers the teeth on each side of an empty space where there once was a tooth. It replaces the missing tooth, making it easier to chew.</p>"),
    svc("implants", "Dental Implants", "implants.jpg",
        "<p>Implants are titanium screws that attach to the bone where you are missing teeth. This allows for a tooth-colored crown to be secured in the missing space. With dental implants you can rediscover your confidence to eat, speak, laugh and enjoy life. Our office offers the following implant restorations:</p>"
        "<h4>Implant Crowns and Bridges</h4><p>These are similar to a traditional crown or bridge, except the restoration sits on the implant instead of your tooth.</p>"
        "<h4>Attachments for Dentures</h4><p>Implants can be used as attachments for traditional dentures, allowing them to “snap” into place. This helps increase the stability and retention of the denture.</p>"
        "<h4>Fixed Hybrids</h4><p>This is a restoration that replaces all or most of the teeth in your arch. It is different from a denture in that you do not take the fixed hybrid out — it is screwed into place on the implants. Other advantages include being more stable and smaller than a traditional denture, making it a great alternative for patients who suffer from a gag reflex.</p>"),
    svc("dentures", "Complete & Partial Dentures", "dentures.jpg",
        "<p>If you have lost several teeth and can’t chew and smile like you once did, we have options to help. We can replace all your teeth with a complete denture or make a partial denture to work with your existing teeth.</p>"
        "<p>We can also incorporate implants into the denture design to help it stay in place, providing a more secure denture.</p>"),
    svc("oral-surgery", "Oral Surgery", "oral.jpg",
        "<p>Oral surgery is required for many situations, such as extracting wisdom teeth, preparing for dentures or extracting infected and non-restorable teeth. We offer extractions and alveoloplasty, which is shaping of the bone after an extraction to help your denture fit better.</p>"
        + checklist(["Tooth extractions", "Surgical root tip extractions", "Alveoloplasty"])),
    svc("periodontics", "Periodontics", "periodontics.jpg",
        "<p>Slow but progressive, periodontal disease swells the gingiva and destroys the bone that supports your teeth. Once the bone is lost, it does not regenerate. It may be generalized, affecting all of your teeth, or localized, affecting one tooth. This disease affects both men and women of all ethnicities, from teen years through adulthood.</p>"
        "<p>In its early stages, you will be unaware of its presence. Dental hygiene habits, medications, smoking, alcohol, diet, general health or heredity may play a role in its progression. Initial symptoms may include swollen gums that bleed when you brush and an odor to your breath. Symptoms can advance to loosening and shifting of teeth and their eventual loss. Please speak with one of our team members today to learn more.</p>"
        + checklist(["Periodontal scaling &amp; root planing", "Periodontal surgery", "Gingival medicament placements", "Gingivoplasty"])),
    svc("root-canals", "Root Canals", "rootcanal.jpg",
        "<p>A root canal is needed when decay or trauma to a tooth has irreversibly damaged the nerve. The nerve cannot heal itself, so when this happens the tooth either needs to be extracted or have a root canal. If not treated promptly, an extremely painful and dangerous infection called a dental abscess may develop.</p>"
        "<p>During the root canal procedure we remove the damaged and infected nerve tissue, disinfect the root canal, and then refill it with a sterile material to seal the canal from bacteria. If the procedure is on a back tooth, we will normally recommend a crown to help strengthen and protect the tooth.</p>"),
]

services = f"""<section class="page-hero">
  <div class="container">
    <h1>Services &amp; Procedures</h1>
    <p>We offer a wide range of services to help you achieve a state of oral health and give you the smile you want — all in a comfortable and friendly environment.</p>
  </div>
</section>
<section class="section--mist" style="padding:28px 0">
  <div class="container service-index">{svc_index}</div>
</section>
<section>
  <div class="container">
    {"".join(services_body)}
  </div>
</section>

{cta_band("Not Sure What You Need?", "Your doctor and hygienist will help you find the treatment best suited to your needs. Give us a call to get started.")}"""
page("services.html", "Dental Services in Asheville, NC | Zachary Holcombe D.M.D.",
     "Preventive care, cosmetic dentistry, dental implants, dentures, oral surgery, periodontics and root canals in Asheville, NC.",
     services)

# ---------------- New patients / forms ----------------
new_patients = f"""<section class="page-hero">
  <div class="container">
    <h1>New Patients</h1>
    <p>New smiles are always welcome! Here’s how to get ready for your first visit.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <ol class="steps">
      <li><h3>Call Us</h3><p>Schedule your first appointment at <a href="{TEL}">{PHONE}</a>, Monday–Thursday, 8:00am–5:00pm.</p></li>
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

{reviews_section()}

{visit_section()}"""
page("new-patients.html", "New Patients & Forms | Zachary Holcombe D.M.D. – Asheville Dentist",
     "New patients are always welcome. Download patient forms and schedule your first visit with Dr. Zachary Holcombe in Asheville, NC.",
     new_patients)

# ---------------- Contact ----------------
contact = f"""<section class="page-hero">
  <div class="container">
    <h1>Contact Us</h1>
    <p>Give us a call to make an appointment — we’ll be glad to help.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cards">
      <div class="card"><div class="card__head">Call</div><p>The fastest way to schedule or ask a question.</p><a class="btn" href="{TEL}">{PHONE}</a></div>
      <div class="card"><div class="card__head">Visit</div><p>{ADDR1}<br>{ADDR2}</p><a class="btn" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a></div>
      <div class="card"><div class="card__head">Hours</div><p>Monday–Thursday<br>8:00am – 5:00pm<br>Friday–Sunday Closed</p></div>
    </div>
  </div>
</section>

{visit_section()}"""
page("contact.html", "Contact & Appointments | Zachary Holcombe D.M.D. – Asheville Dentist",
     "Call 828-684-3839 to schedule with Dr. Zachary Holcombe at 1944 Hendersonville Rd., Suite B-2, Asheville, NC 28803.",
     contact)

print("built", sorted(p.name for p in OUT.glob("*.html")))
