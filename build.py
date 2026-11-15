import html
ISSUES = "https://github.com/daniil-pastuhov/bestbefore-privacy/issues"
OFF = "https://world.openfoodfacts.org/privacy"
GPS = "https://policies.google.com/privacy"
FIREBASE = "https://firebase.google.com/support/privacy"
CSS = """:root{--bg:#fff;--fg:#1d2420;--mut:#5b6660;--ac:#1f7a4d;--bd:#dfe5e1;--card:#f5f8f6}
@media(prefers-color-scheme:dark){:root{--bg:#121614;--fg:#e6ebe8;--mut:#9aa6a0;--ac:#5fc794;--bd:#2a332e;--card:#1a201d}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:32px 16px 64px}h1{font-size:1.9rem;line-height:1.2;margin:.2em 0}
h2{font-size:1.2rem;margin:2em 0 .4em}p,li{margin:.5em 0}ul{padding-left:1.2em}a{color:var(--ac)}
.mut{color:var(--mut);font-size:.9rem}.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:4px 18px;margin:20px 0}
nav{display:flex;gap:14px;flex-wrap:wrap;font-size:.95rem}nav a[aria-current]{font-weight:700;text-decoration:none;color:var(--fg)}
.langs a{display:block;padding:14px 18px;margin:10px 0;border:1px solid var(--bd);border-radius:12px;background:var(--card);text-decoration:none;font-weight:600}"""

# Icons from the app icon (FoodTrack repo, store-listing/google-play/icon-512.png), on every page.
ICONS = '<link rel="icon" href="favicon.ico" sizes="16x16 32x32 48x48"><link rel="icon" type="image/png" sizes="32x32" href="img/icon-32.png"><link rel="apple-touch-icon" href="img/apple-touch-icon.png">'
NAV = [("en","English"),("ru","Русский"),("nb","Norsk")]
def nav(cur):
    return "<nav>"+" ".join(f'<a href="{c}.html" hreflang="{c}"'+(' aria-current="page"' if c==cur else '')+f'>{n}</a>' for c,n in NAV)+"</nav>"

# Google renamed Vertex AI to Gemini Enterprise Agent Platform; the old data governance page
# (cloud.google.com/vertex-ai/generative-ai/docs/data-governance) now redirects here.
VERTEX = "https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention"
# Email address for privacy requests made privately, kept as character codes (user part and domain
# separately) so that neither this file nor the generated pages contain a harvestable address.
# Both lists are empty until the owner confirms the address; while empty, the Contact sentence is
# left out. To fill in: [ord(c) for c in "user"] and [ord(c) for c in "domain.tld"].
PRIVACY_EMAIL_USER_CODES = [100, 97, 110, 105, 101, 108, 98, 101, 108, 108, 111, 110, 101, 119, 111, 114, 100]
PRIVACY_EMAIL_DOMAIN_CODES = [103, 109, 97, 105, 108, 46, 99, 111, 109]
EMAIL_WORDS = {"en": ("at", "dot"), "ru": ("собака", "точка"), "nb": ("krøllalfa", "punktum")}
def _broken(text):
    # Readable text with an empty element in the middle, so the plain string is not in the source.
    h = len(text) // 2
    return html.escape(text[:h]) + "<span></span>" + html.escape(text[h:])
def private_contact(sentence, lang, eid="pc"):
    """One sentence with the private address: a script turns it into a normal mailto link at load
    time; without JavaScript the text reads e.g. "name at example dot com" in the page's language."""
    if not (PRIVACY_EMAIL_USER_CODES and PRIVACY_EMAIL_DOMAIN_CODES):
        return ""
    at, dot = EMAIL_WORDS[lang]
    user = "".join(map(chr, PRIVACY_EMAIL_USER_CODES))
    domain = "".join(map(chr, PRIVACY_EMAIL_DOMAIN_CODES))
    fallback = _broken(user) + f" {at} " + f" {dot} ".join(_broken(x) for x in domain.split("."))
    js = ("(function(){var e=document.getElementById('" + eid + "');if(!e)return;"
          "var f=function(c){return String.fromCharCode.apply(null,c)},"
          f"a=f({PRIVACY_EMAIL_USER_CODES})+f([64])+f({PRIVACY_EMAIL_DOMAIN_CODES}),"
          "l=document.createElement('a');l.href='mail'+'to:'+a;l.textContent=a;"
          "e.textContent='';e.appendChild(l);})();")
    return " " + sentence.format(f'<span id="{eid}">{fallback}</span><script>{js}</script>')
def L(*items):
    return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"

T = {}
T["en"] = dict(app="BestBefore", title="Privacy Policy", upd="Last updated: 14 November 2026", secs=[
("The short version", ["<p>BestBefore keeps your pantry on your phone. You need no account, and there is no advertising and no analytics. Apart from crash reports (see “Crash reports”), we receive data only from people who buy recipes, and only once they start a purchase (see “Buying recipes”). If you do not buy recipes, nothing changes for you. We do not sell your personal data.</p>"]),
("Who is responsible", ["<p>The data controller is Daniil Pastuhov, Norway: the individual developer who publishes BestBefore and is responsible for the data described in this policy. To reach him, see “Contact”.</p>"]),
("What the app stores", ["<p>Your pantry items, expiry dates, shopping list, settings (including your allergen list and cooking preferences), product photos, saved recipes and any shop locations you save are stored only in the app's local database on your device. They are not sent to us. The one exception is a recipe request from our server, which you send yourself (with “Send all products” on, it includes your whole pantry); see “Recipes from our server”.</p>"]),
("Camera", ["<p>The camera is used to scan barcodes, read printed expiry dates and photograph food items. Recognition runs on your device (Google ML Kit on Android, Apple Vision on iOS). Photos you take are saved only on your device.</p>"]),
("Internet requests", ["<p>When you scan a barcode, the app asks <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a> for the product's name and picture. That request contains the barcode number, and, as with any web request, Open Food Facts' servers can see your IP address. No name, account or device identifier is added by the app. Product pictures are also loaded from Open Food Facts. See their <a href=\""+OFF+"\">privacy policy</a>.</p>"]),
("Crash reports", ["<p>If the app crashes, it sends a crash report to Firebase Crashlytics, a Google service, so we can find and fix the bug. A report contains the technical details of the crash (the stack trace), the device model, the operating system and app versions, free memory and disk space at the time, and a random installation ID that Firebase creates to group reports from the same installation. It contains no pantry items, photos, locations, name or account. Crash reports are not used for advertising or tracking, and are kept for 90 days. See <a href=\""+FIREBASE+"\">Firebase's privacy information</a>.</p>"]),
("Location (optional)", ["<p>Location is off by default. If you turn on shop reminders, you can save a shop's position and the app shows your shopping list when you are near it. Saved positions stay on your device. On Android, nearby-shop detection is performed by Google Play services on your device; see <a href=\""+GPS+"\">Google's privacy policy</a>. You can turn the feature off, or revoke the permission, at any time.</p>"]),
("Notifications, backups and sharing", ["<ul><li>Expiry reminders and digests are scheduled locally on your device.</li><li>Exporting a backup or sharing a shopping list or recipe idea only happens when you choose to, and goes where you send it.</li><li>Your phone's own backup (Google or iCloud) may include the app's data. That is controlled by your device settings, not by us.</li></ul>"]),
("Recipes", ["<p>The Recipe tab can suggest a recipe from the items you tick, in three ways:</p>", L(
  "<b>Share or copy a prompt (free).</b> The app writes a text and hands it to the app you choose, or copies it. We receive nothing. What happens next is up to that app and its own privacy policy.",
  "<b>On this phone (free).</b> On supported phones, the phone's own model writes the recipe (Gemini Nano on Android, Apple Foundation Models on iPhone). Nothing is sent to us.",
  "<b>From our server (paid).</b> You buy recipes in Google Play or the App Store, and our server writes each recipe or three-day menu."),
  "<p>If you turn on <b>Send all products</b> in Recipe settings, the rest of your pantry is also offered to the recipe, as items it may use besides the ones you ticked. It is off unless you turn it on. When it is on, the shared prompt lists those items too, and a recipe from our server sends them as described in “Recipes from our server”; the phone's own model still sends nothing anywhere. Turning it off stops this for later requests.</p>",
  "<p>The next six sections apply only if you start a purchase of recipes.</p>"]),
("Buying recipes", [
  "<p>You buy recipes through Google Play or the App Store. We never see your payment details. Our server checks each purchase with the store and keeps a record of it: the store, the product, the quantity, the number of recipes, whether it was a test purchase, the dates, its state (added, used, refunded), the store's order or transaction number, and the buyer identifiers described under “Refunds”. On Google Play, the store's purchase token is kept only until the purchase is completed; after that, only a scrambled (hashed) form of it stays, as the record's name.</p>",
  "<p>Our server runs on Google Firebase: Authentication, Cloud Functions, Firestore and App Check. Cloud Functions and Firestore run in Google's EU region europe-west1 (Belgium).</p>",
  "<p>When you start a purchase, the app creates an anonymous identifier on our server (a random Firebase user ID). It holds your recipe balance and the numbers of recipes bought, used and refunded. It is not linked to your name or email. When you buy, the app gives the store a code made from this identifier, so that the purchase and any refund can be matched to your balance.</p>",
  "<p>Signing in is optional. You can sign in with Apple or Google on iPhone, and with Google on Android, so your recipes can be used on other phones. Sign in with Apple is not available on Android: to use an account made with Apple on an Android phone, add Google sign-in to it in the iPhone app first. We then keep the account identifier from Apple or Google and your email address (with Sign in with Apple, this may be Apple's relay address). We do not ask for your name: with Sign in with Apple, the app asks Apple only for your email address. With Sign in with Google, Google also passes the name and profile picture link of your Google account to Firebase Authentication. Our server removes them from your account's main record after you sign in, but Firebase Authentication keeps a copy in the record of your Google sign-in until your account is deleted, and we cannot remove that copy separately. We do not use them.</p>",
  "<p>When you sign in with Apple on iPhone, the app also gives our server the one-time code from that sign-in. Our server exchanges it with Apple for a token (a refresh token) and keeps that token, encrypted, solely to remove Apple's link to the app when you delete your account, also if you delete it in the Android app. It is used for nothing else, and it is deleted when your account is deleted or Sign in with Apple is removed from it.</p>",
  "<p>If you sign in on a phone that holds recipes under an anonymous identifier, and you agree, those recipes move to your account and the anonymous identifier is deleted. A record that they were moved, and to which account, stays, so that a later refund reaches the right account.</p>"]),
("Recipes from our server", [
  "<p>When you ask our server for a recipe or a three-day menu, the app sends:</p>", L(
  "the names, best-before dates and quantities of the items you ticked and, if you have turned on “Send all products” in Recipe settings, of all the other items in your pantry, as items the recipe may use (at most 30 items in all). “Send all products” is off unless you turn it on, and turning it off stops this for later requests;",
  "your cooking preferences: difficulty, level of detail, servings, time, meal, diet and language;",
  "the allergen list from Settings;",
  "today's date and a random request number."),
  "<p>Our server passes the items (including any sent with “Send all products”), preferences, allergens and date to Google's Gemini model on Vertex AI, which writes the recipe. No name, email or device identifier is sent to the model. We use Vertex AI's “global” endpoint, so Google may process the request outside the EU/EEA. Google processes it as our service provider under its Google Cloud terms; see <a href=\""+VERTEX+"\">Google's Vertex AI data governance page</a>.</p>",
  "<p>Your allergen list can reveal something about your health, so we treat it as data concerning health. The app sends it to our server only with your explicit consent (GDPR Article 9(2)(a)): before your first recipe request to our server while allergens are set, a short step shows what is sent, why and to whom, and you agree or cancel. The app records your answer, with the date, on your phone. You can withdraw your consent at any time in Recipe → Recipe settings; our server then writes no recipes while allergens are set, because a recipe written without them could be unsafe (the free ways, the phone's own model and the shared prompt, still work and send nothing to us). The allergen list is used only to write the recipe and to check the answer, and it is not stored.</p>",
  "<p>Our server checks requests and answers automatically, to stop the model being misused: it refuses item or allergen names that do not look like food names, and answers that contain, for example, links, contact details, an allergen from your list or text that is not about cooking. A refused name or answer is not stored or logged. Our server counts refused attempts under your identifier for the current day and logs the rule that refused them with a scrambled (hashed) form of your identifier; after several in one day, recipe requests from your account are refused until the next day.</p>",
  "<p>We do not log or keep what you send, neither the items you ticked nor the rest of your pantry. Our server keeps only a fingerprint (a hash) of the request, so that a repeated request can be recognised and is not charged twice. The recipe or menu written back, which names the ingredients it uses, is kept on our server for 7 days, so that the app can still collect it if the connection is lost. Then it is deleted automatically (Google's automatic deletion usually runs within a day after that). The app saves the recipe on your phone, where it stays until you delete it.</p>"]),
("Technical data for buyers", [L(
  "<b>App Check.</b> With each request to our server, the app proves that it is a genuine copy, through Firebase App Check: with Google Play Integrity on Android and Apple App Attest on iPhone. This starts only when you start a purchase.",
  "<b>IP address.</b> Our server uses your IP address to limit how many requests one source can send in a minute. It counts requests per address for the current minute in memory only, and does not store the address. Google's infrastructure also records each request to our server, with its IP address, in our server's technical logs.",
  "<b>Usage counts.</b> For each recipe request, our server logs one line with a scrambled (hashed) form of your identifier, the kind of request, how much text the model read and wrote (tokens), the result and the estimated cost. The line never contains your items, allergens, the prompt or the recipe. Our server also keeps, under your identifier, the number of requests, refused attempts and the estimated cost in the current minute and day, to apply limits.",
  "<b>Daily totals.</b> Our server keeps daily totals for all users together (requests, recipes, estimated cost), with no user data.",
  "<b>Technical logs</b> are kept by Google Cloud Logging for 30 days.",
  "<b>Crash reports</b>, as described in “Crash reports”.")]),
("Refunds", [
  "<p>Google Play and the App Store tell our server when a purchase is refunded, and the refunded recipes are taken off your balance. If you had already used them, your balance can go below zero.</p>",
  "<p>On the App Store, the purchase sheet tells you before you buy that if you ask Apple for a refund, we tell Apple how many of the recipes you have used. For a purchase made after you saw this, we record that you saw it, and when. If you then ask Apple for a refund, Apple asks us about the purchase, and we tell Apple that the recipes were delivered and what share of the purchase you have used. For other purchases we tell Apple nothing.</p>",
  "<p>If purchases are refunded again and again after the recipes were used, buying recipes is switched off for that buyer; recipes already bought can still be used. To do this, each purchase is recorded with buyer identifiers: on the App Store, an identifier Apple gives this app for your Apple account (its app transaction ID); on Google Play, your identifier on our server and a scrambled (hashed) form of each Apple or Google account identifier linked to your account, if any. When a refund takes recipes that were already used, we keep a record of it under those identifiers: the purchase, the date, the store and the number of used recipes refunded.</p>"]),
("Deleting your account", [
  "<p>You can delete your account in the app: Recipe tab → Recipe settings → Account → Delete account. If you are signed in, you sign in once more first. If you bought recipes without signing in, use Recipe settings → Your recipes → Delete my data from our server, if your version of the app has this option. You can also ask us by email, without the app; see <a href=\"delete.html#en\">Delete your account and data</a>. When an account is deleted:</p>", L(
  "your sign-in and email address are deleted from our server (with Sign in with Google, also the copy of the Google name and picture link that Firebase Authentication kept). If your account uses Sign in with Apple, our server also asks Apple to revoke the app's access to your Apple Account, whether you delete the account in the iPhone app or the Android app, and deletes the token it kept for this. If that does not succeed (for example, Apple cannot be reached, or you last signed in with Apple before we started keeping this token), the app tells you, and you can remove the link yourself in your Apple Account settings, under Sign in with Apple;",
  "the recipes and menus kept on our server, and the per-minute and per-day counts, are deleted;",
  "your unused recipes are lost and cannot be refunded."),
  "<p>What stays, and why:</p>", L(
  "every purchase record, no longer linked to your account. It holds no name or email, but it keeps your old identifier, the buyer identifiers (see “Refunds”) and the store's order or transaction number, which Apple or Google can link to you. It is the only way to stop one store purchase being added twice, and we need it to handle later refunds and for our accounts;",
  "a closed record under your old identifier, with the date of deletion, the number of recipes lost and the totals of recipes bought, used and refunded, the counts behind the refund and misuse limits, and the buyer identifiers. It stops a deleted account being used again, and keeps our accounts correct;",
  "a record of refunds after use, if there is one (see “Refunds”), to prevent fraud. It is not deleted;",
  "technical logs until they expire after 30 days, and the daily totals, which hold no user data."),
  "<p>Deleting the app does not delete anything on our server. If you never signed in, the unused recipes are then lost, and we can find your identifier later only from the order number on the store's receipt for a purchase made with it. Saved recipes and your pantry stay on your phone until you delete them.</p>"]),
("Who receives data, and where", [L(
  "<b>Google</b>, as our service provider: Firebase (Authentication, App Check, Cloud Functions, Firestore, Crashlytics), Google Cloud Logging and Vertex AI (Gemini). Google Play handles purchases and refunds on Android, and Play Integrity checks the app.",
  "<b>Apple</b>: the App Store handles purchases and refunds on iPhone, and receives the information described under “Refunds” if you ask Apple for a refund; App Attest checks the app; Sign in with Apple on iPhone, if you use it, including exchanging and revoking the token described under “Buying recipes”.",
  "<b>Open Food Facts</b>, for barcode lookups, as described above."),
  "<p>We do not show ads, do not use analytics and do not sell your data. Cloud Functions and Firestore are in the EU. Vertex AI's global endpoint, Firebase Authentication, App Check and Crashlytics may process data outside the EU/EEA, for example in the United States. Google covers such transfers in its data processing terms, which include the EU's standard contractual clauses.</p>"]),
("Legal bases", ["<p>Under the GDPR, we rely on:</p>", L(
  "<b>contract</b> (Article 6(1)(b)): to check your purchases, hold your recipes and your sign-in, write the recipes you ask for, and keep the Sign in with Apple token needed to remove Apple's link when you delete your account;",
  "<b>explicit consent</b> (Article 6(1)(a) and Article 9(2)(a)): sending your allergen list with a recipe request to our server and to Google's model. You can withdraw it at any time in Recipe settings; this does not affect requests made before;",
  "<b>legitimate interests</b> (Article 6(1)(f)): crash reports, App Check, rate limits, usage counts, the automatic checks of requests and answers, refund records and answering Apple's questions about a refund, to keep the service working and to prevent fraud and abuse; and keeping purchase records after an account is deleted, so that one purchase cannot be used twice;",
  "<b>legal obligation</b> (Article 6(1)(c)): keeping the records we need for accounting.")]),
("Children", ["<p>The app is not directed at children. Apart from the crash reports and, for people who buy recipes, the data described above, we do not knowingly collect data from anyone.</p>"]),
("Your control and your rights", ["<p>You can edit or delete any item inside the app. Uninstalling the app deletes its data from your device. If you bought recipes, you can delete your account as described in “Deleting your account”, in the app or by email: see <a href=\"delete.html#en\">Delete your account and data</a>.</p>",
  "<p>You have the right to ask for a copy of your data, to have it corrected or deleted, to restrict or object to its use, and to complain to the data protection authority where you live (in Norway, Datatilsynet). To use these rights, contact us (see “Contact”). If you never signed in, we can tell which data is yours only from the order number on a store receipt for one of your purchases.</p>"]),
("Changes", ["<p>If this policy changes, the new version will be published on this page with an updated date.</p>"]),
("Contact", ["<p>Questions or requests? <a href=\""+ISSUES+"\">Open an issue</a> on GitHub. Issues are public, so do not put your email address or other personal details in them."+private_contact("For a privacy request you would rather not make in public, email {}.", "en")+"</p>"]),
], home="Choose your language")

