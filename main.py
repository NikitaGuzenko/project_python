import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command
import random

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token="6894414755:AAEOxgnEpSzDHEwFgECAxiEMHjq4d0P0QHA", parse_mode="HTML")
dp = Dispatcher(bot=bot)
router = Router()


game_started = False


async def write_to_file(message: types.Message):
    with open("user_responses.txt", "a") as file:
        file.write(f"User ID: {message.from_user.id}, Response: {message.text}\n")
        file.flush()  # Очистить буфер вывода и убедиться, что данные записаны на диск


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await write_to_file( message)
    kb = [[types.KeyboardButton(text="Глава 1", callback_data="Глава 1")]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Начать главу 1",
        one_time_keyboard=True
    )
    await message.answer("Вы - мастер магии, чьи десятилетия посвящены изучению тайн и волшебных существ. "
                         "Вчера, как обычно, вы отправились к своему другу Гендрику, чтобы насладиться чашечкой "
                         "горячего чая. Однако, когда вы прибыли, обнаружили, что его дом был полностью разрушен, "
                         "а Гендрика нигде не было. С помощью магии вы установили направление, куда унесли вашего друга"
                         " магические существа. Полный решимости и намерений найти Гендрика и спасти его из рук чудовищ"
                         ", вы входите в Загадочный лес!", reply_markup=keyboard)


async def check_text_4(message: types.Message):
    text = message.text.lower()
    return text in ('глава 1', "вернуться назад")


