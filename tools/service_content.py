"""Long-form content for each service page.

Practice-specific facts come from the original dentalasheville.com site. Everything else is
general patient education and should be reviewed by Dr. Holcombe before launch.

Each entry:
  h1, title (<= ~60 chars), meta (<= ~155 chars), lead (intro paragraphs),
  sections: list of (h2, html) rendered in order,
  steps_title + steps: numbered "what to expect" list of (title, text),
  faqs: list of (question, answer_html) — also emitted as FAQPage schema,
  related: slugs for the "Related services" block,
  procedure: fields for the MedicalProcedure schema.
"""


def link(slug, text):
    return f'<a href="{slug}.html">{text}</a>'


def h3_list(items):
    return "".join(f"<h3>{t}</h3><p>{p}</p>" for t, p in items)


def bullets(items):
    return '<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


SERVICE_CONTENT = {
    # ------------------------------------------------------------------
    "preventive-care": dict(
        h1="Preventive Dental Care &amp; Checkups in Asheville, NC",
        title="Dental Checkups & Cleanings in Asheville, NC | Dr. Holcombe",
        meta="Dental exams, professional cleanings, X-rays, oral cancer screenings, sealants and fluoride for the whole family in Asheville, NC. Call 828-684-3839.",
        lead=[
            "One of the easiest ways to prevent the decline of your oral health is to maintain a regular schedule of having your teeth cleaned by our dental hygienist. A professional cleaning minimizes the accumulation of harmful plaque and calculus on your teeth, and your hygienist will give you instruction on personalized home care.",
            "By working together, we can prevent the advance of gum disease and help ensure healthy teeth and a beautiful smile in the years ahead. We care for patients of all ages — from children to senior adults.",
        ],
        sections=[
            ("Why Preventive Dental Care Matters",
             "<p>Tooth decay and gum disease usually start quietly. In the early stages you may not feel any pain at all, which is why routine visits are so valuable: small problems are easier, more comfortable and less costly to treat when they are found early.</p>"
             f"<p>Regular cleanings remove hardened plaque (calculus) that brushing and flossing can’t reach. Left in place, it irritates the gums and can lead to {link('periodontics', 'periodontal (gum) disease')}, which destroys the bone that supports your teeth.</p>"),
            ("Preventive &amp; Diagnostic Services We Offer", h3_list([
                ("Examinations and Consultations", "Dr. Holcombe checks your teeth, gums, bite and existing dental work, then talks with you about what he sees and any treatment options so you can make informed decisions."),
                ("Professional Dental Cleanings", "Your hygienist removes plaque and calculus above and below the gumline and polishes your teeth, then shows you techniques tailored to your mouth."),
                ("Dental Radiographs (X-rays)", "X-rays reveal what can’t be seen during a visual exam, such as decay between teeth, infection at the root and bone levels. We take them only as often as your individual needs call for."),
                ("Oral Cancer Screenings", "A quick, painless check of your lips, tongue, cheeks, throat and the floor of your mouth for any unusual changes that should be watched or evaluated further."),
                ("Sealants", "A thin, tooth-colored protective coating on the chewing surfaces of back teeth that helps keep food and bacteria out of deep grooves. Sealants are most often recommended for children and teens."),
                ("Fluoride Application", "A professional fluoride treatment strengthens enamel and helps protect teeth against decay for both children and adults."),
            ])),
            ("Caring for Your Smile Between Visits", bullets([
                "Brush twice a day for two minutes with a fluoride toothpaste.",
                "Clean between your teeth once a day with floss or another interdental cleaner.",
                "Limit sugary snacks and drinks, especially sipping or snacking throughout the day.",
                "Avoid tobacco, which raises the risk of gum disease and oral cancer.",
                "Call us if you notice bleeding gums, sensitivity, a broken tooth or a sore that doesn’t heal.",
            ])),
        ],
        steps_title="What to Expect at Your Checkup",
        steps=[
            ("Health history", "We review your medical history, medications and any concerns you have."),
            ("Cleaning", "Your hygienist cleans and polishes your teeth and checks your gums."),
            ("X-rays as needed", "We take radiographs when they’re due based on your needs."),
            ("Exam &amp; screening", "Dr. Holcombe examines your teeth and gums and performs an oral cancer screening."),
            ("Your plan", "We explain what we found, answer your questions and recommend your next visit."),
        ],
        faqs=[
            ("How often should I have my teeth cleaned?", "Many patients do well with a checkup and cleaning every six months. If you have a history of gum disease or other risk factors, Dr. Holcombe may recommend more frequent visits. Your schedule is based on your own needs."),
            ("Are dental X-rays safe?", "Dental X-rays use a very low dose of radiation. We take them only when they will provide information needed for your care, and how often depends on your individual risk for problems."),
            ("Who should get dental sealants?", "Sealants are most commonly placed on the permanent back teeth of children and teens, whose deep grooves are prone to cavities. Some adults benefit too. We’ll let you know if sealants are a good fit."),
            ("What happens during an oral cancer screening?", "Dr. Holcombe looks at and gently feels the tissues of your mouth, tongue and throat for lumps, patches or sores. It takes only a few minutes and is part of your routine exam."),
            ("Do you see children?", "Yes. We would like to take care of your entire family, from children to senior adults."),
        ],
        related=["childrens-dentistry", "periodontics", "crowns-bridges"],
        procedure=dict(type="DiagnosticProcedure", body="Teeth and gums",
                       how="Routine dental examination, professional cleaning, radiographs as needed, oral cancer screening, sealants and fluoride application."),
    ),

    # ------------------------------------------------------------------
    "cosmetic-dentistry": dict(
        h1="Cosmetic Dentistry in Asheville, NC",
        title="Cosmetic Dentist in Asheville, NC | Whitening, Veneers, Crowns",
        meta="Teeth whitening, tooth-colored fillings, veneers, crowns and bridges from Dr. Zachary Holcombe in Asheville, NC. Smile with confidence. Call 828-684-3839.",
        lead=[
            "We understand the importance of being able to smile with confidence. A great smile is one of the best ways to make a positive impression, which is why we offer a wide variety of treatments to help give you the smile you want.",
            "Every cosmetic plan starts with a conversation about your goals and an exam to make sure your teeth and gums are healthy enough to support the result you want.",
        ],
        sections=[
            ("Cosmetic Treatments We Offer", h3_list([
                ("Teeth Whitening", "Whitening helps you have a brighter, whiter smile. Teeth naturally change color over time and also become discolored from coffee, tea, red wine and smoking. Whitening is not for every situation, but we would love to discuss whether it could benefit you."),
                ("Tooth-Colored Fillings", "We offer resin composite fillings that blend in with your natural tooth, so repairs from cavities or small chips are hard to notice."),
                ("Veneers", "Veneers cover the front surface of a tooth to change its shape or color. They can improve teeth that are stained, chipped, worn or slightly uneven."),
                ("Crowns and Bridges", f"Natural-looking crowns restore cracked, worn or discolored teeth, and bridges fill the gap left by a missing tooth. Learn more about {link('crowns-bridges', 'dental crowns and bridges')}."),
            ])),
            ("Is Cosmetic Dentistry Right for You?",
             "<p>You may benefit from a cosmetic consultation if you have:</p>" + bullets([
                 "Stained or yellowed teeth",
                 "Chipped, cracked or worn teeth",
                 "Teeth that are uneven or oddly shaped",
                 "A gap from a missing tooth",
                 "Older fillings that are dark or easy to see",
             ]) +
             f"<p>If we find decay or gum disease during your exam, we’ll treat that first through {link('preventive-care', 'preventive care')} or {link('periodontics', 'gum treatment')} so your cosmetic work lasts.</p>"),
            ("Caring for Your Results", bullets([
                "Brush twice daily and clean between your teeth every day.",
                "After whitening, limit coffee, tea, red wine and tobacco to keep your shade longer.",
                "Avoid chewing ice, pens or other hard objects that can chip teeth and restorations.",
                "Keep up with regular checkups so we can monitor crowns, bridges, veneers and fillings.",
            ])),
        ],
        steps_title="Your Cosmetic Consultation",
        steps=[
            ("Talk about your goals", "Tell us what you’d like to change about your smile."),
            ("Exam", "Dr. Holcombe checks the health of your teeth and gums."),
            ("Review options", "We explain which treatments fit your goals, along with the pros and cons of each."),
            ("Your plan", "Together we choose a plan, and you decide what’s right for you."),
        ],
        faqs=[
            ("Is professional teeth whitening safe?", "Whitening under a dentist’s guidance is a common and generally safe way to brighten natural teeth. Some people have temporary sensitivity. We’ll check that whitening is appropriate for your teeth before you start."),
            ("Will whitening change the color of my crowns or fillings?", "No. Whitening works on natural tooth enamel and does not change the color of crowns, veneers or fillings. If you have visible restorations, we’ll talk through how to keep everything matching."),
            ("What’s the difference between a veneer and a crown?", "A veneer covers only the front surface of a tooth and is mainly used to improve appearance. A crown covers the entire tooth and is used when a tooth needs extra strength and protection as well."),
            ("Can you replace my old silver fillings with tooth-colored ones?", "Often, yes. Dr. Holcombe will check your existing fillings and let you know whether replacing them with tooth-colored composite makes sense."),
            ("How long do crowns and bridges last?", "With good home care and regular checkups, crowns and bridges can last many years. How long depends on your bite, habits and oral hygiene."),
        ],
        related=["crowns-bridges", "dental-implants", "preventive-care"],
        procedure=dict(type="TherapeuticProcedure", body="Teeth",
                       how="Teeth whitening, tooth-colored composite fillings, veneers, crowns and bridges."),
    ),

    # ------------------------------------------------------------------
    "dental-implants": dict(
        h1="Dental Implant Restorations in Asheville, NC",
        title="Dental Implant Restorations in Asheville, NC | Dr. Holcombe",
        meta="Implant crowns, bridges, snap-in dentures and fixed hybrids from Dr. Zachary Holcombe in Asheville, NC. Replace missing teeth with confidence.",
        lead=[
            "With dental implants you can rediscover your confidence to eat, speak, laugh and enjoy life. Implants are titanium screws that attach to the bone where you are missing teeth, allowing a natural-looking, tooth-colored restoration to be secured in the space.",
            "Dr. Holcombe provides implant restorations — the custom teeth that attach to your implants, from a single crown to a full arch. The implant post itself is placed by a surgical specialist, and we’ll help coordinate your care from your first consultation to your finished smile.",
        ],
        sections=[
            ("What Is a Dental Implant?",
             "<p>A dental implant has three parts: a titanium post that sits in the jawbone and acts like a tooth root, a connector, and the restoration you see — a crown, bridge or denture. Once the bone has bonded with the post, the implant provides a strong, stable base for your new teeth.</p>"),
            ("Implant Restorations We Offer", h3_list([
                ("Implant Crowns and Bridges", "These are similar to a traditional crown or bridge, except the restoration sits on the implant instead of your natural tooth."),
                ("Implant Attachments for Dentures", f"Implants can be used as attachments for {link('dentures', 'traditional dentures')}, allowing them to “snap” into place. This increases the stability and retention of the denture."),
                ("Fixed Hybrids", "A fixed hybrid replaces all or most of the teeth in an arch. Unlike a denture, you don’t take it out — it is screwed into place on the implants. It is more stable and smaller than a traditional denture, making it a great alternative for patients who struggle with a gag reflex."),
            ])),
            ("Benefits of Dental Implants", bullets([
                "Look, feel and function much like natural teeth",
                "Replace a tooth without reshaping the neighboring teeth, as a traditional bridge requires",
                "Help preserve the jawbone, which tends to shrink where teeth are missing",
                "Let you eat, speak and laugh without worrying about slipping teeth",
                "Can stabilize a loose denture or replace it with a fixed option",
            ])),
            ("Are You a Candidate for Implants?",
             "<p>Most adults who are missing one or more teeth can be evaluated for implants. Good candidates generally have healthy gums and enough jawbone to support the implant. Smoking, uncontrolled diabetes and some medications can affect healing, so we’ll review your health history carefully.</p>"
             f"<p>If you have active gum disease, we’ll treat it first through {link('periodontics', 'periodontal therapy')}. If a failing tooth needs to come out, we can start with an {link('oral-surgery', 'extraction')}.</p>"),
            ("Caring for Your Implants",
             f"<p>Implants can’t get cavities, but the gums and bone around them can become inflamed just like natural teeth. Brush twice a day, clean around the implant daily and keep up with {link('preventive-care', 'regular cleanings and checkups')} so we can monitor the implant and your restoration.</p>"),
        ],
        steps_title="The Dental Implant Process",
        steps=[
            ("Consultation", "Dr. Holcombe examines your mouth, reviews X-rays and discusses your options and timeline."),
            ("Implant placement", "The implant post is placed in the jawbone by a surgical specialist. We’ll help coordinate this step and explain what to expect."),
            ("Healing", "Over the following months, the bone bonds with the implant to create a solid foundation."),
            ("Your new teeth", "Dr. Holcombe designs and attaches your custom crown, bridge, denture attachment or fixed hybrid."),
            ("Ongoing care", "Routine checkups and cleanings help your implant last."),
        ],
        faqs=[
            ("How long do dental implants last?", "With good home care and regular checkups, implants can last for many years. The crown or other restoration on top may eventually need to be replaced due to normal wear."),
            ("Does Dr. Holcombe place the implant?", "Dr. Holcombe focuses on implant restorations — the crowns, bridges and dentures that attach to your implants. The implant post is placed by a surgical specialist, and our office helps coordinate your care so the process is as smooth as possible."),
            ("Should I choose an implant or a bridge?", "Both replace missing teeth. An implant stands on its own and doesn’t require reshaping neighboring teeth, while a traditional bridge is anchored to the teeth on either side. Dr. Holcombe will help you weigh the pros and cons for your situation."),
            ("Can implants help my loose denture?", f"Yes. A few implants can serve as attachments that let your denture snap securely into place, or support a fixed hybrid that stays in. Learn more about our {link('dentures', 'denture options')}."),
            ("Do I need one implant for every missing tooth?", "Not necessarily. Implant bridges and fixed hybrids can replace several teeth using fewer implants."),
        ],
        related=["dentures", "crowns-bridges", "oral-surgery"],
        procedure=dict(type="TherapeuticProcedure", body="Jawbone and teeth",
                       how="After a specialist places a titanium implant in the jawbone and it heals, Dr. Holcombe restores it with a crown, bridge, denture attachment or fixed hybrid."),
    ),

    # ------------------------------------------------------------------
    "dentures": dict(
        h1="Complete &amp; Partial Dentures in Asheville, NC",
        title="Dentures in Asheville, NC | Complete, Partial & Implant Dentures",
        meta="Complete, partial and implant-supported dentures from Dr. Zachary Holcombe in Asheville, NC. Chew, speak and smile with confidence. Call 828-684-3839.",
        lead=[
            "If you have lost several teeth and can’t chew and smile like you once did, we have options to help. We can replace all your teeth with a complete denture or make a partial denture that works with your existing teeth.",
            f"We can also incorporate {link('dental-implants', 'dental implants')} into the denture design to help it stay in place, providing a more secure fit.",
        ],
        sections=[
            ("Denture Options", h3_list([
                ("Complete Dentures", "A full set of replacement teeth for the upper jaw, lower jaw or both, for patients who are missing all of their teeth in an arch."),
                ("Partial Dentures", "A removable appliance that fills the gaps left by missing teeth and attaches to your remaining natural teeth. It also helps keep those teeth from shifting."),
                ("Implant-Retained (Snap-In) Dentures", f"Implants act as anchors so your denture “snaps” into place, improving stability and chewing. <a href=\"dental-implants.html\">Learn about dental implants</a>."),
                ("Fixed Hybrids", "For patients who want teeth that don’t come out, a fixed hybrid screws onto implants and replaces all or most of the teeth in an arch."),
            ])),
            ("Signs Dentures May Help", bullets([
                "You are missing several teeth or all teeth in an arch",
                "Chewing is difficult or painful",
                "Remaining teeth are badly decayed, loose or failing",
                "Your current denture is loose, uncomfortable or worn",
            ])),
            ("Adjusting to &amp; Caring for Your Dentures", bullets([
                "Start with soft foods cut into small pieces, then work back to your usual diet.",
                "Practice speaking and reading aloud — your tongue and cheeks adapt quickly.",
                "Call us if you develop a sore spot; a simple adjustment usually helps.",
                "Clean your denture daily with a denture brush and keep it moist when it’s out of your mouth.",
                "Follow Dr. Holcombe’s instructions about removing your denture at night to let your gums rest.",
                "Keep regular checkups. Your mouth changes over time, and dentures may need relining or replacing.",
            ])),
        ],
        steps_title="Getting Your Dentures",
        steps=[
            ("Exam &amp; planning", "We evaluate your teeth, gums and bone and talk through your options."),
            ("Preparing your mouth", f"If needed, we remove failing teeth and smooth the bone with {link('oral-surgery', 'alveoloplasty')} so your denture fits better."),
            ("Impressions &amp; bite", "We record the shape of your mouth and how your jaws come together."),
            ("Try-in", "You preview the fit, look and bite before the denture is finished."),
            ("Delivery &amp; adjustments", "We fit your new denture and make adjustments as you get used to it."),
        ],
        faqs=[
            ("How long does it take to get used to new dentures?", "Most people need a few weeks to feel comfortable eating and speaking with new dentures. Sore spots are common at first and can usually be fixed with a quick adjustment."),
            ("What is the difference between complete and partial dentures?", "A complete denture replaces all the teeth in an arch. A partial denture replaces some missing teeth and attaches to your remaining natural teeth."),
            ("Should I sleep in my dentures?", "Many patients are advised to remove dentures at night to let the gums rest and to keep the denture clean. Dr. Holcombe will give you instructions for your specific denture."),
            ("Will my dentures need to be replaced?", "Over time the gums and bone under a denture change shape, so dentures may need to be relined or remade to keep a good fit. Regular checkups help us catch this early."),
            ("How can implants make my denture more secure?", f"Implants placed in the jaw can act as attachments that hold your denture firmly in place. See our {link('dental-implants', 'dental implants')} page for details."),
        ],
        related=["dental-implants", "oral-surgery", "preventive-care"],
        procedure=dict(type="TherapeuticProcedure", body="Teeth and jaw",
                       how="Removable complete or partial dentures, optionally retained by dental implants, are made from impressions and bite records and fitted with adjustments."),
    ),

    # ------------------------------------------------------------------
    "oral-surgery": dict(
        h1="Tooth Extractions &amp; Oral Surgery in Asheville, NC",
        title="Tooth Extractions & Oral Surgery in Asheville, NC | Dr. Holcombe",
        meta="Tooth extractions, surgical root tip extractions and alveoloplasty with Dr. Zachary Holcombe in Asheville, NC. Clear aftercare. Call 828-684-3839.",
        lead=[
            "Oral surgery is needed in many situations, such as removing wisdom teeth, preparing the mouth for dentures, or extracting infected and non-restorable teeth.",
            "We offer extractions and alveoloplasty — shaping of the bone after an extraction to help a denture fit better — in a comfortable, friendly setting.",
        ],
        sections=[
            ("Oral Surgery Procedures We Offer", h3_list([
                ("Tooth Extractions", "Removal of a tooth that is badly damaged, infected or can’t be saved."),
                ("Surgical Root Tip Extractions", "Removal of a broken root or root tip that remains in the bone after a tooth has fractured."),
                ("Alveoloplasty", f"Smoothing and reshaping the jawbone after extractions so that {link('dentures', 'dentures')} fit comfortably and securely."),
            ])),
            ("When Is a Tooth Extraction Needed?",
             bullets([
                 "Severe decay or a fracture that can’t be repaired",
                 "Infection that can’t be treated another way",
                 "Advanced gum disease that has loosened the tooth",
                 "Wisdom teeth that are causing problems",
                 "Preparing the mouth for dentures",
             ]) +
             f"<p>Whenever possible, we try to save your natural tooth — for example with a {link('root-canals', 'root canal')} and crown. If an extraction is the best choice, we’ll talk about replacing the tooth with an {link('dental-implants', 'implant')}, a {link('crowns-bridges', 'bridge')} or a {link('dentures', 'denture')}.</p>"
             "<p>Dr. Holcombe will evaluate your wisdom teeth and let you know whether they can be removed in our office or whether a referral to an oral surgeon is the better choice.</p>"),
            ("Recovering After an Extraction", bullets([
                "Bite gently on gauze to help a blood clot form.",
                "Rest for the remainder of the day and keep your head elevated.",
                "For the first few days, avoid straws, smoking and forceful spitting, which can dislodge the clot and cause a painful “dry socket.”",
                "Use an ice pack on the outside of your cheek to reduce swelling.",
                "Eat soft foods and chew on the other side.",
                "Take any medications exactly as directed.",
                "Call us if you have heavy bleeding, increasing pain or swelling, or a fever.",
            ])),
        ],
        steps_title="What to Expect",
        steps=[
            ("Exam &amp; X-rays", "We evaluate the tooth and surrounding bone and explain your options."),
            ("Numbing", "Local anesthetic numbs the area so you feel pressure, not pain."),
            ("Removal", "The tooth or root tip is gently removed, and the bone is smoothed if needed."),
            ("Aftercare", "You go home with gauze and clear written instructions."),
            ("Replacement plan", "We discuss options to replace the tooth if needed."),
        ],
        faqs=[
            ("Does a tooth extraction hurt?", "The area is fully numbed, so you should feel pressure but not sharp pain during the procedure. Some soreness afterward is normal and usually improves over a few days."),
            ("How long does it take to recover from an extraction?", "Most people feel much better within a few days after a simple extraction. Surgical extractions can take a little longer. Following your aftercare instructions helps you heal well."),
            ("What is a dry socket?", "A dry socket happens when the blood clot in the extraction site is dislodged too early, exposing the bone. It can be quite painful. Avoiding straws, smoking and forceful spitting for the first few days lowers the risk. Call us if you think you have one."),
            ("Should I replace a tooth that was extracted?", f"Usually, yes. A gap can let neighboring teeth shift and make chewing harder. Options include {link('dental-implants', 'implants')}, {link('crowns-bridges', 'bridges')} and {link('dentures', 'partial dentures')}."),
            ("What is alveoloplasty?", "Alveoloplasty is the smoothing and reshaping of the jawbone, typically after extractions, so a denture fits better and more comfortably."),
        ],
        related=["dentures", "dental-implants", "root-canals"],
        procedure=dict(type="SurgicalProcedure", body="Teeth and jawbone",
                       how="Teeth or retained root tips are removed under local anesthesia; alveoloplasty reshapes the bone to prepare for dentures."),
    ),

    # ------------------------------------------------------------------
    "periodontics": dict(
        h1="Gum Disease Treatment (Periodontics) in Asheville, NC",
        title="Gum Disease Treatment in Asheville, NC | Periodontics",
        meta="Scaling and root planing, periodontal surgery and gum disease treatment from Dr. Zachary Holcombe in Asheville, NC. Protect your teeth. Call 828-684-3839.",
        lead=[
            "Slow but progressive, periodontal disease swells the gums (gingiva) and destroys the bone that supports your teeth. Once the bone is lost, it does not regenerate. The disease may be generalized, affecting all of your teeth, or localized to a single tooth.",
            "Gum disease affects men and women of all ethnicities, from the teen years through adulthood. In its early stages you may be unaware of it — which is why regular exams matter.",
        ],
        sections=[
            ("Signs of Gum Disease", bullets([
                "Gums that bleed when you brush or floss",
                "Red, swollen or tender gums",
                "Persistent bad breath",
                "Gums pulling away from the teeth",
                "Loose or shifting teeth",
            ])),
            ("What Raises Your Risk?",
             "<p>Dental hygiene habits, medications, smoking, alcohol, diet, general health and heredity can all play a role in how gum disease progresses. Conditions such as diabetes are also associated with gum disease.</p>"),
            ("Periodontal Treatments We Offer", h3_list([
                ("Scaling &amp; Root Planing", "A deep cleaning that removes plaque and calculus from below the gumline and smooths the root surfaces so the gums can heal and reattach."),
                ("Periodontal Surgery", "When deep cleaning isn’t enough, surgical treatment can help reach and clean deeper areas and reduce pockets around the teeth."),
                ("Gingival Medicament Placement", "Medication placed directly into gum pockets to help control bacteria and support healing."),
                ("Gingivoplasty", "Reshaping of the gum tissue to restore healthier contours that are easier to keep clean."),
            ])),
            ("Keeping Your Gums Healthy After Treatment",
             "<p>Gum disease can be controlled, but it needs ongoing care. Many patients need periodontal maintenance cleanings more often than twice a year. At home, brush twice daily, clean between your teeth every day and avoid tobacco.</p>"
             f"<p>Healthy gums are also important if you’re considering {link('dental-implants', 'dental implants')}, since the tissue around implants can become inflamed too.</p>"),
        ],
        steps_title="What to Expect",
        steps=[
            ("Gum measurements", "We gently measure the pockets around each tooth to check for gum disease."),
            ("X-rays", "Radiographs show the level of bone supporting your teeth."),
            ("Treatment plan", "Dr. Holcombe explains the findings and recommends treatment."),
            ("Treatment", "Deep cleaning or other therapy is completed, with the area numbed for comfort."),
            ("Maintenance", "Regular follow-up cleanings help keep the disease under control."),
        ],
        faqs=[
            ("Can gum disease be reversed?", f"Gingivitis, the earliest stage, can often be reversed with professional cleanings and good home care through {link('preventive-care', 'preventive care')}. Periodontitis can be treated and controlled, but bone that has been lost does not grow back — so early treatment matters."),
            ("Is scaling and root planing painful?", "The area is numbed so you stay comfortable during treatment. Your gums may be tender for a few days afterward."),
            ("How often will I need cleanings after treatment?", "Many patients with a history of gum disease need maintenance cleanings more often than twice a year. Dr. Holcombe will recommend a schedule based on how your gums respond."),
            ("Is gum disease linked to other health problems?", "Research has found associations between gum disease and conditions such as diabetes and heart disease. Keeping your gums healthy is part of caring for your overall health."),
            ("Can gum disease cause tooth loss?", f"Yes. As gum disease destroys the supporting bone, teeth can loosen, shift and eventually be lost. If teeth are lost, options include {link('dental-implants', 'implants')} and {link('dentures', 'dentures')}."),
        ],
        related=["preventive-care", "dental-implants", "oral-surgery"],
        procedure=dict(type="TherapeuticProcedure", body="Gums and supporting bone",
                       how="Periodontal charting and radiographs, followed by scaling and root planing, medicament placement, gingivoplasty or periodontal surgery as needed."),
    ),

    # ------------------------------------------------------------------
    "root-canals": dict(
        h1="Root Canal Treatment in Asheville, NC",
        title="Root Canal Treatment in Asheville, NC | Dr. Zachary Holcombe",
        meta="Relieve tooth pain and save your natural tooth with root canal treatment from Dr. Zachary Holcombe in Asheville, NC. Call 828-684-3839.",
        lead=[
            "A root canal is needed when decay or trauma has irreversibly damaged the nerve inside a tooth. The nerve cannot heal itself, so the tooth either needs a root canal or must be extracted.",
            "If it isn’t treated promptly, an extremely painful and dangerous infection called a dental abscess may develop. Root canal treatment removes the infection and lets you keep your natural tooth.",
        ],
        sections=[
            ("Signs You May Need a Root Canal",
             bullets([
                 "A persistent or throbbing toothache",
                 "Sensitivity to hot or cold that lingers",
                 "Pain when biting or chewing",
                 "Swollen or tender gums near a tooth",
                 "A tooth that has darkened in color",
                 "A small bump or pimple on the gum",
             ]) +
             "<p>Sometimes there are no symptoms at all, and the problem is found on an X-ray during a routine checkup.</p>"),
            ("Saving Your Natural Tooth",
             f"<p>Keeping your own tooth is usually the best option when it can be saved. If a tooth can’t be saved, we’ll discuss an {link('oral-surgery', 'extraction')} and replacement options such as a {link('dental-implants', 'dental implant')}.</p>"),
            ("After Your Root Canal", bullets([
                "Some tenderness for a few days is normal.",
                "Avoid chewing hard foods on the tooth until it has its final restoration.",
                "Take any medications as directed.",
                "Call us if you notice swelling or worsening pain.",
                "Keep brushing, flossing and visiting us for regular checkups.",
            ])),
        ],
        steps_title="The Root Canal Procedure",
        steps=[
            ("Exam &amp; X-rays", "We confirm the diagnosis and explain your options."),
            ("Numbing", "Local anesthetic keeps you comfortable."),
            ("Cleaning the canal", "The damaged and infected nerve tissue is removed and the canal is disinfected."),
            ("Sealing", "The canal is filled with a sterile material to seal it from bacteria."),
            ("Protecting the tooth", f"For back teeth, we normally recommend a {link('crowns-bridges', 'crown')} to strengthen and protect the tooth."),
        ],
        faqs=[
            ("Is a root canal painful?", "Root canal treatment is done with local anesthetic, and its purpose is to relieve the pain caused by an infected or damaged nerve. Most patients feel some tenderness for a few days afterward."),
            ("Is it better to have a root canal or pull the tooth?", f"When a tooth can be saved, keeping it is usually best for chewing and for preventing neighboring teeth from shifting. If extraction is the better choice, we’ll discuss {link('dental-implants', 'implants')}, {link('crowns-bridges', 'bridges')} and {link('dentures', 'partial dentures')} to replace it."),
            ("Will I need a crown after a root canal?", "For back teeth, we normally recommend a crown, because a tooth that has had a root canal can become brittle and is more likely to crack."),
            ("What happens if I wait?", "The infection won’t heal on its own. Waiting can lead to a dental abscess, more pain and a greater chance of losing the tooth."),
            ("How long will a tooth with a root canal last?", "With a proper final restoration, good home care and regular checkups, a tooth that has had a root canal can last for many years."),
        ],
        related=["crowns-bridges", "emergency-dentistry", "oral-surgery"],
        procedure=dict(type="TherapeuticProcedure", body="Tooth pulp and root canal",
                       how="Under local anesthesia, damaged or infected nerve tissue is removed, the canal is disinfected and sealed with a sterile filling, and the tooth is usually protected with a crown."),
    ),
}


