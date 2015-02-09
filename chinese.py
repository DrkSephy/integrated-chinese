# coding: utf8
# print u'你'.encode('utf-8')
import random
import argparse


words = [
    # Chapter 1: Vocabulary
    # Page 21
    {'character': u'你', 'chapter': 1, 'id': 1,     'pinyin': u'nǐ',            'type': 'pronoun',            'translation': 'you' },                                
    {'character': u'好', 'chapter': 1, 'id': 2,     'pinyin': u'hǎo',           'type': 'adjective',            'translation': 'fine; good; nice; O.K.; it’s settled' },                            
    {'character': u'请', 'chapter': 1, 'id': 3,     'pinyin': u'qǐng',          'type': 'verb',            'translation': 'please (polite form of request); to treat or to invite (somebody)'},
    {'character': u'问', 'chapter': 1, 'id': 4,     'pinyin': u'wèn',           'type': 'verb',            'translation': 'to ask (a question)'},
    {'character': u'贵', 'chapter': 1, 'id': 5,     'pinyin': u'guì',           'type': 'adjective',            'translation': 'honorable; expensive'},
    {'character': u'姓', 'chapter': 1, 'id': 6,     'pinyin': u'xìng',          'type': 'verb/noun',            'translation': '(one’s) surname is...; to be surnamed; surname'},
    {'character': u'我', 'chapter': 1, 'id': 7,     'pinyin': u'wǒ',            'type': 'pronoun',            'translation': 'I; me'},
    {'character': u'呢', 'chapter': 1, 'id': 8,     'pinyin': u'ne',            'type': 'question particle',            'translation': '(question particle)'},
    {'character': u'小姐','chapter': 1, 'id': 9,    'pinyin': u'xiǎojie',       'type': 'noun',            'translation': ' Miss; young lady'},
    {'character': u'叫',  'chapter': 1, 'id': 10,    'pinyin': u'jiào',          'type': 'verb',            'translation': 'to be called; to call'},
    {'character': u'什么','chapter': 1, 'id': 11,    'pinyin': u'shénme',         'type': 'question pronoun',            'translation': 'what'}, 
    {'character': u'名字','chapter': 1, 'id': 12,    'pinyin': u'míngzi',         'type': 'noun',            'translation': 'name'},
    {'character': u'先生','chapter': 1, 'id': 13,    'pinyin': u'xiānsheng',      'type': 'noun',            'translation': 'Mr.; husband; teacher'},
    {'character': u'李友','chapter': 1, 'id': 14,     'pinyin': u'lǐ yǒu',         'type': '--',            'translation': '(a personal name)'},
    {'character': u'李', 'chapter': 1, 'id': '14-alt',     'pinyin': u'lǐ',            'type': '--',            'translation': '(a surname); plum'},
    {'character': u'王朋','chapter': 1, 'id': 15,     'pinyin': u'wáng péng',     'type': '--',            'translation': '(a personal name)'},
    {'character': u'王',  'chapter': 1, 'id': '15-alt',   'pinyin': u'wáng',          'type': '--',            'translation': '(a surname); king'},

    # Page 28
    {'character': u'是 ' , 'chapter': 1,  'id': 1,    'pinyin': u'shì',         'type': 'verb',           'translation': 'to be '},
    {'character': u'老师', 'chapter': 1, 'id': 2,     'pinyin': u'lǎoshī',       'type': 'noun',            'translation': 'teacher'},  
    {'character': u'吗 ' , 'chapter': 1, 'id': 3,    'pinyin': u'mǎ',          'type': 'question particle',            'translation': '(question particle)'},
    {'character': u'不 ' , 'chapter': 1, 'id': 4,    'pinyin': u'bù',          'type': 'adverb',            'translation': 'not; no'},
    {'character': u'学生', 'chapter': 1, 'id': 5,    'pinyin': u'xuésheng',     'type': 'noun',             'translation': 'student '},
    {'character': u'也 ' , 'chapter': 1, 'id': 6,    'pinyin': u'yě',          'type': 'adverb',            'translation': 'too; also'},
    {'character': u'人 ' , 'chapter': 1, 'id': 7,    'pinyin': u'rén',         'type': 'noun',            'translation': 'people; person'},
    {'character': u'中国', 'chapter': 1, 'id': 8,    'pinyin': u'zhōngguó',    'type': '--',             'translation': 'China'},
    {'character': u'北京', 'chapter': 1, 'id': 9,    'pinyin': u'běijīng',      'type': '--',             'translation': 'Beijing'},
    {'character': u'美国', 'chapter': 1, 'id': 10,    'pinyin': u'měiguó',       'type': '--',            'translation': 'America '},
    {'character': u'纽约', 'chapter': 1, 'id': 11,    'pinyin': u'niǔyuē',       'type': '--',            'translation': 'New York'},

    #page 43
    {'character': u'那 ',  'chapter': 2, 'id': 1,     'pinyin':u'nā',           'type': 'pronoun',           'translation': 'that'},
    {'character': u'的 ' , 'chapter': 2, 'id': 2,     'pinyin':u'de',           'type': 'particle',           'translation': '(a possessive or descriptive particle)'},
    {'character': u'照片',  'chapter': 2, 'id': 3,      'pinyin':u'zhàopiàn',     'type': 'noun',            'translation': 'picture; photo'},
    {'character': u'这 ' , 'chapter': 2, 'id': 4,     'pinyin':u'zhè',          'type': 'pronoun',           'translation': 'this'},
    {'character': u'爸爸', 'chapter': 2, 'id': 5,      'pinyin':u'bàba',         'type': 'noun',            'translation': 'father, dad'},
    {'character': u'妈妈', 'chapter': 2, 'id': 6,      'pinyin':u'māma',         'type': 'noun',            'translation': 'mother, mom'},
    {'character': u'个 ', 'chapter': 2, 'id':  7,     'pinyin':u'gè',            'type': 'measure word',           'translation': '(measure word for many common everyday objects)'},
    {'character': u'女 ', 'chapter': 2, 'id':  8,     'pinyin':u'nǚ',           'type': 'adjective',           'translation': 'female'},
    {'character': u'孩子', 'chapter': 2, 'id': 9,     'pinyin':u'háizi',         'type': 'noun',            'translation': 'child'},
    {'character': u'谁 ' , 'chapter': 2, 'id': 10,     'pinyin':u'shéi',         'type': 'question pronoun',            'translation': 'who'},
    {'character': u'他 ' , 'chapter': 2, 'id': 11,     'pinyin':u'tā',           'type': 'pronoun',           'translation': 'she; her'},
    {'character': u'姐姐', 'chapter': 2, 'id': 12,    'pinyin':u'jiějie',        'type': 'noun',             'translation': 'older sister'},
    {'character': u'男 ' , 'chapter': 2, 'id': 13,    'pinyin':u'nán',          'type': 'adjective',           'translation': 'male'},
    {'character': u'弟弟', 'chapter': 2, 'id': 14,      'pinyin':u'dìdi',          'type': 'noun',            'translation': 'younger brother'},
    {'character': u'他 ' , 'chapter': 2, 'id': 15,     'pinyin':u'tā',           'type': 'pronoun',           'translation': 'he; him'},
    {'character': u'大哥', 'chapter': 2, 'id': 16,      'pinyin':u'dàgē',          'type': 'noun',             'translation': 'eldest brother'},
    {'character': u'儿子', 'chapter': 2, 'id': 17,     'pinyin':u'érzi',          'type': 'noun',             'translation': 'son'},
    {'character': u'有 ' , 'chapter': 2, 'id': 18,     'pinyin':u'yǒu',           'type': 'verb',            'translation': 'to have; to exist'},
    {'character': u'女儿', 'chapter': 2, 'id': 19,     'pinyin':u'nǚér',          'type': 'noun',             'translation': 'daughter'},
    {'character': u'没 ' , 'chapter': 2, 'id': 20,     'pinyin':u'méi',           'type': 'adverb',             'translation': 'not'},
    {'character': u'高文中', 'chapter': 2, 'id': 21,    'pinyin':u'gāowénzhōng',    'type': '--',            'translation': '(a personal name)'},
    {'character': u'高 ' , 'chapter': 2, 'id': '21-alt',      'pinyin':u'gāo',           'type': '--',            'translation': '(a surname), tall; high'},

    # page 51
    {'character': u'家 ',  'chapter': 2, 'id': 1,        'pinyin': u'jiā',          'type': 'noun',      'translation': 'family; home'},
    {'character': u'几 ',  'chapter': 2, 'id': 2,       'pinyin': u'jī',           'type': 'numerical',          'translation': 'how many; some; a few'},
    {'character': u'口 ',  'chapter': 2, 'id': 3,       'pinyin': u'kǒu',          'type': 'measure word',        'translation': '(measure word for number of family members)'},
    {'character': u'哥哥', 'chapter': 2, 'id': 4,       'pinyin': u'gēge',          'type': 'noun',       'translation': 'older brother'},
    {'character': u'两 ',  'chapter': 2, 'id': 5,       'pinyin': u'liǎng',        'type': 'numerical',      'translation': 'two; a couple of'},
    {'character': u'妹妹', 'chapter': 2, 'id': 6,       'pinyin': u'mèimei',        'type': 'noun',       'translation': 'younger sister'},
    {'character': u'和 ',  'chapter': 2, 'id': 7,       'pinyin': u'hé',           'type': 'conjunction',      'translation': 'and '},
    {'character': u'大姐', 'chapter': 2, 'id': 8,      'pinyin': u'dàjiě',         'type': 'noun',       'translation': 'eldest sister'},
    {'character': u'二姐', 'chapter': 2, 'id': 9,      'pinyin': u'èrjiě',         'type': 'noun',       'translation': 'second oldest sister  '},
    {'character': u'做 ',  'chapter': 2, 'id': 10,       'pinyin': u'zuò',          'type': 'verb',       'translation': 'todo '},
    {'character': u'工作', 'chapter': 2, 'id': 11,       'pinyin': u'gōngzuò',       'type': 'noun/verb',       'translation': 'job; to work'},
    {'character': u'律师', 'chapter': 2, 'id': 12,      'pinyin': u'lǜshī',         'type': 'noun',       'translation': 'lawyer'},
    {'character': u'英文', 'chapter': 2, 'id': 13,       'pinyin': u'yīngwén',       'type': 'noun',        'translation': 'English (language)'},
    {'character': u'都 ' , 'chapter': 2, 'id': 14,       'pinyin': u'dōu',          'type': 'adverb',       'translation': 'both; all'},
    {'character': u'大学生', 'chapter': 2, 'id': 15,      'pinyin': u'dàxuéshēng',    'type': 'noun',       'translation': 'college student'},
    {'character': u'大学',  'chapter': 2, 'id': '15-alt',       'pinyin': u'dàxué',         'type': 'noun',        'translation': 'university; college'},
    {'character': u'医生',  'chapter': 2, 'id': 16,        'pinyin': u'yīshēng',       'type': 'noun',        'translation': 'doctor, physician'},
    {'character': u'白英爱', 'chapter': 2, 'id': 17,      'pinyin': u'bái yīng ài',   'type': '--',       'translation': '(a personal name)'},

    # Page 68
    {'character': u'九月', 'chapter': 3, 'id': 1,   'pinyin': u'jiǔyuè',           'type': 'noun',      'translation': 'September'},
    {'character': u'月 ', 'chapter': 3, 'id':  2,   'pinyin': u'yuè',              'type': 'noun',     'translation': 'month'},
    {'character': u'十二', 'chapter': 3, 'id': 3,   'pinyin': u'shíèr',            'type': 'numerical',      'translation': 'twelve'},
    {'character': u'号 ' , 'chapter': 3, 'id': 4,   'pinyin': u'háo',              'type': 'measure word',     'translation': '(measure word for number in a series; day of the month)'},
    {'character': u'星期', 'chapter': 3, 'id': 5,    'pinyin': u'xīngqī',          'type': 'noun',     'translation': 'week'},
    {'character': u'星期四', 'chapter': 3, 'id': 6,   'pinyin': u'xīngqīsì',        'type': 'noun',     'translation': 'Thursday'},
    {'character': u'天 ',  'chapter': 3, 'id': 7,    'pinyin': u'tiān',            'type': 'noun',     'translation': 'day'},
    {'character': u'生日', 'chapter': 3, 'id': 8,    'pinyin': u'shēngrì',          'type': 'noun',     'translation': 'birthday'},
    {'character': u'生 ',  'chapter': 3, 'id': '8-alt',   'pinyin': u'shēng',           'type': 'verb',     'translation': 'to give birth to; to be born'},
    {'character': u'日 ',  'chapter': 3, 'id': '8-alt2',    'pinyin': u'rì',              'type': 'noun',     'translation': 'day; sun'},
    {'character': u'今年', 'chapter': 3, 'id': 9,   'pinyin': u'jīnnián',         'type': 'time word',     'translation': 'this year'},
    {'character': u'年 ',  'chapter': 3, 'id': '9-alt',   'pinyin': u'nián',            'type': 'noun',     'translation': 'year'},
    {'character': u'多 ',  'chapter': 3, 'id': 10,  'pinyin': u'duō',             'type': 'adverb',     'translation': 'how many/much; to what extent; many'},
    {'character': u'大 ',  'chapter': 3, 'id': 11,   'pinyin': u'dà',              'type': 'adjective',     'translation': 'big; old'},
    {'character': u'十八', 'chapter': 3, 'id': 12,   'pinyin': u'shíbā',           'type': 'numerical',     'translation': 'eighteen'},
    {'character': u'岁 ',  'chapter': 3, 'id': 13,   'pinyin': u'suì',             'type': 'noun',     'translation': 'year (of age)'},
    {'character': u'吃 ',  'chapter': 3, 'id': 14,   'pinyin': u'chī',             'type': 'verb',     'translation': 'to eat'},
    {'character': u'饭 ',  'chapter': 3, 'id':  15,  'pinyin': u'fàn',             'type': 'noun',     'translation': 'meal; (cooked) rice'},
    {'character': u'怎么样', 'chapter': 3, 'id': 16,   'pinyin': u'zěnmeyàng',       'type': 'question pronoun',     'translation': 'Is it O.K.? How is that? How does that sound?'},
    {'character': u'太了',  'chapter': 3, 'id': 17,   'pinyin': u'tài..le',          'type': '--',    'translation': 'too; extremely'},
    {'character': u'谢谢',  'chapter': 3, 'id': 18,  'pinyin': u'xièxie',           'type': 'verb',    'translation': 'to thank'},
    {'character': u'喜欢',  'chapter': 3, 'id': 19,  'pinyin': u'xǐhuan',           'type': 'verb',    'translation': 'to like '},
    {'character': u'蔡 ',  'chapter': 3, 'id': 20,   'pinyin': u'cài',              'type': 'noun',    'translation': 'dishes, cuisine'},
    {'character': u'还是', 'chapter': 3, 'id': 21,   'pinyin': u'háishi',           'type': 'conjunction',    'translation': 'or '},
    {'character': u'可是', 'chapter': 3, 'id': 22,  'pinyin': u'kěshì',            'type': 'conjunction',    'translation': 'but '},
    {'character': u'我们', 'chapter': 3, 'id': 23,   'pinyin': u'wǒmen',            'type': 'pronoun',    'translation': 'we '},
    {'character': u'点 ',  'chapter': 3, 'id': 24,   'pinyin': u'diǎn',             'type': 'measure word',    'translation': 'o’clock (lit. dot, point, thus “points on the clock”)'},
    {'character': u'半 ',  'chapter': 3, 'id': 25,   'pinyin': u'bàn',              'type': 'numerical',    'translation': 'half; half an hour'},
    {'character': u'晚上', 'chapter': 3, 'id': 26,   'pinyin': u'wǎnshang',         'type': 'timeword/noun',    'translation': 'evening; night'},
    {'character': u'见 ',  'chapter': 3, 'id': 27,   'pinyin': u'jiàn',             'type': 'verb',    'translation': 'to see '},
    {'character': u'再见', 'chapter': 3, 'id': 28,   'pinyin': u'zàijiàn',          'type': 'verb',    'translation': 'goodbye; see you '},
    {'character': u'再 ',  'chapter': 3, 'id': '28-alt',   'pinyin': u'zài',              'type': 'adverb',    'translation': 'again '},
    {'character': u'英国', 'chapter': 3, 'id': 29,   'pinyin': u'yīngguó',          'type': '--',    'translation': 'Britain; England'},

    # Chapter 3: Dates and Times
    # Page 85
    {'character': u'现在 ', 'chapter': 3, 'id': 1,        'pinyin': u'xiànzài',      'type': 'time word',    'translation': 'now'},
    {'character': u'刻  ', 'chapter': 3, 'id':  2,     'pinyin': u'kè',            'type': 'measure word',    'translation': 'quarter(of an hour)'},
    {'character': u'事  ', 'chapter': 3, 'id':  3,     'pinyin': u'shì',           'type': 'noun',    'translation': 'matter; affair; event'},
    {'character': u'今天 ', 'chapter': 3, 'id': 4,      'pinyin': u'jīntiān',       'type': 'time word',   'translation': 'today '},
    {'character': u'很  ', 'chapter': 3, 'id':  5,     'pinyin': u'hěn',            'type': 'adverb',    'translation': 'very'},
    {'character': u'忙  ', 'chapter': 3, 'id':  6,     'pinyin': u'máng',           'type': 'adjective',    'translation': 'very'},
    {'character': u'明天 ', 'chapter': 3, 'id': 7,      'pinyin': u'míngtiān',       'type': 'time word',   'translation': 'tomorrow'},
    {'character': u'晚饭 ', 'chapter': 3, 'id': 8,      'pinyin': u'wǎnfàn',         'type': 'noun',   'translation': 'dinner; supper'},
    {'character': u'为什么', 'chapter': 3, 'id': 9,      'pinyin': u'wèishénme',       'type': 'question pronoun',   'translation': 'why'},
    {'character': u'为  ', 'chapter': 3, 'id': '9-alt',      'pinyin': u'wéi',             'type': 'prep',    'translation': 'for '},
    {'character': u'因为 ', 'chapter': 3, 'id': 10,      'pinyin': u'yīnwèi',         'type': 'conjunction',   'translation': 'because'},
    {'character': u'还  ', 'chapter': 3, 'id': 11,     'pinyin': u'hái',             'type': 'adverb',    'translation': 'also; too; as well'},
    {'character': u'同学 ', 'chapter': 3, 'id': 12,      'pinyin': u'tóngxué',        'type': 'noun',   'translation': 'classmate'},
    {'character': u'认识 ', 'chapter': 3, 'id': 13,     'pinyin': u'rènshi',        'type': 'verb',   'translation': 'to be acquainted with; to recognize'},
    {'character': u'朋友 ', 'chapter': 3, 'id': 14,      'pinyin': u'péngyou',       'type': 'noun',   'translation': 'friend'},

    # Chapter 4
    # Page 100
    {'character': u'周末',  'chapter': 4, 'id': 1,    'pinyin': u'zhōumò',        'type': 'noun',      'translation': 'weekend'},
    {'character': u'打球',  'chapter': 4, 'id': 2,   'pinyin': u'dǎ qiú',        'type': 'verb plus object',      'translation': 'to play ball'},
    {'character': u'打 ' , 'chapter': 4, 'id': '2-alt',   'pinyin': u'dá',            'type': 'verb',     'translation': 'to hit'},
    {'character': u'球 ' , 'chapter': 4, 'id': '2-alt2',   'pinyin': u'qiú',           'type': 'noun',      'translation': 'ball '},
    {'character': u'看 ' , 'chapter': 4, 'id': 3,   'pinyin': u'kān',           'type': 'verb',      'translation': 'to watch; to look; to read'},
    {'character': u'电视',  'chapter': 4, 'id': 4,    'pinyin': u'diànshì',       'type': 'noun',      'translation': 'television'},
    {'character': u'电 ' , 'chapter': 4, 'id': '4-alt',   'pinyin': u'diàn',          'type': 'noun',      'translation': 'electricity'},
    {'character': u'视 ' , 'chapter': 4, 'id': '4-alt2',   'pinyin': u'shì',           'type': 'noun',      'translation': 'vision'},
    {'character': u'唱歌',  'chapter': 4, 'id': 5,    'pinyin': u'chàng gē(r)',     'type': 'verb plus object',      'translation': 'to sing(a song) '},
    {'character': u'唱 ', 'chapter': 4, 'id': '5-alt',   'pinyin': u'chàng',         'type': 'verb',   'translation': 'to sing'},
    {'character': u'歌 ', 'chapter': 4, 'id': '5-alt2',   'pinyin': u'gē',            'type': 'noun',   'translation': 'song '},
    {'character': u'跳舞', 'chapter': 4, 'id': 6,  'pinyin': u' tiàowǔ',        'type': 'verb plus object',  'translation': 'to dance'},
    {'character': u'跳 ', 'chapter': 4, 'id': '6-alt',   'pinyin': u'tiào',          'type': 'verb',    'translation': 'to  jump'},
    {'character': u'舞 ', 'chapter': 4, 'id': '6-alt2',   'pinyin': u'wǔ',            'type': 'noun',    'translation': 'dance '},
    {'character': u'听 ', 'chapter': 4, 'id': 7,   'pinyin': u'tīng',          'type': 'verb',    'translation': 'to listen '},
    {'character': u'音乐', 'chapter': 4, 'id': 8,  'pinyin': u'yīnyuè',        'type': 'noun',  'translation': ' music'},
    {'character': u'书 ', 'chapter': 4, 'id': 9,   'pinyin': u'shū',            'type': 'noun',    'translation': 'book'},
    {'character': u'对 ', 'chapter': 4, 'id': 10,   'pinyin': u'duì',            'type': 'adjective',    'translation': 'right; correct'},
    {'character': u'有的', 'chapter': 4, 'id': 11,  'pinyin': u'yǒude',          'type': 'pronoun',  'translation': 'some '},
    {'character': u'时候', 'chapter': 4, 'id': 12,  'pinyin': u'shíhou',         'type': 'noun',  'translation': '(a point in) time; moment; (a duration of) time'},
    {'character': u'电影', 'chapter': 4, 'id': 13,    'pinyin': u'diànyǐng',       'type': 'noun',  'translation': 'movie'},
    {'character': u'影 ', 'chapter': 4, 'id': '13-alt',   'pinyin': u'yǐng',           'type': 'noun',   'translation': 'shadow'},
    {'character': u'常常', 'chapter': 4, 'id': 14,   'pinyin': u'chángcháng',    'type': 'adverb',  'translation': 'often'},
    {'character': u'那 ', 'chapter': 4, 'id': 15,   'pinyin': u'nā',             'type': 'conjunction',   'translation': 'in that case; then'},
    {'character': u'去 ', 'chapter': 4, 'id': 16,   'pinyin': u'qù',             'type': 'verb',  'translation': 'to go '},
    {'character': u'外国', 'chapter': 4, 'id': 17,  'pinyin': u'wàiguó',        'type': 'noun',  'translation': 'foreign country'},
    {'character': u'请客', 'chapter': 4, 'id': 18, 'pinyin': u'qǐng kè',       'type': 'verb plus object',  'translation': 'to invite someone (to dinner, coffee, etc.); to play the host '},
    {'character': u'昨天', 'chapter': 4, 'id': 19,  'pinyin': u'zuótiān',       'type': 'time word',  'translation': 'yesterday'},
    {'character': u'所以', 'chapter': 4, 'id': 20,  'pinyin': u'suǒyǐ',         'type': 'conjunction',  'translation': 'so '},

    # Page 112
    {'character': u'小  ', 'chapter':4,  'id': 1,   'pinyin': u'xiǎo',          'type': 'adjective',    'translation': 'small; little'},
    {'character': u'好久 ', 'chapter':4,  'id': 2,    'pinyin': u'hǎojiǔ',        'type': 'a',    'translation': 'long time'},
    {'character': u'好  ', 'chapter':4,  'id': '2-alt',   'pinyin': u'hǎo',           'type': 'adverb',    'translation': 'very '},
    {'character': u'久  ', 'chapter':4,  'id': '2-alt2',   'pinyin': u'jiǔ',           'type': 'adjective',    'translation': 'long(of time)'},
    {'character': u'不错 ', 'chapter':4,  'id': 3,   'pinyin': u'bùcuò',         'type': 'adjective',     'translation': 'pretty good'},
    {'character': u'错  ', 'chapter':4,  'id': '3-alt',   'pinyin': u'cuò',           'type': 'adjective',    'translation': 'wrong '},
    {'character': u'想  ', 'chapter':4,  'id': 4,   'pinyin': u'xiǎng',         'type': 'modal verb',    'translation': 'to want to; would like to; to think'},
    {'character': u'觉得 ', 'chapter':4,  'id': 5,  'pinyin': u'juéde',          'type': 'verb',     'translation': 'to feel; to think'},
    {'character': u'有意思', 'chapter':4,  'id': 6,  'pinyin': u'yǒu yìsi',       'type': 'adjective',       'translation': 'interesting'},
    {'character': u'意思 ', 'chapter':4,  'id': '6-alt',   'pinyin': u'yìsi',          'type': 'noun',     'translation': 'meaning'},
    {'character': u'只  ', 'chapter':4,  'id': 7,   'pinyin': u'zhī',           'type': 'adverb',    'translation': 'only '},
    {'character': u'睡觉 ', 'chapter':4,  'id': 8,    'pinyin': u'shuì jiào',    'type': 'verb plus object',      'translation': 'to sleep '}, 
    {'character': u'睡  ', 'chapter':4,  'id': '8-alt',   'pinyin': u'shuì',          'type': 'verb',    'translation': 'to sleep'},
    {'character': u'觉  ', 'chapter':4,  'id': '8-alt2',   'pinyin': u'jiào',          'type': 'noun',    'translation': 'sleep '},
    {'character': u'算了 ', 'chapter':4,  'id': 9,    'pinyin': u'suàn le',       'type': '--',    'translation': 'forget it; never mind'},
    {'character': u'找  ', 'chapter':4,  'id': 10,   'pinyin': u'zhǎo',          'type': 'verb',    'translation': 'to look for '},
    {'character': u'别人 ', 'chapter':4,  'id': 11,  'pinyin': u'biéren',         'type': 'noun',     'translation': 'other people; another person'},
    {'character': u'备的 ', 'chapter':4,  'id': 12,   'pinyin': u'bèi (de)',      'type': 'adjective',   'translation': 'other'},

    # Chapter 5
    {'character': u'呀   ', 'chapter': 5,  'id': 1, 'pinyin': u'ya',            'type': 'particle',       'translation': '(interjectory particle used to soften a question)'},
    {'character': u'进   ', 'chapter': 5,  'id': 2, 'pinyin': u'jìn',           'type': 'verb',       'translation': 'to enter'},
    {'character': u'快   ', 'chapter': 5,  'id': 3, 'pinyin': u'kuài',          'type': 'adv/adj',    'translation': 'fast, quick; quickly'},
    {'character': u'进来  ', 'chapter': 5,  'id': 4, 'pinyin': u'jìn lái',       'type': 'verb plus complement',       'translation': 'to come in'},
    {'character': u'来   ', 'chapter': 5,  'id': 5, 'pinyin': u'lái',           'type': 'verb',      'translation': 'to come '},
    {'character': u'介绍  ', 'chapter': 5,  'id': 6, 'pinyin': u'jièshào',       'type': 'verb',    'translation': 'to introduce'},
    {'character': u'一下  ', 'chapter': 5,  'id': 7, 'pinyin': u'yī xià',        'type': 'n+m',    'translation': 'once; a bit'},
    {'character': u'高兴  ', 'chapter': 5,  'id': 8, 'pinyin': u'gāoxìng',       'type': 'adjective',    'translation': 'happy, pleased     '},
    {'character': u'漂亮  ', 'chapter': 5,  'id': 9, 'pinyin': u'piàoliang',     'type': 'adjective',   'translation': 'pretty'},
    {'character': u'坐   ', 'chapter': 5,  'id': 10, 'pinyin': u'zuò',            'type': 'verb',    'translation': 'to sit '},
    {'character': u'在   ', 'chapter': 5,  'id': 11, 'pinyin': u'zài',            'type': 'prep',     'translation': 'at; in; on'},
    {'character': u'那人  ', 'chapter': 5,  'id': 12, 'pinyin': u'nǎr',           'type': 'question pronoun',     'translation': 'where '},
    {'character': u'学校  ', 'chapter': 5,  'id': 13, 'pinyin': u'xuéxiào',       'type': 'noun',     'translation': 'school '},
    {'character': u'喝   ', 'chapter': 5,  'id': 14, 'pinyin': u'hē',             'type': 'verb',    'translation': 'to drink'},
    {'character': u'点   ', 'chapter': 5,  'id': 15, 'pinyin': u'diǎn(r)',        'type': 'measure word',    'translation': 'a little, a bit; some'},
    {'character': u'茶   ', 'chapter': 5,  'id': 16,  'pinyin': u'chá',            'type': 'noun',    'translation': 'tea '},
    {'character': u'咖啡  ', 'chapter': 5,  'id': 17, 'pinyin': u'kāfēi',         'type': 'noun',     'translation': 'coffee'},
    {'character': u'吧   ', 'chapter': 5,  'id': 18, 'pinyin': u'bā',             'type': 'particle',    'translation': '(a sentence-final particle)'},
    {'character': u'要   ', 'chapter': 5,  'id': 19, 'pinyin': u'yāo',            'type': 'verb',    'translation': 'to want'},
    {'character': u'瓶   ', 'chapter': 5,  'id': 20, 'pinyin': u'píng',           'type': ' measure word/noun',    'translation': '(measure word for bottles); bottle'},
    {'character': u'可乐  ', 'chapter': 5,  'id': 21, 'pinyin': u'kělè',          'type': 'noun',    'translation': '[Coke or Pepsi] cola'},
    {'character': u'可以  ', 'chapter': 5,  'id': 22, 'pinyin': u'kěyǐ',          'type': 'modal verb',    'translation': 'can; may'},
    {'character': u'对不起 ', 'chapter': 5,  'id': 23, 'pinyin': u'duìbuqǐ',       'type': 'verb',     'translation': 'sorry'},
    {'character': u'给   ', 'chapter': 5,  'id': 24,  'pinyin': u'gěi',            'type': 'verb',    'translation': 'to give '},
    {'character': u'被   ', 'chapter': 5,  'id': 25, 'pinyin': u'bèi',            'type': 'measure word',    'translation': '(measure word for cup and glass)'},
    {'character': u'水   ', 'chapter': 5,  'id': 26, 'pinyin': u'shuǐ',           'type': 'noun',    'translation': 'water'},
    {'character': u'高小音 ', 'chapter': 5, 'id': 27, 'pinyin': u'gāo xiǎoyīn',   'type': '--',     'translation': '(a personal name)'},

    # Page 136
    {'character': u'玩  ', 'chapter': 5, 'id': 1,    'pinyin': u'wán(r)',        'type': 'verb',     'translation': 'to have fun; to play              '},
    {'character': u'了  ', 'chapter': 5, 'id': 2,   'pinyin': u'le',            'type': 'particle',     'translation': '(a dynamic particle)'},
    {'character': u'图书馆', 'chapter': 5, 'id': 3,   'pinyin': u'túshūguǎn',     'type': 'noun',      'translation': 'library'},
    {'character': u'一起 ', 'chapter': 5, 'id': 4,  'pinyin': u'yīqǐ',           'type': 'adverb',      'translation': 'together '},
    {'character': u'聊天 ', 'chapter': 5, 'id': 5,   'pinyin': u'liáo tiān(r)',   'type': 'verb plus object',      'translation': 'to chat   '},
    {'character': u'聊  ', 'chapter': 5, 'id': '5-alt',    'pinyin': u'liáo',           'type': 'verb',     'translation': 'to chat'},
    {'character': u'天  ', 'chapter': 5, 'id': '5-alt2',   'pinyin': u'tiān',           'type': 'noun',     'translation': 'sky '},
    {'character': u'才  ', 'chapter': 5, 'id': 6,    'pinyin': u'cái',            'type': 'adverb',     'translation': 'not until; only then'},
    {'character': u'回家 ', 'chapter': 5, 'id': 7,   'pinyin': u'huí jiā',        'type': 'verb plus object',      'translation': 'to go home   '},
    {'character': u'回  ', 'chapter': 5, 'id':  '7-alt',   'pinyin': u'huí',           'type': 'verb',     'translation': 'to return'},

    # Chapter 6 page 152
    {'character': u'给  ', 'chapter': 6, 'id': 1,    'pinyin': u'gěi',              'type': 'prep',     'translation': 'to; for'},
    {'character': u'打电话', 'chapter': 6, 'id': 2,    'pinyin': u'dǎ diànhuà',       'type': 'verb plus object',       'translation': 'to make a phone call'},
    {'character': u'电话 ', 'chapter': 6, 'id': '2-alt',   'pinyin': u'diànhuà',           'type': 'noun',        'translation': 'telephone     '},
    {'character': u'喂  ', 'chapter': 6, 'id': 3,    'pinyin': u'wéi/wèi',           'type': 'interjection',    'translation': '(on telephone) Hello!; Hey!'},
    {'character': u'在  ', 'chapter': 6, 'id': 4,    'pinyin': u'zài',              'type': 'verb',        'translation': 'to be present; to be at (a place)'},
    {'character': u'就  ', 'chapter': 6, 'id': 5,    'pinyin': u'jiù',              'type': 'adverb',     'translation': 'precisely; exactly'},
    {'character': u'您  ', 'chapter': 6, 'id': 6,    'pinyin': u'nín',              'type': 'pronoun',      'translation': 'you(honorific)'},
    {'character': u'那  ', 'chapter': 6, 'id':  7,   'pinyin': u'nā/něi',           'type': 'question pronoun',      'translation': 'which'},
    {'character': u'位  ', 'chapter': 6, 'id': 8,    'pinyin': u'wèi',              'type': 'measure word',        'translation': '(polite measure word for people)'},
    {'character': u'下午 ', 'chapter': 6, 'id': 9,    'pinyin': u'xiàwǔ',             'type': 'time word',        'translation': 'afternoon '},
    {'character': u'时间 ', 'chapter': 6, 'id': 10,    'pinyin': u'shíjiān',           'type': 'noun',        'translation': 'time  '},
    {'character': u'问题 ', 'chapter': 6, 'id': 11,   'pinyin': u'wèntí',             'type': 'noun',        'translation': 'question; problem'},
    {'character': u'要  ', 'chapter': 6, 'id': 12,     'pinyin': u'yāo',               'type': 'modal verb',      'translation': 'will, be going to; to want to, to have a desire to'},
    {'character': u'开会 ', 'chapter': 6, 'id': 13,    'pinyin': u'kāi huì',           'type': 'verb plus object',     'translation':  'to have a meeting '},
    {'character': u'开  ', 'chapter': 6, 'id': '13-alt',     'pinyin': u'kāi',               'type': 'verb',       'translation': 'to open; to hold (a meeting, party, etc.)'},
    {'character': u'会  ', 'chapter': 6, 'id': '13-alt2',     'pinyin': u'huì',               'type': 'noun',       'translation': 'meeting'},
    {'character': u'上午 ', 'chapter': 6, 'id': 14,    'pinyin': u'shàngwǔ',            'type': 'time word',       'translation': 'morning          '},
    {'character': u'节  ', 'chapter': 6, 'id': 15,   'pinyin': u'jiē',               'type': 'measure word',      'translation': '(measure word for class periods)'},
    {'character': u'棵  ', 'chapter': 6, 'id': 16,    'pinyin': u'kē',                'type': 'noun',      'translation': 'class; course; lesson'},
    {'character': u'年级 ', 'chapter': 6, 'id': 17,   'pinyin': u'niánjí',             'type': 'noun',      'translation': 'grade in school'},
    {'character': u'考试 ', 'chapter': 6, 'id': 18,   'pinyin': u'kǎo shì',            'type': 'verb plus object/noun',       'translation': 'to give or take a test; test '},
    {'character': u'考  ', 'chapter': 6, 'id': '18-alt',    'pinyin': u'kǎo',                'type': 'verb',      'translation': 'to give or take a test'},
    {'character': u'试  ', 'chapter': 6, 'id': '18-alt2',    'pinyin': u'shì',                'type': 'noun/verb',      'translation': 'test; to try; to experiment'},
    {'character': u'以后 ', 'chapter': 6, 'id': 19,   'pinyin': u'yǐhòu',              'type': 'time word',     'translation': 'after; from now on, later on '},
    {'character': u'空  ', 'chapter': 6, 'id': 20,     'pinyin': u'kòng(r)',            'type': 'noun',      'translation': 'free time'},
    {'character': u'要是 ', 'chapter': 6, 'id': 21,    'pinyin': u'yàoshi',             'type': 'conjunction',   'translation': 'if '},
    {'character': u'方便 ', 'chapter': 6, 'id': 22,    'pinyin': u'fāngbiàn',           'type': 'adjective',     'translation': 'convenient '},
    {'character': u'到  ', 'chapter': 6, 'id': 23,    'pinyin': u'dào',                'type': 'verb',      'translation': 'to go to; to arrive'},
    {'character': u'办公室', 'chapter': 6, 'id': 24,   'pinyin': u'bàngōngshì',          'type': 'noun',       'translation': 'office '},
    {'character': u'行  ', 'chapter': 6, 'id': 25,     'pinyin': u'xíng',               'type': 'verb',      'translation': 'all right; O.K.'},
    {'character': u'等  ', 'chapter': 6, 'id': 26,     'pinyin': u'děng',               'type': 'verb',      'translation': 'to wait; to wait for '},
    {'character': u'别  ', 'chapter': 6, 'id': 27,     'pinyin': u'bié',                'type': 'adverb',    'translation': 'dont'},
    {'character': u'客气 ', 'chapter': 6, 'id': 28,    'pinyin': u'kèqi',               'type': 'adjective',   'translation': 'polite '},
    {'character': u'常老师', 'chapter': 6, 'id': 29,   'pinyin': u'cháng lǎoshī',       'type': ' --',    'translation': 'Teacher Chang   '},

    # Page 162
    {'character': u'下个', 'chapter': 6,  'id': 1,    'pinyin': u'xià gè',        'type': '--',      'translation': 'next one '},
    {'character': u'下 ', 'chapter': 6, 'id': '1-alt',     'pinyin': u'xià',           'type': '--',     'translation': 'below; next'},
    {'character': u'中文', 'chapter': 6, 'id': 2,    'pinyin': u'zhōngwén',      'type': 'noun',        'translation': 'Chinese language'},
    {'character': u'文 ', 'chapter': 6, 'id': '2-alt',    'pinyin': u'wén',            'type': 'noun',       'translation': 'language; script; written language'},
    {'character': u'帮 ', 'chapter': 6, 'id': 3,    'pinyin': u'bāng',           'type': 'verb',     'translation': 'to help'},
    {'character': u'准备', 'chapter': 6, 'id': 4,    'pinyin': u'zhǔnbèi',        'type': 'verb',    'translation': ' to prepare'},
    {'character': u'练习', 'chapter': 6, 'id': 5,   'pinyin': u'liànxí',         'type': 'verb',    'translation': ' to practice'},
    {'character': u'说 ', 'chapter': 6, 'id': 6,    'pinyin': u'shuō',           'type': 'verb',     'translation': 'to say, to speak'},
    {'character': u'啊 ', 'chapter': 6, 'id': 7,    'pinyin': u'a',              'type': 'particle',     'translation': '(a sentence-final particle of exclamation, interrogation, etc.)'},
    {'character': u'但是', 'chapter': 6, 'id': 8,    'pinyin': u'dànshì',         'type': 'conjunction',    'translation': 'but '},
    {'character': u'得 ', 'chapter': 6, 'id': 9,    'pinyin': u'déi',            'type': 'adverb',     'translation': 'must; to have to '},
    {'character': u'跟 ', 'chapter': 6, 'id': 10,    'pinyin': u'gēn',            'type': 'prep',     'translation': 'with '},
    {'character': u'见面', 'chapter': 6, 'id': 11,    'pinyin': u'jiàn miàn',      'type': 'verb plus object',     'translation': ' to meetup; to meet with '},
    {'character': u'面 ', 'chapter': 6, 'id': '11-alt',    'pinyin': u'miàn',           'type': 'noun',     'translation': 'face '},
    {'character': u'回来', 'chapter': 6, 'id': 12,    'pinyin': u'huí lai',        'type': 'verb plus complement',     'translation': 'to come back'},
]