T["ru"] = dict(app="Срокоед", title="Политика конфиденциальности", upd="Последнее обновление: 14 ноября 2026 г.", secs=[
("Коротко", ["<p>Срокоед хранит ваши продукты на вашем телефоне. Аккаунт не нужен, рекламы и аналитики нет. Помимо отчётов о сбоях (см. «Отчёты о сбоях»), мы получаем данные только от тех, кто покупает рецепты, и только после того, как покупка начата (см. «Покупка рецептов»). Если вы не покупаете рецепты, для вас ничего не меняется. Мы не продаём ваши персональные данные.</p>"]),
("Кто отвечает за данные", ["<p>Оператор (контролёр) данных — Daniil Pastuhov, Норвегия: частный разработчик, который публикует Срокоед и отвечает за данные, описанные в этой политике. Как с ним связаться, см. «Контакты».</p>"]),
("Что хранит приложение", ["<p>Продукты, сроки годности, список покупок, настройки (включая список аллергенов и предпочтения в готовке), фотографии продуктов, сохранённые рецепты и сохранённые вами магазины хранятся только в локальной базе данных приложения на вашем устройстве. Они не отправляются нам. Единственное исключение — запрос рецепта с нашего сервера, который вы отправляете сами (если включено «Отправлять все продукты», в нём все ваши продукты); см. «Рецепты с нашего сервера».</p>"]),
("Камера", ["<p>Камера используется для сканирования штрихкодов, распознавания напечатанных сроков годности и фотографирования продуктов. Распознавание выполняется на устройстве (Google ML Kit на Android, Apple Vision на iOS). Сделанные фотографии сохраняются только на вашем устройстве.</p>"]),
("Запросы в интернет", ["<p>Когда вы сканируете штрихкод, приложение запрашивает у <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a> название и изображение продукта. Запрос содержит номер штрихкода, а серверы Open Food Facts, как и любого сайта, видят ваш IP-адрес. Приложение не добавляет имя, аккаунт или идентификатор устройства. Изображения продуктов тоже загружаются с Open Food Facts. См. их <a href=\""+OFF+"\">политику конфиденциальности</a>.</p>"]),
("Отчёты о сбоях", ["<p>Если приложение аварийно завершится, оно отправит отчёт о сбое в Firebase Crashlytics, сервис Google, чтобы мы могли найти и исправить ошибку. Отчёт содержит технические сведения о сбое (трассировку стека), модель устройства, версии операционной системы и приложения, объём свободной памяти и места на диске в момент сбоя, а также случайный идентификатор установки, который Firebase создаёт, чтобы объединять отчёты одной установки. В отчёте нет ваших продуктов, фотографий, мест, имени или аккаунта. Отчёты о сбоях не используются для рекламы или отслеживания и хранятся 90 дней. См. <a href=\""+FIREBASE+"\">сведения Firebase о конфиденциальности</a>.</p>"]),
("Местоположение (по желанию)", ["<p>По умолчанию местоположение отключено. Если вы включите напоминания у магазинов, вы можете сохранить положение магазина, и приложение покажет список покупок, когда вы рядом. Сохранённые места остаются на вашем устройстве. На Android определение близости к магазину выполняют сервисы Google Play на вашем устройстве; см. <a href=\""+GPS+"\">политику конфиденциальности Google</a>. Функцию можно отключить, а разрешение отозвать в любой момент.</p>"]),
("Уведомления, резервные копии и обмен", ["<ul><li>Напоминания о сроках и сводки планируются локально на вашем устройстве.</li><li>Экспорт резервной копии и отправка списка покупок или идеи рецепта происходят только по вашему действию и попадают туда, куда вы их отправите.</li><li>Резервная копия самого телефона (Google или iCloud) может включать данные приложения. Это определяется настройками устройства, а не нами.</li></ul>"]),
("Рецепты", ["<p>Во вкладке «Рецепт» можно получить рецепт из отмеченных продуктов тремя способами:</p>", L(
  "<b>Отправить или скопировать запрос (бесплатно).</b> Приложение составляет текст и передаёт его в выбранное вами приложение или копирует его. Мы ничего не получаем. Что будет дальше, зависит от того приложения и его политики конфиденциальности.",
  "<b>На этом телефоне (бесплатно).</b> На поддерживаемых телефонах рецепт пишет собственная модель телефона (Gemini Nano на Android, Apple Foundation Models на iPhone). Нам ничего не отправляется.",
  "<b>С нашего сервера (платно).</b> Вы покупаете рецепты в Google Play или App Store, и каждый рецепт или меню на три дня пишет наш сервер."),
  "<p>Если в «Настройках рецептов» включить <b>«Отправлять все продукты»</b>, рецепту предлагаются и остальные продукты из вашей кладовой — те, которые он может использовать помимо отмеченных. По умолчанию эта настройка выключена. Когда она включена, общий запрос перечисляет и эти продукты, а рецепт с нашего сервера отправляет их, как описано в разделе «Рецепты с нашего сервера»; собственная модель телефона по-прежнему ничего никуда не отправляет. Если выключить настройку, последующие запросы отправляются уже без них.</p>",
  "<p>Следующие шесть разделов касаются вас, только если вы начали покупку рецептов.</p>"]),
("Покупка рецептов", [
  "<p>Рецепты покупаются через Google Play или App Store. Платёжные данные мы никогда не видим. Наш сервер проверяет каждую покупку в магазине и хранит запись о ней: магазин, товар, количество, число рецептов, была ли это тестовая покупка, даты, состояние (зачислена, использована, возвращена), номер заказа или транзакции в магазине и идентификаторы покупателя, описанные в разделе «Возвраты». В Google Play токен покупки хранится только до завершения покупки; после этого остаётся лишь его необратимо преобразованная (хешированная) форма в качестве имени записи.</p>",
  "<p>Наш сервер работает на Google Firebase: Authentication, Cloud Functions, Firestore и App Check. Cloud Functions и Firestore работают в регионе Google в ЕС europe-west1 (Бельгия).</p>",
  "<p>Когда вы начинаете покупку, приложение создаёт на нашем сервере анонимный идентификатор (случайный идентификатор пользователя Firebase). К нему привязаны ваш баланс рецептов и число купленных, использованных и возвращённых рецептов. Он не связан с вашим именем или адресом электронной почты. При покупке приложение передаёт магазину код, полученный из этого идентификатора, чтобы покупку и возможный возврат можно было сопоставить с вашим балансом.</p>",
  "<p>Входить в аккаунт не обязательно. На iPhone можно войти через Apple или Google, на Android — через Google, чтобы пользоваться рецептами на других телефонах. Вход через Apple на Android недоступен: чтобы пользоваться на телефоне с Android аккаунтом, созданным через Apple, сначала добавьте к нему вход через Google в приложении на iPhone. Тогда мы храним идентификатор аккаунта Apple или Google и ваш адрес электронной почты (при входе через Apple это может быть адрес-посредник Apple). Мы не спрашиваем ваше имя: при входе через Apple приложение запрашивает у Apple только адрес электронной почты. При входе через Google Google также передаёт имя и ссылку на фото профиля вашего аккаунта Google в Firebase Authentication. После входа наш сервер удаляет их из основной записи вашего аккаунта, но Firebase Authentication хранит их копию в записи о входе через Google, пока аккаунт не будет удалён, и отдельно удалить эту копию мы не можем. Мы их не используем.</p>",
  "<p>Когда вы входите через Apple на iPhone, приложение также передаёт нашему серверу одноразовый код этого входа. Наш сервер обменивает его у Apple на токен (refresh token) и хранит этот токен в зашифрованном виде только для того, чтобы удалить связь Apple с приложением, когда вы удаляете аккаунт, в том числе если вы удаляете его в приложении для Android. Ни для чего другого он не используется и удаляется, когда удаляется ваш аккаунт или из него убирают вход через Apple.</p>",
  "<p>Если вы входите на телефоне, где есть рецепты под анонимным идентификатором, и соглашаетесь, эти рецепты переносятся в ваш аккаунт, а анонимный идентификатор удаляется. Остаётся запись о том, что они перенесены, и в какой аккаунт, чтобы последующий возврат попал в нужный аккаунт.</p>"]),
("Рецепты с нашего сервера", [
  "<p>Когда вы запрашиваете у нашего сервера рецепт или меню на три дня, приложение отправляет:</p>", L(
  "названия, сроки годности и количество отмеченных продуктов, а если в «Настройках рецептов» включено «Отправлять все продукты», — и всех остальных продуктов из вашей кладовой, которые рецепт может использовать (всего не более 30 продуктов). Эта настройка выключена, пока вы сами её не включите, а после выключения последующие запросы отправляются без остальных продуктов;",
  "ваши предпочтения в готовке: сложность, подробность, число порций, время, приём пищи, диету и язык;",
  "список аллергенов из настроек;",
  "сегодняшнюю дату и случайный номер запроса."),
  "<p>Наш сервер передаёт продукты (в том числе отправленные с настройкой «Отправлять все продукты»), предпочтения, аллергены и дату модели Google Gemini в Vertex AI, которая пишет рецепт. Имя, адрес электронной почты или идентификатор устройства модели не отправляются. Мы используем «глобальную» точку доступа Vertex AI (global), поэтому Google может обрабатывать запрос за пределами ЕС/ЕЭЗ. Google обрабатывает его как наш поставщик услуг по условиям Google Cloud; см. <a href=\""+VERTEX+"\">страницу Google об управлении данными в Vertex AI</a>.</p>",
  "<p>Список аллергенов может кое-что сказать о вашем здоровье, поэтому мы относимся к нему как к данным о здоровье. Приложение отправляет его на наш сервер только с вашего явного согласия (статья 9(2)(a) GDPR): перед первым запросом рецепта к нашему серверу, когда заданы аллергены, короткий шаг показывает, что отправляется, зачем и кому, и вы соглашаетесь или отменяете. Приложение сохраняет ваш ответ с датой на телефоне. Отозвать согласие можно в любое время в разделе «Рецепт» → «Настройки рецептов»; тогда наш сервер не пишет рецепты, пока заданы аллергены, потому что рецепт без их учёта может быть небезопасным (бесплатные способы — собственная модель телефона и общий запрос — продолжают работать и ничего нам не отправляют). Список аллергенов используется только для того, чтобы написать рецепт и проверить ответ, и не хранится.</p>",
  "<p>Наш сервер автоматически проверяет запросы и ответы, чтобы модель нельзя было использовать не по назначению: он отклоняет названия продуктов или аллергенов, не похожие на названия продуктов, и ответы, в которых есть, например, ссылки, контактные данные, аллерген из вашего списка или текст не о готовке. Отклонённое название или ответ не хранится и не записывается в журналы. Наш сервер считает отклонённые попытки под вашим идентификатором за текущий день и записывает в журнал правило, по которому они отклонены, вместе с необратимо преобразованной (хешированной) формой вашего идентификатора; после нескольких таких попыток за день запросы рецептов от вашего аккаунта отклоняются до следующего дня.</p>",
  "<p>Мы не записываем в журналы и не храним то, что вы отправляете, — ни отмеченные продукты, ни остальные. Наш сервер хранит только отпечаток (хеш) запроса, чтобы повторный запрос можно было узнать и не списать за него дважды. Полученный рецепт или меню, где названы использованные продукты, хранится на нашем сервере 7 дней, чтобы приложение могло забрать его, если связь прервалась. Затем он удаляется автоматически (автоматическое удаление Google обычно происходит в течение суток после этого). Приложение сохраняет рецепт на вашем телефоне, где он остаётся, пока вы его не удалите.</p>"]),
("Технические данные покупателей", [L(
  "<b>App Check.</b> При каждом запросе к нашему серверу приложение подтверждает, что это подлинная копия, через Firebase App Check: с помощью Google Play Integrity на Android и Apple App Attest на iPhone. Это начинается только тогда, когда вы начинаете покупку.",
  "<b>IP-адрес.</b> Наш сервер использует ваш IP-адрес, чтобы ограничить число запросов от одного источника в минуту. Он считает запросы с каждого адреса за текущую минуту только в памяти и не сохраняет адрес. Инфраструктура Google также записывает каждый запрос к нашему серверу вместе с IP-адресом в технические журналы нашего сервера.",
  "<b>Учёт использования.</b> Для каждого запроса рецепта наш сервер записывает в журнал одну строку с необратимо преобразованной (хешированной) формой вашего идентификатора, видом запроса, объёмом текста, который модель прочитала и написала (токены), результатом и оценочной стоимостью. В строке никогда нет ваших продуктов, аллергенов, запроса к модели или рецепта. Кроме того, наш сервер хранит под вашим идентификатором число запросов, отклонённых попыток и оценочную стоимость за текущую минуту и день, чтобы применять ограничения.",
  "<b>Дневные итоги.</b> Наш сервер хранит дневные итоги по всем пользователям вместе (запросы, рецепты, оценочная стоимость) без данных пользователей.",
  "<b>Технические журналы</b> хранятся в Google Cloud Logging 30 дней.",
  "<b>Отчёты о сбоях</b> — как описано в разделе «Отчёты о сбоях».")]),
("Возвраты", [
  "<p>Google Play и App Store сообщают нашему серверу, когда за покупку возвращены деньги, и возвращённые рецепты списываются с вашего баланса. Если вы уже их использовали, баланс может стать отрицательным.</p>",
  "<p>В App Store окно покупки до оплаты сообщает, что если вы попросите Apple вернуть деньги, мы сообщим Apple, сколько из этих рецептов вы использовали. Для покупки, сделанной после того, как вы это увидели, мы записываем, что вы это видели, и когда. Если затем вы просите Apple вернуть деньги, Apple спрашивает нас об этой покупке, и мы сообщаем Apple, что рецепты были предоставлены и какую долю покупки вы использовали. О других покупках мы Apple ничего не сообщаем.</p>",
  "<p>Если деньги за покупки возвращают снова и снова после того, как рецепты были использованы, покупка рецептов для этого покупателя отключается; уже купленными рецептами по-прежнему можно пользоваться. Для этого каждая покупка записывается с идентификаторами покупателя: в App Store — идентификатор, который Apple выдаёт этому приложению для вашего аккаунта Apple (его app transaction ID); в Google Play — ваш идентификатор на нашем сервере и необратимо преобразованная (хешированная) форма каждого идентификатора аккаунта Apple или Google, связанного с вашим аккаунтом, если такие есть. Когда возврат забирает уже использованные рецепты, мы храним запись об этом под этими идентификаторами: покупку, дату, магазин и число возвращённых использованных рецептов.</p>"]),
("Удаление аккаунта", [
  "<p>Удалить аккаунт можно в приложении: вкладка «Рецепт» → «Настройки рецептов» → «Аккаунт» → «Удалить аккаунт». Если вы вошли в аккаунт, сначала нужно войти ещё раз. Если вы покупали рецепты без входа, откройте «Настройки рецептов» → «Ваши рецепты» → «Удалить мои данные с сервера», если в вашей версии приложения есть такая возможность. Можно также попросить нас об удалении по электронной почте, без приложения; см. <a href=\"delete.html#ru\">Удаление аккаунта и данных</a>. При удалении аккаунта:</p>", L(
  "ваш вход и адрес электронной почты удаляются с нашего сервера (при входе через Google — также копия имени и ссылки на фото из Google, которую хранил Firebase Authentication). Если ваш аккаунт использует вход через Apple, наш сервер также просит Apple отозвать доступ приложения к вашему Аккаунту Apple — удаляете ли вы аккаунт в приложении на iPhone или в приложении для Android — и удаляет токен, который хранил для этого. Если это не удалось (например, Apple недоступна или вы в последний раз входили через Apple до того, как мы начали хранить этот токен), приложение сообщит об этом, и связь можно убрать самостоятельно в настройках Аккаунта Apple, в разделе «Вход с Apple»;",
  "рецепты и меню, хранящиеся на нашем сервере, а также счётчики за минуту и день удаляются;",
  "неиспользованные рецепты теряются, и деньги за них не возвращаются."),
  "<p>Что остаётся и почему:</p>", L(
  "все записи о покупках, уже не связанные с вашим аккаунтом. В них нет имени или адреса электронной почты, но остаются ваш прежний идентификатор, идентификаторы покупателя (см. «Возвраты») и номер заказа или транзакции в магазине, по которому Apple или Google могут связать покупку с вами. Это единственный способ не дать зачислить одну покупку дважды, и эти записи нужны нам для обработки последующих возвратов и для бухгалтерии;",
  "закрытая запись под вашим прежним идентификатором с датой удаления, числом потерянных рецептов и итогами купленных, использованных и возвращённых рецептов, счётчиками для ограничений по возвратам и злоупотреблениям и идентификаторами покупателя. Она не даёт снова пользоваться удалённым аккаунтом и сохраняет нашу отчётность верной;",
  "запись о возвратах после использования, если она есть (см. «Возвраты»), для предотвращения мошенничества. Она не удаляется;",
  "технические журналы, пока они не истекут через 30 дней, и дневные итоги, в которых нет данных пользователей."),
  "<p>Удаление приложения ничего не удаляет на нашем сервере. Если вы ни разу не входили в аккаунт, неиспользованные рецепты при этом теряются, а найти ваш идентификатор потом мы сможем только по номеру заказа из чека магазина за покупку, сделанную под ним. Сохранённые рецепты и ваши продукты остаются на телефоне, пока вы их не удалите.</p>"]),
("Кто получает данные и где", [L(
  "<b>Google</b> как наш поставщик услуг: Firebase (Authentication, App Check, Cloud Functions, Firestore, Crashlytics), Google Cloud Logging и Vertex AI (Gemini). Google Play обрабатывает покупки и возвраты на Android, а Play Integrity проверяет приложение.",
  "<b>Apple</b>: App Store обрабатывает покупки и возвраты на iPhone и получает сведения, описанные в разделе «Возвраты», если вы просите Apple вернуть деньги; App Attest проверяет приложение; вход через Apple на iPhone, если вы им пользуетесь, включая обмен и отзыв токена, описанные в разделе «Покупка рецептов».",
  "<b>Open Food Facts</b> — для поиска по штрихкоду, как описано выше."),
  "<p>Мы не показываем рекламу, не используем аналитику и не продаём ваши данные. Cloud Functions и Firestore находятся в ЕС. Глобальная точка доступа Vertex AI, Firebase Authentication, App Check и Crashlytics могут обрабатывать данные за пределами ЕС/ЕЭЗ, например в США. Google обеспечивает такие передачи своими условиями обработки данных, которые включают стандартные договорные положения ЕС.</p>"]),
("Правовые основания", ["<p>Согласно GDPR, мы опираемся на:</p>", L(
  "<b>договор</b> (статья 6(1)(b)): чтобы проверять ваши покупки, хранить ваши рецепты и ваш вход, писать рецепты, которые вы запрашиваете, и хранить токен входа через Apple, нужный, чтобы удалить связь с Apple при удалении аккаунта;",
  "<b>явное согласие</b> (статья 6(1)(a) и статья 9(2)(a)): отправка списка аллергенов вместе с запросом рецепта на наш сервер и модели Google. Его можно отозвать в любое время в настройках рецептов; это не затрагивает уже сделанные запросы;",
  "<b>законные интересы</b> (статья 6(1)(f)): отчёты о сбоях, App Check, ограничения частоты запросов, учёт использования, автоматические проверки запросов и ответов, записи о возвратах и ответы на вопросы Apple о возврате — чтобы сервис работал и чтобы предотвращать мошенничество и злоупотребления; а также хранение записей о покупках после удаления аккаунта, чтобы одну покупку нельзя было использовать дважды;",
  "<b>юридическую обязанность</b> (статья 6(1)(c)): хранение записей, нужных для бухгалтерии.")]),
("Дети", ["<p>Приложение не предназначено для детей. Помимо отчётов о сбоях и, для тех, кто покупает рецепты, данных, описанных выше, мы сознательно не собираем ничьих данных.</p>"]),
("Ваш контроль и ваши права", ["<p>Любой продукт можно изменить или удалить прямо в приложении. При удалении приложения его данные удаляются с вашего устройства. Если вы покупали рецепты, вы можете удалить аккаунт, как описано в разделе «Удаление аккаунта», — в приложении или по электронной почте: см. <a href=\"delete.html#ru\">Удаление аккаунта и данных</a>.</p>",
  "<p>Вы вправе запросить копию своих данных, потребовать их исправить или удалить, ограничить их использование или возразить против него, а также подать жалобу в орган по защите данных по месту жительства (в Норвегии — Datatilsynet). Чтобы воспользоваться этими правами, свяжитесь с нами (см. «Контакты»). Если вы ни разу не входили в аккаунт, понять, какие данные ваши, мы можем только по номеру заказа из чека магазина за одну из ваших покупок.</p>"]),
("Изменения", ["<p>Если политика изменится, новая версия будет опубликована на этой странице с обновлённой датой.</p>"]),
("Контакты", ["<p>Есть вопросы или запросы? <a href=\""+ISSUES+"\">Создайте обращение (issue)</a> на GitHub. Обращения публичны, поэтому не указывайте в них адрес электронной почты и другие личные данные."+private_contact("Если вы не хотите отправлять запрос о персональных данных публично, напишите на {}.", "ru")+"</p>"]),
], home="Выберите язык")

