/*
* Model Resources
* */
export const COLLISION_SCENE_URL = new URL("./assets/models/scene_collision.glb", import.meta.url).href;
export const STATIC_SCENE_URL = new URL("./assets/models/scene_desk_obj.glb", import.meta.url).href;

/*
* Texture Resources
* */
export const BOARD_TEXTURES = [
	new URL("./assets/boards/1.png", import.meta.url).href,
	new URL("./assets/boards/2.png", import.meta.url).href,
	new URL("./assets/boards/3.jpg", import.meta.url).href,
	new URL("./assets/boards/4.jpg", import.meta.url).href,
	new URL("./assets/boards/5.png", import.meta.url).href,
	new URL("./assets/boards/6.png", import.meta.url).href,
	new URL("./assets/boards/7.png", import.meta.url).href,
	new URL("./assets/boards/8.jpg", import.meta.url).href,
	new URL("./assets/boards/9.jpg", import.meta.url).href,
	new URL("./assets/boards/10.png", import.meta.url).href
];

/*
* Audio Resources
* */
export const AUDIO_URL = new URL("./assets/audio/747682917.mp3", import.meta.url).href;

/*
* Intro
* */
export const BOARDS_INFO: Record<string, {title: string, author: string, describe: string}> = {
	1: {
	title: "《荷韵清风》",
	author: "雅如",
	describe: `
		这幅作品运用了中国传统工笔重彩画技艺，细腻展现了盛开的荷花与翠绿的荷叶，出自“姑苏工笔画”非遗绘画流派。<br>
		画面清逸淡雅，花瓣层层叠叠，细节之处尽显匠心，仿佛能感受到荷塘深处微风掠过的轻盈。<br>
		它不仅是自然美的写照，更蕴含了“出淤泥而不染”的高洁品格。<br>
		观者仿佛漫步于晨雾缭绕的湖边，心灵随画境沉静，诗意流淌。
	`
},
2: {
	title: "《松鹤长春》",
	author: "仲山",
	describe: `
		此作品采用“湘绣”工艺创作，以丝线刺绣出松树与丹顶鹤，象征长寿与吉祥，是湖南省传统刺绣非遗代表之一。<br>
		精致的羽毛纹理与层叠的松针在深色背景中愈发鲜明，呈现出立体光泽感。<br>
		群鹤神态各异，优雅灵动，寓意岁岁长春、吉庆安康。<br>
		刺绣技艺之精美与文化内涵之深厚，在这一幅中得以完美结合。
	`
},
3: {
	title: "《山居图》",
	author: "李溪",
	describe: `
		这幅画展现了“苗族蜡染”元素与山水田园结合的表现形式，以点彩法描绘层峦叠嶂与农耕田园，源自贵州苗族的非遗技艺演变。<br>
		金黄梯田与翠绿植被交错排列，小村掩映其中，透露出乡野宁静之美。<br>
		画中女子在田间劳作，展现人与自然和谐共生的生活图景。<br>
		作品质朴真实，却又富有诗意，是民族文化与田园意象的交融之作。
	`
},
4: {
	title: "《幽兰寄香》",
	author: "林墨",
	describe: `
		此作为“扬州漆艺画”中的工笔兰花卷，融合细致笔触与天然矿物色，展现文人四君子之一——兰。<br>
		兰花姿态婀娜、色调清雅，寓意高洁隐逸、坚韧不拔。<br>
		淡雅的底色与柔韧的叶片相得益彰，流露出静穆之美。<br>
		兰花在画中仿佛诉说着一段清风明月的故事，是修身养性的文化象征。
	`
},
5: {
	title: "《水影花魂》",
	author: "若溪",
	describe: `
		该作运用了“苏绣”技艺，以丝绸刺绣再现一朵凋零中的莲花，水雾氤氲，光影细腻，是非遗中的艺术瑰宝。<br>
		花瓣半开，花蕊孤立，象征生命的短暂与残美。<br>
		水波微动，仿佛梦境与现实交融，展现出中国传统艺术中“留白”之妙。<br>
		这幅作品静谧而动人，令人沉思于生命的脆弱与自然的永恒。
	`
},
6: {
	title: "《影戏千秋》",
	author: "墨衡",
	describe: `
		本图是对“皮影戏”艺术的致敬，展现了中国传统剪纸皮影的头面、身体与道具组合，体现陕西皮影的非遗魅力。<br>
		精美的雕花与色彩丰富的装饰构建了一个戏剧化的舞台空间。<br>
		皮影人物线条流畅、色彩浓烈，兼具装饰性与叙事性。<br>
		这不仅是视觉艺术，更是流传千年的口传心授与舞台记忆的再现。
	`
},
7: {
	title: "《金峰暮照》",
	author: "尹岳",
	describe: `
		此作源自“羌绣山水画”风格，以细密针法与彩线融合绘画形式，展现一幅金山夕照的奇观景象，传承自四川羌族刺绣技艺。<br>
		黄昏中的山峦与溪水交映生辉，云霞染金，如梦似幻。<br>
		画面结构稳重，色彩层次分明，呈现出自然雄伟与灵动兼具的格局。<br>
		作品既是自然景观的写照，也是民族心灵的映照。
	`
},

	8: {
		title: "《向日葵》",
		author: "小雅",
		describe: `
		阳光照耀，金黄的花盘。<br>
		宛如一盏明灯，指引前行。<br>
		向日葵，你是信仰，你是力量，你是光辉，你是坚毅，你是忠诚，你是爱慕，你是美丽。
		`
	},
	9: {
		title: "《花·虎·蝶》",
		author: "小雅",
		describe: `
		一段奇妙的相遇，是自由和勇气的结合，是一份神秘而又动人的韵味。<br>
		在这片色彩斑斓的花海之中，一只带着蝴蝶翅膀的老虎，骑着踏板车，<br>
		它像是一道闪电，划破了这片美好的天地。<br>
		翅膀轻轻地振动，仿佛随时可以飞离这片美好的天地，飞向更广阔的天空。
		`
	},
	10: {
		title: "《豚》",
		author: "小雅",
		describe: `
		所有的转折隐藏在密集的鸟群中，天空与海洋都无法察觉，怀着美梦却可以看见。<br>
		摸索颠倒的一瞬间，所有的怀念隐藏在相似的日子里，心里的蜘蛛模仿人类张灯结彩
		`
	}
};

/*
* Computer Iframe SRC
* */
export const IFRAME_SRC = new URL("/universe/index.html", import.meta.url).href;

/*
* Events
* */
export const ON_LOAD_PROGRESS = "on-load-progress";
export const ON_LOAD_MODEL_FINISH = "on-load-model-finish";
export const ON_CLICK_RAY_CAST = "on-click-ray-cast";
export const ON_SHOW_TOOLTIP = "on-show-tooltip";
export const ON_HIDE_TOOLTIP = "on-hide-tooltip";
export const ON_KEY_DOWN = "on-key-down";
export const ON_KEY_UP = "on-key-up";
export const ON_ENTER_APP = "on-enter-app";