Chapter1 = [
    {'character': u'你', 'chapter': 1, 'id': 1,     'pinyin': u'nǐ',            'type': 'pronoun',            'translation': 'you' },                                
    {'character': u'好', 'chapter': 1, 'id': 2,     'pinyin': u'hǎo',           'type': 'adjective',            'translation': 'fine; good; nice; O.K.; it’s settled' },                            
    {'character': u'请', 'chapter': 1, 'id': 3,     'pinyin': u'qǐng',          'type': 'verb',            'translation': 'please (polite form of request); to treat or to invite (somebody)'},
    {'character': u'问', 'chapter': 1, 'id': 4,     'pinyin': u'wèn',           'type': 'verb',            'translation': 'to ask (a question)'},
    {'character': u'贵', 'chapter': 1, 'id': 5,     'pinyin': u'guì',           'type': 'adjective',            'translation': 'honorable; expensive'},
    {'character': u'姓', 'chapter': 1, 'id': 6,     'pinyin': u'xìng',          'type': 'verb/noun',            'translation': '(one’s) surname is...; to be surnamed; surname'},
    {'character': u'我', 'chapter': 1, 'id': 7,     'pinyin': u'wǒ',            'type': 'pronoun',            'translation': 'I; me'},
    {'character': u'呢', 'chapter': 1, 'id': 8,     'pinyin': u'ne',            'type': 'question particle',            'translation': '(question particle)'},
    {'character': u'小姐','chapter': 1, 'id': 9,    'pinyin': u'xiǎojie',       'type': 'noun',            'translation': ' Miss; young lady'},
    {'character': u'叫',  'chapter': 1, 'id': 10,    'pinyin': u'jiào',          'type': 'verb',            'translation': 'to be called; to call'},
    {'character': u'什么','chapter': 1, 'id': 11,    'pinyin': u'shénme',         'type': 'question pronoun',            'translation': 'what'}, 
    {'character': u'名字','chapter': 1, 'id': 12,    'pinyin': u'míngzi',         'type': 'noun',            'translation': 'name'},
    {'character': u'先生','chapter': 1, 'id': 13,    'pinyin': u'xiānsheng',      'type': 'noun',            'translation': 'Mr.; husband; teacher'},
    {'character': u'李友','chapter': 1, 'id': 14,     'pinyin': u'lǐ yǒu',         'type': '--',            'translation': '(a personal name)'},
    {'character': u'李', 'chapter': 1, 'id': '14-alt',     'pinyin': u'lǐ',            'type': '--',            'translation': '(a surname); plum'},
    {'character': u'王朋','chapter': 1, 'id': 15,     'pinyin': u'wáng péng',     'type': '--',            'translation': '(a personal name)'},
    {'character': u'王',  'chapter': 1, 'id': '15-alt',   'pinyin': u'wáng',          'type': '--',            'translation': '(a surname); king'},

    # Page 28
    {'character': u'是 ' , 'chapter': 1,  'id': 1,    'pinyin': u'shì',         'type': 'verb',           'translation': 'to be '},
    {'character': u'老师', 'chapter': 1, 'id': 2,     'pinyin': u'lǎoshī',       'type': 'noun',            'translation': 'teacher'},  
    {'character': u'吗 ' , 'chapter': 1, 'id': 3,    'pinyin': u'mǎ',          'type': 'question particle',            'translation': '(question particle)'},
    {'character': u'不 ' , 'chapter': 1, 'id': 4,    'pinyin': u'bù',          'type': 'adverb',            'translation': 'not; no'},
    {'character': u'学生', 'chapter': 1, 'id': 5,    'pinyin': u'xuésheng',     'type': 'noun',             'translation': 'student '},
    {'character': u'也 ' , 'chapter': 1, 'id': 6,    'pinyin': u'yě',          'type': 'adverb',            'translation': 'too; also'},
    {'character': u'人 ' , 'chapter': 1, 'id': 7,    'pinyin': u'rén',         'type': 'noun',            'translation': 'people; person'},
    {'character': u'中国', 'chapter': 1, 'id': 8,    'pinyin': u'zhōngguó',    'type': '--',             'translation': 'China'},
    {'character': u'北京', 'chapter': 1, 'id': 9,    'pinyin': u'běijīng',      'type': '--',             'translation': 'Beijing'},
    {'character': u'美国', 'chapter': 1, 'id': 10,    'pinyin': u'měiguó',       'type': '--',            'translation': 'America '},
    {'character': u'纽约', 'chapter': 1, 'id': 11,    'pinyin': u'niǔyuē',       'type': '--',            'translation': 'New York'},
]