T["nb"] = dict(app="Matvakt", title="Personvernerklæring", upd="Sist oppdatert: 14. november 2026", secs=[
("Kort fortalt", ["<p>Matvakt oppbevarer matvarene dine på telefonen din. Du trenger ingen konto, og det finnes ingen reklame og ingen analyse. Utenom krasjrapporter (se «Krasjrapporter») mottar vi data bare fra dem som kjøper oppskrifter, og bare etter at de har startet et kjøp (se «Kjøp av oppskrifter»). Kjøper du ikke oppskrifter, endres ingenting for deg. Vi selger ikke personopplysningene dine.</p>"]),
("Hvem som er ansvarlig", ["<p>Behandlingsansvarlig er Daniil Pastuhov, Norge: enkeltpersonen som utvikler og publiserer Matvakt, og som er ansvarlig for dataene som er beskrevet i denne erklæringen. Se «Kontakt» for hvordan du når ham.</p>"]),
("Hva appen lagrer", ["<p>Matvarer, utløpsdatoer, handleliste, innstillinger (også allergenlisten og matlagingsvalgene dine), bilder av produkter, lagrede oppskrifter og butikker du har lagret, lagres bare i appens lokale database på enheten din. De sendes ikke til oss. Det eneste unntaket er en forespørsel om oppskrift fra serveren vår, som du sender selv (med «Send alle varer» på inneholder den alle matvarene dine); se «Oppskrifter fra serveren vår».</p>"]),
("Kamera", ["<p>Kameraet brukes til å skanne strekkoder, lese påtrykte utløpsdatoer og ta bilder av matvarer. Gjenkjenningen skjer på enheten (Google ML Kit på Android, Apple Vision på iOS). Bilder du tar lagres bare på enheten din.</p>"]),
("Internett-forespørsler", ["<p>Når du skanner en strekkode, henter appen produktets navn og bilde fra <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a>. Forespørselen inneholder strekkodenummeret, og som ved alle nettforespørsler kan Open Food Facts' servere se IP-adressen din. Appen legger ikke til navn, konto eller enhetsidentifikator. Produktbilder lastes også fra Open Food Facts. Se deres <a href=\""+OFF+"\">personvernerklæring</a>.</p>"]),
("Krasjrapporter", ["<p>Hvis appen krasjer, sender den en krasjrapport til Firebase Crashlytics, en tjeneste fra Google, slik at vi kan finne og rette feilen. Rapporten inneholder tekniske detaljer om krasjet (stakksporing), enhetsmodell, versjon av operativsystemet og appen, ledig minne og lagringsplass da krasjet skjedde, og en tilfeldig installasjons-ID som Firebase lager for å gruppere rapporter fra samme installasjon. Den inneholder ingen matvarer, bilder, posisjoner, navn eller konto. Krasjrapporter brukes ikke til reklame eller sporing, og lagres i 90 dager. Se <a href=\""+FIREBASE+"\">Firebases personverninformasjon</a>.</p>"]),
("Posisjon (valgfritt)", ["<p>Posisjon er slått av som standard. Slår du på butikkpåminnelser, kan du lagre posisjonen til en butikk, og appen viser handlelisten når du er i nærheten. Lagrede posisjoner blir på enheten din. På Android utføres oppdagelsen av nærliggende butikker av Google Play-tjenester på enheten din; se <a href=\""+GPS+"\">Googles personvernerklæring</a>. Du kan slå av funksjonen eller trekke tilbake tillatelsen når som helst.</p>"]),
("Varsler, sikkerhetskopier og deling", ["<ul><li>Påminnelser om utløpsdatoer og sammendrag planlegges lokalt på enheten din.</li><li>Eksport av sikkerhetskopi og deling av handleliste eller oppskriftsidé skjer bare når du velger det, og går dit du sender det.</li><li>Telefonens egen sikkerhetskopi (Google eller iCloud) kan inneholde appens data. Det styres av enhetens innstillinger, ikke av oss.</li></ul>"]),
("Oppskrifter", ["<p>I Oppskrift-fanen kan du få en oppskrift ut fra varene du krysser av, på tre måter:</p>", L(
  "<b>Del eller kopier en ledetekst (gratis).</b> Appen skriver en tekst og gir den til appen du velger, eller kopierer den. Vi mottar ingenting. Hva som skjer videre, avgjøres av den appen og dens egen personvernerklæring.",
  "<b>På denne telefonen (gratis).</b> På telefoner som støtter det, skriver telefonens egen modell oppskriften (Gemini Nano på Android, Apple Foundation Models på iPhone). Ingenting sendes til oss.",
  "<b>Fra serveren vår (betalt).</b> Du kjøper oppskrifter i Google Play eller App Store, og serveren vår skriver hver oppskrift eller meny for tre dager."),
  "<p>Slår du på <b>Send alle varer</b> i Oppskriftsinnstillinger, tilbys også resten av matvarene dine til oppskriften, som varer den kan bruke i tillegg til dem du har krysset av. Det er av med mindre du slår det på. Når det er på, tar den delte ledeteksten også med disse varene, og en oppskrift fra serveren vår sender dem som beskrevet under «Oppskrifter fra serveren vår»; telefonens egen modell sender fortsatt ingenting noe sted. Slår du det av, sendes de ikke med senere forespørsler.</p>",
  "<p>De neste seks avsnittene gjelder bare hvis du starter et kjøp av oppskrifter.</p>"]),
("Kjøp av oppskrifter", [
  "<p>Du kjøper oppskrifter gjennom Google Play eller App Store. Vi ser aldri betalingsopplysningene dine. Serveren vår kontrollerer hvert kjøp hos butikken og tar vare på en oversikt over det: butikken, produktet, antallet, antall oppskrifter, om det var et testkjøp, datoene, tilstanden (lagt til, brukt, refundert), butikkens ordre- eller transaksjonsnummer og kjøperidentifikatorene som er beskrevet under «Refusjoner». I Google Play lagres butikkens kjøpstoken bare til kjøpet er fullført; deretter er det bare en enveis omgjort (hashet) form av den som blir igjen, som navnet på oppføringen.</p>",
  "<p>Serveren vår kjører på Google Firebase: Authentication, Cloud Functions, Firestore og App Check. Cloud Functions og Firestore kjører i Googles EU-region europe-west1 (Belgia).</p>",
  "<p>Når du starter et kjøp, oppretter appen en anonym identifikator på serveren vår (en tilfeldig Firebase-bruker-ID). Den holder saldoen din av oppskrifter og antallet oppskrifter som er kjøpt, brukt og refundert. Den er ikke knyttet til navnet eller e-postadressen din. Når du kjøper, gir appen butikken en kode laget av denne identifikatoren, slik at kjøpet og en eventuell refusjon kan kobles til saldoen din.</p>",
  "<p>Innlogging er valgfritt. Du kan logge inn med Apple eller Google på iPhone, og med Google på Android, slik at oppskriftene kan brukes på andre telefoner. Logg på med Apple finnes ikke på Android: for å bruke en konto laget med Apple på en Android-telefon, legger du først til innlogging med Google på den i iPhone-appen. Da tar vi vare på kontoidentifikatoren fra Apple eller Google og e-postadressen din (med Logg på med Apple kan dette være Apples videresendingsadresse). Vi spør ikke om navnet ditt: med Logg på med Apple ber appen Apple bare om e-postadressen din. Med Logg på med Google sender Google også navnet og lenken til profilbildet på Google-kontoen din til Firebase Authentication. Serveren vår fjerner dem fra hovedoppføringen for kontoen din etter at du har logget inn, men Firebase Authentication beholder en kopi i oppføringen for Google-innloggingen din til kontoen slettes, og den kopien kan vi ikke fjerne for seg. Vi bruker dem ikke.</p>",
  "<p>Når du logger inn med Apple på iPhone, gir appen også serveren vår engangskoden fra den innloggingen. Serveren vår bytter den hos Apple mot et token (et refresh token) og tar vare på det, kryptert, bare for å fjerne Apples kobling til appen når du sletter kontoen din, også hvis du sletter den i Android-appen. Det brukes ikke til noe annet, og det slettes når kontoen din slettes eller Logg på med Apple fjernes fra den.</p>",
  "<p>Hvis du logger inn på en telefon som har oppskrifter under en anonym identifikator, og du samtykker, flyttes de oppskriftene til kontoen din, og den anonyme identifikatoren slettes. En oppføring om at de ble flyttet, og til hvilken konto, blir værende, slik at en senere refusjon havner på riktig konto.</p>"]),
("Oppskrifter fra serveren vår", [
  "<p>Når du ber serveren vår om en oppskrift eller en meny for tre dager, sender appen:</p>", L(
  "navnene, utløpsdatoene og antallet av varene du krysset av, og hvis du har slått på «Send alle varer» i Oppskriftsinnstillinger, også av alle de andre matvarene dine, som varer oppskriften kan bruke (høyst 30 varer til sammen). «Send alle varer» er av med mindre du slår det på, og slår du det av, sendes de andre varene ikke med senere forespørsler;",
  "matlagingsvalgene dine: vanskelighetsgrad, detaljnivå, porsjoner, tid, måltid, diett og språk;",
  "allergenlisten fra Innstillinger;",
  "dagens dato og et tilfeldig forespørselsnummer."),
  "<p>Serveren vår sender varene (også dem som sendes med «Send alle varer»), valgene, allergenene og datoen videre til Googles Gemini-modell i Vertex AI, som skriver oppskriften. Ingen navn, e-postadresse eller enhetsidentifikator sendes til modellen. Vi bruker Vertex AIs «globale» endepunkt (global), så Google kan behandle forespørselen utenfor EU/EØS. Google behandler den som vår tjenesteleverandør etter Google Clouds vilkår; se <a href=\""+VERTEX+"\">Googles side om datastyring i Vertex AI</a>.</p>",
  "<p>Allergenlisten din kan si noe om helsen din, så vi behandler den som helseopplysninger. Appen sender den til serveren vår bare med ditt uttrykkelige samtykke (personvernforordningen artikkel 9 nr. 2 bokstav a): før din første forespørsel om oppskrift til serveren vår mens allergener er satt, viser et kort steg hva som sendes, hvorfor og til hvem, og du godtar eller avbryter. Appen lagrer svaret ditt, med dato, på telefonen. Du kan når som helst trekke tilbake samtykket under Oppskrift → Oppskriftsinnstillinger; da skriver ikke serveren vår oppskrifter mens allergener er satt, fordi en oppskrift skrevet uten dem kan være utrygg (de gratis måtene, telefonens egen modell og den delte ledeteksten, virker fortsatt og sender ingenting til oss). Allergenlisten brukes bare til å skrive oppskriften og kontrollere svaret, og den lagres ikke.</p>",
  "<p>Serveren vår kontrollerer forespørsler og svar automatisk, for å hindre at modellen misbrukes: den avviser vare- eller allergennavn som ikke ser ut som navn på mat, og svar som for eksempel inneholder lenker, kontaktopplysninger, et allergen fra listen din eller tekst som ikke handler om matlaging. Et avvist navn eller svar blir ikke lagret eller logget. Serveren vår teller avviste forsøk under identifikatoren din for inneværende døgn og logger regelen som avviste dem, med en enveis omgjort (hashet) form av identifikatoren din; etter flere slike på ett døgn avvises forespørsler om oppskrifter fra kontoen din til neste døgn.</p>",
  "<p>Vi logger ikke og tar ikke vare på det du sender, verken varene du krysset av eller resten av matvarene dine. Serveren vår lagrer bare et fingeravtrykk (en hash) av forespørselen, slik at en gjentatt forespørsel kan kjennes igjen og ikke belastes to ganger. Oppskriften eller menyen som skrives tilbake, og som nevner ingrediensene den bruker, lagres på serveren vår i 7 dager, slik at appen fortsatt kan hente den hvis forbindelsen blir brutt. Deretter slettes den automatisk (Googles automatiske sletting skjer vanligvis innen et døgn etter det). Appen lagrer oppskriften på telefonen din, der den blir til du sletter den.</p>"]),
("Tekniske data for kjøpere", [L(
  "<b>App Check.</b> Ved hver forespørsel til serveren vår beviser appen at den er en ekte kopi, gjennom Firebase App Check: med Google Play Integrity på Android og Apple App Attest på iPhone. Dette starter først når du starter et kjøp.",
  "<b>IP-adresse.</b> Serveren vår bruker IP-adressen din til å begrense hvor mange forespørsler én kilde kan sende i minuttet. Den teller forespørsler per adresse for inneværende minutt bare i minnet, og lagrer ikke adressen. Googles infrastruktur registrerer også hver forespørsel til serveren vår, med IP-adressen, i serverens tekniske logger.",
  "<b>Bruksdata.</b> For hver forespørsel om oppskrift logger serveren vår én linje med en enveis omgjort (hashet) form av identifikatoren din, typen forespørsel, hvor mye tekst modellen leste og skrev (tokens), resultatet og den anslåtte kostnaden. Linjen inneholder aldri varene dine, allergenene, ledeteksten eller oppskriften. Serveren vår lagrer også, under identifikatoren din, antall forespørsler, avviste forsøk og anslått kostnad i inneværende minutt og døgn, for å håndheve grenser.",
  "<b>Daglige totaler.</b> Serveren vår lagrer daglige totaler for alle brukere samlet (forespørsler, oppskrifter, anslått kostnad), uten brukerdata.",
  "<b>Tekniske logger</b> lagres av Google Cloud Logging i 30 dager.",
  "<b>Krasjrapporter</b>, som beskrevet under «Krasjrapporter».")]),
("Refusjoner", [
  "<p>Google Play og App Store gir serveren vår beskjed når et kjøp blir refundert, og de refunderte oppskriftene trekkes fra saldoen din. Hvis du allerede har brukt dem, kan saldoen bli negativ.</p>",
  "<p>I App Store sier kjøpsarket før du kjøper at hvis du ber Apple om refusjon, forteller vi Apple hvor mange av oppskriftene du har brukt. For et kjøp du gjør etter at du har sett dette, registrerer vi at du så det, og når. Ber du deretter Apple om refusjon, spør Apple oss om kjøpet, og vi forteller Apple at oppskriftene ble levert og hvor stor del av kjøpet du har brukt. Om andre kjøp forteller vi Apple ingenting.</p>",
  "<p>Hvis kjøp blir refundert igjen og igjen etter at oppskriftene er brukt, slås kjøp av oppskrifter av for den kjøperen; oppskrifter som allerede er kjøpt, kan fortsatt brukes. For å gjøre dette registreres hvert kjøp med kjøperidentifikatorer: i App Store en identifikator som Apple gir denne appen for Apple-kontoen din (appens app transaction ID); i Google Play identifikatoren din på serveren vår og en enveis omgjort (hashet) form av hver Apple- eller Google-kontoidentifikator som er koblet til kontoen din, hvis det finnes noen. Når en refusjon tar oppskrifter som allerede var brukt, tar vi vare på en oppføring om det under disse identifikatorene: kjøpet, datoen, butikken og antallet brukte oppskrifter som ble refundert.</p>"]),
("Slette kontoen", [
  "<p>Du kan slette kontoen din i appen: Oppskrift-fanen → Oppskriftsinnstillinger → Konto → Slett konto. Er du logget inn, logger du inn én gang til først. Har du kjøpt oppskrifter uten å logge inn, bruker du Oppskriftsinnstillinger → Oppskriftene dine → Slett dataene mine fra serveren vår, hvis din versjon av appen har dette valget. Du kan også be oss om det på e-post, uten appen; se <a href=\"delete.html#nb\">Slett kontoen og dataene dine</a>. Når en konto slettes:</p>", L(
  "innloggingen og e-postadressen din slettes fra serveren vår (med Logg på med Google også kopien av navnet og bildelenken fra Google som Firebase Authentication beholdt). Hvis kontoen din bruker Logg på med Apple, ber serveren vår også Apple om å trekke tilbake appens tilgang til Apple-kontoen din, enten du sletter kontoen i iPhone-appen eller i Android-appen, og sletter tokenet den tok vare på for dette. Lykkes ikke det (for eksempel fordi Apple ikke kan nås, eller fordi du sist logget inn med Apple før vi begynte å ta vare på dette tokenet), sier appen fra, og du kan fjerne koblingen selv i innstillingene for Apple-kontoen, under Logg på med Apple;",
  "oppskriftene og menyene som er lagret på serveren vår, og tellerne for minutt og døgn, slettes;",
  "ubrukte oppskrifter går tapt og kan ikke refunderes."),
  "<p>Hva som blir igjen, og hvorfor:</p>", L(
  "alle kjøpsoppføringer, ikke lenger knyttet til kontoen din. De inneholder ikke navn eller e-postadresse, men beholder den gamle identifikatoren din, kjøperidentifikatorene (se «Refusjoner») og butikkens ordre- eller transaksjonsnummer, som Apple eller Google kan knytte til deg. Det er den eneste måten å hindre at ett kjøp i butikken legges til to ganger, og vi trenger dem for å håndtere senere refusjoner og for regnskapet vårt;",
  "en lukket oppføring under den gamle identifikatoren din, med slettedatoen, antall oppskrifter som gikk tapt, og totalene for oppskrifter som er kjøpt, brukt og refundert, tellerne bak grensene for refusjoner og misbruk, og kjøperidentifikatorene. Den hindrer at en slettet konto brukes igjen, og holder regnskapet vårt riktig;",
  "en oversikt over refusjoner etter bruk, hvis det finnes en (se «Refusjoner»), for å forhindre svindel. Den slettes ikke;",
  "tekniske logger til de utløper etter 30 dager, og de daglige totalene, som ikke inneholder brukerdata."),
  "<p>Å slette appen sletter ingenting på serveren vår. Hvis du aldri har logget inn, går de ubrukte oppskriftene da tapt, og vi kan senere bare finne identifikatoren din ut fra ordrenummeret på butikkens kvittering for et kjøp som ble gjort med den. Lagrede oppskrifter og matvarene dine blir på telefonen til du sletter dem.</p>"]),
("Hvem mottar data, og hvor", [L(
  "<b>Google</b>, som vår tjenesteleverandør: Firebase (Authentication, App Check, Cloud Functions, Firestore, Crashlytics), Google Cloud Logging og Vertex AI (Gemini). Google Play håndterer kjøp og refusjoner på Android, og Play Integrity kontrollerer appen.",
  "<b>Apple</b>: App Store håndterer kjøp og refusjoner på iPhone, og mottar opplysningene som er beskrevet under «Refusjoner» hvis du ber Apple om refusjon; App Attest kontrollerer appen; Logg på med Apple på iPhone, hvis du bruker det, også byttet og tilbakekallingen av tokenet som er beskrevet under «Kjøp av oppskrifter».",
  "<b>Open Food Facts</b>, for strekkodeoppslag, som beskrevet over."),
  "<p>Vi viser ikke reklame, bruker ikke analyse og selger ikke dataene dine. Cloud Functions og Firestore er i EU. Vertex AIs globale endepunkt, Firebase Authentication, App Check og Crashlytics kan behandle data utenfor EU/EØS, for eksempel i USA. Google dekker slike overføringer i sine databehandlingsvilkår, som inneholder EUs standard personvernbestemmelser.</p>"]),
("Rettslig grunnlag", ["<p>Etter personvernforordningen (GDPR) bygger vi på:</p>", L(
  "<b>avtale</b> (artikkel 6 nr. 1 bokstav b): for å kontrollere kjøpene dine, holde oppskriftene og innloggingen din, skrive oppskriftene du ber om, og ta vare på tokenet fra Logg på med Apple som trengs for å fjerne Apples kobling når du sletter kontoen;",
  "<b>uttrykkelig samtykke</b> (artikkel 6 nr. 1 bokstav a og artikkel 9 nr. 2 bokstav a): at allergenlisten din sendes med en forespørsel om oppskrift til serveren vår og til Googles modell. Du kan når som helst trekke det tilbake i oppskriftsinnstillingene; det påvirker ikke forespørsler som allerede er gjort;",
  "<b>berettiget interesse</b> (artikkel 6 nr. 1 bokstav f): krasjrapporter, App Check, begrensning av forespørsler, bruksdata, de automatiske kontrollene av forespørsler og svar, oversikter over refusjoner og svar på Apples spørsmål om en refusjon, for å holde tjenesten i gang og forhindre svindel og misbruk; og at kjøpsoppføringer beholdes etter at en konto er slettet, slik at ett kjøp ikke kan brukes to ganger;",
  "<b>rettslig forpliktelse</b> (artikkel 6 nr. 1 bokstav c): å ta vare på oppføringene vi trenger for regnskapet.")]),
("Barn", ["<p>Appen er ikke rettet mot barn. Utover krasjrapportene og, for dem som kjøper oppskrifter, dataene beskrevet over, samler vi ikke bevisst inn data fra noen.</p>"]),
("Din kontroll og dine rettigheter", ["<p>Du kan endre eller slette alle matvarer i appen. Avinstallerer du appen, slettes dataene fra enheten din. Har du kjøpt oppskrifter, kan du slette kontoen din som beskrevet under «Slette kontoen», i appen eller på e-post: se <a href=\"delete.html#nb\">Slett kontoen og dataene dine</a>.</p>",
  "<p>Du har rett til å be om en kopi av dataene dine, få dem rettet eller slettet, begrense eller protestere mot bruken av dem, og klage til datatilsynsmyndigheten der du bor (i Norge: Datatilsynet). For å bruke disse rettighetene, kontakt oss (se «Kontakt»). Hvis du aldri har logget inn, kan vi bare se hvilke data som er dine ut fra ordrenummeret på butikkens kvittering for ett av kjøpene dine.</p>"]),
("Endringer", ["<p>Hvis erklæringen endres, publiseres den nye versjonen på denne siden med oppdatert dato.</p>"]),
("Kontakt", ["<p>Spørsmål eller forespørsler? <a href=\""+ISSUES+"\">Opprett en sak (issue)</a> på GitHub. Saker er offentlige, så ikke skriv e-postadressen din eller andre personopplysninger i dem."+private_contact("Hvis du ikke vil sende en forespørsel om personvern offentlig, send e-post til {}.", "nb")+"</p>"]),
], home="Velg språk")

