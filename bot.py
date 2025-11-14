from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask, request
import os

TOKEN = "8371602272:AAH5WoH4SzJWlQvqgVEjtI3JeaeUppTZ6vY" 

app = Flask(_name_)

telegram_app = ApplicationBuilder().token(TOKEN).build()
# بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("من نحن ✨️", callback_data="about")],
        [InlineKeyboardButton("خدمات الشحن 📦", callback_data="shipping")],
        [InlineKeyboardButton("خدمات النقل 🚌", callback_data="transport")],
        [InlineKeyboardButton("تواصل معنا 🌐💬", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحباً بك في بوت شركةالمفتي! 👋 اختر من القائمة:", reply_markup=reply_markup)

# دالة التعامل مع الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # الصفحة الرئيسية
    if query.data == "main_menu":
        keyboard = [
            [InlineKeyboardButton("من نحن ✨️", callback_data="about")],
            [InlineKeyboardButton("خدمات الشحن 📦", callback_data="shipping")],
            [InlineKeyboardButton("خدمات النقل 🚌", callback_data="transport")],
            [InlineKeyboardButton("تواصل معنا 🌐💬", callback_data="contact")]
        ]
        await query.edit_message_text("🔙 عدت إلى الصفحة الرئيسية.\nاختر من القائمة:", reply_markup=InlineKeyboardMarkup(keyboard))

    # من نحن
    elif query.data == "about":
        await query.edit_message_text(
            "شركة المفتي للنقل والشحن الدولي\nهي شركة مرخصة من من وزارة النقل والهيئة الناظمة للاتصالات، انطلقت بروئية واضحة\nلتقديم مفهوم جديد لخدمات الشحن والنقل في سوريال\nحيث نؤمن أن المواطن السوري يستحق خدمات شحن ونقل أمنة وموثوقة 💯✅️\nمن خلال اعتمادنا على المعايير الاحترافية الدولية، نسعى الى بناء قطاع شحن ونقل\nحديث يواكب التطور العالمي ويضع مصلحة العميل في المقام الأول.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="main_menu")]])
        )

    # خدمات الشحن 📦
    elif query.data == "shipping":
        keyboard = [
            [InlineKeyboardButton("عناوين المكاتب 📍", callback_data="shipping_internal")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main_menu")]
        ]
        await query.edit_message_text("خدمات الشحن: \n✅️ سرعة في التنفيذ\n✅️ أمان في الخدمة\n✅️ اسعار تنافسية\n✅️ خدمة تتبع إلكتروني\n", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "shipping_internal":
        await query.edit_message_text("📌 دمشق\nالقدم      0965112162\nالبرامكة  0965112158\nفيكتوريا 0965112161\n\n📌 حلب\nساحة الكرنك 0965112156\nالسريان         0965112165\n\n📌 حمص\nجورة الشياح 0965112157\n\n📌 درعا\nدوار الحمامة  0965112159\n\n📌 ادلب\nدوار المحراب 0965112164\n\n📌 طرطوس\nمول الحمرات 0965112160\nشارع الثورة   0965112163", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="shipping")]]))

    # خدمات النقل 🚌
    elif query.data == "transport":
        keyboard = [
            [InlineKeyboardButton("مواعيد الرحلات ⏰", callback_data="transport_schedules")],
            [InlineKeyboardButton("أرقام الاستعلام ☎️", callback_data="transport_numbers")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main_menu")]
        ]
        await query.edit_message_text("اختر من خدمات النقل:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "transport_schedules":
        keyboard = [
            [InlineKeyboardButton("مواعيد رحلات دمشق ⏰", callback_data="trip1")],
            [InlineKeyboardButton("مواعيد رحلات حلب ⏰", callback_data="trip2")],
            [InlineKeyboardButton("مواعيد رحلات حمص ⏰", callback_data="trip3")],
            [InlineKeyboardButton("مواعيد رحلات حماة ⏰", callback_data="trip4")],
            [InlineKeyboardButton("مواعيد رحلات طرطوس ⏰", callback_data="trip5")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="transport")]
        ]
        await query.edit_message_text("الرحلات المتاحة:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "trip1":
        keyboard = [
            [InlineKeyboardButton("دمشق ⬅️ حلب", callback_data="op1")],
            [InlineKeyboardButton("دمشق ⬅️ حمص", callback_data="op2")],
            [InlineKeyboardButton("دمشق ⬅️ طرطوس", callback_data="op3")],
            [InlineKeyboardButton("دمشق ⬅️ الأردن", callback_data="op4")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="transport_schedules")]
        ]
        await query.edit_message_text("اختر وجهتك:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "op1":
        await query.edit_message_text("🔸️ ٧:٣٠ صباحاً\n🔸️٨:٣٠ صباحاً\n🔸️١٠:٣٠ صباحاً\n🔸️١٢:٣٠ ظهراً\n🔸️٢:٣٠ عصراً\n🔸️٤:٣٠ عصراً\n🔸️١٠:٣٠ مساءاً\n🔸️١:٣٠ ليلاً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip1")]]))
    elif query.data == "op2":
        await query.edit_message_text("🔸️ ٧:٣٠ صباحاً\n🔸️٨:٣٠ صباحاً\n🔸️١٠:٣٠ صباحاً\n🔸️١٢:٣٠ ظهراً\n🔸️٢:٣٠ عصراً\n🔸️٤:٣٠ عصراً\n🔸️١٠:٣٠ مساءاً\n🔸️١:٣٠ ليلاً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip1")]]))
    elif query.data == "op3":
        await query.edit_message_text("🔸️١:٣٠ ظهراً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip1")]]))
    elif query.data == "op4":
        await query.edit_message_text("🔸️٧:٣٠ صباحاً\n🔸️١٢:٠٠ ضهراً\n🔸️٢:٣٠ عصراً\🔸️٨:٠٠ مساءاً\n🔸️١٢:٣٠ ليلاً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip1")]]))

    elif query.data == "trip2":
        keyboard = [
            [InlineKeyboardButton("حلب ⬅️ دمشق", callback_data="op5")],
            [InlineKeyboardButton("حلب ⬅️ حمص", callback_data="op6")],
            [InlineKeyboardButton("حلب ⬅️ الأردن", callback_data="op7")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="transport_schedules")]
        ]
        await query.edit_message_text("اختر وجهتك:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "op5":
        await query.edit_message_text("🔸️١٢:٠٠ ليلاً\n🔸️١:٠٠ ليلاً\n🔸️٢:٠٠ ليلاً\n🔸️٣:٣٠ ليلاً\n🔸️٦:٣٠ صباحاً\n🔸️٨:٣٠ صباحاً\n🔸️١١:٠٠ صباحاً\n🔸️١:٠٠ ظهراً\n🔸️١:٠٠ ظهراً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip2")]]))
    elif query.data == "op6":
        await query.edit_message_text("🔸️١٢:٠٠ ليلاً\n🔸️١:٠٠ ليلاً\n🔸️٢:٠٠ ليلاً\n🔸️٣:٣٠ ليلاً\n🔸️٦:٣٠ صباحاً\n🔸️٨:٣٠ صباحاً\n🔸️١١:٠٠ صباحاً\n🔸️١:٠٠ ظهراً\n🔸️١:٠٠ ظهراً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip2")]]))
    elif query.data == "op7":
        await query.edit_message_text("🔸️ ١:٠٠ ليلاً\n🔸️٨:٣٠ صباحاً\n🔸️١:٠٠ ظهراً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip2")]]))

    elif query.data == "trip3":
        keyboard = [
            [InlineKeyboardButton("حمص ⬅️ دمشق", callback_data="op8")],
            [InlineKeyboardButton("حمص ⬅️ حلب", callback_data="op9")],
            [InlineKeyboardButton("حمص ⬅️ الأردن", callback_data="op10")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="transport_schedules")]
        ]
        await query.edit_message_text("اختر وجهتك:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "op8":
        await query.edit_message_text("🔸️ ٣:٣٠ ليلاً\n🔸️ ٤:٣٠ ليلاً\n🔸️ ٦:٠٠ صباحاً\n🔸️ ٩:٠٠ صباحاً\n🔸️ ١١:٠٠ صباحاً\n🔸️ ١:٣٠ ظهراً\n🔸️ ٣:٣٠ عصراً\n🔸️ ٦:٠٠ مساءاً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip3")]]))
    elif query.data == "op9":
        await query.edit_message_text("🔸️ ١:٣٠ ليلاً\n🔸️ ٤:٠٠ ليلاً\n🔸️ ١٠:٠٠ صباحاً\n🔸️ ١١:٠٠ صباحاً\n🔸️ ١:٠٠ ظهراً\n🔸️ ٣:٠٠ ظهراً\n🔸️ ٥:٠٠ عصراً\n🔸️ ٦:٣٠ مساءاً\n🔸️ ٧:٣٠ مساءاً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip3")]]))
    elif query.data == "op10":
        await query.edit_message_text("🔸️ ٣:٣٠ ليلاً\n🔸️ ١١:٠٠ صباحاً\n🔸️ ٣:٣٠ عصراً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip3")]]))

    elif query.data == "trip4":
        keyboard = [
            [InlineKeyboardButton("حماة ⬅️ الأردن", callback_data="op11")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="transport_schedules")]
        ]
        await query.edit_message_text("اختر وجهتك:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "op11":
        await query.edit_message_text(" 🔸️١:٠٠ ظهراً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip4")]]))

    elif query.data == "trip5":
        keyboard = [
            [InlineKeyboardButton("طرطوس ⬅️ دمشق", callback_data="op12")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="transport_schedules")]
        ]
        await query.edit_message_text("اختر وجهتك:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "op12":
        await query.edit_message_text("🔸️ ٩:٠٠ صباحاً", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="trip5")]]))

    elif query.data == "transport_numbers":
        await query.edit_message_text("📞 دمشق\n0950002081\n📞 حلب\n0950002055\n📞 حماة\n0950002047\n📞 حمص\n0950002032\n📞 طرطوس\n0965112160", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="transport")]]))

    # تواصل معنا 🌐💬
    elif query.data == "contact":
        await query.edit_message_text("تواصل معنا عبر 🧡💙\n💬رابط صفحتنا على منصة فيسبوك\nhttps://www.facebook.com/share/19Tmag7VA6/\n💬رابط صفحتنا على منصة انستغرام\nhttps://www.instagram.com/al_mufti_for_travel?igsh=bWI5ZjF0cTUxazl3", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="main_menu")]]))

@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "ok"
if __name__ == '_main_':
    PORT = int(os.environ.get("PORT", 5000))
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(CallbackQueryHandler(button))

    app.run(host="0.0.0.0", port=PORT)