Chapter2 = [
    {'character': u'那 ',  'chapter': 2, 'id': 1,     'pinyin':u'nā',           'type': 'pronoun',           'translation': 'that'},
    {'character': u'的 ' , 'chapter': 2, 'id': 2,     'pinyin':u'de',           'type': 'particle',           'translation': '(a possessive or descriptive particle)'},
    {'character': u'照片',  'chapter': 2, 'id': 3,      'pinyin':u'zhàopiàn',     'type': 'noun',            'translation': 'picture; photo'},
    {'character': u'这 ' , 'chapter': 2, 'id': 4,     'pinyin':u'zhè',          'type': 'pronoun',           'translation': 'this'},
    {'character': u'爸爸', 'chapter': 2, 'id': 5,      'pinyin':u'bàba',         'type': 'noun',            'translation': 'father, dad'},
    {'character': u'妈妈', 'chapter': 2, 'id': 6,      'pinyin':u'māma',         'type': 'noun',            'translation': 'mother, mom'},
    {'character': u'个 ', 'chapter': 2, 'id':  7,     'pinyin':u'gè',            'type': 'measure word',           'translation': '(measure word for many common everyday objects)'},
    {'character': u'女 ', 'chapter': 2, 'id':  8,     'pinyin':u'nǚ',           'type': 'adjective',           'translation': 'female'},
    {'character': u'孩子', 'chapter': 2, 'id': 9,     'pinyin':u'háizi',         'type': 'noun',            'translation': 'child'},
    {'character': u'谁 ' , 'chapter': 2, 'id': 10,     'pinyin':u'shéi',         'type': 'question pronoun',            'translation': 'who'},
    {'character': u'他 ' , 'chapter': 2, 'id': 11,     'pinyin':u'tā',           'type': 'pronoun',           'translation': 'she; her'},
    {'character': u'姐姐', 'chapter': 2, 'id': 12,    'pinyin':u'jiějie',        'type': 'noun',             'translation': 'older sister'},
    {'character': u'男 ' , 'chapter': 2, 'id': 13,    'pinyin':u'nán',          'type': 'adjective',           'translation': 'male'},
    {'character': u'弟弟', 'chapter': 2, 'id': 14,      'pinyin':u'dìdi',          'type': 'noun',            'translation': 'younger brother'},
    {'character': u'他 ' , 'chapter': 2, 'id': 15,     'pinyin':u'tā',           'type': 'pronoun',           'translation': 'he; him'},
    {'character': u'大哥', 'chapter': 2, 'id': 16,      'pinyin':u'dàgē',          'type': 'noun',             'translation': 'eldest brother'},
    {'character': u'儿子', 'chapter': 2, 'id': 17,     'pinyin':u'érzi',          'type': 'noun',             'translation': 'son'},
    {'character': u'有 ' , 'chapter': 2, 'id': 18,     'pinyin':u'yǒu',           'type': 'verb',            'translation': 'to have; to exist'},
    {'character': u'女儿', 'chapter': 2, 'id': 19,     'pinyin':u'nǚér',          'type': 'noun',             'translation': 'daughter'},
    {'character': u'没 ' , 'chapter': 2, 'id': 20,     'pinyin':u'méi',           'type': 'adverb',             'translation': 'not'},
    {'character': u'高文中', 'chapter': 2, 'id': 21,    'pinyin':u'gāowénzhōng',    'type': '--',            'translation': '(a personal name)'},
    {'character': u'高 ' , 'chapter': 2, 'id': '21-alt',      'pinyin':u'gāo',           'type': '--',            'translation': '(a surname), tall; high'},

    # page 51
    {'character': u'家 ',  'chapter': 2, 'id': 1,        'pinyin': u'jiā',          'type': 'noun',      'translation': 'family; home'},
    {'character': u'几 ',  'chapter': 2, 'id': 2,       'pinyin': u'jī',           'type': 'numerical',          'translation': 'how many; some; a few'},
    {'character': u'口 ',  'chapter': 2, 'id': 3,       'pinyin': u'kǒu',          'type': 'measure word',        'translation': '(measure word for number of family members)'},
    {'character': u'哥哥', 'chapter': 2, 'id': 4,       'pinyin': u'gēge',          'type': 'noun',       'translation': 'older brother'},
    {'character': u'两 ',  'chapter': 2, 'id': 5,       'pinyin': u'liǎng',        'type': 'numerical',      'translation': 'two; a couple of'},
    {'character': u'妹妹', 'chapter': 2, 'id': 6,       'pinyin': u'mèimei',        'type': 'noun',       'translation': 'younger sister'},
    {'character': u'和 ',  'chapter': 2, 'id': 7,       'pinyin': u'hé',           'type': 'conjunction',      'translation': 'and '},
    {'character': u'大姐', 'chapter': 2, 'id': 8,      'pinyin': u'dàjiě',         'type': 'noun',       'translation': 'eldest sister'},
    {'character': u'二姐', 'chapter': 2, 'id': 9,      'pinyin': u'èrjiě',         'type': 'noun',       'translation': 'second oldest sister  '},
    {'character': u'做 ',  'chapter': 2, 'id': 10,       'pinyin': u'zuò',          'type': 'verb',       'translation': 'todo '},
    {'character': u'工作', 'chapter': 2, 'id': 11,       'pinyin': u'gōngzuò',       'type': 'noun/verb',       'translation': 'job; to work'},
    {'character': u'律师', 'chapter': 2, 'id': 12,      'pinyin': u'lǜshī',         'type': 'noun',       'translation': 'lawyer'},
    {'character': u'英文', 'chapter': 2, 'id': 13,       'pinyin': u'yīngwén',       'type': 'noun',        'translation': 'English (language)'},
    {'character': u'都 ' , 'chapter': 2, 'id': 14,       'pinyin': u'dōu',          'type': 'adverb',       'translation': 'both; all'},
    {'character': u'大学生', 'chapter': 2, 'id': 15,      'pinyin': u'dàxuéshēng',    'type': 'noun',       'translation': 'college student'},
    {'character': u'大学',  'chapter': 2, 'id': '15-alt',       'pinyin': u'dàxué',         'type': 'noun',        'translation': 'university; college'},
    {'character': u'医生',  'chapter': 2, 'id': 16,        'pinyin': u'yīshēng',       'type': 'noun',        'translation': 'doctor, physician'},
    {'character': u'白英爱', 'chapter': 2, 'id': 17,      'pinyin': u'bái yīng ài',   'type': '--',       'translation': '(a personal name)'},

]