def page(code):
    t=T[code]
    body="".join(f"<h2>{h}</h2>{''.join(ps)}" for h,ps in t["secs"])
    return f"""<!doctype html>
<html lang="{code}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{ICONS}
<title>{t['app']} — {t['title']}</title><meta name="robots" content="index,follow"><style>{CSS}</style></head>
<body><main>{nav(code)}<h1>{t['app']}<br>{t['title']}</h1><p class="mut">{t['upd']}</p><div class="card">{''.join(t['secs'][0][1])}</div>{body.split('</p>',1)[1] if False else ''.join(f"<h2>{h}</h2>{''.join(ps)}" for h,ps in t['secs'][1:])}</main></body></html>"""
for c in T: open(f"{c}.html","w",encoding="utf-8").write(page(c))
open("index.html","w",encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{ICONS}
<title>BestBefore — Privacy Policy</title><style>{CSS}</style></head>
<body><main><h1>BestBefore</h1><p class="mut">Privacy Policy · Personvernerklæring · Политика конфиденциальности</p>
<div class="langs"><a href="en.html" hreflang="en">English — BestBefore</a><a href="ru.html" hreflang="ru">Русский — Срокоед</a><a href="nb.html" hreflang="nb">Norsk — Matvakt</a></div></main></body></html>""")
open("README.md","w").write("# BestBefore privacy policy\n\nStatic pages served by GitHub Pages: English, Russian (Срокоед) and Norwegian (Matvakt), plus `app.html`, a short page about the app with screenshots from `img/`.\n\nSource of truth for the policy text is `build.py`; run `python3 build.py` to regenerate the HTML.\n")
open(".nojekyll","w").write("")

# --- Support page (the App Store's required Support URL) -------------------------------------
APPLE_REFUND = "https://support.apple.com/118223"
GOOGLE_REFUND = "https://support.google.com/googleplay/answer/15574897"
SUPPORT = [
 ("en", "BestBefore — Support", [
  ("Contact", f'<p>Found a bug or have an idea? <a href="{ISSUES}">Open an issue on GitHub</a>. We read every one.</p>'),
  ("Where is my data?", "<p>Your pantry is stored only on your phone, and you need no account for it, so we cannot see or recover it. Use <b>Settings → Data → Export backup</b> to save a copy, and import it on a new phone. If you buy recipes, Google Play or the App Store takes the payment and our server keeps your recipe balance; signing in is optional. See the <a href=\"en.html\">privacy policy</a>.</p>"),
  ("Reminders don't arrive", "<p>Check that notifications are allowed for BestBefore in your phone's settings, and set the reminder time in <b>Settings → Notifications</b>.</p>"),
  ("Shop reminders", "<p>Optional. Save a shop in <b>Settings → Shopping reminders</b>. To get reminders while the app is closed, allow location access <b>always</b> (iPhone) or <b>all the time</b> (Android).</p>"),
  ("Where are my bought recipes?", "<p>If you have not signed in, they stay with this install of the app: if you delete the app or change phone, the unused ones are lost. If you signed in (with Apple or Google on iPhone, with Google on Android), they are kept in your account: after reinstalling, or on a new phone, sign in the same way to use them. Sign in with Apple works only on iPhone: to use your recipes on an Android phone, first add Google sign-in in the iPhone app, under Recipe settings.</p>"),
  ("I paid, but no recipes were added", "<p>The app tries again to confirm the purchase each time it starts, each time you come back to it, and when you tap <b>Try now</b> in the Recipe tab, and adds the recipes when it succeeds, so you do not need to buy again. Make sure you are online. If the store is still waiting for your payment, the recipes are added when it confirms. If you would rather have your money back, ask the store for a refund.</p>"),
  ("Refunds", f'<p>Refunds are requested from the store: <a href="{GOOGLE_REFUND}">Google Play</a> or <a href="{APPLE_REFUND}">the App Store</a>. Refunded recipes are taken off your balance.</p>'),
  ("Deleting your account", "<p>Use <b>Recipe → Recipe settings → Account → Delete account</b>. Your sign-in and email address are deleted from our server, and your unused recipes are lost and cannot be refunded. A record of your purchases stays, no longer linked to you. Your pantry and saved recipes stay on the phone. If your account also uses Sign in with Apple, Apple's link to the app is removed too, from either app; if that ever fails, the app tells you how to remove it in your Apple Account settings. To delete without the app, or if you bought without signing in, see <a href=\"delete.html#en\">Delete your account and data</a>.</p>"),
  ("Deleting your data", "<p>Delete items in the app, use <b>Settings → Data → Clear All Pantry Data</b>, or uninstall the app.</p>"),
 ]),
 ("ru", "Срокоед — поддержка", [
  ("Связаться с нами", f'<p>Нашли ошибку или есть идея? <a href="{ISSUES}">Создайте обращение (issue) на GitHub</a>. Мы читаем каждое.</p>'),
  ("Где хранятся мои данные?", "<p>Продукты хранятся только на вашем телефоне, и аккаунт для этого не нужен, поэтому мы не можем их увидеть или восстановить. Сохраните копию через <b>Настройки → Данные → Экспорт копии</b> и импортируйте её на новом телефоне. Если вы покупаете рецепты, оплату принимает Google Play или App Store, а наш сервер хранит ваш баланс рецептов; входить в аккаунт не обязательно. См. <a href=\"ru.html\">политику конфиденциальности</a>.</p>"),
  ("Не приходят напоминания", "<p>Проверьте, что уведомления для Срокоеда разрешены в настройках телефона, и задайте время в <b>Настройки → Уведомления</b>.</p>"),
  ("Напоминания у магазина", "<p>По желанию. Сохраните магазин в <b>Настройки → Напоминания о покупках</b>. Чтобы напоминания приходили при закрытом приложении, разрешите доступ к геопозиции <b>всегда</b> (iPhone) или <b>в любом режиме</b> (Android).</p>"),
  ("Где мои купленные рецепты?", "<p>Если вы не входили в аккаунт, они привязаны к этой установке приложения: если удалить приложение или сменить телефон, неиспользованные рецепты теряются. Если вы вошли в аккаунт (через Apple или Google на iPhone, через Google на Android), они хранятся в вашем аккаунте: после переустановки или на новом телефоне войдите тем же способом, чтобы ими пользоваться. Вход через Apple работает только на iPhone: чтобы пользоваться рецептами на телефоне с Android, сначала добавьте вход через Google в приложении на iPhone, в настройках рецептов.</p>"),
  ("Я заплатил, но рецепты не добавились", "<p>Приложение снова пытается подтвердить покупку при каждом запуске, каждый раз, когда вы к нему возвращаетесь, и когда вы нажимаете <b>Повторить сейчас</b> во вкладке «Рецепт», и добавляет рецепты, когда это получится, поэтому покупать заново не нужно. Проверьте подключение к интернету. Если магазин ещё ждёт оплату, рецепты добавятся, когда он её подтвердит. Если вы хотите вернуть деньги, попросите возврат в магазине.</p>"),
  ("Возвраты", f'<p>Возврат запрашивается в магазине: <a href="{GOOGLE_REFUND}">Google Play</a> или <a href="{APPLE_REFUND}">App Store</a>. Возвращённые рецепты списываются с вашего баланса.</p>'),
  ("Удаление аккаунта", "<p>Откройте <b>Рецепт → Настройки рецептов → Аккаунт → Удалить аккаунт</b>. Ваш вход и адрес электронной почты удаляются с нашего сервера, а неиспользованные рецепты теряются, и деньги за них не возвращаются. Запись о ваших покупках остаётся, но уже не связана с вами. Продукты и сохранённые рецепты остаются на телефоне. Если ваш аккаунт использует и вход через Apple, связь с Apple тоже удаляется, в любом из приложений; если это когда-нибудь не удастся, приложение подскажет, как убрать её в настройках Аккаунта Apple. Как удалить данные без приложения или если вы покупали без входа, см. <a href=\"delete.html#ru\">Удаление аккаунта и данных</a>.</p>"),
  ("Удаление данных", "<p>Удалите продукты в приложении, воспользуйтесь <b>Настройки → Данные → Очистить все данные кладовой</b> или удалите приложение.</p>"),
 ]),
 ("nb", "Matvakt — brukerstøtte", [
  ("Kontakt", f'<p>Fant du en feil eller har en idé? <a href="{ISSUES}">Opprett en sak (issue) på GitHub</a>. Vi leser alle.</p>'),
  ("Hvor er dataene mine?", "<p>Matvarene lagres bare på telefonen din, og du trenger ingen konto for dem, så vi kan ikke se eller gjenopprette dem. Ta en kopi under <b>Innstillinger → Data → Eksporter sikkerhetskopi</b> og importer den på en ny telefon. Kjøper du oppskrifter, tar Google Play eller App Store imot betalingen, og serveren vår holder saldoen din av oppskrifter; innlogging er valgfritt. Se <a href=\"nb.html\">personvernerklæringen</a>.</p>"),
  ("Påminnelsene kommer ikke", "<p>Sjekk at varsler er tillatt for Matvakt i telefonens innstillinger, og velg tidspunkt under <b>Innstillinger → Varsler</b>.</p>"),
  ("Butikkpåminnelser", "<p>Valgfritt. Lagre en butikk under <b>Innstillinger → Handlepåminnelser</b>. For påminnelser når appen er lukket, tillat posisjon <b>alltid</b> (iPhone) eller <b>hele tiden</b> (Android).</p>"),
  ("Hvor er oppskriftene jeg har kjøpt?", "<p>Hvis du ikke har logget inn, hører de til denne installasjonen av appen: sletter du appen eller bytter telefon, går de ubrukte tapt. Hvis du logget inn (med Apple eller Google på iPhone, med Google på Android), ligger de på kontoen din: etter ny installasjon, eller på en ny telefon, logger du inn på samme måte for å bruke dem. Logg på med Apple virker bare på iPhone: for å bruke oppskriftene på en Android-telefon legger du først til innlogging med Google i iPhone-appen, under Oppskriftsinnstillinger.</p>"),
  ("Jeg betalte, men fikk ingen oppskrifter", "<p>Appen prøver å bekrefte kjøpet på nytt hver gang den starter, hver gang du går tilbake til den, og når du trykker <b>Prøv nå</b> i Oppskrift-fanen, og legger til oppskriftene når det lykkes, så du trenger ikke å kjøpe på nytt. Sørg for at du er på nett. Hvis butikken fortsatt venter på betalingen, legges oppskriftene til når den bekrefter. Vil du heller ha pengene tilbake, ber du butikken om refusjon.</p>"),
  ("Refusjoner", f'<p>Refusjon bes om hos butikken: <a href="{GOOGLE_REFUND}">Google Play</a> eller <a href="{APPLE_REFUND}">App Store</a>. Refunderte oppskrifter trekkes fra saldoen din.</p>'),
  ("Slette kontoen", "<p>Bruk <b>Oppskrift → Oppskriftsinnstillinger → Konto → Slett konto</b>. Innloggingen og e-postadressen din slettes fra serveren vår, og ubrukte oppskrifter går tapt og kan ikke refunderes. En oversikt over kjøpene dine blir igjen, uten kobling til deg. Matvarene og de lagrede oppskriftene blir på telefonen. Bruker kontoen din også Logg på med Apple, fjernes Apples kobling til appen også, fra begge appene; skulle det mislykkes, forteller appen deg hvordan du fjerner den i innstillingene for Apple-kontoen. For å slette uten appen, eller hvis du kjøpte uten å logge inn, se <a href=\"delete.html#nb\">Slett kontoen og dataene dine</a>.</p>"),
  ("Slette dataene", "<p>Slett varer i appen, bruk <b>Innstillinger → Data → Tøm alle data i matskapet</b>, eller avinstaller appen.</p>"),
 ]),
]
body = '<nav>' + " ".join(f'<a href="#{c}">{n}</a>' for c, n in NAV) + '</nav>'
for code, title, secs in SUPPORT:
    body += f'<section id="{code}" lang="{code}"><h1>{title}</h1>' + "".join(f"<h2>{h}</h2>{p}" for h, p in secs) + "</section><hr>"
open("support.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{ICONS}
<title>BestBefore — Support</title><style>{CSS} hr{{border:0;border-top:1px solid var(--bd);margin:40px 0}}</style></head>
<body><main>{body}<p class="mut"><a href="index.html">Privacy Policy</a></p></main></body></html>""")
s = open("index.html", encoding="utf-8").read()
if "support.html" not in s:
    s = s.replace('</div></main>', '</div><p><a href="support.html">Support · Поддержка · Brukerstøtte</a></p></main>')
    open("index.html", "w", encoding="utf-8").write(s)

