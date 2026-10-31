# -*- coding: utf-8 -*-
"""Genera docs/RICHIESTE_ASSET/personaggi_v1.md e oggetti_cap01.md da dati strutturati."""
import os
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STD_CHR=("Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.")
STD_ANI=("Full-body photograph, front view, straight-on at the animal's eye level, the animal standing still and symmetric, all four paws visible, tail visible, neutral pose. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no depth of field, realistic photographic style, detailed fur. No text, no props. 1:1 square.")
STD_PRP=("Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.")
EDIT_CHR={"lato sinistro":"Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.",
 "lato destro":"Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.",
 "retro":"Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.",
 "3/4":"Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else."}
EDIT_PRP={"3/4":"Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.",
 "retro":"Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.",
 "lato":"Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else."}
TIERS={"1,5 M":("Hitem3D multi-vista: risoluzione 1536, numero di facce 1.500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.500.000, texture PBR sì, quad no, GLB."),
 "1,0 M":("Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB."),
 "0,5 M":("Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB.")}
def chk_chr(h): return [f"una sola persona, figura intera, piedi visibili", "braccia staccate dal corpo (A-pose), mani aperte e vuote", "sfondo grigio uniforme, nessuna ombra forte", "nessun logo o scritta sui vestiti", f"proporzioni credibili per l'età (altezza in gioco {h} cm)", "le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura"]
CHR=[
# id, nome, uso, fase, fascia, motivo, descrizione EN, altezza cm, budget, extra
("REQ-CHR-001","Vera Russo — abiti del cap. 1","riflessi (finestrini, specchi), foto di famiglia, mani in prima persona (si ricavano dal modello); cap. 1","Fase 3","1,0 M","non si vede quasi mai da vicino in viso, ma le mani e gli avambracci sono sempre in campo: servono buon dettaglio a distanza di conversazione",
 "A 12-year-old Italian-Russian girl, slim, 152 cm tall, light-brown hair to the shoulder blades in a low ponytail with a blue elastic and loose strands, grey eyes, light olive skin with a few freckles, short nails. She wears a white T-shirt with thin blue stripes, short denim overalls, white sneakers, a red-and-blue string bracelet on her left wrist.",152,"40.000 tri (LOD 15.000 / 5.000); braccia in prima persona come mesh separata da 12.000 tri",""),
("REQ-CHR-002","Vera Russo — pigiama (notte)","scene notturne dei capp. 2–3 (riflessi, piedi nudi, mani)","Fase 4","1,0 M","stesso motivo della scheda 001",
 "The same 12-year-old girl (light-brown hair in a loose low ponytail, grey eyes), wearing light-blue cotton pyjamas with a small star print, long trousers, barefoot, red-and-blue string bracelet.",152,"40.000 tri","Allegare a Nano Banana l'immagine frontale di REQ-CHR-001 come riferimento del viso e scrivere prima del prompt: «Same girl as the reference image, same face and hair.»"),
("REQ-CHR-003","Vera Russo — scuola e casa (settembre)","riflessi e foto nei capp. 3 e mondo libero","Fase 4","1,0 M","stesso motivo",
 "The same 12-year-old girl, wearing an open navy-blue zip hoodie over a plain white T-shirt, blue jeans, white sneakers, red-and-blue string bracelet.",152,"40.000 tri","Allegare REQ-CHR-001 come riferimento del viso (come sopra)."),
("REQ-CHR-010","Babuška Galina — cappotto verde (cap. 1)","cap. 1 (arrivo, abbraccio, primo piano lento sugli occhi SCN-01-13), cap. 2 (arrivo)","Fase 1 (prova pipeline) e Fase 3","1,5 M","primo piano lento sugli occhi e sulle rughe: servono pori, pieghe intorno agli occhi e trama della lana",
 "A small 74-year-old Russian grandmother from Saint Petersburg, 149 cm, slightly rounded shoulders, round face with high cheekbones, pale skin with fine wrinkles, very light grey eyes with many wrinkles around them, silver hair in a low bun. She wears a knee-length dark bottle-green wool coat, 1980s cut with large buttons, buttoned, a cream wool headscarf with small red and blue flowers tied under the chin, a grey skirt below the knee, skin-colour tights, low black shoes. Strong, knotty hands, a worn rose-gold wedding band on the right ring finger.",149,"40.000 tri; testa 4.096 px su Ultra",""),
("REQ-CHR-011","Babuška Galina — vestito di casa e grembiule","capp. 2–3 a cena e in casa; mondo libero","Fase 4","1,0 M","conversazione a tavola, nessun primo piano estremo",
 "The same grandmother (same face, silver bun, no headscarf), wearing a simple cotton dress with tiny dark-blue flowers, sleeves to the elbow, and a faded linen apron, beige slippers.",149,"40.000 tri","Allegare REQ-CHR-010 come riferimento del viso."),
("REQ-CHR-012","Babuška Galina — camicia da notte (cap. 2)","cap. 2, il rito (scalza, con la borsa a fiori in mano: la borsa è un oggetto separato)","Fase 4","1,0 M","scena guidata a 3–4 m, luce del lampione",
 "The same grandmother (same face), silver hair loose in a thin braid over one shoulder, wearing a long white cotton nightgown with long sleeves, barefoot.",149,"40.000 tri","Allegare REQ-CHR-010 come riferimento del viso."),
("REQ-CHR-020","Irina Russo — cap. 1","cap. 1 (cartello, corre incontro alla madre), cap. 2","Fase 3","1,0 M","conversazione",
 "A 41-year-old Russian woman living in Sicily, 168 cm, slender, oval face with high cheekbones, blue-grey eyes, ash-blond shoulder-length hair held back with a claw clip, no make-up except mascara. She wears a white linen shirt with rolled sleeves, navy straight trousers, flat sandals, a thin watch, a small crossbody bag.",168,"40.000 tri","La borsa a tracolla resta sul modello (non è un oggetto di scena)."),
("REQ-CHR-021","Irina Russo — casa (sera)","capp. 2–3, mondo libero","Fase 4","1,0 M","conversazione",
 "The same woman (same face and hair), wearing a soft grey knit sweater, dark leggings, home slippers.",168,"40.000 tri","Allegare REQ-CHR-020 come riferimento."),
("REQ-CHR-030","Salvo Russo — cap. 1","cap. 1 (cammina nervoso, guida), cap. 2","Fase 3","1,0 M","conversazione",
 "A 44-year-old Sicilian man, 178 cm, sturdy with a slight belly, dark brown eyes, short curly black hair with grey temples, two-day stubble, tanned. He wears a dark-blue polo shirt, jeans, brown loafers, a steel watch.",178,"40.000 tri",""),
("REQ-CHR-031","Salvo Russo — al bar","cap. 3 (bar), mondo libero (bar)","Fase 4","1,0 M","conversazione e bancone",
 "The same man (same face), wearing a white shirt with sleeves rolled up and a long black waist apron without any writing, black trousers, black shoes.",178,"40.000 tri","Allegare REQ-CHR-030."),
("REQ-CHR-040","Giulia Russo — cap. 1","cap. 1 (colonna, telefono), cap. 2","Fase 3","1,0 M","conversazione; il telefono è un oggetto separato (REQ-PRP-007)",
 "A 16-year-old Sicilian girl, 165 cm, slim, brown eyes, long straight dark hair with a centre parting, thin eyeliner, chipped navy nail polish. She wears an oversized grey hoodie, denim shorts, black high-top sneakers, large black over-ear headphones around her neck.",165,"40.000 tri",""),
("REQ-CHR-041","Giulia Russo — casa","capp. 2–3, mondo libero","Fase 4","1,0 M","conversazione",
 "The same teenage girl (same face and hair), wearing a loose black T-shirt and grey sweatpants, white socks.",165,"40.000 tri","Allegare REQ-CHR-040."),
("REQ-CHR-050","Mattia Russo — cap. 1","cap. 1 (saltella, il signore, il parcheggio), cap. 2","Fase 3","1,0 M","conversazione con camera abbassata; personaggio molto animato",
 "An imaginary 6-year-old boy, 116 cm, skinny with scraped knees, grey eyes, messy light-brown hair with a cowlick, one missing front baby tooth (mouth closed so it is not visible). He wears a green T-shirt with a printed cartoon dinosaur (generic, no brand), shorts, velcro sandals, a crooked blue baseball cap. A small backpack is NOT included (separate object).",116,"40.000 tri",""),
("REQ-CHR-051","Mattia Russo — pigiama","capp. 2–3 (dorme), 9, 14","Fase 4","1,0 M","conversazione",
 "The same boy (same face), no cap, wearing striped cotton pyjamas (white and light blue), barefoot.",116,"40.000 tri","Allegare REQ-CHR-050."),
("REQ-CHR-060","Nonna Concetta — giorno","cap. 2 (arancini al portone), cap. 4–5, mondo libero","Fase 4","1,0 M","conversazione",
 "A 71-year-old Sicilian grandmother, 146 cm plus teased bouffant hair (total 150 cm), round and energetic, lively black eyes, coppery-brown dyed teased hair, coral earrings, a few rings. She wears a dark floral dress below the knee with a navy cardigan, low-heeled black shoes.",150,"40.000 tri",""),
("REQ-CHR-070","Fomà, il domovoj","capp. 2–3 (e tutto il gioco); cap. 1 solo occhi","Fase 1 (prova pelo) e Fase 4","1,5 M","creatura eroe vista da vicino, pelo e barba con dettaglio fine da trasferire in normal map e mappe del pelo",
 "A tiny ancient Russian house spirit (domovoi), only 32 cm tall like a 1.5-litre water bottle, an old man with an almost cat-like face: big round red shiny nose, furry cheeks, small shiny jet-black eyes, wild messy grey hair, a very long grey beard reaching the floor and trailing behind like a train, the whole body covered in soft grey tabby fur like an old cat, small furry hands with long yellowish nails, bare furry feet. He wears a rough brick-red linen peasant shirt with white embroidery at the collar, belted with a simple rope. Photographed as a realistic creature (not a cartoon), standing upright in A-pose.",32,"40.000 tri + gusci di pelo; barba a ciocche su 8 ossa","Il prompt dice «32 cm»; nell'immagine non c'è nulla per la scala, va bene. Se la barba copre i piedi nella vista frontale, chiedere in modifica: «Same character, beard tucked to one side so both feet are visible»."),
("REQ-CHR-080","Donna Rosalia (Donne di Fora)","cap. 3 (e capp. 4, 8, 12, 13, notti libere)","Fase 4","1,0 M","conversazione notturna; il vestito sarà reso semitrasparente e la gonna sotto il ginocchio diventa nebbia",
 "A tall elegant Sicilian noblewoman of indeterminate age (looks 45), 178 cm, beautiful severe face like the statues of saints in Sicilian processions, black shiny eyes, dark hair gathered high with a tortoiseshell comb, thin gold bracelets on both wrists. She wears a long wine-red (#6E2433) late-19th-century gown with a fitted bodice and narrow waist. Arms in A-pose, hands empty (the lace fan is a separate object).",178,"40.000 tri","Il ventaglio è REQ-PRP-020 (scheda futura nella Fase 4)."),
("REQ-CHR-081","Donna Nina (Donne di Fora)","cap. 3 e seguenti","Fase 4","1,0 M","come Rosalia",
 "A shorter plump Sicilian lady spirit (looks 55), 158 cm, round face, lively mouth, grey curls held in a hair net, a three-strand pearl necklace, a black lace shawl on her shoulders. She wears a long forest-green (#2F5A3A) late-19th-century dress.",158,"40.000 tri",""),
("REQ-CHR-082","Donna Tina (Donne di Fora)","cap. 3 e seguenti","Fase 4","1,0 M","come Rosalia",
 "A young Sicilian woman spirit, almost a girl (looks 19), 163 cm, gentle face with wide curious eyes, long loose wavy light-brown hair. She wears a long pale sky-blue (#A9C9E2) late-19th-century dress.",163,"40.000 tri",""),
("REQ-CHR-090","Nicolò","cap. 3 (banco, carte), cap. 12, mondo libero","Fase 4","1,0 M","conversazione ravvicinata al banco",
 "An imaginary 11-year-old Sicilian boy, 148 cm, thin, short black hair in a buzz cut, glasses with blue frames, wearing a grey T-shirt with a generic T-rex print (no brand), dark jeans, sneakers.",148,"40.000 tri",""),
("REQ-CHR-091","La professoressa di matematica","cap. 3, mondo libero","Fase 4","0,5 M","vista in aula a 3–6 m",
 "A 50-year-old Italian female maths teacher, 165 cm, short grey hair, reading glasses on a chain around the neck, wearing a beige blouse, a long dark skirt, low shoes.",165,"20.000 tri",""),
("REQ-CHR-092","Il professore di musica","cap. 3, mondo libero","Fase 4","0,5 M","vista in aula",
 "A 60-year-old Sicilian male music teacher, 175 cm, long white hair at the back, theatrical air, wearing a brown corduroy jacket, a silk foulard, beige trousers.",175,"20.000 tri",""),
("REQ-CHR-100","Il signore dell'aeroporto","cap. 1 (Mattia gli spiega la babuška)","Fase 3","0,5 M","comparsa con battute a 2–4 m",
 "A 60-year-old good-natured Sicilian man, 175 cm, light panama hat, short-sleeved light-blue shirt, beige trousers, a folded newspaper is NOT included.",175,"20.000 tri",""),
("REQ-CHR-101","Il prete con la valigia a fiori","cap. 1 (porta degli arrivi)","Fase 3","0,5 M","comparsa a 2–4 m; la valigia è REQ-PRP-009",
 "A 55-year-old Italian priest, 172 cm, black clergy shirt with white collar, black trousers, black shoes, kind face, glasses.",172,"20.000 tri",""),
("REQ-CHR-102","Turista tedesco (uomo)","cap. 1, cap. 10 (funivia), mondo libero","Fase 3","0,5 M","comparsa; varianti di colore via script",
 "A 50-year-old German male tourist, 180 cm, sunburnt pink skin, wearing a sun hat, a short-sleeved checked shirt, khaki shorts, sandals with white socks, a small backpack strapped on.",180,"20.000 tri",""),
("REQ-CHR-103","Turista tedesca (donna)","cap. 1, cap. 10, mondo libero","Fase 3","0,5 M","come sopra",
 "A 48-year-old German female tourist, 170 cm, sunburnt, short blond hair, sunglasses on her head, wearing a light floral blouse, beige linen trousers, trekking sandals.",170,"20.000 tri",""),
("REQ-CHR-104","Pallavolista","cap. 1 (squadra di pallavolo, 8 copie con varianti)","Fase 3","0,5 M","comparse in gruppo",
 "A 20-year-old female volleyball player, 182 cm, athletic, hair in a high ponytail, wearing a plain blue-and-white team tracksuit without any logo or text, white sports shoes, a sports bag is NOT included.",182,"20.000 tri","Varianti (capelli, carnagione, altezza ±6 cm) generate via script dalla stessa base."),
("REQ-CHR-105","Barista dell'aeroporto","cap. 1 (bar degli arrivi)","Fase 3","0,5 M","dietro il banco",
 "A 30-year-old Sicilian male barista, 176 cm, short dark hair, neat beard, black shirt, black apron without writing, black trousers.",176,"20.000 tri",""),
("REQ-CHR-106","Addetto al parcheggio","cap. 1 (fallimento morbido del parcheggio)","Fase 3","0,5 M","comparsa",
 "A 40-year-old Sicilian man, 174 cm, wearing a high-visibility yellow vest over a white T-shirt, dark work trousers, work shoes, a cap.",174,"20.000 tri",""),
("REQ-CHR-107","Viaggiatrice in attesa (signora col cartello)","cap. 1","Fase 3","0,5 M","comparsa; il cartello è procedurale",
 "A 65-year-old Italian woman from Bergamo, 160 cm, short grey hair, wearing a light cardigan over a summer dress, comfortable shoes.",160,"20.000 tri",""),
("REQ-CHR-108","Ragazzo con i fiori","cap. 1","Fase 3","0,5 M","comparsa; il mazzo è un oggetto procedurale",
 "A 25-year-old Italian young man, 180 cm, nervous, wearing a white shirt, dark chinos, sneakers.",180,"20.000 tri",""),
("REQ-CHR-109","Viaggiatore generico A (uomo d'affari)","cap. 1 (flussi di passeggeri)","Fase 3","0,5 M","folla",
 "A 45-year-old businessman, 178 cm, navy suit without tie, white shirt, black shoes.",178,"20.000 tri",""),
("REQ-CHR-110","Viaggiatrice generica B (studentessa)","cap. 1 (folla), Corso (folla)","Fase 3","0,5 M","folla",
 "A 22-year-old student, 166 cm, curly hair, wearing a yellow T-shirt, wide jeans, canvas sneakers.",166,"20.000 tri",""),
("REQ-CHR-120","Signora Agata dei gerani","scalinate (capp. 2–14), MIS-S-01, MIS-S-08","Fase 4","0,5 M","comparsa ricorrente",
 "A 78-year-old Sicilian woman, 152 cm, white hair in a bun, black dress with a small white pattern, an old-fashioned apron, slippers.",152,"20.000 tri",""),
("REQ-CHR-121","Vicino dei gelsomini","scalinate","Fase 4","0,5 M","comparsa",
 "A 70-year-old Sicilian man, 170 cm, bald, white vest top, grey trousers with braces, slippers.",170,"20.000 tri",""),
("REQ-CHR-122","Marta, compagna di classe","scuola (capp. 3, 12), mondo libero","Fase 4","0,5 M","comparsa con battute",
 "An imaginary 11-year-old Sicilian girl, 147 cm, dark curly hair in two braids, pink T-shirt, jeans, sneakers.",147,"20.000 tri",""),
("REQ-CHR-123","Compagno di classe (base per 8 varianti)","scuola","Fase 4","0,5 M","folla dell'aula",
 "An imaginary 12-year-old Sicilian boy, 150 cm, short brown hair, plain dark-green sweatshirt, jeans, sneakers.",150,"20.000 tri","Varianti via script."),
("REQ-CHR-124","Signor Sciacca, il tabaccaio","bar di papà (mondo libero)","Fase 4","0,5 M","cliente ricorrente",
 "A 66-year-old Sicilian man, 168 cm, grey moustache, flat cap, beige short-sleeved shirt, brown trousers.",168,"20.000 tri",""),
("REQ-CHR-125","Vigile urbano","Corso Umberto","Fase 4","0,5 M","comparsa",
 "A 45-year-old Italian municipal police officer, 178 cm, white peaked cap and white summer uniform shirt with dark trousers, without any real insignia or text.",178,"20.000 tri",""),
]
ANI=[("REQ-CHR-130","Il gatto rosso del quarto gradino","scalinata (cap. 2 e tutto il gioco), FOT-GAT-01","Fase 4","0,5 M","animale visto a 1–3 m",
 "A big red tabby European shorthair cat, male, sturdy, one ear with a small notch, amber eyes.",30,"12.000 tri + gusci di pelo (6–10)",""),
("REQ-CHR-131","Gatto nero","scalinate e Corso (varianti)","Fase 4","0,5 M","animale",
 "A slender black European shorthair cat, green eyes.",25,"12.000 tri",""),
("REQ-CHR-132","Garibaldi, il gatto di nonna Concetta","casa di Concetta, scalinata","Fase 4","0,5 M","animale",
 "A red-and-white bicolour European shorthair cat, plump, white chest and paws.",28,"12.000 tri","")]

