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

NAV = [("en","English"),("ru","Русский"),("nb","Norsk")]
def nav(cur):
    return "<nav>"+" ".join(f'<a href="{c}.html" hreflang="{c}"'+(' aria-current="page"' if c==cur else '')+f'>{n}</a>' for c,n in NAV)+"</nav>"

VERTEX = "https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance"
# Email address for privacy requests made privately. Empty until the owner confirms the address to
# publish; when set, the Contact section in every language gains one sentence with a mailto: link.
# Never put a placeholder here.
PRIVACY_EMAIL = ""
def private_contact(sentence):
    if not PRIVACY_EMAIL:
        return ""
    e = html.escape(PRIVACY_EMAIL)
    return " " + sentence.format(f'<a href="mailto:{e}">{e}</a>')
def L(*items):
    return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"

T = {}
T["en"] = dict(app="BestBefore", title="Privacy Policy", upd="Last updated: 13 November 2026", secs=[
("The short version", ["<p>BestBefore keeps your pantry on your phone. You need no account, and there is no advertising and no analytics. Apart from crash reports (see “Crash reports”), we receive data only from people who buy recipes, and only once they start a purchase (see “Buying recipes”). If you do not buy recipes, nothing changes for you. We do not sell your personal data.</p>"]),
("Who is responsible", ["<p>The data controller is Daniil Pastuhov, Norway: the individual developer who publishes BestBefore and is responsible for the data described in this policy. To reach him, see “Contact”.</p>"]),
("What the app stores", ["<p>Your pantry items, expiry dates, shopping list, settings (including your allergen list and cooking preferences), product photos, saved recipes and any shop locations you save are stored only in the app's local database on your device. They are not sent to us. The one exception is a recipe request from our server, which you send yourself; see “Recipes from our server”.</p>"]),
("Camera", ["<p>The camera is used to scan barcodes, read printed expiry dates and photograph food items. Recognition runs on your device (Google ML Kit on Android, Apple Vision on iOS). Photos you take are saved only on your device.</p>"]),
("Internet requests", ["<p>When you scan a barcode, the app asks <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a> for the product's name and picture. That request contains the barcode number, and, as with any web request, Open Food Facts' servers can see your IP address. No name, account or device identifier is added by the app. Product pictures are also loaded from Open Food Facts. See their <a href=\""+OFF+"\">privacy policy</a>.</p>"]),
("Crash reports", ["<p>If the app crashes, it sends a crash report to Firebase Crashlytics, a Google service, so we can find and fix the bug. A report contains the technical details of the crash (the stack trace), the device model, the operating system and app versions, free memory and disk space at the time, and a random installation ID that Firebase creates to group reports from the same installation. It contains no pantry items, photos, locations, name or account. Crash reports are not used for advertising or tracking, and are kept for 90 days. See <a href=\""+FIREBASE+"\">Firebase's privacy information</a>.</p>"]),
("Location (optional)", ["<p>Location is off by default. If you turn on shop reminders, you can save a shop's position and the app shows your shopping list when you are near it. Saved positions stay on your device. On Android, nearby-shop detection is performed by Google Play services on your device; see <a href=\""+GPS+"\">Google's privacy policy</a>. You can turn the feature off, or revoke the permission, at any time.</p>"]),
("Notifications, backups and sharing", ["<ul><li>Expiry reminders and digests are scheduled locally on your device.</li><li>Exporting a backup or sharing a shopping list or recipe idea only happens when you choose to, and goes where you send it.</li><li>Your phone's own backup (Google or iCloud) may include the app's data. That is controlled by your device settings, not by us.</li></ul>"]),
("Recipes", ["<p>The Recipe tab can suggest a recipe from the items you tick, in three ways:</p>", L(
  "<b>Share or copy a prompt (free).</b> The app writes a text and hands it to the app you choose, or copies it. We receive nothing. What happens next is up to that app and its own privacy policy.",
  "<b>On this phone (free).</b> On supported phones, the phone's own model writes the recipe (Gemini Nano on Android, Apple Foundation Models on iPhone). Nothing is sent to us.",
  "<b>From our server (paid).</b> You buy recipes in Google Play or the App Store, and our server writes each recipe or three-day menu."),
  "<p>The next six sections apply only if you start a purchase of recipes.</p>"]),
("Buying recipes", [
  "<p>You buy recipes through Google Play or the App Store. We never see your payment details. Our server checks each purchase with the store and keeps a record of it: the store, the product, the quantity, the number of recipes, whether it was a test purchase, the dates, its state (added, used, refunded) and the store's order or transaction number. On Google Play, the store's purchase token is kept only until the purchase is completed; after that, only a scrambled (hashed) form of it stays, as the record's name.</p>",
  "<p>Our server runs on Google Firebase: Authentication, Cloud Functions, Firestore and App Check. Cloud Functions run in Google's EU region europe-west1 (Belgium), and Firestore stores its data in the EU.</p>",
  "<p>When you start a purchase, the app creates an anonymous identifier on our server (a random Firebase user ID). It holds your recipe balance and the numbers of recipes bought, used and refunded. It is not linked to your name or email. When you buy, the app gives the store a code made from this identifier, so that the purchase and any refund can be matched to your balance.</p>",
  "<p>Signing in is optional. You can sign in with Apple or Google, so your recipes can be used on other phones. We then keep the account identifier from Apple or Google and your email address (with Sign in with Apple, this may be Apple's relay address). We do not ask for your name. With Sign in with Google, Google also passes the name and profile picture link of your Google account to Firebase Authentication, which keeps them with your account. We do not use them.</p>",
  "<p>If you sign in on a phone that holds recipes under an anonymous identifier, and you agree, those recipes move to your account and the anonymous identifier is deleted. A record that they were moved, and to which account, stays, so that a later refund reaches the right account.</p>"]),
("Recipes from our server", [
  "<p>When you ask our server for a recipe or a three-day menu, the app sends:</p>", L(
  "the names, best-before dates and quantities of the items you ticked (at most 30);",
  "your cooking preferences: difficulty, level of detail, servings, time, meal, diet and language;",
  "the allergen list from Settings;",
  "today's date and a random request number."),
  "<p>Our server passes the items, preferences, allergens and date to Google's Gemini model on Vertex AI, which writes the recipe. No name, email or device identifier is sent to the model. We use Vertex AI's “global” endpoint, so Google may process the request outside the EU/EEA. Google processes it as our service provider under its Google Cloud terms; see <a href=\""+VERTEX+"\">Google's Vertex AI data governance page</a>.</p>",
  "<p>We do not log or keep what you send. Our server keeps only a fingerprint (a hash) of the request, so that a repeated request can be recognised and is not charged twice. The recipe or menu written back, which names the ingredients it uses, is kept on our server for 7 days, so that the app can still collect it if the connection is lost. Then it is deleted automatically (Google's automatic deletion usually runs within a day after that). The app saves the recipe on your phone, where it stays until you delete it.</p>"]),
("Technical data for buyers", [L(
  "<b>App Check.</b> With each request to our server, the app proves that it is a genuine copy, through Firebase App Check: with Google Play Integrity on Android and Apple App Attest on iPhone. This starts only when you start a purchase.",
  "<b>IP address.</b> Our server uses your IP address to limit how many requests one source can send in a minute. It counts requests per address for the current minute in memory only, and does not store the address. Google's infrastructure also records each request to our server, with its IP address, in our server's technical logs.",
  "<b>Usage counts.</b> For each recipe request, our server logs one line with a scrambled (hashed) form of your identifier, the kind of request, how much text the model read and wrote (tokens), the result and the estimated cost. The line never contains your items, allergens, the prompt or the recipe. Our server also keeps, under your identifier, the number of requests and the estimated cost in the current minute and day, to apply limits.",
  "<b>Daily totals.</b> Our server keeps daily totals for all users together (requests, recipes, estimated cost), with no user data.",
  "<b>Technical logs</b> are kept by Google Cloud Logging for 30 days.",
  "<b>Crash reports</b>, as described in “Crash reports”.")]),
("Refunds", [
  "<p>Google Play and the App Store tell our server when a purchase is refunded, and the refunded recipes are taken off your balance. If you had already used them, your balance can go below zero.</p>",
  "<p>On the App Store, if you ask Apple for a refund, we tell Apple whether you used that purchase, and how much of it. The purchase sheet tells you this before you buy.</p>",
  "<p>If purchases are refunded again and again after the recipes were used, buying recipes is switched off for that buyer. To do this, we keep a record of those refunds, tied to a buyer identifier that the App Store provides, or to your account on Google Play.</p>"]),
("Deleting your account", [
  "<p>You can delete your account in the app: Recipe tab → Recipe settings → Delete account. If you are signed in, you sign in once more first. Then:</p>", L(
  "your sign-in and email address are deleted from our server (with Sign in with Google, also the Google name and picture link). On iPhone, if you signed in with Apple, the app also asks Apple to revoke its access to your Apple ID;",
  "the recipes and menus kept on our server, and the per-minute and per-day counts, are deleted;",
  "your unused recipes are lost and cannot be refunded."),
  "<p>What stays, and why:</p>", L(
  "every purchase record, without any link to you. It holds no name or email, but it keeps the store's order or transaction number, which Apple or Google can link to you. It is the only way to stop one store purchase being added twice, and we need it to handle refunds and for our accounts;",
  "a closed record under your old identifier, with the date of deletion, the number of recipes lost and the totals of recipes bought, used and refunded. It stops a deleted account being used again, and keeps our accounts correct;",
  "a record of refunds after use, if there is one (see “Refunds”), to prevent fraud;",
  "technical logs until they expire after 30 days, and the daily totals, which hold no user data."),
  "<p>Deleting the app does not delete anything on our server. If you never signed in, we cannot tell which identifier was yours, so we cannot find or delete it for you later, and its unused recipes are lost. Saved recipes and your pantry stay on your phone until you delete them.</p>"]),
("Who receives data, and where", [L(
  "<b>Google</b>, as our service provider: Firebase (Authentication, App Check, Cloud Functions, Firestore, Crashlytics), Google Cloud Logging and Vertex AI (Gemini). Google Play handles purchases and refunds on Android, and Play Integrity checks the app.",
  "<b>Apple</b>: the App Store handles purchases and refunds on iPhone; App Attest checks the app; Sign in with Apple, if you use it.",
  "<b>Open Food Facts</b>, for barcode lookups, as described above."),
  "<p>We do not show ads, do not use analytics and do not sell your data. Cloud Functions and Firestore are in the EU. Vertex AI's global endpoint, Firebase Authentication, App Check and Crashlytics may process data outside the EU/EEA, for example in the United States. Google covers such transfers in its data processing terms, which include the EU's standard contractual clauses.</p>"]),
("Legal bases", ["<p>Under the GDPR, we rely on:</p>", L(
  "<b>contract</b> (Article 6(1)(b)): to check your purchases, hold your recipes and your sign-in, and write the recipes you ask for;",
  "<b>legitimate interests</b> (Article 6(1)(f)): crash reports, App Check, rate limits, usage counts and refund records, to keep the service working and to prevent fraud and abuse; and keeping purchase records after an account is deleted, so that one purchase cannot be used twice;",
  "<b>legal obligation</b> (Article 6(1)(c)): keeping the records we need for accounting.")]),
("Children", ["<p>The app is not directed at children. Apart from the crash reports and, for people who buy recipes, the data described above, we do not knowingly collect data from anyone.</p>"]),
("Your control and your rights", ["<p>You can edit or delete any item inside the app. Uninstalling the app deletes its data from your device. If you bought recipes, you can delete your account as described in “Deleting your account”.</p>",
  "<p>You have the right to ask for a copy of your data, to have it corrected or deleted, to restrict or object to its use, and to complain to the data protection authority where you live (in Norway, Datatilsynet). To use these rights, contact us (see “Contact”). If you never signed in, we have no way to tell which data is yours.</p>"]),
("Changes", ["<p>If this policy changes, the new version will be published on this page with an updated date.</p>"]),
("Contact", ["<p>Questions or requests? <a href=\""+ISSUES+"\">Open an issue</a> on GitHub. Issues are public, so do not put your email address or other personal details in them."+private_contact("For a privacy request you would rather not make in public, email {}.")+"</p>"]),
], home="Choose your language")

