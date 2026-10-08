import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://brightnestq.com/click?key=8227f80b0c6b400998699bf6257db3c8", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Skaityti", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Skaityti dabar", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Skaityti dabar", url="https://brightnestq.com/click?key=8227f80b0c6b400998699bf6257db3c8")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("📰 *Sveiki atvyke i Dienos Skaityma.*\n\n"
        "Kiekviena diena atrinkti straipsniai "
        "apie kultura, keliones, virtuve, "
        "moksla ir technologijas — skaitymui "
        "ramiai pokalbyje.\n\n"
        "Paspauskite *Dienos temos* "
        "kad pradetumete.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Kultura — rudens parodos", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Virtuve — lietuviski receptai", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Keliones — penki miesteliai", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("📋 *Dienos temos*\n\n"
        "Trys skaitymai pasirinkti siandien. "
        "Kiekvienas pilnas pokalbyje.\n\n"
        "*Kultura* — rudens parodos: penki "
        "renginiai Lietuvos muziejuose.\n\n"
        "*Virtuve* — lietuviski klasikai: keturi "
        "tradiciniai receptai.\n\n"
        "*Keliones* — penki Lietuvos miesteliai "
        "rudens savaitgaliui.\n\n"
        "Paspauskite antraste kad atidarytumete.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("🎨 *Rudens parodos: penki renginiai "
        "Lietuvos muziejuose*\n\n"
        "Muziejai atidaro nauja sezona.\n\n"
        "*Vilnius — Nacionaline dailes galerija*\n"
        "Didele lietuviu modernaus meno "
        "retrospektyva. Reti kuriniai is "
        "privacių kolekciju ir nepublikuota "
        "archyvine medziaga.\n\n"
        "*Kaunas — M. K. Ciurlionio muziejus*\n"
        "Ciurlionio tapyba ir muzika "
        "naujoje ekspozicijoje. Menas "
        "ir garsas viename.\n\n"
        "*Klaipeda — Lietuvos juru muziejus*\n"
        "Baltijos juros istorija nuo "
        "vikingu iki siuolaikinės laivybos. "
        "Interaktyvios parodos vaikams "
        "ir suaugusiems.\n\n"
        "*Siauliai — Fotografijos muziejus*\n"
        "Nespalvoti reportazai apie "
        "pokario Lietuva. Dokumentinis "
        "ir poetinis zvilgsnis.\n\n"
        "*Druskininkai — Grutas parkas*\n"
        "Sovietiniu skulpturu kolekcija "
        "misku apsuptyje. Istorija "
        "ir atmintis po atviru dangumi.\n\n"
        "_Darbo laikas muzieju svetainese._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("🍳 *Lietuviski klasikai: keturi "
        "tradiciniai receptai*\n\n"
        "Lietuvos virtuve yra sirdinga "
        "ir sotinanti.\n\n"
        "*Cepelinai*\n"
        "Tartu bulviu tesilos idaryti mesa "
        "arba varske. Verdami ir patiekiami "
        "su spirguciais ir grietine. "
        "Lietuvos nacionalinis patiekalas.\n\n"
        "*Saltibarsciai*\n"
        "Saltoji burokeliu sriuba su "
        "kefyru, agurkais, kiausiniais "
        "ir krapais. Patiekiama su "
        "karstu bulviu. Vasaros klasika.\n\n"
        "*Kibinai*\n"
        "Pusmenulio formos pyrageliai "
        "su aviena ir svogunu idaru. "
        "Karaimu tradicija is Traku. "
        "Traski plutele ir sultingas "
        "vidus.\n\n"
        "*Sakotis*\n"
        "Ant iesmeles keptas tortas "
        "is kiausiniu teslos. Saku "
        "formos sakos. Svenciu stalas "
        "be sakocio neimanomas.\n\n"
        "_Kiekiai pagal savo skoni._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("🏠 *Penki Lietuvos miesteliai "
        "rudens savaitgaliui*\n\n"
        "*Trakai*\n"
        "Pilis ant salos ezere. Karaimu "
        "kultura, kibinai ir vandens "
        "atspindziai rudeni. Vienas "
        "graziausiu Lietuvos vaizdu.\n\n"
        "*Kernave*\n"
        "UNESCO paveldo vieta. Penki "
        "piliakalniai virs Neries. "
        "Archeologija, gamta ir tyla.\n\n"
        "*Nida*\n"
        "Kursu nerija. Kopagubris, "
        "Thomo Manno namas ir saulrietis "
        "virs mariu. Rudeni ramu ir tuščia.\n\n"
        "*Anyksciai*\n"
        "Laju takas misko virsunese. "
        "Siaurasis gelezinkelis, vyno "
        "darymas ir Puntukas. Aukstaitijos "
        "sirdis.\n\n"
        "*Zemaitijos Kalvarija*\n"
        "Tyli vieta Zemaitijoje. Baznycia, "
        "mediniai namai ir misko takai. "
        "Lietuvos kaimas gryniausia forma.\n\n"
        "_Apgyvendinima uzsisakykite is anksto._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Zodynas", callback_data="glossary"), types.InlineKeyboardButton(text="❓ DUK", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Kontaktai", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Apie mus", callback_data="about"))
    text = ("🏛 *Santrauka*\n\n"
        "Is sio meniu galite:\n\n"
        "• Skaityti *dienos temas* ir musu straipsnius.\n"
        "• Narsyti skyrius: Kultura, "
        "Keliones, Virtuve, Mokslas.\n"
        "• Perziureti zodyna ir DUK.\n"
        "• Suzinoti apie mus ir susisiekti.\n\n"
        "Pilnam leidimui naudokite "
        "mygtuka zemiau.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("📖 *Trumpas zodynas*\n\n"
        "*Redakcija* — komanda, kuri "
        "atrenka ir rengia tekstus.\n\n"
        "*Vedamasis* — nuomones straipsnis "
        "atidarantis skyriu.\n\n"
        "*Fotoreportazas* — zurnalistine "
        "istorija, sukurta is nuotrauku.\n\n"
        "*Nesenstantis turinys* — tekstas, "
        "kurio aktualumas nepriklauso "
        "nuo dienos naujienų.\n\n"
        "*Korespondentas* — zurnalistas "
        "pranešantis is ivykiu vietos.\n\n"
        "*Rubrika* — nuolatine skiltis "
        "skirta konkrečiai temai.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"))
    text = ("❓ *Dazniausiai uzduodami klausimai*\n\n"
        "*Ar sis botas oficialus?*\n"
        "Dienos Skaitymas yra nepriklausomas "
        "redakcinis projektas.\n\n"
        "*Kaip daznai atnaujinama?*\n"
        "Atranka atnaujinama kas sezona.\n\n"
        "*Kaip isjungti pranešimus?*\n"
        "Per Telegram pokalbio nustatymus.\n\n"
        "*Ar galiu pasidalinti straipsniu?*\n"
        "Taip, naudodami Telegram "
        "dalijimosi funkcija.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Apie mus", callback_data="about"))
    text = ("✏️ *Kontaktai*\n\n"
        "Redakcinei korespondencijai:\n"
        "• El. pastas: redakcija@dienosskaitymas.lt\n\n"
        "*Leidejas*\n"
        "Dienos Skaitymas UAB\n"
        "Gedimino pr. 28\n"
        "01104 Vilnius\n"
        "Lietuva\n\n"
        "Skaitytoju atsiliepimai darbo dienomis.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Santrauka", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Kontaktai", callback_data="contact"))
    text = ("🏛 *Apie Dienos Skaityma*\n\n"
        "Dienos Skaitymas yra nepriklausomas "
        "redakcinis projektas, skirtas "
        "kulturai, kelionems, virtuvei "
        "ir technologijoms.\n\n"
        "Redakcija kasdien atrenka "
        "kokybiška turini informuotai "
        "pertraukelei nuo kasdienybės.\n\n"
        "Sis Telegram leidimas sukurtas "
        "patogiam skaitymui pokalbyje.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Dienos temos", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Sveiki! Paspauskite *Dienos temos* kad pradetumete.", parse_mode="Markdown", reply_markup=markup)


print("Dienos Skaitymas Bot is running...")
bot.infinity_polling()