def card_chr(c,animal=False):
    i,n,u,f,t,mot,d,h,b,ex=c
    std=STD_ANI if animal else STD_CHR
    L=[f"### {i} — {n}",
       f"- **A cosa serve e in quali capitoli**: {u}.",
       f"- **Priorità (fase in cui serve)**: {f}.",
       f"- **Fascia poligoni Tripo/Hitem3D**: **{t}** — {mot}.",
       f"- **Prompt Nano Banana principale (EN)**:", f"  > {d} {std}"]
    if ex: L.append(f"- **Nota**: {ex}")
    L.append("- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:")
    views = {"lato sinistro":EDIT_CHR["lato sinistro"].replace("person","animal") ,"retro":EDIT_CHR["retro"].replace("person","animal")} if animal else EDIT_CHR
    for k,v in views.items(): L.append(f"  - *{k}*: «{v}»")
    L+= [f"- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, {'1:1' if animal else '2:3 verticale'}.",
         f"- **Impostazioni Tripo / Hitem3D**: {TIERS[t]} Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.",
         f"- **Nome file e cartella**: immagini `assets_in/immagini/{i}_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/{i}_hitem3d.glb` (o `_tripo.glb`).",
         f"- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), {'scheletro quadrupede da template' if animal else 'scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto'}, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).",
         f"- **Budget finale in gioco**: {b}.",
         f"- **Controlli automatici**: altezza {h} cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).",
         "- **Controlla l'immagine**: " + "; ".join(chk_chr(h) if not animal else ["un solo animale, intero, quattro zampe e coda visibili","sfondo grigio uniforme","pelo nitido, nessuna sfocatura"]) + ".",
         f"- **In breve**: {n}. Genera la figura intera {'(animale) ' if animal else 'in A-pose '}e le altre viste modificando la prima immagine; in Hitem3D scegli {t} di facce."]
    return '\n'.join(L)+'\n'

