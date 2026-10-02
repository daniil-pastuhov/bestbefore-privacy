import html
ISSUES = "https://github.com/daniil-pastuhov/bestbefore-privacy/issues"
OFF = "https://world.openfoodfacts.org/privacy"
GPS = "https://policies.google.com/privacy"
CSS = """:root{--bg:#fff;--fg:#1d2420;--mut:#5b6660;--ac:#1f7a4d;--bd:#dfe5e1;--card:#f5f8f6}
@media(prefers-color-scheme:dark){:root{--bg:#121614;--fg:#e6ebe8;--mut:#9aa6a0;--ac:#5fc794;--bd:#2a332e;--card:#1a201d}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:32px 16px 64px}h1{font-size:1.9rem;line-height:1.2;margin:.2em 0}
h2{font-size:1.2rem;margin:2em 0 .4em}p,li{margin:.5em 0}ul{padding-left:1.2em}a{color:var(--ac)}
.mut{color:var(--mut);font-size:.9rem}.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:4px 18px;margin:20px 0}
nav{display:flex;gap:14px;flex-wrap:wrap;font-size:.95rem}nav a[aria-current]{font-weight:700;text-decoration:none;color:var(--fg)}
.langs a{display:block;padding:14px 18px;margin:10px 0;border:1px solid var(--bd);border-radius:12px;background:var(--card);text-decoration:none;font-weight:600}"""

NAV = [("en","English"),("ru","Русский"),("nb","Norsk")]
def nav(cur):
    return "<nav>"+" ".join(f'<a href="{c}.html" hreflang="{c}"'+(' aria-current="page"' if c==cur else '')+f'>{n}</a>' for c,n in NAV)+"</nav>"