Chapter3 = [
    {'character': u'九月', 'chapter': 3, 'id': 1,   'pinyin': u'jiǔyuè',           'type': 'noun',      'translation': 'September'},
    {'character': u'月 ', 'chapter': 3, 'id':  2,   'pinyin': u'yuè',              'type': 'noun',     'translation': 'month'},
    {'character': u'十二', 'chapter': 3, 'id': 3,   'pinyin': u'shíèr',            'type': 'numerical',      'translation': 'twelve'},
    {'character': u'号 ' , 'chapter': 3, 'id': 4,   'pinyin': u'háo',              'type': 'measure word',     'translation': '(measure word for number in a series; day of the month)'},
    {'character': u'星期', 'chapter': 3, 'id': 5,    'pinyin': u'xīngqī',          'type': 'noun',     'translation': 'week'},
    {'character': u'星期四', 'chapter': 3, 'id': 6,   'pinyin': u'xīngqīsì',        'type': 'noun',     'translation': 'Thursday'},
    {'character': u'天 ',  'chapter': 3, 'id': 7,    'pinyin': u'tiān',            'type': 'noun',     'translation': 'day'},
    {'character': u'生日', 'chapter': 3, 'id': 8,    'pinyin': u'shēngrì',          'type': 'noun',     'translation': 'birthday'},
    {'character': u'生 ',  'chapter': 3, 'id': '8-alt',   'pinyin': u'shēng',           'type': 'verb',     'translation': 'to give birth to; to be born'},
    {'character': u'日 ',  'chapter': 3, 'id': '8-alt2',    'pinyin': u'rì',              'type': 'noun',     'translation': 'day; sun'},
    {'character': u'今年', 'chapter': 3, 'id': 9,   'pinyin': u'jīnnián',         'type': 'time word',     'translation': 'this year'},
    {'character': u'年 ',  'chapter': 3, 'id': '9-alt',   'pinyin': u'nián',            'type': 'noun',     'translation': 'year'},
    {'character': u'多 ',  'chapter': 3, 'id': 10,  'pinyin': u'duō',             'type': 'adverb',     'translation': 'how many/much; to what extent; many'},
    {'character': u'大 ',  'chapter': 3, 'id': 11,   'pinyin': u'dà',              'type': 'adjective',     'translation': 'big; old'},
    {'character': u'十八', 'chapter': 3, 'id': 12,   'pinyin': u'shíbā',           'type': 'numerical',     'translation': 'eighteen'},
    {'character': u'岁 ',  'chapter': 3, 'id': 13,   'pinyin': u'suì',             'type': 'noun',     'translation': 'year (of age)'},
    {'character': u'吃 ',  'chapter': 3, 'id': 14,   'pinyin': u'chī',             'type': 'verb',     'translation': 'to eat'},
    {'character': u'饭 ',  'chapter': 3, 'id':  15,  'pinyin': u'fàn',             'type': 'noun',     'translation': 'meal; (cooked) rice'},
    {'character': u'怎么样', 'chapter': 3, 'id': 16,   'pinyin': u'zěnmeyàng',       'type': 'question pronoun',     'translation': 'Is it O.K.? How is that? How does that sound?'},
    {'character': u'太了',  'chapter': 3, 'id': 17,   'pinyin': u'tài..le',          'type': '--',    'translation': 'too; extremely'},
    {'character': u'谢谢',  'chapter': 3, 'id': 18,  'pinyin': u'xièxie',           'type': 'verb',    'translation': 'to thank'},
    {'character': u'喜欢',  'chapter': 3, 'id': 19,  'pinyin': u'xǐhuan',           'type': 'verb',    'translation': 'to like '},
    {'character': u'蔡 ',  'chapter': 3, 'id': 20,   'pinyin': u'cài',              'type': 'noun',    'translation': 'dishes, cuisine'},
    {'character': u'还是', 'chapter': 3, 'id': 21,   'pinyin': u'háishi',           'type': 'conjunction',    'translation': 'or '},
    {'character': u'可是', 'chapter': 3, 'id': 22,  'pinyin': u'kěshì',            'type': 'conjunction',    'translation': 'but '},
    {'character': u'我们', 'chapter': 3, 'id': 23,   'pinyin': u'wǒmen',            'type': 'pronoun',    'translation': 'we '},
    {'character': u'点 ',  'chapter': 3, 'id': 24,   'pinyin': u'diǎn',             'type': 'measure word',    'translation': 'o’clock (lit. dot, point, thus “points on the clock”)'},
    {'character': u'半 ',  'chapter': 3, 'id': 25,   'pinyin': u'bàn',              'type': 'numerical',    'translation': 'half; half an hour'},
    {'character': u'晚上', 'chapter': 3, 'id': 26,   'pinyin': u'wǎnshang',         'type': 'timeword/noun',    'translation': 'evening; night'},
    {'character': u'见 ',  'chapter': 3, 'id': 27,   'pinyin': u'jiàn',             'type': 'verb',    'translation': 'to see '},
    {'character': u'再见', 'chapter': 3, 'id': 28,   'pinyin': u'zàijiàn',          'type': 'verb',    'translation': 'goodbye; see you '},
    {'character': u'再 ',  'chapter': 3, 'id': '28-alt',   'pinyin': u'zài',              'type': 'adverb',    'translation': 'again '},
    {'character': u'英国', 'chapter': 3, 'id': 29,   'pinyin': u'yīngguó',          'type': '--',    'translation': 'Britain; England'},

    # Chapter 3: Dates and Times
    # Page 85
    {'character': u'现在 ', 'chapter': 3, 'id': 1,        'pinyin': u'xiànzài',      'type': 'time word',    'translation': 'now'},
    {'character': u'刻  ', 'chapter': 3, 'id':  2,     'pinyin': u'kè',            'type': 'measure word',    'translation': 'quarter(of an hour)'},
    {'character': u'事  ', 'chapter': 3, 'id':  3,     'pinyin': u'shì',           'type': 'noun',    'translation': 'matter; affair; event'},
    {'character': u'今天 ', 'chapter': 3, 'id': 4,      'pinyin': u'jīntiān',       'type': 'time word',   'translation': 'today '},
    {'character': u'很  ', 'chapter': 3, 'id':  5,     'pinyin': u'hěn',            'type': 'adverb',    'translation': 'very'},
    {'character': u'忙  ', 'chapter': 3, 'id':  6,     'pinyin': u'máng',           'type': 'adjective',    'translation': 'very'},
    {'character': u'明天 ', 'chapter': 3, 'id': 7,      'pinyin': u'míngtiān',       'type': 'time word',   'translation': 'tomorrow'},
    {'character': u'晚饭 ', 'chapter': 3, 'id': 8,      'pinyin': u'wǎnfàn',         'type': 'noun',   'translation': 'dinner; supper'},
    {'character': u'为什么', 'chapter': 3, 'id': 9,      'pinyin': u'wèishénme',       'type': 'question pronoun',   'translation': 'why'},
    {'character': u'为  ', 'chapter': 3, 'id': '9-alt',      'pinyin': u'wéi',             'type': 'prep',    'translation': 'for '},
    {'character': u'因为 ', 'chapter': 3, 'id': 10,      'pinyin': u'yīnwèi',         'type': 'conjunction',   'translation': 'because'},
    {'character': u'还  ', 'chapter': 3, 'id': 11,     'pinyin': u'hái',             'type': 'adverb',    'translation': 'also; too; as well'},
    {'character': u'同学 ', 'chapter': 3, 'id': 12,      'pinyin': u'tóngxué',        'type': 'noun',   'translation': 'classmate'},
    {'character': u'认识 ', 'chapter': 3, 'id': 13,     'pinyin': u'rènshi',        'type': 'verb',   'translation': 'to be acquainted with; to recognize'},
    {'character': u'朋友 ', 'chapter': 3, 'id': 14,      'pinyin': u'péngyou',       'type': 'noun',   'translation': 'friend'},
]