PRP=[
("REQ-PRP-001","Il lapot' (scarpa di corteccia)","capp. 1–14: oggetto eroe (borsa, rito, dietro il frigo, stazione)","Fase 1 (prova pipeline) e Fase 3","1,5 M","tenuto in mano e visto a 30–50 cm (cap. 11), fibre intrecciate da trasferire in normal map",
 "An old Russian bast shoe (lapot) woven from strips of light-coloured linden bark, traditional criss-cross weave, low sides, a few bark cords at the heel, the toe visibly worn, darker and frayed, aged and slightly dusty, about 27 cm long. Seen from the side-front.",["3/4","retro","lato"],"15.000 tri; texture 2.048 (4.096 su Ultra)","lunghezza 27 cm ±0,5"),
("REQ-PRP-002","La borsa a fiori","cap. 1 (sotto il braccio della babuška), cap. 2 (rito)","Fase 3","1,0 M","vista a distanza di conversazione e da vicino nello starnuto",
 "A soft cloth shopping tote bag with a dense floral print (red roses and small blue flowers on a dark background), two fabric handles, slightly worn, partly open at the top, with the worn toe of a bark shoe peeking out of the opening. Size about 40 × 35 cm.",["3/4","retro"],"8.000 tri + simulazione di stoffa leggera","larghezza 40 cm ±1; il lapot' dentro viene sostituito da REQ-PRP-001 in Blender"),
("REQ-PRP-003","Valigia grande con lo spago","cap. 1 (carrello), cap. 2","Fase 3","1,0 M","in primo piano sul carrello all'arrivo",
 "An old large hard-shell suitcase from the 1990s, faded brown with scuffed corners, tied around twice with thick natural hemp string knotted on top, 75 × 50 × 28 cm, lying flat.",["3/4","lato"],"6.000 tri","75 cm ±1"),
("REQ-PRP-004","Valigia media con lo spago","cap. 1, cap. 2","Fase 3","1,0 M","come sopra",
 "An old medium soft fabric suitcase, dark green-grey with zip and side straps, tied once around with thick natural hemp string, 62 × 42 × 24 cm, lying flat.",["3/4","lato"],"5.000 tri","62 cm ±1"),
("REQ-PRP-005","Valigia piccola con lo spago (la terza, coi barattoli)","cap. 1, cap. 2 (escono i pirožki), MIS-S-03","Fase 3","1,0 M","si apre al cap. 2 e nella missione",
 "An old small brown leather-look suitcase with two metal clasps and a worn handle, tied crosswise with thick natural hemp string, 50 × 35 × 20 cm, lying flat.",["3/4","lato"],"5.000 tri (coperchio separato)","50 cm ±1"),
("REQ-PRP-006","Cartello di Mattia «BABUŠKA GALINA»","cap. 1 (in mano a Irina), SEG-16","Fase 3","0,5 M","oggetto piatto letto a 1–3 m",
 "A hand-made cardboard sign, 50 × 35 cm, slightly bent, written in uneven children's block letters with a blue marker: BABUŠKA GALINA, and below a child's drawing of a bear that looks like a potato with ears, coloured with brown and yellow crayons. Front view, flat.",["3/4"],"200 tri + texture 2.048","testo leggibile «BABUŠKA GALINA»; Claude ridisegna la scritta in texture se Nano Banana sbaglia le lettere"),
("REQ-PRP-007","Telefono di Giulia","cap. 1 (in mano), capp. 7, 10–11","Fase 3","0,5 M","piccolo, superfici lisce",
 "A modern smartphone with no logo, black, in a translucent purple silicone case with small glitter, a slightly cracked screen protector corner, screen off.",["retro","lato"],"2.000 tri","dimensioni 15 × 7,2 cm"),
("REQ-PRP-008","Telefono di Vera (fotocamera, torcia, orologio)","tutto il gioco, in prima persona","Fase 2","1,0 M","sempre in mano davanti alla camera",
 "A modern smartphone with no logo, in a matte navy-blue silicone case, slightly worn edges, screen off, back camera module with two lenses and a flash.",["retro","lato"],"4.000 tri + schermo come superficie di rendering","dimensioni 14,7 × 7,1 cm"),
("REQ-PRP-009","Valigia a fiori del prete","cap. 1 (porta degli arrivi)","Fase 3","0,5 M","passa a 2–4 m",
 "A hard-shell wheeled cabin suitcase with a cheerful pink and white floral pattern, telescopic handle extended, 55 × 40 × 20 cm, standing upright.",["3/4"],"3.000 tri","55 cm ±1"),
("REQ-PRP-010","Quaderno di scienze di Vera (chiuso)","tutto il gioco (quaderno in primo piano)","Fase 2","1,5 M","sempre in primo piano a 38 cm; bordi delle pagine e copertina da vicino",
 "A used A5 school notebook with a hard sage-green cover, slightly rounded and worn corners, a white rectangular label on the cover with handwritten blue-pen text «SCIENZE — Vera Russo — 1ªB», the pages' edges a bit wavy, closed, lying flat, seen from above at 30 degrees.",["3/4","retro"],"6.000 tri + pagine procedurali","formato A5 (21 × 14,8 cm)"),
("REQ-PRP-011","Coniglio di pezza di Mattia","capp. 1 (nello zaino), 9, 10, 14","Fase 3","1,0 M","in braccio a Mattia in primi piani",
 "An old floppy plush rabbit toy, faded light grey with a pink fabric inner ear, long ears, button eyes, one ear slightly torn and sewn back, sitting.",["3/4","retro"],"4.000 tri","altezza 30 cm"),
("REQ-PRP-012","Zainetto di Mattia","cap. 1, cap. 10 (con il coniglio)","Fase 3","0,5 M","a 1–2 m",
 "A small children's backpack in red fabric with a front pocket and grey straps, partially open zip, no logo.",["3/4","retro"],"2.500 tri","altezza 30 cm"),
("REQ-PRP-013","Monovolume grigia con l'ammaccatura (esterno)","cap. 1 (parcheggio), cap. 2 (arrivo in Via Circonvallazione)","Fase 3","1,0 M","vista da vicino al parcheggio; interni procedurali separati",
 "A generic seven-seat European minivan from about 2015, silver-grey metallic, no brand badges or logos, clean but used, a visible small dent on the rear right side door, side view.",["3/4","retro"],"35.000 tri (esterno) + interni procedurali 25.000","lunghezza 4,6 m ±5 cm"),
]
def card_prp(p):
    i,n,u,f,t,mot,d,views,b,chk=p
    L=[f"### {i} — {n}", f"- **A cosa serve e in quali capitoli**: {u}.", f"- **Priorità (fase in cui serve)**: {f}.",
       f"- **Fascia poligoni Tripo/Hitem3D**: **{t}** — {mot}.", "- **Prompt Nano Banana principale (EN)**:", f"  > {d} {STD_PRP}",
       "- **Prompt di modifica per le altre viste (EN)**:"]
    for v in views: L.append(f"  - *{v}*: «{EDIT_PRP[v]}»")
    tool=TIERS[t].replace("Hitem3D multi-vista","Hitem3D (immagine singola o multi-vista)")
    L+=[ "- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.",
         f"- **Impostazioni Tripo / Hitem3D**: {tool} Per oggetti rigidi è consigliato Tripo.",
         f"- **Nome file e cartella**: `assets_in/immagini/{i}_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/{i}_tripo.glb` (o `_hitem3d.glb`).",
         "- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.",
         f"- **Budget finale in gioco**: {b}.",
         f"- **Controlli automatici**: {chk}; triangoli entro budget; validatore TDD §10; render di revisione.",
         "- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.",
         f"- **In breve**: {n}. Foto dell'oggetto su fondo grigio, poi le viste per modifica; {t} di facce."]
    return '\n'.join(L)+'\n'