T = {}
T["en"] = dict(app="BestBefore", title="Privacy Policy", upd="Last updated: 2 October 2026", secs=[
("The short version", ["<p>BestBefore keeps your pantry on your phone. There is no account, no developer server, no advertising and no analytics. We do not collect, receive, sell or share your personal data.</p>"]),
("What the app stores", ["<p>Your pantry items, expiry dates, shopping list, settings, product photos and any shop locations you save are stored only in the app's local database on your device. They are never sent to us, because we do not run a server.</p>"]),
("Camera", ["<p>The camera is used to scan barcodes, read printed expiry dates and photograph food items. Recognition runs on your device (Google ML Kit on Android, Apple Vision on iOS). Photos you take are saved only on your device.</p>"]),
("Internet requests", ["<p>When you scan a barcode, the app asks <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a> for the product's name and picture. That request contains the barcode number, and, as with any web request, Open Food Facts' servers can see your IP address. No name, account or device identifier is added by the app. Product pictures are also loaded from Open Food Facts. See their <a href=\""+OFF+"\">privacy policy</a>.</p>"]),
("Location (optional)", ["<p>Location is off by default. If you turn on shop reminders, you can save a shop's position and the app shows your shopping list when you are near it. Saved positions stay on your device. On Android, nearby-shop detection is performed by Google Play services on your device; see <a href=\""+GPS+"\">Google's privacy policy</a>. You can turn the feature off, or revoke the permission, at any time.</p>"]),
("Notifications, backups and sharing", ["<ul><li>Expiry reminders and digests are scheduled locally on your device.</li><li>Exporting a backup or sharing a shopping list or recipe idea only happens when you choose to, and goes where you send it.</li><li>Your phone's own backup (Google or iCloud) may include the app's data. That is controlled by your device settings, not by us.</li></ul>"]),
("Children", ["<p>The app is not directed at children and we do not knowingly collect any data from anyone.</p>"]),
("Your control", ["<p>You can edit or delete any item inside the app. Uninstalling the app deletes its data from your device.</p>"]),
("Changes", ["<p>If this policy changes, the new version will be published on this page with an updated date.</p>"]),
("Contact", ["<p>Questions? <a href=\""+ISSUES+"\">Open an issue</a> on GitHub.</p>"]),
], home="Choose your language")
T["ru"] = dict(app="Срокоед", title="Политика конфиденциальности", upd="Последнее обновление: 2 октября 2026 г.", secs=[
("Коротко", ["<p>Срокоед хранит ваши продукты на вашем телефоне. Нет аккаунта, сервера разработчика, рекламы и аналитики. Мы не собираем, не получаем, не продаём и не передаём ваши персональные данные.</p>"]),
("Что хранит приложение", ["<p>Продукты, сроки годности, список покупок, настройки, фотографии продуктов и сохранённые вами магазины хранятся только в локальной базе данных приложения на вашем устройстве. Они никогда не отправляются нам, потому что у нас нет сервера.</p>"]),
("Камера", ["<p>Камера используется для сканирования штрихкодов, распознавания напечатанных сроков годности и фотографирования продуктов. Распознавание выполняется на устройстве (Google ML Kit на Android, Apple Vision на iOS). Сделанные фотографии сохраняются только на вашем устройстве.</p>"]),
("Запросы в интернет", ["<p>Когда вы сканируете штрихкод, приложение запрашивает у <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a> название и изображение продукта. Запрос содержит номер штрихкода, а серверы Open Food Facts, как и любого сайта, видят ваш IP-адрес. Приложение не добавляет имя, аккаунт или идентификатор устройства. Изображения продуктов тоже загружаются с Open Food Facts. См. их <a href=\""+OFF+"\">политику конфиденциальности</a>.</p>"]),
("Местоположение (по желанию)", ["<p>По умолчанию местоположение отключено. Если вы включите напоминания у магазинов, вы можете сохранить положение магазина, и приложение покажет список покупок, когда вы рядом. Сохранённые места остаются на вашем устройстве. На Android определение близости к магазину выполняют сервисы Google Play на вашем устройстве; см. <a href=\""+GPS+"\">политику конфиденциальности Google</a>. Функцию можно отключить, а разрешение отозвать в любой момент.</p>"]),
("Уведомления, резервные копии и обмен", ["<ul><li>Напоминания о сроках и сводки планируются локально на вашем устройстве.</li><li>Экспорт резервной копии и отправка списка покупок или идеи рецепта происходят только по вашему действию и попадают туда, куда вы их отправите.</li><li>Резервная копия самого телефона (Google или iCloud) может включать данные приложения. Это определяется настройками устройства, а не нами.</li></ul>"]),
("Дети", ["<p>Приложение не предназначено для детей, и мы сознательно не собираем ничьих данных.</p>"]),
("Ваш контроль", ["<p>Любой продукт можно изменить или удалить прямо в приложении. При удалении приложения его данные удаляются с вашего устройства.</p>"]),
("Изменения", ["<p>Если политика изменится, новая версия будет опубликована на этой странице с обновлённой датой.</p>"]),
("Контакты", ["<p>Есть вопросы? <a href=\""+ISSUES+"\">Создайте обращение (issue)</a> на GitHub.</p>"]),
], home="Выберите язык")
T["nb"] = dict(app="Matvakt", title="Personvernerklæring", upd="Sist oppdatert: 2. oktober 2026", secs=[
("Kort fortalt", ["<p>Matvakt oppbevarer matvarene dine på telefonen din. Det finnes ingen konto, ingen server hos utvikleren, ingen reklame og ingen analyse. Vi samler ikke inn, mottar, selger eller deler personopplysningene dine.</p>"]),
("Hva appen lagrer", ["<p>Matvarer, utløpsdatoer, handleliste, innstillinger, bilder av produkter og butikker du har lagret, lagres bare i appens lokale database på enheten din. De sendes aldri til oss, fordi vi ikke har noen server.</p>"]),
("Kamera", ["<p>Kameraet brukes til å skanne strekkoder, lese påtrykte utløpsdatoer og ta bilder av matvarer. Gjenkjenningen skjer på enheten (Google ML Kit på Android, Apple Vision på iOS). Bilder du tar lagres bare på enheten din.</p>"]),
("Internett-forespørsler", ["<p>Når du skanner en strekkode, henter appen produktets navn og bilde fra <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a>. Forespørselen inneholder strekkodenummeret, og som ved alle nettforespørsler kan Open Food Facts' servere se IP-adressen din. Appen legger ikke til navn, konto eller enhetsidentifikator. Produktbilder lastes også fra Open Food Facts. Se deres <a href=\""+OFF+"\">personvernerklæring</a>.</p>"]),
("Posisjon (valgfritt)", ["<p>Posisjon er slått av som standard. Slår du på butikkpåminnelser, kan du lagre posisjonen til en butikk, og appen viser handlelisten når du er i nærheten. Lagrede posisjoner blir på enheten din. På Android utføres oppdagelsen av nærliggende butikker av Google Play-tjenester på enheten din; se <a href=\""+GPS+"\">Googles personvernerklæring</a>. Du kan slå av funksjonen eller trekke tilbake tillatelsen når som helst.</p>"]),
("Varsler, sikkerhetskopier og deling", ["<ul><li>Påminnelser om utløpsdatoer og sammendrag planlegges lokalt på enheten din.</li><li>Eksport av sikkerhetskopi og deling av handleliste eller oppskriftsidé skjer bare når du velger det, og går dit du sender det.</li><li>Telefonens egen sikkerhetskopi (Google eller iCloud) kan inneholde appens data. Det styres av enhetens innstillinger, ikke av oss.</li></ul>"]),
("Barn", ["<p>Appen er ikke rettet mot barn, og vi samler ikke bevisst inn data fra noen.</p>"]),
("Din kontroll", ["<p>Du kan endre eller slette alle matvarer i appen. Avinstallerer du appen, slettes dataene fra enheten din.</p>"]),
("Endringer", ["<p>Hvis erklæringen endres, publiseres den nye versjonen på denne siden med oppdatert dato.</p>"]),
("Kontakt", ["<p>Spørsmål? <a href=\""+ISSUES+"\">Opprett en sak (issue)</a> på GitHub.</p>"]),
], home="Velg språk")

def page(code):
    t=T[code]
    body="".join(f"<h2>{h}</h2>{''.join(ps)}" for h,ps in t["secs"])
    return f"""<!doctype html>
<html lang="{code}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['app']} — {t['title']}</title><meta name="robots" content="index,follow"><style>{CSS}</style></head>
<body><main>{nav(code)}<h1>{t['app']}<br>{t['title']}</h1><p class="mut">{t['upd']}</p><div class="card">{''.join(t['secs'][0][1])}</div>{body.split('</p>',1)[1] if False else ''.join(f"<h2>{h}</h2>{''.join(ps)}" for h,ps in t['secs'][1:])}</main></body></html>"""
for c in T: open(f"{c}.html","w",encoding="utf-8").write(page(c))
open("index.html","w",encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BestBefore — Privacy Policy</title><style>{CSS}</style></head>
<body><main><h1>BestBefore</h1><p class="mut">Privacy Policy · Personvernerklæring · Политика конфиденциальности</p>
<div class="langs"><a href="en.html" hreflang="en">English — BestBefore</a><a href="ru.html" hreflang="ru">Русский — Срокоед</a><a href="nb.html" hreflang="nb">Norsk — Matvakt</a></div></main></body></html>""")
open("README.md","w").write("# BestBefore privacy policy\n\nStatic pages served by GitHub Pages: English, Russian (Срокоед) and Norwegian (Matvakt).\n\nSource of truth for the policy text is `build.py`; run `python3 build.py` to regenerate the HTML.\n")
open(".nojekyll","w").write("")