Chapter4 = [
    {'character': u'周末',  'chapter': 4, 'id': 1,    'pinyin': u'zhōumò',        'type': 'noun',      'translation': 'weekend'},
    {'character': u'打球',  'chapter': 4, 'id': 2,   'pinyin': u'dǎ qiú',        'type': 'verb plus object',      'translation': 'to play ball'},
    {'character': u'打 ' , 'chapter': 4, 'id': '2-alt',   'pinyin': u'dá',            'type': 'verb',     'translation': 'to hit'},
    {'character': u'球 ' , 'chapter': 4, 'id': '2-alt2',   'pinyin': u'qiú',           'type': 'noun',      'translation': 'ball '},
    {'character': u'看 ' , 'chapter': 4, 'id': 3,   'pinyin': u'kān',           'type': 'verb',      'translation': 'to watch; to look; to read'},
    {'character': u'电视',  'chapter': 4, 'id': 4,    'pinyin': u'diànshì',       'type': 'noun',      'translation': 'television'},
    {'character': u'电 ' , 'chapter': 4, 'id': '4-alt',   'pinyin': u'diàn',          'type': 'noun',      'translation': 'electricity'},
    {'character': u'视 ' , 'chapter': 4, 'id': '4-alt2',   'pinyin': u'shì',           'type': 'noun',      'translation': 'vision'},
    {'character': u'唱歌',  'chapter': 4, 'id': 5,    'pinyin': u'chàng gē(r)',     'type': 'verb plus object',      'translation': 'to sing(a song) '},
    {'character': u'唱 ', 'chapter': 4, 'id': '5-alt',   'pinyin': u'chàng',         'type': 'verb',   'translation': 'to sing'},
    {'character': u'歌 ', 'chapter': 4, 'id': '5-alt2',   'pinyin': u'gē',            'type': 'noun',   'translation': 'song '},
    {'character': u'跳舞', 'chapter': 4, 'id': 6,  'pinyin': u' tiàowǔ',        'type': 'verb plus object',  'translation': 'to dance'},
    {'character': u'跳 ', 'chapter': 4, 'id': '6-alt',   'pinyin': u'tiào',          'type': 'verb',    'translation': 'to  jump'},
    {'character': u'舞 ', 'chapter': 4, 'id': '6-alt2',   'pinyin': u'wǔ',            'type': 'noun',    'translation': 'dance '},
    {'character': u'听 ', 'chapter': 4, 'id': 7,   'pinyin': u'tīng',          'type': 'verb',    'translation': 'to listen '},
    {'character': u'音乐', 'chapter': 4, 'id': 8,  'pinyin': u'yīnyuè',        'type': 'noun',  'translation': ' music'},
    {'character': u'书 ', 'chapter': 4, 'id': 9,   'pinyin': u'shū',            'type': 'noun',    'translation': 'book'},
    {'character': u'对 ', 'chapter': 4, 'id': 10,   'pinyin': u'duì',            'type': 'adjective',    'translation': 'right; correct'},
    {'character': u'有的', 'chapter': 4, 'id': 11,  'pinyin': u'yǒude',          'type': 'pronoun',  'translation': 'some '},
    {'character': u'时候', 'chapter': 4, 'id': 12,  'pinyin': u'shíhou',         'type': 'noun',  'translation': '(a point in) time; moment; (a duration of) time'},
    {'character': u'电影', 'chapter': 4, 'id': 13,    'pinyin': u'diànyǐng',       'type': 'noun',  'translation': 'movie'},
    {'character': u'影 ', 'chapter': 4, 'id': '13-alt',   'pinyin': u'yǐng',           'type': 'noun',   'translation': 'shadow'},
    {'character': u'常常', 'chapter': 4, 'id': 14,   'pinyin': u'chángcháng',    'type': 'adverb',  'translation': 'often'},
    {'character': u'那 ', 'chapter': 4, 'id': 15,   'pinyin': u'nā',             'type': 'conjunction',   'translation': 'in that case; then'},
    {'character': u'去 ', 'chapter': 4, 'id': 16,   'pinyin': u'qù',             'type': 'verb',  'translation': 'to go '},
    {'character': u'外国', 'chapter': 4, 'id': 17,  'pinyin': u'wàiguó',        'type': 'noun',  'translation': 'foreign country'},
    {'character': u'请客', 'chapter': 4, 'id': 18, 'pinyin': u'qǐng kè',       'type': 'verb plus object',  'translation': 'to invite someone (to dinner, coffee, etc.); to play the host '},
    {'character': u'昨天', 'chapter': 4, 'id': 19,  'pinyin': u'zuótiān',       'type': 'time word',  'translation': 'yesterday'},
    {'character': u'所以', 'chapter': 4, 'id': 20,  'pinyin': u'suǒyǐ',         'type': 'conjunction',  'translation': 'so '},

    # Page 112
    {'character': u'小  ', 'chapter':4,  'id': 1,   'pinyin': u'xiǎo',          'type': 'adjective',    'translation': 'small; little'},
    {'character': u'好久 ', 'chapter':4,  'id': 2,    'pinyin': u'hǎojiǔ',        'type': 'a',    'translation': 'long time'},
    {'character': u'好  ', 'chapter':4,  'id': '2-alt',   'pinyin': u'hǎo',           'type': 'adverb',    'translation': 'very '},
    {'character': u'久  ', 'chapter':4,  'id': '2-alt2',   'pinyin': u'jiǔ',           'type': 'adjective',    'translation': 'long(of time)'},
    {'character': u'不错 ', 'chapter':4,  'id': 3,   'pinyin': u'bùcuò',         'type': 'adjective',     'translation': 'pretty good'},
    {'character': u'错  ', 'chapter':4,  'id': '3-alt',   'pinyin': u'cuò',           'type': 'adjective',    'translation': 'wrong '},
    {'character': u'想  ', 'chapter':4,  'id': 4,   'pinyin': u'xiǎng',         'type': 'modal verb',    'translation': 'to want to; would like to; to think'},
    {'character': u'觉得 ', 'chapter':4,  'id': 5,  'pinyin': u'juéde',          'type': 'verb',     'translation': 'to feel; to think'},
    {'character': u'有意思', 'chapter':4,  'id': 6,  'pinyin': u'yǒu yìsi',       'type': 'adjective',       'translation': 'interesting'},
    {'character': u'意思 ', 'chapter':4,  'id': '6-alt',   'pinyin': u'yìsi',          'type': 'noun',     'translation': 'meaning'},
    {'character': u'只  ', 'chapter':4,  'id': 7,   'pinyin': u'zhī',           'type': 'adverb',    'translation': 'only '},
    {'character': u'睡觉 ', 'chapter':4,  'id': 8,    'pinyin': u'shuì jiào',    'type': 'verb plus object',      'translation': 'to sleep '}, 
    {'character': u'睡  ', 'chapter':4,  'id': '8-alt',   'pinyin': u'shuì',          'type': 'verb',    'translation': 'to sleep'},
    {'character': u'觉  ', 'chapter':4,  'id': '8-alt2',   'pinyin': u'jiào',          'type': 'noun',    'translation': 'sleep '},
    {'character': u'算了 ', 'chapter':4,  'id': 9,    'pinyin': u'suàn le',       'type': '--',    'translation': 'forget it; never mind'},
    {'character': u'找  ', 'chapter':4,  'id': 10,   'pinyin': u'zhǎo',          'type': 'verb',    'translation': 'to look for '},
    {'character': u'别人 ', 'chapter':4,  'id': 11,  'pinyin': u'biéren',         'type': 'noun',     'translation': 'other people; another person'},
    {'character': u'备的 ', 'chapter':4,  'id': 12,   'pinyin': u'bèi (de)',      'type': 'adjective',   'translation': 'other'},

]