@dp.message(check_text_4)
async def capter_1(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Пойти налево", callback_data="Пойти налево"),  # Corrected callback_data
            types.KeyboardButton(text="Пойти направо", callback_data="Пойти направо"),  # Corrected callback_data
            types.KeyboardButton(text="Изучить символы", callback_data="Изучить символы")
            # Assuming you want to handle this as well
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите путь",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('1.jpg')
    await bot.send_photo(message.chat.id, photo=photo, caption=
    "Исследуя глубины Загадочного леса, вы столкнулись с "
    "необычным зрелищем. Поляна, окруженная деревьями, "
    "которые казались не просто деревьями, а источниками "
    "неизвестной магии, излучала яркий синий свет. "
    "\n\nДве дороги, ведущие в разные стороны, стояли перед вами,"
    " каждая из них обещала новые открытия и испытания."
    "Одна дорога казалась более темной и непроницаемой, "
    "словно ведущая в глубины леса, где скрываются самые опасные "
    "и неизвестные существа. Другая дорога, напротив, казалась "
    "более светлой, однако гораздо более загадочной. "
    "К тому же, необычные деревья на этой поляне не покидали вашей головы."
    "\n\nВы знали, что каждый выбор, который вы сделаете, может "
    "привести к новым приключениям или к конечной гибели. "
    "Но в ваших глазах горел огонь решимости, готовый преодолеть "
    "любые препятствия на пути к спасению Гендрика."
    "\nКакой же путь вы выберете?",
                         reply_markup=keyboard)


async def check_text(message: types.Message):
    text = message.text.lower()
    return text in ('последовать указаниям духов', 'пойти налево', "выбрать левый путь")


@dp.message(check_text)
async def left_road(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Ударить в голову", callback_data="Ударить в голову"),  # Corrected callback_data
            types.KeyboardButton(text="Ударить в ногу", callback_data="Ударить в ногу"),  # Corrected callback_data
            types.KeyboardButton(text="Ударить в руку", callback_data="Ударить в руку")
            # Assuming you want to handle this as well
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Куда будем бить?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('left_road.png')
    await message.answer_photo(photo=photo,
                               caption="Идя вдоль этой узкой тропинки, вы не замечаете ничего подозрительного."
                                       " Однако, с каждым шагом, ощущение неожиданности усиливается, "
                                       "подсказывая, что в этом лесу вы не одиноки. Лес вокруг вас, с его "
                                       "таинственными тенистыми уголками и шумом ветвей, кажется живым и "
                                       "загадочным, как будто он сам наблюдает за вами.\n\nВнезапно, из-за "
                                       "огромного валуна поднимается гигантский тролль. Его кожа, покрытая "
                                       "глубокими морщинами, блестит в свете заката, а глаза, сверкающие "
                                       "как два огня, смотрят на вас с неподдельным интересом. Он "
                                       "просыпается от сна, не ожидая ужинать, но радушно встречает вас. "
                                       "Его враждебный вид и полная боевая готовность говорят о том, что "
                                       "бегство невозможно. Остается только драться за свою жизнь!",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "ударить в голову")
async def hit_head(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Вы проиграли :(",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Вы решаете ударить тролля в голову и замахиваетесь для сильного удара, но тролль оказывается быстрее. "
    "Вас откидывает к дереву и вы теряете сознание. Перед отключкой вас посещает последняя в жизни мысль: "
    "кажется это конец вам и вашему путешествию",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "ударить в руку")
async def hit_head(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Вы проиграли :(",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Вы успеваете легким движением посоха ударить тролля в руку. Этот удар не нанес троллю каких-либо "
    "повреждений, однако сильно разозлил его. "
    "Тролль крича от боли, ринулся на вас. Вы отлетели назад и ударились о дерево. "
    "Теряя сознание, вы осознаете, что это конец для вас.",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "ударить в ногу")
async def hit_leg(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Идти дальше")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Какие действие предпримите?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('you_win.png')
    await message.answer_photo(photo=photo,
                               caption="В глубине темного леса лежал тролль, и его огромная "
                                       "фигура выделялась на фоне мрачных деревьев. Нога оказалась слабым местом этого "
                                       "существа, и с помощью этой уязвимости, вы смогли обездвижить его. \n\nОднако даже в "
                                       "таком положении, тролль оставался опасным, его глаза горели яростью и ненависть"
                                       "ю, а его мускулистая рука, готовая к удару, висела бездейственной. Но вы знали, "
                                       "что даже в таком состоянии, тролль не был беспомощным. Поэтому, собрав все свои "
                                       "силы, вы прикончили его, оставив лишь холодный ветер, шепчущий в листьях деревь"
                                       "ев. \n\nПуть дальше открыт, но в сердце оставалась память о том, как вы смогли прео"
                                       "долеть опасность, стоявшую перед вами. Это было не просто победа, это был шаг "
                                       "вперед, шаг к свободе и безопасности. И хотя дорога была трудной, вы знали, что "
                                       "каждый шаг приближал вас к цели.",
                               reply_markup=keyboard)


async def check_text_3(message: types.Message):
    text = message.text.lower()
    return text in ("идти дальше", 'последовать подсказке духов', 'выбрать правый путь', 'идти по карте')


@dp.message(check_text_3)
async def bridge(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Восстановить мост"),
            types.KeyboardButton(text="Искать обходной путь")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Какие действие предпримите?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('bridge.png')
    await message.answer_photo(photo=photo,
                               caption="Долго вы шли по этой тропинке и наконец впереди замаячило что-то большое."
                                       " Перед вами лежал разрушенный мост, пересекающий ущелье, его "
                                       "разрушенные опоры и обломки каменных блоков напоминали о прошлом величии и "
                                       "теперь виднелись лишь следы разрушения. Ваши заклинания могли восстановить его,"
                                       " но это требовало не только времени, но и магической энергии. В этот момент, "
                                       "когда вы отдавались восстановлению, вы могли стать уязвимыми перед возможными "
                                       "нападениями или ловушками, спрятанными в глубинах леса. Или же, вы могли "
                                       "поискать обходной путь, который, возможно, завершил бы ваше путешествие "
                                       "неудачей, но позволил бы избежать дальнейших испытаний. \n\nВы смотрели "
                                       "на разрушенный мост, и в ваших глазах отражались все возможные исходы вашего "
                                       "выбора. Каждый из них был как карта, на которой вы могли увидеть различные "
                                       "пути, ведущие к разным концам. Вы знали, что каждый выбор имеет свои риски и "
                                       "награды, и что ваша судьба зависела от того, какой путь вы выберете. ",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "восстановить мост")
async def bridge_construct(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Прыгнуть в ущелье"),
            types.KeyboardButton(text="Сразиться с волками")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Какие действие предпримите?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('wolfs.png')
    await message.answer_photo(photo=photo,
                               caption="Вы приняли решение восстановить мост, несмотря на знание, что это потребует "
                                       "от вас не только времени, но и магической энергии. Каждый камень, каждый блок, "
                                       "каждое заклинание, каждое "
                                       "мгновение, было как шаг в неизвестность, каждый из которых мог стать "
                                       "последним.\n\nКогда мост был почти восстановлен, из леса выбежала стая "
                                       "разъяренных волков. Их глаза горели яростью, их лапы были готовы к атаке, и "
                                       "их зубы блестели в ожидании крови. Ваши силы уже были на пределе, каждый из "
                                       "ваших движений был тяжелым, каждый вздох был глубоким и трудным.\n\nВ этой "
                                       "ситуации, когда каждый мгновение могло стать последним, важно было принять "
                                       "быстрое и решительное действие, чтобы спасти себя. Ваша жизнь зависела от того, "
                                       "сможете ли вы отразить атаку или уйти от нее. Ваша судьба зависела от того, с"
                                       "можете ли вы сохранить свою жизнь или потеряете ее в этом мгновении",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "сразиться с волками")
async def wolf_fight(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Вы проиграли :(",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('wolfs.png')
    await message.answer_photo(photo=photo, caption=
    "Вы потратили слишком много сил на восстановление моста, и когда стая разъяренных волков обнаружила вас, ваша "
    "история была на грани завершения. Волки, как будто чувствовали вашу слабость, бросились на вас с беспощадной "
    "яростью. Ваши попытки сопротивления были беспомощны, и в конечном итоге, вы умерли, оставшись на поле боя, где "
    "ваша жизнь и была потеряна.",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "прыгнуть в ущелье")
async def gorge(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Драться с драконом вместе с Гендриком"),
            types.KeyboardButton(text="Отвлечь дракона на себя"),
            types.KeyboardButton(text="Убежать")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Что будем делать с драконом?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('dragon.png')
    await message.answer_photo(photo=photo, caption=
    "Осознавая, что в борьбе с волками вы потратили немало сил и не сможете сражаться, вы принимаете решение на "
    "отступление. Смело прыгая в ущелье, вы ощущаете жесткость земли под собой, но серьезные ранения не останавливают "
    "вас. С каждым шагом вы продолжаете свой путь. В ваших глазах отражается не только решимость, но и некоторое "
    "тревожное волнение, которое не позволяет вам полностью отпустить страх.\n\nИзучив местность, вы нашли путь, который"
    " ведет к пещере. В ее глубинах вы обнаружили Гендрика, а также огромного дракона, который его охраняет. "
    "Ваши глаза, полные недоумения и тревоги, встречаются с Гендриком, и в них отражается не только радость, но и "
    "страх перед чудовищем. Вы чувствуете, как сердце бьется в груди, как будто оно пытается вырваться из груди, "
    "но вы сдерживаете его, понимая, что сейчас не место для паники. Необходимо принять верное решение, "
    "учитывая ваше ранение, для спасения "
    "вашего друга",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "отвлечь дракона на себя")
async def hero(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Героическая смерть",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Осознавая безвыходность своего положения, вы решили отвлечь дракона на себя, понимая, что "
    "справиться с этим существом в одиночку было бы невозможно. \n\nВы крикнули Гендрику: 'Беги!', и с полными боли "
    "глазами Гендрик повиновался вашему приказу. Дракон, легко справившийся с вашими усилиями, оставил вас на поле боя, "
    "тяжело раненным и без надежды на спасение. Ваша гибель, хоть и была трагической, позволила спасти вашего друга, Гендрика, "
    "от неминуемой гибели.",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "драться с драконом вместе с гендриком")
async def both_deth(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Вы проиграли :(",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Вы и Гендрик, оба раненные, решили вступить в бой с драконом. Ваша решимость и мужество, несмотря на неравные "
    "шансы, были вдохновляющими. Вы знали, что схватка будет жестокой и безжалостной, но вы были готовы сражаться до "
    "последнего вздоха.\n\nСражение началось с молниеносной атаки дракона, его огромные крылья развевались в воздухе, а "
    "его глаза горели яростью и жаждой крови. Вы и Гендрик, стоя на передовой, встретили его атаку, каждый из вас с "
    "оружием в руках, готовый к битве.\n\nВаша схватка была жестокой и безжалостной. Дракон, несмотря на ваши усилия, "
    "был слишком мощным. Его огненные дыхания и острые когти нанесли вам смертельные раны. Вы и Гендрик, оба раненные, "
    "продолжали бороться, но силы покидали вас.\n\nВ конце концов, оба вы погибли, не сумев справиться с мощью дракона. "
    "Ваша гибель была трагической, но она также была символом вашего мужества и решимости. Ваши тела лежали на поле боя,"
    " но ваша дух продолжал жить в сердцах тех, кто помнил вас.",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "убежать")
async def coward(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Вы трус",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "При виде дракона, ваше тело застыло на месте, страх парализовал вас. Ваше сердце стучало в груди, как будто "
    "пытаясь вырваться из груди, а дыхание было коротким и неровным. Ваши глаза расширились от ужаса, и вы не могли "
    "отвести взгляд от монстра, который стоял перед вами, готовый к атаке. В вашем уме возникло мгновенное осознание "
    "того, что вы не сможете справиться с этим существом, и страх заполнил вас полностью.\n\nВы попытались кричать, но "
    "ваш голос застрял в горле, и вы могли только смотреть, как Гендрик, стоящий рядом с вами, пытается подготовиться "
    "к бою. Но в вашем сердце было только место для страха, и вы не могли сосредоточиться на чем-либо другом.\n\nВнезапно, "
    "ваше тело начало двигаться, но не в направлении боя. Ваши ноги подчинялись вашему страху, и вы бежали, "
    "оставляя за собой своего друга. Вы оставили Гендрика на растерзание дракону",
                               reply_markup=keyboard)


async def check_text_2(message: types.Message):
    text = message.text.lower()
    return text in ("искать обходной путь")


@dp.message(check_text_2)
async def workaround(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Объединиться с Гендриком в борьбе с драконом"),
            types.KeyboardButton(text="Отвлечь дракона на себя"),
            types.KeyboardButton(text="Убежать")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Что будем делать с драконом?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "С каждым шагом вы продолжаете свой путь. В ваших глазах отражается не только решимость, но и некоторое "
    "тревожное волнение, которое не позволяет вам полностью отпустить страх.\n\nИзучив местность, вы нашли путь, который"
    " ведет к пещере. В ее глубинах вы обнаружили Гендрика, а также огромного дракона, который его охраняет. "
    "Ваши глаза, полные недоумения и тревоги, встречаются с Гендриком, и в них отражается не только радость, но и "
    "страх перед чудовищем. Вы чувствуете, как сердце бьется в груди, как будто оно пытается вырваться из груди, "
    "но вы сдерживаете его, понимая, что сейчас не место для паники. Необходимо принять верное решение "
    "для спасения "
    "вашего друга",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "объединиться с гендриком в борьбе с драконом")
async def coward(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="/start")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Вы победили",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Вы решили вступить в схватку с драконом, полным решимости и смелости. "
    "Даже несмотря на свои уже полученные ранения, ваш верный друг Гендрик оказывает вам помощь, "
    "используя все свои знания и умения. Схватка с драконом оказывается невероятно ожесточенной, "
    "ведь чудовище проявляет несравненную силу. Однако, благодаря вашей храбрости и верности друга, "
    "вам удается одержать победу над этим злобным созданием. С усталыми и поврежденными телами, "
    "вы направляетесь домой, чтобы залечить свои раны и восстановиться после такой тяжелой битвы. "
    "Оба осознаете, что истинная дружба и взаимопомощь являются невероятно ценными и сильными силами, "
    "способными преодолеть любые трудности и преграды.",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "пойти направо")
async def right_road(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Помогу ему, укрою у себя"),
            types.KeyboardButton(text="Не буду помогать, но позову на помощь"),
            types.KeyboardButton(text="Пройду мимо")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Какой ответ дадите духам?",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Вы решили отправиться в путь, окутанный в магический аромат, который исходил из всего вокруг, как будто каждый "
    "лист и каждый ветерок были наполнены тайной силой. Внезапно, перед вами появились древние духи Загадочного леса, "
    "их присутствие ощущалось как нежный ветер, проносящий с собой эхо древних времен, напоминая о том, что мир, в "
    "котором мы живем, полон тайн и чудес. Они обратились к вам с вопросом, предложив помощь в вашем путешествии, но "
    "только если вы ответите на их вопрос.\n\nОни спрашивают: 'Странник, мы хотим услышать ответ. На своем пути в этом "
    "путешествии ты видишь на дороге брошенного щенка, твои действия?'",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "помогу ему, укрою у себя")
async def help_the_puppy(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Последовать подсказке духов")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Идите дальше",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "Ваш ответ, пронизанный искренностью и глубиной души, вызывает удивление и восхищение у духов леса. "
    "Они, в свою очередь, желают поделиться с вами тайной, которая может открыть перед вами правильную дорогу в "
    "Загадочном лесу. Этот обмен знаниями и мудростью становится символом нового начала, где каждый шаг вперед ведет "
    "к новым открытиям и пониманию, где же ваш друг Гендрик",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "пройду мимо")
async def dont_help_the_puppy(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Последовать указаниям духов")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Идите дальше",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "В глубинах леса, где души деревьев и животных сливаются в единое целое, духи леса, обитающие в его тайных уголках, "
    "смотрели на вас с недовольством. Их глаза, полные мудрости и знаний, отражали разочарование в вашем ответе. "
    "Однако, несмотря на это, они решили предложить вам свою помощь. Несмотря на недоброе предчувствие относительно "
    "этой дороги вы решили принять помощь Духов, ведь вы были поражены глубиной разочарования в их глазах и решили не "
    "расстраивать их еще больше",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "не буду помогать, но позову на помощь")
async def dont_help_the_puppy(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Выбрать левый путь"),
            types.KeyboardButton(text="Выбрать правый путь")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Идите дальше",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "В глубинах леса, где души деревьев и животных сливаются в единое целое, духи леса, обитающие в его тайных уголках, "
    "смотрели на вас с недовольством. Их глаза, полные мудрости и знаний, отражали разочарование в вашем ответе. "
    "Однако, несмотря на это, они решили предложить вам свою помощь. Несмотря на недоброе предчувствие относительно "
    "этой дороги вы решили принять помощь Духов, ведь вы были поражены глубиной разочарования в их глазах и решили не "
    "расстраивать их еще больше",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "изучить символы")
async def trees(message: types.Message):
    await write_to_file( message)
    kb = [
        [
            types.KeyboardButton(text="Начать игру"),
            types.KeyboardButton(text="Вернуться назад")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Сделайте выбор",
        one_time_keyboard=True
    )
    photo = types.FSInputFile('troll_win.png')
    await message.answer_photo(photo=photo, caption=
    "В сердце Загадочного леса, где сливаются границы между миром людей и миром природы, вы решили остановиться. "
    "Ваши глаза, наполненные любопытством и решимостью, устремлялись к странным деревьям, которые казались лабиринтом, "
    "созданным самим природой. Вы почувствовали, что в этих деревьях скрыта логика, непохожая на всё, что вы видели "
    "раньше. Это было как вход в загадочный мир, где каждый шаг мог привести к открытию или к забвению.\n\nВы поняли, "
    "что перед вами не просто лес, а место, где каждый куст и каждая листва играют роль в большой игре. Игра, в которой "
    "каждый шаг, каждое движение, каждое решение, могут привести к неожиданным исходам. Игра, в которой вы можете "
    "выбрать путь, ведущий к спасению друга, или же путь, который приведёт к потере.\n\nВы чувствуете, что перед вами "
    "стоит задача, которая требует от вас не только физической силы, но и ума, мудрости и решимости.",
                               reply_markup=keyboard)


@dp.message(F.text.lower() == "начать игру")
async def start_game(message: types.Message):
    await write_to_file( message)
    global secret_number, game_started
    secret_number = random.randint(1, 100)
    game_started = True
    await message.answer("Добро пожаловать в числовую угадайку! Я загадал число от 1 до 100. "
                         "Попробуйте угадать его.")


@dp.message()
async def guess_number(message: types.Message):
    await write_to_file( message)
    global secret_number, game_started
    if message.text.isdigit() and game_started:
        guess = int(message.text)
        if guess == secret_number:
            await message.answer("Поздравляю! Вы угадали число!")
            kb = [
                [
                    types.KeyboardButton(text="Идти по карте"),
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True,
                input_field_placeholder="следуй подсказке",
                one_time_keyboard=True
            )
            photo = types.FSInputFile('troll_win.png')
            await message.answer_photo(photo=photo, caption=
            "После успешного решения задачи вы обнаружили, что перед вами разверзлись тайные пути Загадочного леса, "
            "как будто сама природа раскрывала свои двери перед вашим искусным взглядом. Ваша находчивость и "
            "мудрость привели к тому, что таинственная карта, обнаруженная в гуще леса, раскрыла свои тайны, "
            "указав вам непроторенный путь к древнему мосту.\n\nТаким образом, ваше "
            "смелое и преданные стремление приводит вас к каждому новому испытанию, превращая ваше путешествие "
            "в захватывающий эпос, где каждое препятствие - лишь шаг ближе к возвращению Гендрика в мир безопасности "
            "и спокойствия.",
                                       reply_markup=keyboard)
        elif guess < secret_number:
            await message.answer("Нет, загаданное число больше.")
        else:
            await message.answer("Нет, загаданное число меньше.")
    elif game_started:
        await message.answer("Пожалуйста, введите целое число от 1 до 100.")





# Функция для записи ответов пользователя в файл

# Запуск процесса поллинга новых апдейтов
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())


# # "6894414755:AAEOxgnEpSzDHEwFgECAxiEMHjq4d0P0QHA"

