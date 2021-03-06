from telebot.types import InlineKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def remove_keyboard():
    keyboard = ReplyKeyboardRemove(True)

    return keyboard


def main_menu():
    keyboard = ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True, one_time_keyboard=False
    )
    keyboard.add(
        KeyboardButton("Mövzu və rəngi dəyşdirin")
    )

    return keyboard


def themes():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="3024 Gecə", callback_data="carbon_3024-night"),
        InlineKeyboardButton(text="A11y Qaranlıq", callback_data="carbon_a11y-dark"),
        InlineKeyboardButton(text="Qara lövhə", callback_data="carbon_blackboard"),
        InlineKeyboardButton(text="Baza 16 (Qaranlıq)", callback_data="carbon_base16-dark"),
        InlineKeyboardButton(text="Baza 16 (İşıq)", callback_data="carbon_base16-light"),
        InlineKeyboardButton(text="Cobalt", callback_data="carbon_cobalt"),
        InlineKeyboardButton(text="Duotone", callback_data="carbon_duotone-dark"),
        InlineKeyboardButton(text="Dracula", callback_data="carbon_dracula-pro"),
        InlineKeyboardButton(text="Hopscotch", callback_data="carbon_hopscotch"),
        InlineKeyboardButton(text="Lucario", callback_data="carbon_lucario"),
        InlineKeyboardButton(text="Material", callback_data="carbon_material"),
        InlineKeyboardButton(text="Monokai", callback_data="carbon_monokai"),
        InlineKeyboardButton(text="Gecə bayquşu", callback_data="carbon_nightowl"),
        InlineKeyboardButton(text="Nord", callback_data="carbon_nord"),
        InlineKeyboardButton(text="Oceanic Next", callback_data="carbon_oceanic-next"),
        InlineKeyboardButton(text="Bir İşıq", callback_data="carbon_one-light"),
        InlineKeyboardButton(text="Bir Qaranlıq", callback_data="carbon_one-dark"),
        InlineKeyboardButton(text="Panda", callback_data="carbon_panda-syntax"),
        InlineKeyboardButton(text="Parasio", callback_data="carbon_parasio-dark"),
        InlineKeyboardButton(text="Seti", callback_data="carbon_seti"),
        InlineKeyboardButton(text="Bənövşəyi rəng çalarları", callback_data="carbon_shades-of-purple"),
        InlineKeyboardButton(text="Günəşləşmiş (Qaranlıq)", callback_data="carbon_solarized+dark"),
        InlineKeyboardButton(text="Günəşləşmiş (İşıq)", callback_data="carbon_solarized+light"),
        InlineKeyboardButton(text="SynthWave '84", callback_data="carbon_synthwave-84"),
        InlineKeyboardButton(text="Twilight", callback_data="carbon_twilight"),
        InlineKeyboardButton(text="Verminal", callback_data="carbon_verminal"),
        InlineKeyboardButton(text="VSCode", callback_data="carbon_vscode"),
        InlineKeyboardButton(text="Yeti", callback_data="carbon_yeti"),
        InlineKeyboardButton(text="Zenburn", callback_data="carbon_zenburn"),
    )

    return keyboard


def colors():
    keyboard = InlineKeyboardMarkup(row_width=4)
    keyboard.add(
        InlineKeyboardButton(text="Qırmızı", callback_data="color_#FF0000"),
        InlineKeyboardButton(text="Narıncı", callback_data="color_#FF5733"),
        InlineKeyboardButton(text="Sarı", callback_data="color_#FFFF00"),
        InlineKeyboardButton(text="Yaşıl", callback_data="color_#008000"),
        InlineKeyboardButton(text="Mavi", callback_data="color_#0000FF"),
        InlineKeyboardButton(text="Bənövşəyi", callback_data="color_#800080"),
        InlineKeyboardButton(text="Qəhvəyi", callback_data="color_#A52A2A"),
        InlineKeyboardButton(text="Magenta", callback_data="color_#FF00FF"),
        InlineKeyboardButton(text="Tan", callback_data="color_#D2B48C"),
        InlineKeyboardButton(text="Zeytun", callback_data="color_#00FFFF"),
        InlineKeyboardButton(text="Olive", callback_data="color_#808000"),
        InlineKeyboardButton(text="Maroon", callback_data="color_#800000"),
        InlineKeyboardButton(text="Aquamarine", callback_data="color_#00FFFF"),
        InlineKeyboardButton(text="Firuzəyi", callback_data="color_#30D5C8"),
        InlineKeyboardButton(text="Əhəng", callback_data="color_#00FF00"),
        InlineKeyboardButton(text="Teal", callback_data="color_#008080"),
        InlineKeyboardButton(text="Indigo", callback_data="color_#4B0082"),
        InlineKeyboardButton(text="Bənövşəyi.2", callback_data="color_#EE82EE"),
        InlineKeyboardButton(text="Çəhrayı", callback_data="color_#FFC0CB"),
        InlineKeyboardButton(text="Qara", callback_data="color_#000000"),
        InlineKeyboardButton(text="Ağ", callback_data="color_#FFFFFF"),
        InlineKeyboardButton(text="Boz", callback_data="color_#808080"),
    )

    return keyboard