Chapter5 = [
    {'character': u'呀   ', 'chapter': 5,  'id': 1, 'pinyin': u'ya',            'type': 'particle',       'translation': '(interjectory particle used to soften a question)'},
    {'character': u'进   ', 'chapter': 5,  'id': 2, 'pinyin': u'jìn',           'type': 'verb',       'translation': 'to enter'},
    {'character': u'快   ', 'chapter': 5,  'id': 3, 'pinyin': u'kuài',          'type': 'adv/adj',    'translation': 'fast, quick; quickly'},
    {'character': u'进来  ', 'chapter': 5,  'id': 4, 'pinyin': u'jìn lái',       'type': 'verb plus complement',       'translation': 'to come in'},
    {'character': u'来   ', 'chapter': 5,  'id': 5, 'pinyin': u'lái',           'type': 'verb',      'translation': 'to come '},
    {'character': u'介绍  ', 'chapter': 5,  'id': 6, 'pinyin': u'jièshào',       'type': 'verb',    'translation': 'to introduce'},
    {'character': u'一下  ', 'chapter': 5,  'id': 7, 'pinyin': u'yī xià',        'type': 'n+m',    'translation': 'once; a bit'},
    {'character': u'高兴  ', 'chapter': 5,  'id': 8, 'pinyin': u'gāoxìng',       'type': 'adjective',    'translation': 'happy, pleased     '},
    {'character': u'漂亮  ', 'chapter': 5,  'id': 9, 'pinyin': u'piàoliang',     'type': 'adjective',   'translation': 'pretty'},
    {'character': u'坐   ', 'chapter': 5,  'id': 10, 'pinyin': u'zuò',            'type': 'verb',    'translation': 'to sit '},
    {'character': u'在   ', 'chapter': 5,  'id': 11, 'pinyin': u'zài',            'type': 'prep',     'translation': 'at; in; on'},
    {'character': u'那人  ', 'chapter': 5,  'id': 12, 'pinyin': u'nǎr',           'type': 'question pronoun',     'translation': 'where '},
    {'character': u'学校  ', 'chapter': 5,  'id': 13, 'pinyin': u'xuéxiào',       'type': 'noun',     'translation': 'school '},
    {'character': u'喝   ', 'chapter': 5,  'id': 14, 'pinyin': u'hē',             'type': 'verb',    'translation': 'to drink'},
    {'character': u'点   ', 'chapter': 5,  'id': 15, 'pinyin': u'diǎn(r)',        'type': 'measure word',    'translation': 'a little, a bit; some'},
    {'character': u'茶   ', 'chapter': 5,  'id': 16,  'pinyin': u'chá',            'type': 'noun',    'translation': 'tea '},
    {'character': u'咖啡  ', 'chapter': 5,  'id': 17, 'pinyin': u'kāfēi',         'type': 'noun',     'translation': 'coffee'},
    {'character': u'吧   ', 'chapter': 5,  'id': 18, 'pinyin': u'bā',             'type': 'particle',    'translation': '(a sentence-final particle)'},
    {'character': u'要   ', 'chapter': 5,  'id': 19, 'pinyin': u'yāo',            'type': 'verb',    'translation': 'to want'},
    {'character': u'瓶   ', 'chapter': 5,  'id': 20, 'pinyin': u'píng',           'type': ' measure word/noun',    'translation': '(measure word for bottles); bottle'},
    {'character': u'可乐  ', 'chapter': 5,  'id': 21, 'pinyin': u'kělè',          'type': 'noun',    'translation': '[Coke or Pepsi] cola'},
    {'character': u'可以  ', 'chapter': 5,  'id': 22, 'pinyin': u'kěyǐ',          'type': 'modal verb',    'translation': 'can; may'},
    {'character': u'对不起 ', 'chapter': 5,  'id': 23, 'pinyin': u'duìbuqǐ',       'type': 'verb',     'translation': 'sorry'},
    {'character': u'给   ', 'chapter': 5,  'id': 24,  'pinyin': u'gěi',            'type': 'verb',    'translation': 'to give '},
    {'character': u'被   ', 'chapter': 5,  'id': 25, 'pinyin': u'bèi',            'type': 'measure word',    'translation': '(measure word for cup and glass)'},
    {'character': u'水   ', 'chapter': 5,  'id': 26, 'pinyin': u'shuǐ',           'type': 'noun',    'translation': 'water'},
    {'character': u'高小音 ', 'chapter': 5, 'id': 27, 'pinyin': u'gāo xiǎoyīn',   'type': '--',     'translation': '(a personal name)'},

    # Page 136
    {'character': u'玩  ', 'chapter': 5, 'id': 1,    'pinyin': u'wán(r)',        'type': 'verb',     'translation': 'to have fun; to play              '},
    {'character': u'了  ', 'chapter': 5, 'id': 2,   'pinyin': u'le',            'type': 'particle',     'translation': '(a dynamic particle)'},
    {'character': u'图书馆', 'chapter': 5, 'id': 3,   'pinyin': u'túshūguǎn',     'type': 'noun',      'translation': 'library'},
    {'character': u'一起 ', 'chapter': 5, 'id': 4,  'pinyin': u'yīqǐ',           'type': 'adverb',      'translation': 'together '},
    {'character': u'聊天 ', 'chapter': 5, 'id': 5,   'pinyin': u'liáo tiān(r)',   'type': 'verb plus object',      'translation': 'to chat   '},
    {'character': u'聊  ', 'chapter': 5, 'id': '5-alt',    'pinyin': u'liáo',           'type': 'verb',     'translation': 'to chat'},
    {'character': u'天  ', 'chapter': 5, 'id': '5-alt2',   'pinyin': u'tiān',           'type': 'noun',     'translation': 'sky '},
    {'character': u'才  ', 'chapter': 5, 'id': 6,    'pinyin': u'cái',            'type': 'adverb',     'translation': 'not until; only then'},
    {'character': u'回家 ', 'chapter': 5, 'id': 7,   'pinyin': u'huí jiā',        'type': 'verb plus object',      'translation': 'to go home   '},
    {'character': u'回  ', 'chapter': 5, 'id':  '7-alt',   'pinyin': u'huí',           'type': 'verb',     'translation': 'to return'},
]