head_p=open(os.path.join(BASE,'work','strumenti','intro_personaggi.md'),encoding='utf-8').read()
head_o=open(os.path.join(BASE,'work','strumenti','intro_oggetti.md'),encoding='utf-8').read()
tail_o=open(os.path.join(BASE,'work','strumenti','web_oggetti.md'),encoding='utf-8').read()
out=[head_p]+[card_chr(c) for c in CHR]+["## Animali\n"]+[card_chr(c,True) for c in ANI]+["## Fonti\n- `PIPELINE_ASSET.md` §2–§5; `PERSONAGGI.md`.\n- [Nano Banana — riferimenti multipli e coerenza (Runway)](https://help.runwayml.com/hc/en-us/articles/50317213804435-Creating-images-with-Nano-Banana)\n- [Hitem3D — risoluzioni](https://www.hitem3d.ai/de/ai-faq/how-to-choose-the-model-resolution-for-hitem3d)\n"]
open(os.path.join(BASE,'docs','RICHIESTE_ASSET','personaggi_v1.md'),'w',encoding='utf-8').write('\n'.join(out))
out=[head_o]+[card_prp(p) for p in PRP]+[tail_o]
open(os.path.join(BASE,'docs','RICHIESTE_ASSET','oggetti_cap01.md'),'w',encoding='utf-8').write('\n'.join(out))
print(len(CHR)+len(ANI),'schede personaggi;',len(PRP),'schede oggetti')