# Services added from the practice's onboarding form (October 2026).
SERVICE_CONTENT.update({
    # ------------------------------------------------------------------
    "crowns-bridges": dict(
        h1="Dental Crowns, Bridges &amp; Fillings in Asheville, NC",
        title="Dental Crowns & Bridges in Asheville, NC | Dr. Holcombe",
        meta="Natural-looking dental crowns, bridges and tooth-colored fillings from Dr. Zachary Holcombe in Asheville, NC. We file all insurance. Call 828-684-3839.",
        lead=[
            "When a tooth is cracked, worn, badly decayed or missing, restorative dentistry brings back its strength, function and appearance. Dr. Holcombe provides crowns, bridges and tooth-colored fillings designed to blend in with your natural smile.",
            "Because you see the same dentist at every visit, Dr. Holcombe gets to know your teeth over time — so he can catch small problems early and recommend the simplest repair that will last.",
        ],
        sections=[
            ("Restorative Treatments We Offer", h3_list([
                ("Dental Crowns", f"A crown is a custom cap that covers the entire visible part of a tooth. It protects a cracked, weakened or heavily filled tooth, restores its shape and improves its appearance. Crowns are also used to protect a tooth after a {link('root-canals', 'root canal')} and to restore {link('dental-implants', 'dental implants')}."),
                ("Dental Bridges", "A bridge replaces one or more missing teeth by anchoring a replacement tooth to the teeth on each side of the gap. It restores your bite, helps you chew comfortably and keeps neighboring teeth from drifting."),
                ("Tooth-Colored Fillings", "Resin composite fillings repair cavities and small chips while matching the natural color of your tooth, so they’re hard to notice."),
            ])),
            ("When Do You Need a Crown?",
             bullets([
                 "A large cavity that is too big for a filling",
                 "A cracked, broken or badly worn tooth",
                 "A tooth that has had a root canal, especially a back tooth",
                 "A large, old filling that is breaking down",
                 "A discolored or misshapen tooth you’d like to improve",
                 "Restoring a dental implant",
             ]) +
             f"<p>If a tooth is missing, a bridge, an {link('dental-implants', 'implant restoration')} or a {link('dentures', 'partial denture')} can fill the space. Dr. Holcombe will explain the pros and cons of each.</p>"),
            ("Caring for Crowns and Bridges", bullets([
                "Brush twice a day and clean between your teeth daily — including under a bridge with floss threaders or a water flosser.",
                "Avoid chewing ice, hard candy and other hard objects.",
                f"If you grind or clench your teeth, ask about a {link('tmj-night-guards', 'custom night guard')} to protect your restorations.",
                f"Keep up with {link('preventive-care', 'regular checkups and cleanings')} so we can check the fit and the health of the tooth underneath.",
            ])),
        ],
        steps_title="Getting a Dental Crown",
        steps=[
            ("Exam &amp; X-rays", "Dr. Holcombe evaluates the tooth and explains your options."),
            ("Preparing the tooth", "The tooth is numbed and gently shaped so the crown fits securely."),
            ("Impressions &amp; temporary", "We record the shape of your tooth and protect it with a temporary crown while your custom crown is made."),
            ("Final crown", "Your permanent crown is checked for fit, bite and color, then cemented in place."),
        ],
        faqs=[
            ("How long does a dental crown last?", "With good home care and regular checkups, a crown can last many years. How long depends on your bite, habits such as grinding, and how well the tooth and gums are cared for."),
            ("Does getting a crown hurt?", "The tooth is numbed before it’s prepared, so most patients feel pressure rather than pain. It’s normal for the tooth to feel a little sensitive for a few days afterward."),
            ("Should I get a filling or a crown?", "Small and medium cavities can usually be repaired with a filling. When a large part of the tooth is damaged or the tooth is cracked, a crown protects it better and helps prevent it from breaking."),
            ("How do I care for a temporary crown?", "Chew on the other side when you can, avoid sticky and hard foods, and slide floss out to the side rather than pulling it up. Call us if your temporary comes loose."),
            ("Will insurance cover my crown?", f"Many dental plans cover part of the cost of crowns and bridges. We file all insurance for you, and we offer financing through CareCredit and Cherry. See our {link('new-patients', 'insurance and financing information')}."),
        ],
        related=["root-canals", "dental-implants", "cosmetic-dentistry"],
        procedure=dict(type="TherapeuticProcedure", body="Teeth",
                       how="The tooth is numbed and shaped, impressions are taken, a temporary crown is placed, and a custom crown or bridge is cemented at a follow-up visit. Cavities are repaired with tooth-colored composite fillings."),
    ),

    # ------------------------------------------------------------------
    "emergency-dentistry": dict(
        h1="Emergency Dentist in Asheville, NC",
        title="Emergency Dentist in Asheville, NC | Dr. Zachary Holcombe",
        meta="Toothache, broken tooth or lost crown? Call Dr. Zachary Holcombe in Asheville, NC at 828-684-3839. We’ll see you as quickly as possible.",
        lead=[
            "A toothache, a broken tooth or a lost crown can’t always wait for your next checkup. If you have a dental emergency, call our office at 828-684-3839 and we’ll do our best to see you as quickly as possible.",
            "We welcome both current and new patients with urgent dental needs. When you call, let us know what happened and how you’re feeling so we can help you right away.",
        ],
        sections=[
            ("Common Dental Emergencies We Treat", bullets([
                "Severe or throbbing toothache",
                "Chipped, cracked or broken tooth",
                "Knocked-out or loosened tooth",
                "Lost filling or crown",
                "Swelling or a painful bump on the gum",
                "Broken denture",
                "Injury to the teeth or mouth",
            ])),
            ("What to Do Until You Can See Us", h3_list([
                ("Toothache", "Rinse with warm water and gently floss to remove anything caught between your teeth. A cold compress on the outside of your cheek can ease discomfort. Don’t put aspirin directly on your gums."),
                ("Chipped or Broken Tooth", "Save any pieces, rinse your mouth with warm water and apply a cold compress to reduce swelling. Call us right away."),
                ("Knocked-Out Tooth", "Pick the tooth up by the crown (the part you chew with), not the root. If it’s dirty, rinse it briefly without scrubbing. If you can, gently place it back in its socket; otherwise keep it in milk. Call us immediately — the sooner it’s treated, the better the chance of saving it."),
                ("Lost Filling or Crown", "Keep the crown if you have it and bring it with you. Avoid chewing on that side until we can see you."),
                ("Swelling or Infection", f"Swelling can be a sign of an infection that needs prompt treatment, often with a {link('root-canals', 'root canal')} or an {link('oral-surgery', 'extraction')}. Call us as soon as possible."),
            ])),
            ("When to Go to the Emergency Room",
             "<p>Go to the nearest emergency room or call 911 if you have swelling that affects your breathing or swallowing, bleeding that won’t stop, a possible broken jaw, or a serious injury to your head or face. If our office is closed and you have severe swelling or a fever, don’t wait — seek emergency medical care.</p>"),
            ("Preventing Dental Emergencies", bullets([
                f"Keep up with {link('preventive-care', 'regular checkups')} so small problems are found before they become painful.",
                f"Wear a mouthguard for sports, and ask about a {link('tmj-night-guards', 'night guard')} if you grind your teeth.",
                "Don’t chew ice, hard candy or pens, or use your teeth to open packages.",
                f"Fix cracked teeth and worn fillings early — a {link('crowns-bridges', 'crown')} can protect a weak tooth before it breaks.",
            ])),
        ],
        steps_title="What Happens When You Call",
        steps=[
            ("Call us", "Call 828-684-3839 and tell us what happened."),
            ("Get advice", "We’ll let you know what to do right away and when we can see you."),
            ("Exam &amp; X-rays", "Dr. Holcombe finds the cause of the problem."),
            ("Relief", "We relieve your pain and treat the problem, or stabilize it and plan the next step."),
        ],
        faqs=[
            ("Do you see emergency patients who aren’t current patients?", "Yes. New patients with urgent dental problems are welcome. Call our office and we’ll do our best to see you as quickly as possible."),
            ("What are your hours for emergencies?", "Our office is open Monday through Thursday, 8:00am to 5:00pm. Call as early in the day as you can. If we’re closed and you have severe swelling, trouble breathing or swallowing, or uncontrolled bleeding, go to the nearest emergency room."),
            ("Is a toothache an emergency?", "A toothache that is severe, lasts more than a day or two, or comes with swelling or fever should be checked as soon as possible. It can be a sign of infection."),
            ("What should I do with a knocked-out tooth?", "Handle it by the crown, not the root, rinse it briefly if it’s dirty, and try to place it back in the socket or keep it in milk. Call us right away — time matters."),
            ("My crown came off. Is that an emergency?", f"It’s not usually dangerous, but the tooth underneath can be sensitive and may break. Keep the crown and call us so we can recement or replace it. Learn more about {link('crowns-bridges', 'crowns')}."),
        ],
        related=["root-canals", "oral-surgery", "crowns-bridges"],
        procedure=dict(type="TherapeuticProcedure", body="Teeth and mouth",
                       how="Urgent evaluation with an exam and X-rays, followed by treatment to relieve pain and address the cause, such as recementing a crown, repairing a broken tooth, root canal treatment or extraction."),
    ),

    # ------------------------------------------------------------------
    "tmj-night-guards": dict(
        h1="TMJ Treatment &amp; Night Guards in Asheville, NC",
        title="TMJ Treatment & Night Guards in Asheville, NC | Dr. Holcombe",
        meta="Jaw pain, headaches or teeth grinding? Dr. Zachary Holcombe offers TMJ treatment and custom night guards in Asheville, NC. Call 828-684-3839.",
        lead=[
            "Jaw pain, morning headaches and worn or chipped teeth are often signs of clenching or grinding (bruxism) or a problem with the temporomandibular joint (TMJ) — the joint that connects your jaw to your skull.",
            "Dr. Holcombe can evaluate your symptoms and recommend conservative treatment, including a custom-fitted night guard that protects your teeth and helps ease the strain on your jaw.",
        ],
        sections=[
            ("Signs of TMJ Problems or Teeth Grinding", bullets([
                "Jaw pain, soreness or tiredness, especially in the morning",
                "Headaches or earaches without another clear cause",
                "Clicking, popping or grating sounds when you open your mouth",
                "Difficulty opening your mouth fully, or a jaw that feels stuck",
                "Teeth that look flat, worn, chipped or cracked",
                "Sensitive teeth or broken fillings",
                "A partner who hears you grinding at night",
            ])),
            ("TMJ &amp; Grinding Treatments We Offer", h3_list([
                ("Custom Night Guards", "A night guard is a thin, comfortable appliance made from impressions of your teeth. Worn while you sleep, it cushions your teeth from grinding and clenching forces and helps protect your jaw muscles and joints."),
                ("TMJ Evaluation", "Dr. Holcombe examines your jaw joints, muscles and bite and talks with you about your symptoms and habits to find the most likely cause."),
                ("Conservative TMJ Treatment", "Many TMJ symptoms improve with simple, non-surgical care — such as a custom oral appliance, adjustments to your bite where needed, and changes to daily habits."),
                ("Repairing Worn Teeth", f"Teeth damaged by years of grinding can be rebuilt with {link('crowns-bridges', 'crowns or fillings')} once the grinding is under control."),
            ])),
            ("Easing Jaw Pain at Home", bullets([
                "Eat softer foods and cut food into small pieces while your jaw is sore.",
                "Avoid chewing gum and very chewy or hard foods.",
                "Use a warm compress or ice pack on the sore side, whichever feels better.",
                "Notice daytime clenching and remind yourself: lips together, teeth apart.",
                "Wear your night guard every night and bring it to your checkups.",
            ])),
        ],
        steps_title="Getting a Custom Night Guard",
        steps=[
            ("Evaluation", "Dr. Holcombe checks your teeth, jaw and bite and talks about your symptoms."),
            ("Impressions", "We take impressions of your teeth for a precise, comfortable fit."),
            ("Fitting", "We fit your night guard and make any adjustments it needs."),
            ("Follow-up", "We check your night guard, your teeth and your symptoms at future visits."),
        ],
        faqs=[
            ("Is a custom night guard better than a store-bought one?", "A custom night guard is made from impressions of your teeth, so it fits more precisely, tends to be more comfortable and stays in place better than a boil-and-bite guard. A better fit makes it easier to wear every night."),
            ("What causes teeth grinding?", "Grinding and clenching can be linked to stress, sleep habits, an uneven bite and other factors. Many people don’t know they do it until a dentist notices wear on their teeth or a partner hears it at night."),
            ("Can TMJ problems go away on their own?", "Some jaw pain improves with rest and simple self-care. If symptoms last more than a couple of weeks, keep coming back, or make it hard to eat or open your mouth, schedule an evaluation."),
            ("How do I clean my night guard?", "Rinse it after each use, brush it gently with a soft toothbrush and cool water, let it dry and keep it in its case. Avoid hot water, which can warp it."),
            ("Will a night guard protect my crowns and fillings?", f"Yes. A night guard helps protect natural teeth as well as {link('crowns-bridges', 'crowns, bridges and fillings')} from the heavy forces of grinding."),
        ],
        related=["crowns-bridges", "preventive-care", "emergency-dentistry"],
        procedure=dict(type="TherapeuticProcedure", body="Temporomandibular joint, jaw muscles and teeth",
                       how="Evaluation of the jaw joints, muscles and bite, followed by conservative treatment such as a custom-fitted night guard made from impressions of the teeth."),
    ),

    # ------------------------------------------------------------------
    "childrens-dentistry": dict(
        h1="Children’s Dentistry in Asheville, NC",
        title="Children’s Dentist in Asheville, NC | Family Dentistry",
        meta="Gentle checkups, cleanings, fluoride and sealants for kids at our family dental practice in Asheville, NC. The whole family can see Dr. Holcombe.",
        lead=[
            "Healthy smiles start early. As a family practice, we love caring for children and helping them build good habits — and a comfortable relationship with the dentist — that last a lifetime.",
            "Parents and kids can see the same dentist, which makes scheduling easier and helps your child feel at home in our office.",
        ],
        sections=[
            ("Dental Care for Kids", h3_list([
                ("Checkups and Cleanings", f"Gentle exams and cleanings help keep your child’s teeth healthy and let us spot problems early. Learn more about {link('preventive-care', 'preventive care')}."),
                ("Fluoride Treatments", "Professional fluoride strengthens enamel and helps protect growing teeth from cavities."),
                ("Dental Sealants", "Thin, tooth-colored coatings on the chewing surfaces of back teeth help keep food and bacteria out of deep grooves where cavities often start."),
                ("Tooth-Colored Fillings", f"If a cavity does develop, we repair it with {link('crowns-bridges', 'tooth-colored fillings')} that blend in naturally."),
                ("Guidance for Parents", "We’ll share tips on brushing, flossing, snacks and habits like thumb-sucking, tailored to your child’s age."),
            ])),
            ("When Should My Child First See the Dentist?",
             "<p>The American Dental Association recommends a child’s first dental visit within six months of the first tooth appearing, and no later than the first birthday. Early visits are short and relaxed — they help your child get used to the dental office and give us a chance to answer your questions.</p>"),
            ("Healthy Habits at Home", bullets([
                "Brush twice a day with a fluoride toothpaste — a smear the size of a grain of rice for children under 3, and a pea-sized amount for ages 3 to 6.",
                "Help your child brush until they can do it well on their own.",
                "Start flossing once teeth touch each other.",
                "Limit sugary drinks and snacks, and avoid putting a baby to bed with a bottle of milk or juice.",
                "Have kids wear a mouthguard for sports.",
            ])),
        ],
        steps_title="Your Child’s Visit",
        steps=[
            ("A warm welcome", "We introduce your child to our team and the dental chair at their own pace."),
            ("Gentle cleaning", "We clean and polish your child’s teeth."),
            ("Exam", "Dr. Holcombe checks teeth, gums and development, with X-rays when needed."),
            ("Protection", "Fluoride or sealants may be recommended to prevent cavities."),
            ("Tips for home", "We share age-appropriate advice and answer your questions."),
        ],
        faqs=[
            ("At what age should my child see a dentist?", "By their first birthday, or within six months of the first tooth coming in. Early visits help prevent problems and make dental visits feel normal."),
            ("Are baby teeth really important?", "Yes. Baby teeth help children chew, speak and smile, and they hold space for the permanent teeth. Cavities in baby teeth can cause pain and infection."),
            ("Can my whole family see Dr. Holcombe?", "Yes. We care for patients of all ages — from young children to senior adults — so the whole family can come to one office."),
            ("Are dental X-rays safe for children?", "Dental X-rays use a very low dose of radiation, and we take them only when needed for your child’s care."),
            ("How can I help my child feel comfortable at the dentist?", "Keep your words positive and simple, avoid sharing your own dental worries, and schedule visits at a time of day when your child is usually rested. Our team will take it slow."),
        ],
        related=["preventive-care", "emergency-dentistry", "crowns-bridges"],
        procedure=dict(type="DiagnosticProcedure", body="Teeth and gums",
                       how="Age-appropriate exams, cleanings, fluoride treatments, sealants and tooth-colored fillings for children."),
    ),
})