Chapter6 = [
    {'character': u'给  ', 'chapter': 6, 'id': 1,    'pinyin': u'gěi',              'type': 'prep',     'translation': 'to; for'},
    {'character': u'打电话', 'chapter': 6, 'id': 2,    'pinyin': u'dǎ diànhuà',       'type': 'verb plus object',       'translation': 'to make a phone call'},
    {'character': u'电话 ', 'chapter': 6, 'id': '2-alt',   'pinyin': u'diànhuà',           'type': 'noun',        'translation': 'telephone     '},
    {'character': u'喂  ', 'chapter': 6, 'id': 3,    'pinyin': u'wéi/wèi',           'type': 'interjection',    'translation': '(on telephone) Hello!; Hey!'},
    {'character': u'在  ', 'chapter': 6, 'id': 4,    'pinyin': u'zài',              'type': 'verb',        'translation': 'to be present; to be at (a place)'},
    {'character': u'就  ', 'chapter': 6, 'id': 5,    'pinyin': u'jiù',              'type': 'adverb',     'translation': 'precisely; exactly'},
    {'character': u'您  ', 'chapter': 6, 'id': 6,    'pinyin': u'nín',              'type': 'pronoun',      'translation': 'you(honorific)'},
    {'character': u'那  ', 'chapter': 6, 'id':  7,   'pinyin': u'nā/něi',           'type': 'question pronoun',      'translation': 'which'},
    {'character': u'位  ', 'chapter': 6, 'id': 8,    'pinyin': u'wèi',              'type': 'measure word',        'translation': '(polite measure word for people)'},
    {'character': u'下午 ', 'chapter': 6, 'id': 9,    'pinyin': u'xiàwǔ',             'type': 'time word',        'translation': 'afternoon '},
    {'character': u'时间 ', 'chapter': 6, 'id': 10,    'pinyin': u'shíjiān',           'type': 'noun',        'translation': 'time  '},
    {'character': u'问题 ', 'chapter': 6, 'id': 11,   'pinyin': u'wèntí',             'type': 'noun',        'translation': 'question; problem'},
    {'character': u'要  ', 'chapter': 6, 'id': 12,     'pinyin': u'yāo',               'type': 'modal verb',      'translation': 'will, be going to; to want to, to have a desire to'},
    {'character': u'开会 ', 'chapter': 6, 'id': 13,    'pinyin': u'kāi huì',           'type': 'verb plus object',     'translation':  'to have a meeting '},
    {'character': u'开  ', 'chapter': 6, 'id': '13-alt',     'pinyin': u'kāi',               'type': 'verb',       'translation': 'to open; to hold (a meeting, party, etc.)'},
    {'character': u'会  ', 'chapter': 6, 'id': '13-alt2',     'pinyin': u'huì',               'type': 'noun',       'translation': 'meeting'},
    {'character': u'上午 ', 'chapter': 6, 'id': 14,    'pinyin': u'shàngwǔ',            'type': 'time word',       'translation': 'morning          '},
    {'character': u'节  ', 'chapter': 6, 'id': 15,   'pinyin': u'jiē',               'type': 'measure word',      'translation': '(measure word for class periods)'},
    {'character': u'棵  ', 'chapter': 6, 'id': 16,    'pinyin': u'kē',                'type': 'noun',      'translation': 'class; course; lesson'},
    {'character': u'年级 ', 'chapter': 6, 'id': 17,   'pinyin': u'niánjí',             'type': 'noun',      'translation': 'grade in school'},
    {'character': u'考试 ', 'chapter': 6, 'id': 18,   'pinyin': u'kǎo shì',            'type': 'verb plus object/noun',       'translation': 'to give or take a test; test '},
    {'character': u'考  ', 'chapter': 6, 'id': '18-alt',    'pinyin': u'kǎo',                'type': 'verb',      'translation': 'to give or take a test'},
    {'character': u'试  ', 'chapter': 6, 'id': '18-alt2',    'pinyin': u'shì',                'type': 'noun/verb',      'translation': 'test; to try; to experiment'},
    {'character': u'以后 ', 'chapter': 6, 'id': 19,   'pinyin': u'yǐhòu',              'type': 'time word',     'translation': 'after; from now on, later on '},
    {'character': u'空  ', 'chapter': 6, 'id': 20,     'pinyin': u'kòng(r)',            'type': 'noun',      'translation': 'free time'},
    {'character': u'要是 ', 'chapter': 6, 'id': 21,    'pinyin': u'yàoshi',             'type': 'conjunction',   'translation': 'if '},
    {'character': u'方便 ', 'chapter': 6, 'id': 22,    'pinyin': u'fāngbiàn',           'type': 'adjective',     'translation': 'convenient '},
    {'character': u'到  ', 'chapter': 6, 'id': 23,    'pinyin': u'dào',                'type': 'verb',      'translation': 'to go to; to arrive'},
    {'character': u'办公室', 'chapter': 6, 'id': 24,   'pinyin': u'bàngōngshì',          'type': 'noun',       'translation': 'office '},
    {'character': u'行  ', 'chapter': 6, 'id': 25,     'pinyin': u'xíng',               'type': 'verb',      'translation': 'all right; O.K.'},
    {'character': u'等  ', 'chapter': 6, 'id': 26,     'pinyin': u'děng',               'type': 'verb',      'translation': 'to wait; to wait for '},
    {'character': u'别  ', 'chapter': 6, 'id': 27,     'pinyin': u'bié',                'type': 'adverb',    'translation': 'dont'},
    {'character': u'客气 ', 'chapter': 6, 'id': 28,    'pinyin': u'kèqi',               'type': 'adjective',   'translation': 'polite '},
    {'character': u'常老师', 'chapter': 6, 'id': 29,   'pinyin': u'cháng lǎoshī',       'type': ' --',    'translation': 'Teacher Chang   '},

    # Page 162
    {'character': u'下个', 'chapter': 6,  'id': 1,    'pinyin': u'xià gè',        'type': '--',      'translation': 'next one '},
    {'character': u'下 ', 'chapter': 6, 'id': '1-alt',     'pinyin': u'xià',           'type': '--',     'translation': 'below; next'},
    {'character': u'中文', 'chapter': 6, 'id': 2,    'pinyin': u'zhōngwén',      'type': 'noun',        'translation': 'Chinese language'},
    {'character': u'文 ', 'chapter': 6, 'id': '2-alt',    'pinyin': u'wén',            'type': 'noun',       'translation': 'language; script; written language'},
    {'character': u'帮 ', 'chapter': 6, 'id': 3,    'pinyin': u'bāng',           'type': 'verb',     'translation': 'to help'},
    {'character': u'准备', 'chapter': 6, 'id': 4,    'pinyin': u'zhǔnbèi',        'type': 'verb',    'translation': ' to prepare'},
    {'character': u'练习', 'chapter': 6, 'id': 5,   'pinyin': u'liànxí',         'type': 'verb',    'translation': ' to practice'},
    {'character': u'说 ', 'chapter': 6, 'id': 6,    'pinyin': u'shuō',           'type': 'verb',     'translation': 'to say, to speak'},
    {'character': u'啊 ', 'chapter': 6, 'id': 7,    'pinyin': u'a',              'type': 'particle',     'translation': '(a sentence-final particle of exclamation, interrogation, etc.)'},
    {'character': u'但是', 'chapter': 6, 'id': 8,    'pinyin': u'dànshì',         'type': 'conjunction',    'translation': 'but '},
    {'character': u'得 ', 'chapter': 6, 'id': 9,    'pinyin': u'déi',            'type': 'adverb',     'translation': 'must; to have to '},
    {'character': u'跟 ', 'chapter': 6, 'id': 10,    'pinyin': u'gēn',            'type': 'prep',     'translation': 'with '},
    {'character': u'见面', 'chapter': 6, 'id': 11,    'pinyin': u'jiàn miàn',      'type': 'verb plus object',     'translation': ' to meetup; to meet with '},
    {'character': u'面 ', 'chapter': 6, 'id': '11-alt',    'pinyin': u'miàn',           'type': 'noun',     'translation': 'face '},
    {'character': u'回来', 'chapter': 6, 'id': 12,    'pinyin': u'huí lai',        'type': 'verb plus complement',     'translation': 'to come back'},
]