# --- Account and data deletion page (Google Play's "delete account" URL) ----------------------
DELETE = [
 ("en", "BestBefore — Delete your account and data", "Privacy Policy", [
  (None, "<p>This page explains how to delete your data from BestBefore, the grocery and expiry-date tracker for Android and iPhone by Daniil Pastuhov. For all the details, see the <a href=\"en.html\">privacy policy</a>.</p>"),
  ("Data on your phone", "<p>Your pantry, shopping list, settings (including your allergen list), photos and saved recipes are stored only on your phone. None of it is on our server. Deleting the app deletes all of it. To delete only some of it, delete items or saved recipes in the app. Your phone's own backup (Google or iCloud) may keep a copy until you delete it there.</p>"),
  ("Do you have an account on our server?", "<p>Only if you started buying recipes in the Recipe tab. Such an account is either signed in, with Apple (on iPhone) or Google (on iPhone and Android), or not signed in, and then it belongs only to the phone you bought on. If you never started a purchase, we hold no data about you, apart from crash reports (see below).</p>"),
  ("Delete it in the app", "<p>Open the Recipe tab → Recipe settings.</p>" + L(
    "<b>Signed in:</b> under Account, tap <b>Delete account</b> and sign in once more to confirm. You can do this in the iPhone app or the Android app.",
    "<b>Bought without signing in:</b> under Your recipes, tap <b>Delete my data from our server</b>. It works only on the phone you bought on, before you delete the app, and it is unavailable while a purchase is still being completed. If your version of the app does not show it, update the app, or email us as described below.")),
  ("Ask us to delete it without the app", "<p>" + private_contact("Email {}.", "en", "pc-en").strip() + " Say which sign-in the account uses (Apple or Google) and the email address of that account. If you chose Hide My Email with Sign in with Apple, this is the relay address shown in your Apple Account settings under Sign in with Apple. If you bought without signing in, give instead the order number of one of your purchases: on Google Play, the order number on the Google Play receipt email or in your order history in Google Play (it starts with “GPA.”); on the App Store, the Order ID on the receipt Apple emailed you (it starts with letters, for example “MK…”), not a transaction ID. Purchases made in a test environment have no receipt. We will ask you to confirm the request by replying to us (for a signed-in account, we write to the account's address), and delete the account within 30 days.</p>"),
  ("What is deleted", L(
    "your sign-in and email address (with Sign in with Google, also the copy of the Google name and picture link that Firebase Authentication kept);",
    "your account identifier and your recipe balance;",
    "the Sign in with Apple token, if your account uses Sign in with Apple: our server asks Apple to revoke the app's access to your Apple Account, then deletes the token. If that does not succeed, we tell you, and you can remove the link yourself in your Apple Account settings, under Sign in with Apple;",
    "recipes and menus still held on our server so that the app can collect them (at most 7 days), and the per-minute and per-day counts;",
    "your unused recipes are lost and cannot be refunded.")),
  ("What is kept, and why", L(
    "a record of each purchase, no longer linked to your account: the store, the pack, the date and the store's order or transaction number, with your old identifier and the buyer identifiers, but no name or email. It stops the same purchase being added twice, lets refunds still be handled, and we need it for our accounts and to prevent fraud;",
    "a closed record under your old identifier (the date of deletion, the totals of recipes, the counts behind the limits), so that a deleted account cannot be used again and our accounts stay correct;",
    "a record of refunds after use, if there is one, to prevent fraud;",
    "technical logs, until they expire after 30 days.") +
    "<p>We keep these on the basis of our legitimate interests (GDPR Article 6(1)(f)) and our legal obligation to keep accounts (Article 6(1)(c)). Apple and Google keep their own records of your purchases, under their own privacy policies.</p>"),
  ("Crash reports", "<p>Crash reports (Firebase Crashlytics) are not linked to any account and contain no name or account; they are deleted automatically after 90 days.</p>"),
 ]),
 ("ru", "Срокоед — удаление аккаунта и данных", "Политика конфиденциальности", [
  (None, "<p>Здесь описано, как удалить свои данные из Срокоеда (BestBefore) — приложения для учёта продуктов и сроков годности для Android и iPhone от Daniil Pastuhov. Все подробности — в <a href=\"ru.html\">политике конфиденциальности</a>.</p>"),
  ("Данные на телефоне", "<p>Продукты, список покупок, настройки (включая список аллергенов), фотографии и сохранённые рецепты хранятся только на вашем телефоне. На нашем сервере их нет. При удалении приложения удаляется всё это. Чтобы удалить только часть, удалите продукты или сохранённые рецепты в приложении. Резервная копия самого телефона (Google или iCloud) может хранить копию, пока вы не удалите её там.</p>"),
  ("Есть ли у вас аккаунт на нашем сервере?", "<p>Только если вы начинали покупку рецептов во вкладке «Рецепт». Такой аккаунт либо с входом — через Apple (на iPhone) или Google (на iPhone и Android), — либо без входа, и тогда он привязан только к телефону, на котором вы покупали. Если вы ни разу не начинали покупку, у нас нет данных о вас, кроме отчётов о сбоях (см. ниже).</p>"),
  ("Удаление в приложении", "<p>Откройте вкладку «Рецепт» → «Настройки рецептов».</p>" + L(
    "<b>Если вы вошли в аккаунт:</b> в разделе «Аккаунт» нажмите <b>«Удалить аккаунт»</b> и для подтверждения войдите ещё раз. Это можно сделать и в приложении на iPhone, и в приложении для Android.",
    "<b>Если вы покупали без входа:</b> в разделе «Ваши рецепты» нажмите <b>«Удалить мои данные с сервера»</b>. Это работает только на телефоне, на котором вы покупали, и только пока приложение не удалено; пока покупка ещё не завершена, кнопка недоступна. Если в вашей версии приложения её нет, обновите приложение или напишите нам, как описано ниже.")),
  ("Запрос на удаление без приложения", "<p>" + private_contact("Напишите на {}.", "ru", "pc-ru").strip() + " Укажите, какой вход использует аккаунт (Apple или Google), и адрес электронной почты этого аккаунта. Если при входе через Apple вы выбрали «Скрыть e-mail», это адрес-посредник, который указан в настройках Аккаунта Apple в разделе «Вход с Apple». Если вы покупали без входа, вместо этого укажите номер заказа одной из покупок: в Google Play — номер заказа из письма-чека от Google Play или из истории заказов в Google Play (он начинается с «GPA.»); в App Store — номер заказа (Order ID) из чека, который Apple прислала вам по электронной почте (он начинается с букв, например «MK…»), а не идентификатор транзакции. У покупок в тестовой среде чека нет. Мы попросим вас подтвердить запрос ответом на наше письмо (для аккаунта с входом мы напишем на адрес аккаунта) и удалим аккаунт в течение 30 дней.</p>"),
  ("Что удаляется", L(
    "ваш вход и адрес электронной почты (при входе через Google — также копия имени и ссылки на фото из Google, которую хранил Firebase Authentication);",
    "идентификатор аккаунта и баланс рецептов;",
    "токен входа через Apple, если ваш аккаунт использует вход через Apple: наш сервер просит Apple отозвать доступ приложения к вашему Аккаунту Apple, а затем удаляет токен. Если это не удалось, мы сообщим вам, и связь можно убрать самостоятельно в настройках Аккаунта Apple, в разделе «Вход с Apple»;",
    "рецепты и меню, которые ещё хранятся на нашем сервере, чтобы приложение могло их забрать (не дольше 7 дней), а также счётчики за минуту и день;",
    "неиспользованные рецепты теряются, и деньги за них не возвращаются.")),
  ("Что остаётся и почему", L(
    "запись о каждой покупке, уже не связанная с вашим аккаунтом: магазин, пакет рецептов, дата и номер заказа или транзакции в магазине, а также ваш прежний идентификатор и идентификаторы покупателя, но без имени и адреса электронной почты. Она не даёт зачислить одну и ту же покупку дважды, позволяет по-прежнему обрабатывать возвраты и нужна нам для бухгалтерии и для предотвращения мошенничества;",
    "закрытая запись под вашим прежним идентификатором (дата удаления, итоги по рецептам, счётчики для ограничений), чтобы удалённым аккаунтом нельзя было снова воспользоваться и наша отчётность оставалась верной;",
    "запись о возвратах после использования, если она есть, для предотвращения мошенничества;",
    "технические журналы — пока они не истекут через 30 дней.") +
    "<p>Мы храним их на основании наших законных интересов (статья 6(1)(f) GDPR) и юридической обязанности вести бухгалтерию (статья 6(1)(c)). Apple и Google хранят собственные записи о ваших покупках по своим политикам конфиденциальности.</p>"),
  ("Отчёты о сбоях", "<p>Отчёты о сбоях (Firebase Crashlytics) не связаны ни с каким аккаунтом и не содержат имени или аккаунта; они удаляются автоматически через 90 дней.</p>"),
 ]),
 ("nb", "Matvakt — slett kontoen og dataene dine", "Personvernerklæring", [
  (None, "<p>Her står det hvordan du sletter dataene dine fra Matvakt (BestBefore), appen for matvarer og utløpsdatoer for Android og iPhone fra Daniil Pastuhov. Alle detaljene står i <a href=\"nb.html\">personvernerklæringen</a>.</p>"),
  ("Data på telefonen", "<p>Matvarene, handlelisten, innstillingene (også allergenlisten), bildene og de lagrede oppskriftene dine lagres bare på telefonen din. Ingenting av det ligger på serveren vår. Sletter du appen, slettes alt sammen. Vil du bare slette noe av det, sletter du varer eller lagrede oppskrifter i appen. Telefonens egen sikkerhetskopi (Google eller iCloud) kan ha en kopi til du sletter den der.</p>"),
  ("Har du en konto på serveren vår?", "<p>Bare hvis du har startet et kjøp av oppskrifter i Oppskrift-fanen. En slik konto er enten med innlogging – med Apple (på iPhone) eller Google (på iPhone og Android) – eller uten innlogging, og da hører den bare til telefonen du kjøpte på. Har du aldri startet et kjøp, har vi ingen data om deg, utenom krasjrapporter (se nedenfor).</p>"),
  ("Slett i appen", "<p>Åpne Oppskrift-fanen → Oppskriftsinnstillinger.</p>" + L(
    "<b>Logget inn:</b> trykk <b>Slett konto</b> under Konto, og logg inn én gang til for å bekrefte. Det kan du gjøre både i iPhone-appen og i Android-appen.",
    "<b>Kjøpt uten å logge inn:</b> trykk <b>Slett dataene mine fra serveren vår</b> under Oppskriftene dine. Det virker bare på telefonen du kjøpte på, før du sletter appen, og det er ikke tilgjengelig mens et kjøp fortsatt fullføres. Viser ikke din versjon av appen dette valget, kan du oppdatere appen eller sende oss en e-post som beskrevet nedenfor.")),
  ("Be om sletting uten appen", "<p>" + private_contact("Send e-post til {}.", "nb", "pc-nb").strip() + " Skriv hvilken innlogging kontoen bruker (Apple eller Google), og e-postadressen til kontoen. Har du valgt Skjul e-postadressen min med Logg på med Apple, er det videresendingsadressen som vises i innstillingene for Apple-kontoen under Logg på med Apple. Har du kjøpt uten å logge inn, oppgir du i stedet ordrenummeret for ett av kjøpene: i Google Play ordrenummeret i kvitteringen fra Google Play på e-post eller i ordrehistorikken i Google Play (det begynner med «GPA.»); i App Store ordre-ID-en (Order ID) i kvitteringen Apple sendte deg på e-post (den begynner med bokstaver, for eksempel «MK…»), ikke en transaksjons-ID. Kjøp gjort i et testmiljø har ingen kvittering. Vi ber deg bekrefte forespørselen ved å svare oss (for en konto med innlogging skriver vi til kontoens adresse), og sletter kontoen innen 30 dager.</p>"),
  ("Dette slettes", L(
    "innloggingen og e-postadressen din (med Logg på med Google også kopien av navnet og bildelenken fra Google som Firebase Authentication beholdt);",
    "kontoidentifikatoren og saldoen din av oppskrifter;",
    "tokenet fra Logg på med Apple, hvis kontoen din bruker Logg på med Apple: serveren vår ber Apple om å trekke tilbake appens tilgang til Apple-kontoen din, og sletter deretter tokenet. Lykkes ikke det, sier vi fra, og du kan fjerne koblingen selv i innstillingene for Apple-kontoen, under Logg på med Apple;",
    "oppskrifter og menyer som fortsatt ligger på serveren vår slik at appen kan hente dem (høyst 7 dager), og tellerne for minutt og døgn;",
    "ubrukte oppskrifter går tapt og kan ikke refunderes.")),
  ("Dette blir igjen, og hvorfor", L(
    "en oppføring for hvert kjøp, ikke lenger knyttet til kontoen din: butikken, pakken, datoen og butikkens ordre- eller transaksjonsnummer, sammen med den gamle identifikatoren din og kjøperidentifikatorene, men uten navn eller e-postadresse. Den hindrer at samme kjøp legges til to ganger, gjør at refusjoner fortsatt kan håndteres, og vi trenger den for regnskapet vårt og for å forhindre svindel;",
    "en lukket oppføring under den gamle identifikatoren din (slettedatoen, totalene for oppskrifter, tellerne bak grensene), slik at en slettet konto ikke kan brukes igjen og regnskapet vårt blir riktig;",
    "en oversikt over refusjoner etter bruk, hvis det finnes en, for å forhindre svindel;",
    "tekniske logger, til de utløper etter 30 dager.") +
    "<p>Dette beholder vi på grunnlag av vår berettigede interesse (personvernforordningen artikkel 6 nr. 1 bokstav f) og vår rettslige forpliktelse til å føre regnskap (artikkel 6 nr. 1 bokstav c). Apple og Google har sine egne opplysninger om kjøpene dine, etter sine egne personvernerklæringer.</p>"),
  ("Krasjrapporter", "<p>Krasjrapporter (Firebase Crashlytics) er ikke knyttet til noen konto og inneholder verken navn eller konto; de slettes automatisk etter 90 dager.</p>"),
 ]),
]
body = '<nav>' + " ".join(f'<a href="#{c}">{n}</a>' for c, n in NAV) + '</nav>'
for code, title, policy, secs in DELETE:
    body += f'<section id="{code}" lang="{code}"><h1>{title}</h1>' + "".join((f"<h2>{h}</h2>" if h else "") + p for h, p in secs) + f'<p class="mut"><a href="{code}.html">{policy}</a></p></section><hr>'