T["ru"] = dict(app="Срокоед", title="Политика конфиденциальности", upd="Последнее обновление: 13 ноября 2026 г.", secs=[
("Коротко", ["<p>Срокоед хранит ваши продукты на вашем телефоне. Аккаунт не нужен, рекламы и аналитики нет. Помимо отчётов о сбоях (см. «Отчёты о сбоях»), мы получаем данные только от тех, кто покупает рецепты, и только после того, как покупка начата (см. «Покупка рецептов»). Если вы не покупаете рецепты, для вас ничего не меняется. Мы не продаём ваши персональные данные.</p>"]),
("Кто отвечает за данные", ["<p>Оператор (контролёр) данных — Daniil Pastuhov, Норвегия: частный разработчик, который публикует Срокоед и отвечает за данные, описанные в этой политике. Как с ним связаться, см. «Контакты».</p>"]),
("Что хранит приложение", ["<p>Продукты, сроки годности, список покупок, настройки (включая список аллергенов и предпочтения в готовке), фотографии продуктов, сохранённые рецепты и сохранённые вами магазины хранятся только в локальной базе данных приложения на вашем устройстве. Они не отправляются нам. Единственное исключение — запрос рецепта с нашего сервера, который вы отправляете сами; см. «Рецепты с нашего сервера».</p>"]),
("Камера", ["<p>Камера используется для сканирования штрихкодов, распознавания напечатанных сроков годности и фотографирования продуктов. Распознавание выполняется на устройстве (Google ML Kit на Android, Apple Vision на iOS). Сделанные фотографии сохраняются только на вашем устройстве.</p>"]),
("Запросы в интернет", ["<p>Когда вы сканируете штрихкод, приложение запрашивает у <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a> название и изображение продукта. Запрос содержит номер штрихкода, а серверы Open Food Facts, как и любого сайта, видят ваш IP-адрес. Приложение не добавляет имя, аккаунт или идентификатор устройства. Изображения продуктов тоже загружаются с Open Food Facts. См. их <a href=\""+OFF+"\">политику конфиденциальности</a>.</p>"]),
("Отчёты о сбоях", ["<p>Если приложение аварийно завершится, оно отправит отчёт о сбое в Firebase Crashlytics, сервис Google, чтобы мы могли найти и исправить ошибку. Отчёт содержит технические сведения о сбое (трассировку стека), модель устройства, версии операционной системы и приложения, объём свободной памяти и места на диске в момент сбоя, а также случайный идентификатор установки, который Firebase создаёт, чтобы объединять отчёты одной установки. В отчёте нет ваших продуктов, фотографий, мест, имени или аккаунта. Отчёты о сбоях не используются для рекламы или отслеживания и хранятся 90 дней. См. <a href=\""+FIREBASE+"\">сведения Firebase о конфиденциальности</a>.</p>"]),
("Местоположение (по желанию)", ["<p>По умолчанию местоположение отключено. Если вы включите напоминания у магазинов, вы можете сохранить положение магазина, и приложение покажет список покупок, когда вы рядом. Сохранённые места остаются на вашем устройстве. На Android определение близости к магазину выполняют сервисы Google Play на вашем устройстве; см. <a href=\""+GPS+"\">политику конфиденциальности Google</a>. Функцию можно отключить, а разрешение отозвать в любой момент.</p>"]),
("Уведомления, резервные копии и обмен", ["<ul><li>Напоминания о сроках и сводки планируются локально на вашем устройстве.</li><li>Экспорт резервной копии и отправка списка покупок или идеи рецепта происходят только по вашему действию и попадают туда, куда вы их отправите.</li><li>Резервная копия самого телефона (Google или iCloud) может включать данные приложения. Это определяется настройками устройства, а не нами.</li></ul>"]),
("Рецепты", ["<p>Во вкладке «Рецепт» можно получить рецепт из отмеченных продуктов тремя способами:</p>", L(
  "<b>Отправить или скопировать запрос (бесплатно).</b> Приложение составляет текст и передаёт его в выбранное вами приложение или копирует его. Мы ничего не получаем. Что будет дальше, зависит от того приложения и его политики конфиденциальности.",
  "<b>На этом телефоне (бесплатно).</b> На поддерживаемых телефонах рецепт пишет собственная модель телефона (Gemini Nano на Android, Apple Foundation Models на iPhone). Нам ничего не отправляется.",
  "<b>С нашего сервера (платно).</b> Вы покупаете рецепты в Google Play или App Store, и каждый рецепт или меню на три дня пишет наш сервер."),
  "<p>Следующие шесть разделов касаются вас, только если вы начали покупку рецептов.</p>"]),
("Покупка рецептов", [
  "<p>Рецепты покупаются через Google Play или App Store. Платёжные данные мы никогда не видим. Наш сервер проверяет каждую покупку в магазине и хранит запись о ней: магазин, товар, количество, число рецептов, была ли это тестовая покупка, даты, состояние (зачислена, использована, возвращена) и номер заказа или транзакции в магазине. В Google Play токен покупки хранится только до завершения покупки; после этого остаётся лишь его необратимо преобразованная (хешированная) форма в качестве имени записи.</p>",
  "<p>Наш сервер работает на Google Firebase: Authentication, Cloud Functions, Firestore и App Check. Cloud Functions работают в регионе Google в ЕС europe-west1 (Бельгия), а Firestore хранит данные в ЕС.</p>",
  "<p>Когда вы начинаете покупку, приложение создаёт на нашем сервере анонимный идентификатор (случайный идентификатор пользователя Firebase). К нему привязаны ваш баланс рецептов и число купленных, использованных и возвращённых рецептов. Он не связан с вашим именем или адресом электронной почты. При покупке приложение передаёт магазину код, полученный из этого идентификатора, чтобы покупку и возможный возврат можно было сопоставить с вашим балансом.</p>",
  "<p>Входить в аккаунт не обязательно. Вы можете войти через Apple или Google, чтобы пользоваться рецептами на других телефонах. Тогда мы храним идентификатор аккаунта Apple или Google и ваш адрес электронной почты (при входе через Apple это может быть адрес-посредник Apple). Мы не спрашиваем ваше имя. При входе через Google Google также передаёт имя и ссылку на фото профиля вашего аккаунта Google в Firebase Authentication, где они хранятся вместе с аккаунтом. Мы их не используем.</p>",
  "<p>Если вы входите на телефоне, где есть рецепты под анонимным идентификатором, и соглашаетесь, эти рецепты переносятся в ваш аккаунт, а анонимный идентификатор удаляется. Остаётся запись о том, что они перенесены, и в какой аккаунт, чтобы последующий возврат попал в нужный аккаунт.</p>"]),
("Рецепты с нашего сервера", [
  "<p>Когда вы запрашиваете у нашего сервера рецепт или меню на три дня, приложение отправляет:</p>", L(
  "названия, сроки годности и количество отмеченных продуктов (не более 30);",
  "ваши предпочтения в готовке: сложность, подробность, число порций, время, приём пищи, диету и язык;",
  "список аллергенов из настроек;",
  "сегодняшнюю дату и случайный номер запроса."),
  "<p>Наш сервер передаёт продукты, предпочтения, аллергены и дату модели Google Gemini в Vertex AI, которая пишет рецепт. Имя, адрес электронной почты или идентификатор устройства модели не отправляются. Мы используем «глобальную» точку доступа Vertex AI (global), поэтому Google может обрабатывать запрос за пределами ЕС/ЕЭЗ. Google обрабатывает его как наш поставщик услуг по условиям Google Cloud; см. <a href=\""+VERTEX+"\">страницу Google об управлении данными в Vertex AI</a>.</p>",
  "<p>Мы не записываем в журналы и не храним то, что вы отправляете. Наш сервер хранит только отпечаток (хеш) запроса, чтобы повторный запрос можно было узнать и не списать за него дважды. Полученный рецепт или меню, где названы использованные продукты, хранится на нашем сервере 7 дней, чтобы приложение могло забрать его, если связь прервалась. Затем он удаляется автоматически (автоматическое удаление Google обычно происходит в течение суток после этого). Приложение сохраняет рецепт на вашем телефоне, где он остаётся, пока вы его не удалите.</p>"]),
("Технические данные покупателей", [L(
  "<b>App Check.</b> При каждом запросе к нашему серверу приложение подтверждает, что это подлинная копия, через Firebase App Check: с помощью Google Play Integrity на Android и Apple App Attest на iPhone. Это начинается только тогда, когда вы начинаете покупку.",
  "<b>IP-адрес.</b> Наш сервер использует ваш IP-адрес, чтобы ограничить число запросов от одного источника в минуту. Он считает запросы с каждого адреса за текущую минуту только в памяти и не сохраняет адрес. Инфраструктура Google также записывает каждый запрос к нашему серверу вместе с IP-адресом в технические журналы нашего сервера.",
  "<b>Учёт использования.</b> Для каждого запроса рецепта наш сервер записывает в журнал одну строку с необратимо преобразованной (хешированной) формой вашего идентификатора, видом запроса, объёмом текста, который модель прочитала и написала (токены), результатом и оценочной стоимостью. В строке никогда нет ваших продуктов, аллергенов, запроса к модели или рецепта. Кроме того, наш сервер хранит под вашим идентификатором число запросов и оценочную стоимость за текущую минуту и день, чтобы применять ограничения.",
  "<b>Дневные итоги.</b> Наш сервер хранит дневные итоги по всем пользователям вместе (запросы, рецепты, оценочная стоимость) без данных пользователей.",
  "<b>Технические журналы</b> хранятся в Google Cloud Logging 30 дней.",
  "<b>Отчёты о сбоях</b> — как описано в разделе «Отчёты о сбоях».")]),
("Возвраты", [
  "<p>Google Play и App Store сообщают нашему серверу, когда за покупку возвращены деньги, и возвращённые рецепты списываются с вашего баланса. Если вы уже их использовали, баланс может стать отрицательным.</p>",
  "<p>Если в App Store вы просите Apple вернуть деньги, мы сообщаем Apple, использовали ли вы эту покупку и в каком объёме. Об этом говорится в окне покупки до того, как вы платите.</p>",
  "<p>Если деньги за покупки возвращают снова и снова после того, как рецепты были использованы, покупка рецептов для этого покупателя отключается. Для этого мы храним запись об этих возвратах, привязанную к идентификатору покупателя, который предоставляет App Store, или к вашему аккаунту в Google Play.</p>"]),
("Удаление аккаунта", [
  "<p>Удалить аккаунт можно в приложении: вкладка «Рецепт» → «Настройки рецептов» → «Удалить аккаунт». Если вы вошли в аккаунт, сначала нужно войти ещё раз. Затем:</p>", L(
  "ваш вход и адрес электронной почты удаляются с нашего сервера (при входе через Google — также имя и ссылка на фото из Google). На iPhone, если вы входили через Apple, приложение также просит Apple отозвать его доступ к вашему Apple ID;",
  "рецепты и меню, хранящиеся на нашем сервере, а также счётчики за минуту и день удаляются;",
  "неиспользованные рецепты теряются, и деньги за них не возвращаются."),
  "<p>Что остаётся и почему:</p>", L(
  "все записи о покупках, без связи с вами. В них нет имени или адреса электронной почты, но остаётся номер заказа или транзакции в магазине, по которому Apple или Google могут связать покупку с вами. Это единственный способ не дать зачислить одну покупку дважды, и эти записи нужны нам для обработки возвратов и для бухгалтерии;",
  "закрытая запись под вашим прежним идентификатором с датой удаления, числом потерянных рецептов и итогами купленных, использованных и возвращённых рецептов. Она не даёт снова пользоваться удалённым аккаунтом и сохраняет нашу отчётность верной;",
  "запись о возвратах после использования, если она есть (см. «Возвраты»), для предотвращения мошенничества;",
  "технические журналы, пока они не истекут через 30 дней, и дневные итоги, в которых нет данных пользователей."),
  "<p>Удаление приложения ничего не удаляет на нашем сервере. Если вы ни разу не входили в аккаунт, мы не можем понять, какой идентификатор был вашим, поэтому не сможем потом найти или удалить его для вас, а его неиспользованные рецепты теряются. Сохранённые рецепты и ваши продукты остаются на телефоне, пока вы их не удалите.</p>"]),
("Кто получает данные и где", [L(
  "<b>Google</b> как наш поставщик услуг: Firebase (Authentication, App Check, Cloud Functions, Firestore, Crashlytics), Google Cloud Logging и Vertex AI (Gemini). Google Play обрабатывает покупки и возвраты на Android, а Play Integrity проверяет приложение.",
  "<b>Apple</b>: App Store обрабатывает покупки и возвраты на iPhone; App Attest проверяет приложение; вход через Apple, если вы им пользуетесь.",
  "<b>Open Food Facts</b> — для поиска по штрихкоду, как описано выше."),
  "<p>Мы не показываем рекламу, не используем аналитику и не продаём ваши данные. Cloud Functions и Firestore находятся в ЕС. Глобальная точка доступа Vertex AI, Firebase Authentication, App Check и Crashlytics могут обрабатывать данные за пределами ЕС/ЕЭЗ, например в США. Google обеспечивает такие передачи своими условиями обработки данных, которые включают стандартные договорные положения ЕС.</p>"]),
("Правовые основания", ["<p>Согласно GDPR, мы опираемся на:</p>", L(
  "<b>договор</b> (статья 6(1)(b)): чтобы проверять ваши покупки, хранить ваши рецепты и ваш вход и писать рецепты, которые вы запрашиваете;",
  "<b>законные интересы</b> (статья 6(1)(f)): отчёты о сбоях, App Check, ограничения частоты запросов, учёт использования и записи о возвратах — чтобы сервис работал и чтобы предотвращать мошенничество и злоупотребления; а также хранение записей о покупках после удаления аккаунта, чтобы одну покупку нельзя было использовать дважды;",
  "<b>юридическую обязанность</b> (статья 6(1)(c)): хранение записей, нужных для бухгалтерии.")]),
("Дети", ["<p>Приложение не предназначено для детей. Помимо отчётов о сбоях и, для тех, кто покупает рецепты, данных, описанных выше, мы сознательно не собираем ничьих данных.</p>"]),
("Ваш контроль и ваши права", ["<p>Любой продукт можно изменить или удалить прямо в приложении. При удалении приложения его данные удаляются с вашего устройства. Если вы покупали рецепты, вы можете удалить аккаунт, как описано в разделе «Удаление аккаунта».</p>",
  "<p>Вы вправе запросить копию своих данных, потребовать их исправить или удалить, ограничить их использование или возразить против него, а также подать жалобу в орган по защите данных по месту жительства (в Норвегии — Datatilsynet). Чтобы воспользоваться этими правами, свяжитесь с нами (см. «Контакты»). Если вы ни разу не входили в аккаунт, мы не можем понять, какие данные ваши.</p>"]),
("Изменения", ["<p>Если политика изменится, новая версия будет опубликована на этой странице с обновлённой датой.</p>"]),
("Контакты", ["<p>Есть вопросы или запросы? <a href=\""+ISSUES+"\">Создайте обращение (issue)</a> на GitHub. Обращения публичны, поэтому не указывайте в них адрес электронной почты и другие личные данные."+private_contact("Если вы не хотите отправлять запрос о персональных данных публично, напишите на {}.")+"</p>"]),
], home="Выберите язык")

