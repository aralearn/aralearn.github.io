#!/usr/bin/env python3
"""Writes the home page in English (/index.html) and Polish (/pl/index.html).

Both come from one template so they always have the same sections and phones;
only the words differ. Run after changing any text here:  python3 tools/make_home.py

Screenshots live in /shots as <name>-light.webp and <name>-dark.webp (603 x 1311,
from the iPhone app's QA run); the page shows the dark one when the visitor's
device is in dark mode.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- words

EN = dict(
    lang="en", path="/", other="/pl/",
    title="Ara: Learn Georgian",
    description="A colourful Georgian companion: learn from zero and use phrases in Georgia, "
                "offline. Try it in your browser; for iPhone soon.",
    status="For iPhone · coming soon · now in testing",
    h1='Learn Georgian.<br><span class="hl">Use it today.</span>',
    lead="A colourful companion for people living in or visiting Georgia. <strong>Learn</strong> "
         "the alphabet and the language from zero, and <strong>use</strong> a phrasebook for "
         "real situations, offline, from day one.",
    cta="Try Ara in your browser",
    cta_note="Free, on any phone or computer: the whole course and the phrasebook, with audio. "
             "No account; your progress stays on your device. On iPhone, tap Share, then Add to "
             "Home Screen, and Ara works offline like an app.",
    hero_alt=["The alphabet chart in Ara", "Ara's Home screen: greeting, search, progress and the next lesson",
              "A phrase card: ask the taxi to stop here, in Georgian, with audio"],
    mascot_alt="Ara the macaw waving",
    walk_title="What's in Ara",
    walk_lead="Two halves that work together: a course that starts at the first letter, and a "
              "phrasebook you can use the moment you land.",
    steps=[
        dict(shot="letter", color="pomegranate", chip="Learn",
             h="Start from the very first letter.",
             p=["Georgian has its own alphabet: 33 letters, no capitals, one sound each. Ara "
                "teaches them one at a time, with audio and a tip for every sound."],
             items=["33 letters, each with its sound", "Reading from the first lesson",
                    "Already reading Georgian? Start further along"],
             alt="Learning a new letter, with its name, sound and audio"),
        dict(shot="lesson", color="saperavi", chip="Lessons",
             h="Short lessons that stay with you.",
             p=["59 lessons in six stages, from the first letter to the dinner table. 15 kinds of "
                "exercise: listen, match pairs, spell, build a sentence, choose your reply."],
             items=["Words you'll really use", "Grammar in plain words", "Tap any word to see its meaning",
                    "A wrong answer comes back at the end"],
             alt="An exercise: what does პური (bread) mean?"),
        dict(shot="phrasebook", color="tkemali", chip="Use in Georgia",
             h="302 phrases for real situations.",
             p=["Ready from day one, with nothing to unlock: 11 situations, each with the words "
                "you need right now. Save a phrase and it joins your reviews."],
             items=["Transport", "Shopping & bazaar", "Restaurants & cafés", "Health & pharmacy",
                    "Home & everyday", "Emergencies, with 112"],
             alt="The Use in Georgia tab: search, emergency phrases and situations"),
        dict(shot="show", color="blacksea", chip="Show mode",
             h="Too shy to say it? Show it.",
             p=["One tap turns a phrase into big, clear Georgian to show a driver or a shopkeeper. "
                "Or play it aloud, slowly if you like."],
             items=["Big text, light or dark", "Audio, normal or slow",
                    "A sounds-like spelling to say it yourself"],
             alt="Show mode: a phrase in large Georgian letters to show someone"),
        dict(shot="dialogue", color="gold", chip="Conversations",
             h="Practise real conversations.",
             p=["21 everyday dialogues: at the bazaar, on a marshrutka, at a friend's for dinner. "
                "Read along, hear every line, then take a side and answer yourself."],
             items=["Taking a taxi", "At the bazaar", "At the pharmacy", "Dinner at a friend's",
                    "Buying a SIM card", "Calling 112"],
             alt="A conversation at the bazaar between a seller and a customer"),
        dict(shot="search", color="saperavi", chip="Words",
             h="Find any word, however you type it.",
             p=["Search in English, in Georgian or in Latin letters, and typos are fine. Words, "
                "phrases, situations and conversations, all in one place."],
             items=["Every word in the app, with its meaning", "What you know and what's new"],
             alt="Searching for water: words and phrases with it"),
        dict(shot="review", color="pomegranate", chip="Review",
             h="Remember it next week, too.",
             p=["Each word comes back just before you'd forget it: after a day, then three, then "
                "eight. Miss one and it returns in ten minutes."],
             items=["A few minutes a day", "The difficult words, gathered for you"],
             alt="Review: 14 items due today and the difficult words"),
        dict(shot="progress", color="tkemali", chip="Progress",
             h="From Just landed to Tamada.",
             p=["No points to collect. Ara shows what you can actually do, from reading shop signs "
                "to raising a toast at a supra."],
             items=["Just landed", "Sign reader", "Bazaar regular", "Supra guest",
                    "Tamada's apprentice", "Tamada"],
             alt="Progress: the stage Sign reader and what you can already do"),
    ],
    tiles_title="And a few more things",
    tiles=[
        dict(icon="offline", color="tkemali", h="Works offline",
             p="The course, the phrasebook and every audio clip are inside the app. No signal at the bazaar? No problem."),
        dict(icon="lock", color="saperavi", h="Nothing collected",
             p='No account, no ads, no tracking. Your progress stays on your phone. <a href="/privacy">Privacy policy</a>'),
        dict(icon="voice", color="blacksea", h="Two voices",
             p="Hear every word from Eka or Giorgi. They're synthetic voices, and Ara labels them so."),
        dict(icon="lang", color="gold", h="English or Polish",
             p="All of Ara in your language. For Polish speakers, sounds and grammar are compared with Polish."),
        dict(icon="tap", color="pomegranate", h="Tap any word",
             p="Every Georgian word in examples, phrases and conversations explains itself with one tap."),
        dict(icon="sos", color="ink", h="Help in an emergency",
             p="Emergency phrases right at the top of the phrasebook, and a button that calls 112."),
    ],
    end_title="Say გამარჯობა to Georgian.",
    end_text="Ara is free in your browser today, and coming to iPhone soon.",
    privacy="Privacy policy", support="Support",
    footer_privacy="/privacy", footer_support="/support",
    lang_label="Language",
)

PL = dict(
    lang="pl", path="/pl/", other="/",
    title="Ara: nauka gruzińskiego",
    description="Kolorowy towarzysz do gruzińskiego: nauka od zera i rozmówki na co dzień w Gruzji, "
                "bez internetu. Wypróbuj w przeglądarce; wkrótce na iPhone'a.",
    status="Na iPhone'a · wkrótce · teraz w testach",
    h1='Ucz się gruzińskiego.<br><span class="hl">Mów już dziś.</span>',
    lead="Kolorowy towarzysz dla osób, które mieszkają w Gruzji albo ją odwiedzają. "
         "<strong>Ucz się</strong> alfabetu i języka od zera i <strong>korzystaj</strong> z "
         "rozmówek na prawdziwe sytuacje, bez internetu, od pierwszego dnia.",
    cta="Wypróbuj Arę w przeglądarce",
    cta_note="Za darmo, na każdym telefonie i komputerze: cały kurs i rozmówki, z nagraniami. Bez "
             "konta; postępy zostają na Twoim urządzeniu. Na iPhonie stuknij „Udostępnij”, potem "
             "„Do ekranu początkowego”, a Ara zadziała bez internetu jak aplikacja.",
    hero_alt=["Tablica alfabetu w Arze", "Ekran startowy Ary: powitanie, wyszukiwarka, postępy i następna lekcja",
              "Karta zwrotu: prośba do taksówkarza, żeby się tu zatrzymał, po gruzińsku, z nagraniem"],
    mascot_alt="Ara, papuga ara, macha skrzydłem",
    walk_title="Co jest w Arze",
    walk_lead="Dwie połowy, które działają razem: kurs od pierwszej litery i rozmówki, z których "
              "skorzystasz zaraz po wylądowaniu.",
    steps=[
        dict(shot="letter", color="pomegranate", chip="Nauka",
             h="Zacznij od pierwszej litery.",
             p=["Gruziński ma własny alfabet: 33 litery, bez wielkich liter, każda to jeden dźwięk. "
                "Ara przedstawia je po kolei, z nagraniem i wskazówką do każdego dźwięku, porównaną z polskim."],
             items=["33 litery, każda ze swoim dźwiękiem", "Czytanie od pierwszej lekcji",
                    "Już czytasz po gruzińsku? Zacznij dalej"],
             alt="Nauka nowej litery: nazwa, dźwięk i nagranie"),
        dict(shot="lesson", color="saperavi", chip="Lekcje",
             h="Krótkie lekcje, które zostają.",
             p=["59 lekcji w sześciu etapach, od pierwszej litery do suto zastawionego stołu. "
                "15 rodzajów ćwiczeń: słuchanie, łączenie w pary, pisanie, układanie zdań, wybór odpowiedzi."],
             items=["Słowa, których naprawdę użyjesz", "Gramatyka prostymi słowami, w porównaniu z polską",
                    "Stuknij słowo, by zobaczyć, co znaczy", "Błędna odpowiedź wraca na końcu"],
             alt="Ćwiczenie: co znaczy პური (chleb)?"),
        dict(shot="phrasebook", color="tkemali", chip="W Gruzji",
             h="302 zwroty na prawdziwe sytuacje.",
             p=["Gotowe od pierwszego dnia, nic do odblokowania: 11 sytuacji, w każdej słowa "
                "potrzebne od razu. Zapisz zwrot, a trafi do Twoich powtórek."],
             items=["Transport", "Zakupy i bazar", "Restauracje i kawiarnie", "Zdrowie i apteka",
                    "Dom i codzienność", "Nagłe wypadki, z numerem 112"],
             alt="Zakładka W Gruzji: wyszukiwarka, zwroty awaryjne i sytuacje"),
        dict(shot="show", color="blacksea", chip="Pokaż",
             h="Wstydzisz się powiedzieć? Pokaż.",
             p=["Jedno stuknięcie i zwrot pojawia się dużymi, wyraźnymi literami: do pokazania "
                "kierowcy albo sprzedawcy. Albo odtwórz go na głos, także wolniej."],
             items=["Duży tekst, jasny lub ciemny", "Nagranie w zwykłym lub wolnym tempie",
                    "Zapis „jak to brzmi”, żeby powiedzieć samemu"],
             alt="Tryb Pokaż: zwrot dużymi gruzińskimi literami do pokazania komuś"),
        dict(shot="dialogue", color="gold", chip="Rozmowy",
             h="Ćwicz prawdziwe rozmowy.",
             p=["21 codziennych dialogów: na bazarze, w marszrutce, na kolacji u znajomych. "
                "Czytaj, słuchaj każdej kwestii, a potem wybierz stronę i odpowiadaj sam."],
             items=["Taksówka", "Na bazarze", "W aptece", "Kolacja u znajomych",
                    "Karta SIM", "Telefon pod 112"],
             alt="Rozmowa na bazarze między sprzedawcą a klientem"),
        dict(shot="search", color="saperavi", chip="Słowa",
             h="Znajdź każde słowo, jakkolwiek je wpiszesz.",
             p=["Szukaj po polsku, po gruzińsku albo łacinką; literówki nie szkodzą. Słowa, "
                "zwroty, sytuacje i rozmowy w jednym miejscu."],
             items=["Każde słowo z aplikacji, ze znaczeniem", "Co już znasz, a co jest nowe"],
             alt="Wyszukiwanie słowa „woda”: słowa i zwroty z nim"),
        dict(shot="review", color="pomegranate", chip="Powtórki",
             h="Pamiętaj także za tydzień.",
             p=["Każde słowo wraca tuż przed tym, zanim je zapomnisz: po dniu, potem po trzech, "
                "potem po ośmiu. Pomyłka? Wróci za dziesięć minut."],
             items=["Kilka minut dziennie", "Trudne słowa zebrane w jednym miejscu"],
             alt="Powtórki: 14 na dziś i trudne słowa"),
        dict(shot="progress", color="tkemali", chip="Postępy",
             h="Od lądowania do tamady.",
             p=["Bez punktów do zbierania. Ara pokazuje, co naprawdę już umiesz: od czytania "
                "szyldów po wznoszenie toastu na suprze."],
             items=["Świeżo po lądowaniu", "Czytelnik szyldów", "Bywalec bazaru", "Gość na suprze",
                    "Uczeń tamady", "Tamada"],
             alt="Postępy: etap Czytelnik szyldów i to, co już umiesz"),
    ],
    tiles_title="I jeszcze kilka rzeczy",
    tiles=[
        dict(icon="offline", color="tkemali", h="Działa bez internetu",
             p="Kurs, rozmówki i wszystkie nagrania są w aplikacji. Brak zasięgu na bazarze? Żaden problem."),
        dict(icon="lock", color="saperavi", h="Nic nie zbieramy",
             p='Bez konta, reklam i śledzenia. Postępy zostają na Twoim telefonie. <a href="/pl/privacy">Polityka prywatności</a>'),
        dict(icon="voice", color="blacksea", h="Dwa głosy",
             p="Każde słowo czyta Eka albo Giorgi. To głosy syntetyczne i Ara tak je opisuje."),
        dict(icon="lang", color="gold", h="Po polsku lub po angielsku",
             p="Cała Ara w Twoim języku. Wymowę i gramatykę wyjaśniamy w porównaniu z polskim."),
        dict(icon="tap", color="pomegranate", h="Stuknij dowolne słowo",
             p="Każde gruzińskie słowo w przykładach, zwrotach i rozmowach wyjaśnia się jednym stuknięciem."),
        dict(icon="sos", color="ink", h="Pomoc w nagłej sytuacji",
             p="Zwroty awaryjne na samej górze rozmówek i przycisk, który dzwoni pod 112."),
    ],
    end_title="Powiedz gruzińskiemu გამარჯობა.",
    end_text="Ara jest już za darmo w przeglądarce, a wkrótce na iPhonie.",
    privacy="Polityka prywatności", support="Pomoc",
    footer_privacy="/pl/privacy", footer_support="/pl/support",
    lang_label="Język",
)

# ---------------------------------------------------------------- pieces

ICONS = {  # simple 24 x 24 line icons, drawn here
    "offline": '<path d="M2 8.5a15 15 0 0 1 20 0M5.5 12a10 10 0 0 1 13 0M9 15.5a5 5 0 0 1 6 0"/><circle cx="12" cy="19" r="1.2" fill="currentColor"/><path d="M3 3l18 18"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
    "voice": '<path d="M4 9.5v5h3.5L12 18.5v-13L7.5 9.5z"/><path d="M15.5 9a4 4 0 0 1 0 6M18 6.5a7.5 7.5 0 0 1 0 11"/>',
    "lang": '<path d="M3.5 5.5h9M8 3.5v2M10.5 5.5c-.7 3.8-3 6.6-6.5 8.5M6 8.5c1.2 2.2 3 3.8 5 4.8"/><path d="M12.5 20.5l4-10 4 10M14 17h5"/>',
    "tap": '<path d="M9.5 11V5.5a1.8 1.8 0 0 1 3.6 0V11l4.6 1a2 2 0 0 1 1.6 2.2l-.6 4.3a3 3 0 0 1-3 2.5h-4.2a3 3 0 0 1-2.4-1.2L5.4 15.6a1.7 1.7 0 0 1 2.6-2.2l1.5 1.6"/><path d="M6 6.5a5.5 5.5 0 0 1 10.4-1.5"/>',
    "sos": '<path d="M12 3.5l9 16H3z"/><path d="M12 10v4.5"/><circle cx="12" cy="17" r="1" fill="currentColor"/>',
}


def phone(shot, alt, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    alt_attr = f'alt="{alt}"' if alt else 'alt=""'
    return (f'<div class="phone {cls}"><div class="screen"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="/shots/{shot}-dark.webp">'
            f'<img src="/shots/{shot}-light.webp" width="603" height="1311" {alt_attr} {load} decoding="async">'
            f'</picture></div></div>')


def header(t, current):
    en_cur = ' aria-current="page"' if t["lang"] == "en" else ""
    pl_cur = ' aria-current="page"' if t["lang"] == "pl" else ""
    en_href = current["en"]
    pl_href = current["pl"]
    return f'''<header class="top">
  <a class="brand" href="{t["path"]}"><img src="/icon.png" alt=""><span class="name">Ara</span></a>
  <nav class="lang" aria-label="{t["lang_label"]}"><a href="{en_href}" hreflang="en" lang="en"{en_cur}>EN</a><a href="{pl_href}" hreflang="pl" lang="pl"{pl_cur}>PL</a></nav>
</header>'''


def page(t):
    steps_html, shots_html, ticks = [], [], []
    for i, s in enumerate(t["steps"]):
        paras = "".join(f"<p>{p}</p>" for p in s["p"])
        items = "".join(f"<li>{x}</li>" for x in s["items"])
        steps_html.append(f'''    <article class="step{' is-active' if i == 0 else ''}" data-step="{i}" style="--c: var(--{s["color"]})">
      <div class="art">{phone(s["shot"], s["alt"])}</div>
      <span class="chip">{s["chip"]}</span>
      <h3>{s["h"]}</h3>
      {paras}
      <ul class="list">{items}</ul>
    </article>''')
        shots_html.append(f'<div class="shot" data-shot="{i}" style="--c: var(--{s["color"]})">'
                          f'{phone(s["shot"], "", "flat")}</div>')
        ticks.append(f'<i style="--c: var(--{s["color"]})"></i>')

    tiles = "".join(f'''
    <div class="tile" style="--c: var(--{x["color"]})">
      <svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[x["icon"]]}</svg>
      <h3>{x["h"]}</h3>
      <p>{x["p"]}</p>
    </div>''' for x in t["tiles"])

    alt = t["hero_alt"]
    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["description"]}">
<link rel="alternate" hreflang="en" href="https://aralearn.github.io/">
<link rel="alternate" hreflang="pl" href="https://aralearn.github.io/pl/">
<link rel="alternate" hreflang="x-default" href="https://aralearn.github.io/">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["description"]}">
<meta property="og:image" content="https://aralearn.github.io/icon.png">
<link rel="icon" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800;900&display=swap">
<link rel="stylesheet" href="/style.css">
<script src="/site.js" defer></script>
</head>
<body class="home">
<!-- Made by tools/make_home.py: change the words there, then run it again. -->
<div class="wrap wide">
{header(t, dict(en="/", pl="/pl/"))}

<main>
<section class="hero2">
  <div class="hero-text">
    <span class="pill">{t["status"]}</span>
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <div class="try">
      <a class="cta" href="/app/">{t["cta"]}</a>
      <p class="muted">{t["cta_note"]}</p>
    </div>
  </div>
  <div class="fan">
    <div class="glow" aria-hidden="true"></div>
    {phone("alphabet", alt[0], "left")}
    {phone("phrase", alt[2], "right")}
    {phone("home", alt[1], "center", eager=True)}
    <img class="mascot" src="/mascot.png" width="360" height="525" alt="{t["mascot_alt"]}">
  </div>
</section>

<div class="stripe"></div>

<section class="walk" id="whats-in-ara" data-active="0">
  <div class="walk-head">
    <h2>{t["walk_title"]}</h2>
    <p class="lead">{t["walk_lead"]}</p>
  </div>
  <div class="walk-grid">
    <div class="steps">
{chr(10).join(steps_html)}
    </div>
    <div class="pin" aria-hidden="true">
      <div class="pin-in">
        <div class="stack">{"".join(shots_html)}</div>
        <div class="ticks">{"".join(ticks)}</div>
      </div>
    </div>
  </div>
</section>

<section class="tiles-sec">
  <h2>{t["tiles_title"]}</h2>
  <div class="tiles">{tiles}
  </div>
</section>

<section class="end">
  <h2>{t["end_title"]}</h2>
  <p>{t["end_text"]}</p>
  <a class="cta" href="/app/">{t["cta"]}</a>
  <p class="muted">{t["status"]}</p>
</section>
</main>
<footer>
  <a href="{t["path"]}">Ara</a> · <a href="{t["footer_privacy"]}">{t["privacy"]}</a> · <a href="{t["footer_support"]}">{t["support"]}</a> · <a href="mailto:ara.learn.app@gmail.com">ara.learn.app@gmail.com</a>
</footer>
</div>
</body>
</html>
'''


def main():
    for t, out in [(EN, "index.html"), (PL, "pl/index.html")]:
        path = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(t))
        print("wrote", out)


if __name__ == "__main__":
    main()