open("delete.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{ICONS}
<title>BestBefore — Delete your account and data</title><meta name="robots" content="index,follow"><style>{CSS} hr{{border:0;border-top:1px solid var(--bd);margin:40px 0}}</style></head>
<body><main>{body}<p class="mut"><a href="index.html">BestBefore</a> · <a href="support.html">Support</a></p></main></body></html>""")
s = open("index.html", encoding="utf-8").read()
if "delete.html" not in s:
    s = s.replace('</main></body>', '<p><a href="delete.html">Delete your account and data · Удаление аккаунта и данных · Slett kontoen og dataene dine</a></p></main></body>')
    open("index.html", "w", encoding="utf-8").write(s)

# --- About page: what the app is, with screenshots and store links ---------------------------
# The index stays the privacy policy's language chooser (the stores link to it); this page is
# linked from it. Screenshots in img/ are 360 px wide JPEG copies of the App Store screenshots
# (FoodTrack repo, store-listing/app-store/<locale>/screenshots/1-4.png).
APP_STORE = "https://apps.apple.com/app/id6818647200"
SOURCE = "https://github.com/daniil-pastuhov/FoodTrack"
APP_CSS = """.lead{font-size:1.1rem}.shots{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:24px 0}
@media(min-width:640px){.shots{grid-template-columns:repeat(4,1fr)}}
.shots img{width:100%;height:auto;display:block;border-radius:10px;border:1px solid var(--bd)}
.btn{display:inline-block;padding:10px 18px;border-radius:10px;background:var(--ac);color:var(--bg);font-weight:600;text-decoration:none}
h2.name{font-size:1.9rem;line-height:1.2;margin:.2em 0}h3{font-size:1.2rem;margin:2em 0 .4em}
.vh{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.get p{margin:.8em 0}.get .mut{white-space:nowrap}hr{border:0;border-top:1px solid var(--bd);margin:40px 0}"""
ABOUT = [
 ("en", "BestBefore", "An expiry date tracker for your fridge, freezer and cupboard", [
  "Know what's about to expire", "Scan the pack, the date is read", "Cook what needs using first", "A three-day menu around what you have (with a recipe pack)"],
  "The three-day menu (last picture) needs a recipe pack: an optional one-off purchase, no subscription.",
  "<p class=\"lead\">Scan a barcode and the product is filled in from Open Food Facts; point the camera at the printed date and the phone reads it. Your food is sorted by where you keep it, a reminder comes before something expires, essentials you use up go onto the shopping list, and the Recipe tab turns what is about to expire into a recipe or, with a recipe pack, a three-day menu. Home Screen widgets show what to use first.</p>",
  [("Free, private, open source", L(
    "Free, with no ads and no subscription. No account needed.",
    "Your pantry stays on your phone. Export a backup whenever you like.",
    "No tracking. The app sends crash reports, and barcodes are looked up on Open Food Facts.",
    f'Open source (Apache-2.0): <a href="{SOURCE}">the source code is on GitHub</a>.',
    "In English, Russian and Norwegian.")),
   ("Recipes from what is about to expire", L(
    "Free: share a ready-made prompt to the AI app you already use.",
    "Free on the device itself, where it supports it: Apple Intelligence on iPhone and iPad (iOS or iPadOS 26 or later), Gemini Nano on some Android phones.",
    "Optional recipe packs, bought once in the app (no subscription): recipes written by our server, and the three-day menu. A recipe from a pack sends the items you tick, your recipe settings and your allergens to our server. The free ways send nothing to us.")),
   ("Get it", f'<div class="get"><p><a class="btn" href="{APP_STORE}">Download on the App Store</a> <span class="mut">iPhone and iPad</span></p><p><b>Android:</b> Google Play, in closed testing, not public yet.</p></div>')],
  ("Privacy policy", "Support", "Delete your account and data", "Source code")),
 ("ru", "Срокоед", "Сроки годности продуктов в холодильнике, морозилке и кладовой", [
  "Видно, что скоро испортится", "Наведите камеру — срок распознан", "Готовьте из того, что пора съесть", "Меню на три дня под ваши продукты (с пакетом рецептов)"],
  "Для меню на три дня (последний снимок экрана) нужен пакет рецептов — разовая покупка по желанию, без подписки.",
  "<p class=\"lead\">Отсканируйте штрихкод — название продукта подставится из Open Food Facts; наведите камеру на напечатанную дату — телефон сам её распознает. Продукты разложены по местам хранения, напоминание приходит до того, как срок истечёт, закончившиеся важные продукты попадают в список покупок, а вкладка «Рецепт» превращает то, что скоро испортится, в рецепт или — с пакетом рецептов — в меню на три дня. Виджеты на экране «Домой» показывают, что съесть в первую очередь.</p>",
  [("Бесплатно, приватно, с открытым кодом", L(
    "Бесплатно, без рекламы и без подписки. Аккаунт не нужен.",
    "Ваши продукты хранятся на телефоне. Резервную копию можно сохранить в любой момент.",
    "Без слежки. Приложение отправляет отчёты о сбоях, а штрихкоды ищет в Open Food Facts.",
    f'Открытый код (Apache-2.0): <a href="{SOURCE}">исходный код на GitHub</a>.',
    "На русском, английском и норвежском.")),
   ("Рецепты из того, что скоро испортится", L(
    "Бесплатно: отправьте готовый запрос в ИИ-приложение, которым уже пользуетесь.",
    "Бесплатно на самом устройстве, если оно это поддерживает: Apple Intelligence на iPhone и iPad (iOS или iPadOS 26 и новее), Gemini Nano на некоторых телефонах Android.",
    "По желанию — пакеты рецептов, разовая покупка в приложении (без подписки): рецепты с нашего сервера и меню на три дня. Для рецепта из пакета приложение отправляет на сервер отмеченные продукты, настройки рецепта и аллергены. Бесплатные способы нам ничего не отправляют.")),
   ("Где скачать", f'<div class="get"><p><a class="btn" href="{APP_STORE}">Загрузить в App Store</a> <span class="mut">iPhone и iPad</span></p><p><b>Android:</b> Google Play, идёт закрытое тестирование, в открытом доступе приложения пока нет.</p></div>')],
  ("Политика конфиденциальности", "Поддержка", "Удаление аккаунта и данных", "Исходный код")),
 ("nb", "Matvakt", "Holdbarhet på maten i kjøleskapet, fryseren og matskapet", [
  "Se hva som snart går ut", "Skann pakken, datoen leses av", "Lag mat av det som må brukes først", "Meny for tre dager rundt det du har (med oppskriftspakke)"],
  "Menyen for tre dager (siste skjermbilde) krever en oppskriftspakke – et valgfritt engangskjøp, ikke abonnement.",
  "<p class=\"lead\">Skann strekkoden, så fylles varen ut fra Open Food Facts; rett kameraet mot den påtrykte datoen, så leser telefonen den. Maten sorteres etter hvor du oppbevarer den, du får en påminnelse før noe går ut på dato, faste varer du bruker opp havner på handlelisten, og Oppskrift-fanen gjør det som snart går ut om til en oppskrift eller, med en oppskriftspakke, en meny for tre dager. Widgeter på Hjem-skjermen viser hva du bør bruke først.</p>",
  [("Gratis, privat og åpen kildekode", L(
    "Gratis, uten reklame og uten abonnement. Ingen konto nødvendig.",
    "Matvarene dine blir på telefonen. Ta sikkerhetskopi når du vil.",
    "Ingen sporing. Appen sender krasjrapporter, og strekkoder slås opp i Open Food Facts.",
    f'Åpen kildekode (Apache-2.0): <a href="{SOURCE}">kildekoden ligger på GitHub</a>.',
    "På norsk, engelsk og russisk.")),
   ("Oppskrifter av det som snart går ut", L(
    "Gratis: del en ferdig ledetekst med KI-appen du allerede bruker.",
    "Gratis på selve enheten, der den støtter det: Apple Intelligence på iPhone og iPad (iOS eller iPadOS 26 eller nyere), Gemini Nano på noen Android-telefoner.",
    "Valgfrie oppskriftspakker, engangskjøp i appen (ikke abonnement): oppskrifter skrevet av serveren vår, og menyen for tre dager. En oppskrift fra en pakke sender varene du krysser av, oppskriftsinnstillingene og allergenene dine til serveren vår. De gratis alternativene sender ingenting til oss.")),
   ("Last ned", f'<div class="get"><p><a class="btn" href="{APP_STORE}">Last ned i App Store</a> <span class="mut">iPhone og iPad</span></p><p><b>Android:</b> Google Play, i lukket testing, ikke offentlig ennå.</p></div>')],
  ("Personvernerklæring", "Brukerstøtte", "Slett kontoen og dataene dine", "Kildekode")),
]
def app_nav(cur):
    return '<nav>' + " ".join(f'<a href="#{c}" hreflang="{c}"' + (' aria-current="page"' if c == cur else '') + f'>{n}</a>' for c, n in NAV) + '</nav>'
body = ''
for n, (code, name, sub, alts, shots_note, lead, secs, links) in enumerate(ABOUT):
    lazy = '' if n == 0 else ' loading="lazy"'
    shots = '<div class="shots">' + "".join(
        f'<img src="img/{code}-{i}.jpg" width="360" height="782" alt="{html.escape(a)}"{lazy}>' for i, a in enumerate(alts, 1)) + f'</div><p class="mut">{shots_note}</p>'
    policy, support, delete, source = links
    body += (f'<section id="{code}" lang="{code}">{app_nav(code)}<h2 class="name">{name}</h2><p class="mut">{sub}</p>{lead}{shots}'
             + "".join(f"<h3>{h}</h3>{p}" for h, p in secs)
             + f'<p class="mut"><a href="{code}.html">{policy}</a> · <a href="support.html#{code}">{support}</a> · '
               f'<a href="delete.html#{code}">{delete}</a> · <a href="{SOURCE}">{source}</a></p></section><hr>')
SITE = "https://daniil-pastuhov.github.io/bestbefore-privacy/"
# Android is in closed testing, not public on Google Play, so the title names only the iPhone.
APP_TITLE = "BestBefore — Expiry date tracker for iPhone"
APP_DESC = "BestBefore (Срокоед, Matvakt): a free, open-source expiry date tracker. Scan groceries, get a reminder before food goes off, and cook what is about to expire. No account, no ads."
open("app.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{ICONS}
<title>{APP_TITLE}</title>
<meta name="description" content="{APP_DESC}">
<link rel="canonical" href="{SITE}app.html">
<meta property="og:type" content="website"><meta property="og:site_name" content="BestBefore">
<meta property="og:title" content="{APP_TITLE}"><meta property="og:description" content="{APP_DESC}">
<meta property="og:url" content="{SITE}app.html"><meta property="og:image" content="{SITE}img/en-1.jpg">
<meta property="og:image:width" content="360"><meta property="og:image:height" content="782">
<meta property="og:image:alt" content="{html.escape(ABOUT[0][3][0])}"><meta name="twitter:card" content="summary">
<meta name="robots" content="index,follow"><style>{CSS}
{APP_CSS}</style></head>
<body><main><h1 class="vh">BestBefore · <span lang="ru">Срокоед</span> · <span lang="nb">Matvakt</span></h1>{body}<p class="mut"><a href="index.html">Privacy Policy</a> · <a href="support.html">Support</a></p></main></body></html>""")
s = open("index.html", encoding="utf-8").read()
if "app.html" not in s:
    s = s.replace('<div class="langs">', '<p><a href="app.html">About the app · О приложении · Om appen</a></p><div class="langs">', 1)
    open("index.html", "w", encoding="utf-8").write(s)