parser = argparse.ArgumentParser(description='Select a chapter.')
parser.add_argument('-o', '--chapter', help='Select a particular chapter')
args = parser.parse_args()
if args.chapter == '1':
    choice = random.randint(0, len(Chapter1) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(Chapter1[choice]['chapter'])
    print 'Vocabulary ID: ' + str(Chapter1[choice]['id'])
    print 'Characters:    ' + Chapter1[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + Chapter1[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + Chapter1[choice]['type']
    print 'Translation:   ' + Chapter1[choice]['translation']
elif args.chapter == '2':
    choice = random.randint(0, len(Chapter2) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(Chapter2[choice]['chapter'])
    print 'Vocabulary ID: ' + str(Chapter2[choice]['id'])
    print 'Characters:    ' + Chapter2[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + Chapter2[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + Chapter2[choice]['type']
    print 'Translation:   ' + Chapter2[choice]['translation']
elif args.chapter == '3':
    choice = random.randint(0, len(Chapter3) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(Chapter3[choice]['chapter'])
    print 'Vocabulary ID: ' + str(Chapter3[choice]['id'])
    print 'Characters:    ' + Chapter3[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + Chapter3[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + Chapter3[choice]['type']
    print 'Translation:   ' + Chapter3[choice]['translation']
elif args.chapter == '4':
    choice = random.randint(0, len(Chapter4) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(Chapter4[choice]['chapter'])
    print 'Vocabulary ID: ' + str(Chapter4[choice]['id'])
    print 'Characters:    ' + Chapter4[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + Chapter4[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + Chapter4[choice]['type']
    print 'Translation:   ' + Chapter4[choice]['translation']
elif args.chapter == '5':
    choice = random.randint(0, len(Chapter5) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(Chapter5[choice]['chapter'])
    print 'Vocabulary ID: ' + str(Chapter5[choice]['id'])
    print 'Characters:    ' + Chapter5[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + Chapter5[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + Chapter5[choice]['type']
    print 'Translation:   ' + Chapter5[choice]['translation']
elif args.chapter == '6':
    choice = random.randint(0, len(Chapter6) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(Chapter6[choice]['chapter'])
    print 'Vocabulary ID: ' + str(Chapter6[choice]['id'])
    print 'Characters:    ' + Chapter6[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + Chapter6[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + Chapter6[choice]['type']
    print 'Translation:   ' + Chapter6[choice]['translation']
else:
    choice = random.randint(0,len(words) - 1)
    print '-'*40
    print '   Integrated Chinese Word of the Day'
    print '-'*40
    print 'Chapter:       ' + str(words[choice]['chapter'])
    print 'Vocabulary ID: ' + str(words[choice]['id'])
    print 'Characters:    ' + words[choice]['character'].encode('utf-8')
    print 'Pinyin:        ' + words[choice]['pinyin'].encode('utf-8')
    print 'Type:          ' + words[choice]['type']
    print 'Translation:   ' + words[choice]['translation']