T["nb"] = dict(app="Matvakt", title="Personvernerklæring", upd="Sist oppdatert: 13. november 2026", secs=[
("Kort fortalt", ["<p>Matvakt oppbevarer matvarene dine på telefonen din. Du trenger ingen konto, og det finnes ingen reklame og ingen analyse. Utenom krasjrapporter (se «Krasjrapporter») mottar vi data bare fra dem som kjøper oppskrifter, og bare etter at de har startet et kjøp (se «Kjøp av oppskrifter»). Kjøper du ikke oppskrifter, endres ingenting for deg. Vi selger ikke personopplysningene dine.</p>"]),
("Hvem som er ansvarlig", ["<p>Behandlingsansvarlig er Daniil Pastuhov, Norge: enkeltpersonen som utvikler og publiserer Matvakt, og som er ansvarlig for dataene som er beskrevet i denne erklæringen. Se «Kontakt» for hvordan du når ham.</p>"]),
("Hva appen lagrer", ["<p>Matvarer, utløpsdatoer, handleliste, innstillinger (også allergenlisten og matlagingsvalgene dine), bilder av produkter, lagrede oppskrifter og butikker du har lagret, lagres bare i appens lokale database på enheten din. De sendes ikke til oss. Det eneste unntaket er en forespørsel om oppskrift fra serveren vår, som du sender selv; se «Oppskrifter fra serveren vår».</p>"]),
("Kamera", ["<p>Kameraet brukes til å skanne strekkoder, lese påtrykte utløpsdatoer og ta bilder av matvarer. Gjenkjenningen skjer på enheten (Google ML Kit på Android, Apple Vision på iOS). Bilder du tar lagres bare på enheten din.</p>"]),
("Internett-forespørsler", ["<p>Når du skanner en strekkode, henter appen produktets navn og bilde fra <a href=\"https://world.openfoodfacts.org\">Open Food Facts</a>. Forespørselen inneholder strekkodenummeret, og som ved alle nettforespørsler kan Open Food Facts' servere se IP-adressen din. Appen legger ikke til navn, konto eller enhetsidentifikator. Produktbilder lastes også fra Open Food Facts. Se deres <a href=\""+OFF+"\">personvernerklæring</a>.</p>"]),
("Krasjrapporter", ["<p>Hvis appen krasjer, sender den en krasjrapport til Firebase Crashlytics, en tjeneste fra Google, slik at vi kan finne og rette feilen. Rapporten inneholder tekniske detaljer om krasjet (stakksporing), enhetsmodell, versjon av operativsystemet og appen, ledig minne og lagringsplass da krasjet skjedde, og en tilfeldig installasjons-ID som Firebase lager for å gruppere rapporter fra samme installasjon. Den inneholder ingen matvarer, bilder, posisjoner, navn eller konto. Krasjrapporter brukes ikke til reklame eller sporing, og lagres i 90 dager. Se <a href=\""+FIREBASE+"\">Firebases personverninformasjon</a>.</p>"]),
("Posisjon (valgfritt)", ["<p>Posisjon er slått av som standard. Slår du på butikkpåminnelser, kan du lagre posisjonen til en butikk, og appen viser handlelisten når du er i nærheten. Lagrede posisjoner blir på enheten din. På Android utføres oppdagelsen av nærliggende butikker av Google Play-tjenester på enheten din; se <a href=\""+GPS+"\">Googles personvernerklæring</a>. Du kan slå av funksjonen eller trekke tilbake tillatelsen når som helst.</p>"]),
("Varsler, sikkerhetskopier og deling", ["<ul><li>Påminnelser om utløpsdatoer og sammendrag planlegges lokalt på enheten din.</li><li>Eksport av sikkerhetskopi og deling av handleliste eller oppskriftsidé skjer bare når du velger det, og går dit du sender det.</li><li>Telefonens egen sikkerhetskopi (Google eller iCloud) kan inneholde appens data. Det styres av enhetens innstillinger, ikke av oss.</li></ul>"]),
("Oppskrifter", ["<p>I Oppskrift-fanen kan du få en oppskrift ut fra varene du krysser av, på tre måter:</p>", L(
  "<b>Del eller kopier en ledetekst (gratis).</b> Appen skriver en tekst og gir den til appen du velger, eller kopierer den. Vi mottar ingenting. Hva som skjer videre, avgjøres av den appen og dens egen personvernerklæring.",
  "<b>På denne telefonen (gratis).</b> På telefoner som støtter det, skriver telefonens egen modell oppskriften (Gemini Nano på Android, Apple Foundation Models på iPhone). Ingenting sendes til oss.",
  "<b>Fra serveren vår (betalt).</b> Du kjøper oppskrifter i Google Play eller App Store, og serveren vår skriver hver oppskrift eller meny for tre dager."),
  "<p>De neste seks avsnittene gjelder bare hvis du starter et kjøp av oppskrifter.</p>"]),
("Kjøp av oppskrifter", [
  "<p>Du kjøper oppskrifter gjennom Google Play eller App Store. Vi ser aldri betalingsopplysningene dine. Serveren vår kontrollerer hvert kjøp hos butikken og tar vare på en oversikt over det: butikken, produktet, antallet, antall oppskrifter, om det var et testkjøp, datoene, tilstanden (lagt til, brukt, refundert) og butikkens ordre- eller transaksjonsnummer. I Google Play lagres butikkens kjøpstoken bare til kjøpet er fullført; deretter er det bare en enveis omgjort (hashet) form av den som blir igjen, som navnet på oppføringen.</p>",
  "<p>Serveren vår kjører på Google Firebase: Authentication, Cloud Functions, Firestore og App Check. Cloud Functions kjører i Googles EU-region europe-west1 (Belgia), og Firestore lagrer dataene sine i EU.</p>",
  "<p>Når du starter et kjøp, oppretter appen en anonym identifikator på serveren vår (en tilfeldig Firebase-bruker-ID). Den holder saldoen din av oppskrifter og antallet oppskrifter som er kjøpt, brukt og refundert. Den er ikke knyttet til navnet eller e-postadressen din. Når du kjøper, gir appen butikken en kode laget av denne identifikatoren, slik at kjøpet og en eventuell refusjon kan kobles til saldoen din.</p>",
  "<p>Innlogging er valgfritt. Du kan logge inn med Apple eller Google, slik at oppskriftene kan brukes på andre telefoner. Da tar vi vare på kontoidentifikatoren fra Apple eller Google og e-postadressen din (med Logg på med Apple kan dette være Apples videresendingsadresse). Vi spør ikke om navnet ditt. Med Logg på med Google sender Google også navnet og lenken til profilbildet på Google-kontoen din til Firebase Authentication, som lagrer dem sammen med kontoen. Vi bruker dem ikke.</p>",
  "<p>Hvis du logger inn på en telefon som har oppskrifter under en anonym identifikator, og du samtykker, flyttes de oppskriftene til kontoen din, og den anonyme identifikatoren slettes. En oppføring om at de ble flyttet, og til hvilken konto, blir værende, slik at en senere refusjon havner på riktig konto.</p>"]),
("Oppskrifter fra serveren vår", [
  "<p>Når du ber serveren vår om en oppskrift eller en meny for tre dager, sender appen:</p>", L(
  "navnene, utløpsdatoene og antallet av varene du krysset av (høyst 30);",
  "matlagingsvalgene dine: vanskelighetsgrad, detaljnivå, porsjoner, tid, måltid, diett og språk;",
  "allergenlisten fra Innstillinger;",
  "dagens dato og et tilfeldig forespørselsnummer."),
  "<p>Serveren vår sender varene, valgene, allergenene og datoen videre til Googles Gemini-modell i Vertex AI, som skriver oppskriften. Ingen navn, e-postadresse eller enhetsidentifikator sendes til modellen. Vi bruker Vertex AIs «globale» endepunkt (global), så Google kan behandle forespørselen utenfor EU/EØS. Google behandler den som vår tjenesteleverandør etter Google Clouds vilkår; se <a href=\""+VERTEX+"\">Googles side om datastyring i Vertex AI</a>.</p>",
  "<p>Vi logger ikke og tar ikke vare på det du sender. Serveren vår lagrer bare et fingeravtrykk (en hash) av forespørselen, slik at en gjentatt forespørsel kan kjennes igjen og ikke belastes to ganger. Oppskriften eller menyen som skrives tilbake, og som nevner ingrediensene den bruker, lagres på serveren vår i 7 dager, slik at appen fortsatt kan hente den hvis forbindelsen blir brutt. Deretter slettes den automatisk (Googles automatiske sletting skjer vanligvis innen et døgn etter det). Appen lagrer oppskriften på telefonen din, der den blir til du sletter den.</p>"]),
("Tekniske data for kjøpere", [L(
  "<b>App Check.</b> Ved hver forespørsel til serveren vår beviser appen at den er en ekte kopi, gjennom Firebase App Check: med Google Play Integrity på Android og Apple App Attest på iPhone. Dette starter først når du starter et kjøp.",
  "<b>IP-adresse.</b> Serveren vår bruker IP-adressen din til å begrense hvor mange forespørsler én kilde kan sende i minuttet. Den teller forespørsler per adresse for inneværende minutt bare i minnet, og lagrer ikke adressen. Googles infrastruktur registrerer også hver forespørsel til serveren vår, med IP-adressen, i serverens tekniske logger.",
  "<b>Bruksdata.</b> For hver forespørsel om oppskrift logger serveren vår én linje med en enveis omgjort (hashet) form av identifikatoren din, typen forespørsel, hvor mye tekst modellen leste og skrev (tokens), resultatet og den anslåtte kostnaden. Linjen inneholder aldri varene dine, allergenene, ledeteksten eller oppskriften. Serveren vår lagrer også, under identifikatoren din, antall forespørsler og anslått kostnad i inneværende minutt og døgn, for å håndheve grenser.",
  "<b>Daglige totaler.</b> Serveren vår lagrer daglige totaler for alle brukere samlet (forespørsler, oppskrifter, anslått kostnad), uten brukerdata.",
  "<b>Tekniske logger</b> lagres av Google Cloud Logging i 30 dager.",
  "<b>Krasjrapporter</b>, som beskrevet under «Krasjrapporter».")]),
("Refusjoner", [
  "<p>Google Play og App Store gir serveren vår beskjed når et kjøp blir refundert, og de refunderte oppskriftene trekkes fra saldoen din. Hvis du allerede har brukt dem, kan saldoen bli negativ.</p>",
  "<p>I App Store: Hvis du ber Apple om refusjon, forteller vi Apple om du har brukt det kjøpet, og hvor mye av det. Kjøpsarket sier dette før du kjøper.</p>",
  "<p>Hvis kjøp blir refundert igjen og igjen etter at oppskriftene er brukt, slås kjøp av oppskrifter av for den kjøperen. For å gjøre dette tar vi vare på en oversikt over disse refusjonene, knyttet til en kjøperidentifikator som App Store gir oss, eller til kontoen din i Google Play.</p>"]),
("Slette kontoen", [
  "<p>Du kan slette kontoen din i appen: Oppskrift-fanen → Oppskriftsinnstillinger → Slett konto. Er du logget inn, logger du inn én gang til først. Deretter:</p>", L(
  "innloggingen og e-postadressen din slettes fra serveren vår (med Logg på med Google også navnet og bildelenken fra Google). På iPhone, hvis du logget inn med Apple, ber appen også Apple om å trekke tilbake appens tilgang til Apple-ID-en din;",
  "oppskriftene og menyene som er lagret på serveren vår, og tellerne for minutt og døgn, slettes;",
  "ubrukte oppskrifter går tapt og kan ikke refunderes."),
  "<p>Hva som blir igjen, og hvorfor:</p>", L(
  "alle kjøpsoppføringer, uten noen kobling til deg. De inneholder ikke navn eller e-postadresse, men beholder butikkens ordre- eller transaksjonsnummer, som Apple eller Google kan knytte til deg. Det er den eneste måten å hindre at ett kjøp i butikken legges til to ganger, og vi trenger dem for å håndtere refusjoner og for regnskapet vårt;",
  "en lukket oppføring under den gamle identifikatoren din, med slettedatoen, antall oppskrifter som gikk tapt, og totalene for oppskrifter som er kjøpt, brukt og refundert. Den hindrer at en slettet konto brukes igjen, og holder regnskapet vårt riktig;",
  "en oversikt over refusjoner etter bruk, hvis det finnes en (se «Refusjoner»), for å forhindre svindel;",
  "tekniske logger til de utløper etter 30 dager, og de daglige totalene, som ikke inneholder brukerdata."),
  "<p>Å slette appen sletter ingenting på serveren vår. Hvis du aldri har logget inn, kan vi ikke vite hvilken identifikator som var din, så vi kan ikke finne eller slette den for deg senere, og de ubrukte oppskriftene på den går tapt. Lagrede oppskrifter og matvarene dine blir på telefonen til du sletter dem.</p>"]),
("Hvem mottar data, og hvor", [L(
  "<b>Google</b>, som vår tjenesteleverandør: Firebase (Authentication, App Check, Cloud Functions, Firestore, Crashlytics), Google Cloud Logging og Vertex AI (Gemini). Google Play håndterer kjøp og refusjoner på Android, og Play Integrity kontrollerer appen.",
  "<b>Apple</b>: App Store håndterer kjøp og refusjoner på iPhone; App Attest kontrollerer appen; Logg på med Apple, hvis du bruker det.",
  "<b>Open Food Facts</b>, for strekkodeoppslag, som beskrevet over."),
  "<p>Vi viser ikke reklame, bruker ikke analyse og selger ikke dataene dine. Cloud Functions og Firestore er i EU. Vertex AIs globale endepunkt, Firebase Authentication, App Check og Crashlytics kan behandle data utenfor EU/EØS, for eksempel i USA. Google dekker slike overføringer i sine databehandlingsvilkår, som inneholder EUs standard personvernbestemmelser.</p>"]),
("Rettslig grunnlag", ["<p>Etter personvernforordningen (GDPR) bygger vi på:</p>", L(
  "<b>avtale</b> (artikkel 6 nr. 1 bokstav b): for å kontrollere kjøpene dine, holde oppskriftene og innloggingen din og skrive oppskriftene du ber om;",
  "<b>berettiget interesse</b> (artikkel 6 nr. 1 bokstav f): krasjrapporter, App Check, begrensning av forespørsler, bruksdata og oversikter over refusjoner, for å holde tjenesten i gang og forhindre svindel og misbruk; og at kjøpsoppføringer beholdes etter at en konto er slettet, slik at ett kjøp ikke kan brukes to ganger;",
  "<b>rettslig forpliktelse</b> (artikkel 6 nr. 1 bokstav c): å ta vare på oppføringene vi trenger for regnskapet.")]),
("Barn", ["<p>Appen er ikke rettet mot barn. Utover krasjrapportene og, for dem som kjøper oppskrifter, dataene beskrevet over, samler vi ikke bevisst inn data fra noen.</p>"]),
("Din kontroll og dine rettigheter", ["<p>Du kan endre eller slette alle matvarer i appen. Avinstallerer du appen, slettes dataene fra enheten din. Har du kjøpt oppskrifter, kan du slette kontoen din som beskrevet under «Slette kontoen».</p>",
  "<p>Du har rett til å be om en kopi av dataene dine, få dem rettet eller slettet, begrense eller protestere mot bruken av dem, og klage til datatilsynsmyndigheten der du bor (i Norge: Datatilsynet). For å bruke disse rettighetene, kontakt oss (se «Kontakt»). Hvis du aldri har logget inn, har vi ingen måte å vite hvilke data som er dine.</p>"]),
("Endringer", ["<p>Hvis erklæringen endres, publiseres den nye versjonen på denne siden med oppdatert dato.</p>"]),
("Kontakt", ["<p>Spørsmål eller forespørsler? <a href=\""+ISSUES+"\">Opprett en sak (issue)</a> på GitHub. Saker er offentlige, så ikke skriv e-postadressen din eller andre personopplysninger i dem."+private_contact("Hvis du ikke vil sende en forespørsel om personvern offentlig, send e-post til {}.")+"</p>"]),
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

# --- Support page (the App Store's required Support URL) -------------------------------------
APPLE_REFUND = "https://support.apple.com/118223"
GOOGLE_REFUND = "https://support.google.com/googleplay/answer/2479637"
SUPPORT = [
 ("en", "BestBefore — Support", [
  ("Contact", f'<p>Found a bug or have an idea? <a href="{ISSUES}">Open an issue on GitHub</a>. We read every one.</p>'),
  ("Where is my data?", "<p>Your pantry is stored only on your phone, and you need no account for it, so we cannot see or recover it. Use <b>Settings → Data → Export backup</b> to save a copy, and import it on a new phone. If you buy recipes, Google Play or the App Store takes the payment and our server keeps your recipe balance; signing in is optional. See the <a href=\"en.html\">privacy policy</a>.</p>"),
  ("Reminders don't arrive", "<p>Check that notifications are allowed for BestBefore in your phone's settings, and set the reminder time in <b>Settings → Notifications</b>.</p>"),
  ("Shop reminders", "<p>Optional. Save a shop in <b>Settings → Shopping reminders</b>. To get reminders while the app is closed, allow location access <b>always</b> (iPhone) or <b>all the time</b> (Android).</p>"),
  ("Where are my bought recipes?", "<p>If you have not signed in, they stay with this install of the app: if you delete the app or change phone, the unused ones are lost. If you signed in with Apple or Google, they are kept in your account: after reinstalling, or on a new phone, sign in the same way to use them.</p>"),
  ("I paid, but no recipes were added", "<p>The app keeps trying to confirm the purchase and adds the recipes when it succeeds, so you do not need to buy again. Open the Recipe tab while online, or tap <b>Try now</b>. If the store is still waiting for your payment, the recipes are added when it confirms. If you would rather have your money back, ask the store for a refund.</p>"),
  ("Refunds", f'<p>Refunds are handled by the store, not by us: <a href="{GOOGLE_REFUND}">Google Play</a> or <a href="{APPLE_REFUND}">the App Store</a>. Refunded recipes are taken off your balance.</p>'),
  ("Deleting your account", "<p>Use <b>Recipe → Recipe settings → Delete account</b>. Your sign-in and email address are deleted from our server, and your unused recipes are lost and cannot be refunded. A record of your purchases stays, no longer linked to you. Your pantry and saved recipes stay on the phone.</p>"),
  ("Deleting your data", "<p>Delete items in the app, use <b>Settings → Data → Clear All Pantry Data</b>, or uninstall the app.</p>"),
 ]),
 ("ru", "Срокоед — поддержка", [
  ("Связаться с нами", f'<p>Нашли ошибку или есть идея? <a href="{ISSUES}">Создайте обращение (issue) на GitHub</a>. Мы читаем каждое.</p>'),
  ("Где хранятся мои данные?", "<p>Продукты хранятся только на вашем телефоне, и аккаунт для этого не нужен, поэтому мы не можем их увидеть или восстановить. Сохраните копию через <b>Настройки → Данные → Экспорт копии</b> и импортируйте её на новом телефоне. Если вы покупаете рецепты, оплату принимает Google Play или App Store, а наш сервер хранит ваш баланс рецептов; входить в аккаунт не обязательно. См. <a href=\"ru.html\">политику конфиденциальности</a>.</p>"),
  ("Не приходят напоминания", "<p>Проверьте, что уведомления для Срокоеда разрешены в настройках телефона, и задайте время в <b>Настройки → Уведомления</b>.</p>"),
  ("Напоминания у магазина", "<p>По желанию. Сохраните магазин в <b>Настройки → Напоминания о покупках</b>. Чтобы напоминания приходили при закрытом приложении, разрешите доступ к геопозиции <b>всегда</b> (iPhone) или <b>в любом режиме</b> (Android).</p>"),
  ("Где мои купленные рецепты?", "<p>Если вы не входили в аккаунт, они привязаны к этой установке приложения: если удалить приложение или сменить телефон, неиспользованные рецепты теряются. Если вы вошли через Apple или Google, они хранятся в вашем аккаунте: после переустановки или на новом телефоне войдите тем же способом, чтобы ими пользоваться.</p>"),
  ("Я заплатил, но рецепты не добавились", "<p>Приложение продолжает подтверждать покупку и добавит рецепты, когда это получится, поэтому покупать заново не нужно. Откройте вкладку «Рецепт» при подключении к интернету или нажмите <b>Повторить сейчас</b>. Если магазин ещё ждёт оплату, рецепты добавятся, когда он её подтвердит. Если вы хотите вернуть деньги, попросите возврат в магазине.</p>"),
  ("Возвраты", f'<p>Возвратами занимается магазин, а не мы: <a href="{GOOGLE_REFUND}">Google Play</a> или <a href="{APPLE_REFUND}">App Store</a>. Возвращённые рецепты списываются с вашего баланса.</p>'),
  ("Удаление аккаунта", "<p>Откройте <b>Рецепт → Настройки рецептов → Удалить аккаунт</b>. Ваш вход и адрес электронной почты удаляются с нашего сервера, а неиспользованные рецепты теряются, и деньги за них не возвращаются. Запись о ваших покупках остаётся, но уже не связана с вами. Продукты и сохранённые рецепты остаются на телефоне.</p>"),
  ("Удаление данных", "<p>Удалите продукты в приложении, воспользуйтесь <b>Настройки → Данные → Очистить все данные кладовой</b> или удалите приложение.</p>"),
 ]),
 ("nb", "Matvakt — brukerstøtte", [
  ("Kontakt", f'<p>Fant du en feil eller har en idé? <a href="{ISSUES}">Opprett en sak (issue) på GitHub</a>. Vi leser alle.</p>'),
  ("Hvor er dataene mine?", "<p>Matvarene lagres bare på telefonen din, og du trenger ingen konto for dem, så vi kan ikke se eller gjenopprette dem. Ta en kopi under <b>Innstillinger → Data → Eksporter sikkerhetskopi</b> og importer den på en ny telefon. Kjøper du oppskrifter, tar Google Play eller App Store imot betalingen, og serveren vår holder saldoen din av oppskrifter; innlogging er valgfritt. Se <a href=\"nb.html\">personvernerklæringen</a>.</p>"),
  ("Påminnelsene kommer ikke", "<p>Sjekk at varsler er tillatt for Matvakt i telefonens innstillinger, og velg tidspunkt under <b>Innstillinger → Varsler</b>.</p>"),
  ("Butikkpåminnelser", "<p>Valgfritt. Lagre en butikk under <b>Innstillinger → Handlepåminnelser</b>. For påminnelser når appen er lukket, tillat posisjon <b>alltid</b> (iPhone) eller <b>hele tiden</b> (Android).</p>"),
  ("Hvor er oppskriftene jeg har kjøpt?", "<p>Hvis du ikke har logget inn, hører de til denne installasjonen av appen: sletter du appen eller bytter telefon, går de ubrukte tapt. Hvis du logget inn med Apple eller Google, ligger de på kontoen din: etter ny installasjon, eller på en ny telefon, logger du inn på samme måte for å bruke dem.</p>"),
  ("Jeg betalte, men fikk ingen oppskrifter", "<p>Appen fortsetter å prøve å bekrefte kjøpet og legger til oppskriftene når det lykkes, så du trenger ikke å kjøpe på nytt. Åpne Oppskrift-fanen med internettforbindelse, eller trykk <b>Prøv nå</b>. Hvis butikken fortsatt venter på betalingen, legges oppskriftene til når den bekrefter. Vil du heller ha pengene tilbake, ber du butikken om refusjon.</p>"),
  ("Refusjoner", f'<p>Refusjoner håndteres av butikken, ikke av oss: <a href="{GOOGLE_REFUND}">Google Play</a> eller <a href="{APPLE_REFUND}">App Store</a>. Refunderte oppskrifter trekkes fra saldoen din.</p>'),
  ("Slette kontoen", "<p>Bruk <b>Oppskrift → Oppskriftsinnstillinger → Slett konto</b>. Innloggingen og e-postadressen din slettes fra serveren vår, og ubrukte oppskrifter går tapt og kan ikke refunderes. En oversikt over kjøpene dine blir igjen, uten kobling til deg. Matvarene og de lagrede oppskriftene blir på telefonen.</p>"),
  ("Slette dataene", "<p>Slett varer i appen, bruk <b>Innstillinger → Data → Tøm alle data i matskapet</b>, eller avinstaller appen.</p>"),
 ]),
]
body = '<nav>' + " ".join(f'<a href="#{c}">{n}</a>' for c, n in NAV) + '</nav>'
for code, title, secs in SUPPORT:
    body += f'<section id="{code}" lang="{code}"><h1>{title}</h1>' + "".join(f"<h2>{h}</h2>{p}" for h, p in secs) + "</section><hr>"
open("support.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BestBefore — Support</title><style>{CSS} hr{{border:0;border-top:1px solid var(--bd);margin:40px 0}}</style></head>
<body><main>{body}<p class="mut"><a href="index.html">Privacy Policy</a></p></main></body></html>""")
s = open("index.html", encoding="utf-8").read()
if "support.html" not in s:
    s = s.replace('</div></main>', '</div><p><a href="support.html">Support · Поддержка · Brukerstøtte</a></p></main>')
    open("index.html", "w", encoding="utf-8").write(s)
