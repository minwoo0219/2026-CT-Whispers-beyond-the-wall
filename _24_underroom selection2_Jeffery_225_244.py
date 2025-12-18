import pygame
import sys

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 225~244 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
EPILOGUE_COLOR = (0, 60, 140)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 120)
TEXT_SPEED = 2  # 타자기 속도

# ------------------------------------------------------
# 타자기 상태
# ------------------------------------------------------
current_text = ""
full_text = ""
text_index = 0
typing_done = False
displayed_text = ""


def start_typing(lines):
    """타자기 텍스트 초기화"""
    global full_text, current_text, text_index, typing_done, displayed_text
    full_text = "\n".join(lines)
    current_text = ""
    displayed_text = ""
    text_index = 0
    typing_done = False


def update_typing():
    """한 글자씩 출력"""
    global current_text, text_index, typing_done, displayed_text

    if typing_done:
        return

    for _ in range(TEXT_SPEED):
        if text_index < len(full_text):
            current_text += full_text[text_index]
            text_index += 1
        else:
            typing_done = True
            break

    displayed_text = current_text


# ------------------------------------------------------
# 대사 출력 (채팅창) - 전체적으로 조금 위
# ------------------------------------------------------
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 170  # 살짝 위로
    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, TEXT_COLOR)
        SCREEN.blit(txt, (x, y + i * 32))


# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
william_bg = pygame.transform.scale(
    pygame.image.load("william_underway.png").convert(), (WIDTH, HEIGHT)
)

jeffrey_bg = pygame.transform.scale(
    pygame.image.load("Jeffrey_underway.png").convert(), (WIDTH, HEIGHT)
)

castle_outside = pygame.transform.scale(
    pygame.image.load("castle_outside.png").convert(), (WIDTH, HEIGHT)
)

castle_outside2 = pygame.transform.scale(
    pygame.image.load("castle_outside2.png").convert(), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)

# ------------------------------------------------------
# 캐릭터 이미지
# ------------------------------------------------------
# 엘레노어
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELEN_HEIGHT = 620
ratio_e = ELEN_HEIGHT / elen_raw.get_height()
ELEN_WIDTH = int(elen_raw.get_width() * ratio_e)
elen_img = pygame.transform.scale(elen_raw, (ELEN_WIDTH, ELEN_HEIGHT))
ELEN_POS = (-200, HEIGHT - ELEN_HEIGHT)

# 제프리
jeff_raw = pygame.image.load("Jeffrey.png").convert_alpha()
JEFF_HEIGHT = 650
ratio_j = JEFF_HEIGHT / jeff_raw.get_height()
JEFF_WIDTH = int(jeff_raw.get_width() * ratio_j)
jeff_img = pygame.transform.scale(jeff_raw, (JEFF_WIDTH, JEFF_HEIGHT))
JEFF_POS = (-200, HEIGHT - JEFF_HEIGHT)

# 어떤 씬에 캐릭터를 띄울지
ELEN_SCENES = {225, 227, 232}
JEFF_SCENES = {229, 234, 235, 238}

# ------------------------------------------------------
# 대사 (길면 2~3줄로 분리)
# ------------------------------------------------------
dialogues = {
    225: [
        "“하... 아무리 생각해도 제프리는",
        "거짓말하지 않는 것 같아.”",
    ],
    226: [
        "나는 그렇게 제프리의 뒤에 서서 걸음을 옮겼다.",
        "통로 끝에서 무언가 이상한 형체가 희미하게 보였다.",
    ],
    227: [
        "“저기... 무언가가 있어요.",
        "윌리엄의 목소리를 가진 존재.. 너무 이상해요.”",
    ],
    228: [
        "그는 잠시 눈을 감았다가 떴다.",
        "그의 표정은 평소처럼 무심하지만, 눈 끝이 날카롭게 빛났다.",
    ],
    229: [
        "“...알고 있었다.. 성벽 너머의 속삭임,",
        "그 존재는 너를 증오하는 자고 목소리를 흉내 낼 수 있다.",
        "당신이 아는 윌리엄 목소리도, 그 존재가 흉내낸 것 뿐이다.”",
    ],
    230: [
        "나는 안도의 한숨을 내쉬었다.",
        "아직 위험은 남아있지만, 정체를 알고 있다는 사실만으로",
        "마음이 조금 놓였다.",
    ],
    231: [
        "엘리노어는 제프리에게 조심스럽게 말했다.",
    ],
    232: [
        "“제프리... 제발, 제가 안전하게",
        "나갈 수 있도록 도와줘요.”",
    ],
    233: [
        "제프리는 나를 잠시 바라보다가",
        "무심하게 고개를 끄덕였다.",
    ],
    234: [
        "“좋다. 하지만 내가 말하는 길을 따라 가야 한다.”",
    ],
    235: [
        "“조금이라도 벗어난다면, 그 존재에 잡힐 것이다.”",
    ],
    236: [
        "그는 석조 벽을 따라 통로를 안내하며 숨겨진 비밀 문을 열어준다.",
        "작은 열쇠와 기계 장치 덕분에 지하실 깊은 곳으로",
        "안전하게 이동할 수 있는 길이 열렸다.",
    ],
    237: [
        "드디어 성에서 나왔다.",
        "나는 긴장 속에서도 제프리의 안내를 따라",
        "조심스럽게 발걸음을 옮겼다.",
    ],
    238: [
        "“저 길 끝에는 오래된 출구가 있어.",
        "하지만 성 벽을 넘어야 한다.",
        "속삭임이 따라올 수 있으니 끝까지 긴장을 늦추지 마라.”",
    ],
    239: [
        "나는 고개를 끄덕였다.",
        "조금씩 안도의 숨이 나왔다.",
    ],
    240: [
        "나는 그렇게, 문을 나와 낮은 성벽과 마주했다.",
        "다행히 성벽은 조금만 발을 딛고 올라가면",
        "바깥으로 통할 수 있었다.",
    ],
    241: [
        "이 성을 탈출한 직후 보이는 성의 모습은",
        "내가 겪은 상황과는 대조되게 고요하고 평온했다.",
        "하지만 나는 한참 길을 이동한 뒤에야 비로소 안심할 수 있었다.",
    ],
}

# 242는 흰 배경 위 에필로그 문장 (채팅창 X)
epilogue_242 = [
    "당신은 그렇게, 성을 몰래 빠져나와 윌리엄을 만날 수 있게 되었다.",
    "나중에 들리는 소문으론 국왕은 당신이 나간 직후부터",
    "시름시름 앓다가 원인 모를 병에 걸려 죽어버렸다고 한다.",
    "이후 제프리는 나라의 왕 자리를 물려 받았다.",
    "당신은 더 이상 성 내부의 상황은 듣고 싶지 않았다.",
    "그저 윌리엄과 평화로운 나날들을 보내는 것에 집중했을 뿐...",
    "이제 난 행복했다.",
]

typing_scenes = set(dialogues.keys())  # 225~241만 타자기 효과

# ------------------------------------------------------
# 씬 관리
# ------------------------------------------------------
scene = 225
start_typing(dialogues[225])


# ------------------------------------------------------
# 장면 렌더링
# ------------------------------------------------------
def draw_scene():
    global scene

    # 225~230 : 윌리엄 통로 배경
    if 225 <= scene <= 230:
        SCREEN.blit(william_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        if scene in ELEN_SCENES:
            SCREEN.blit(elen_img, ELEN_POS)
        if scene in JEFF_SCENES:
            SCREEN.blit(jeff_img, JEFF_POS)
        draw_dialogue_line()

    # 231~236 : 제프리 통로 배경
    elif 231 <= scene <= 236:
        SCREEN.blit(jeffrey_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        if scene in ELEN_SCENES:
            SCREEN.blit(elen_img, ELEN_POS)
        if scene in JEFF_SCENES:
            SCREEN.blit(jeff_img, JEFF_POS)
        draw_dialogue_line()

    # 237~240 : 성 외곽 (castle_outside)
    elif 237 <= scene <= 240:
        if scene in (237, 238, 239, 240):
            SCREEN.blit(castle_outside, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    # 241 : castle_outside2
    elif scene == 241:
        SCREEN.blit(castle_outside2, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    # 242 : 흰 배경, 에필로그 텍스트
    elif scene == 242:
        SCREEN.fill(WHITE)
        start_y = 150
        for i, line in enumerate(epilogue_242):
            t = FONT.render(line, True, EPILOGUE_COLOR)
            x = (WIDTH - t.get_width()) // 2
            y = start_y + i * 32
            SCREEN.blit(t, (x, y))

    # 243 : 흰 배경만 (잠깐 쉬는 장면)
    elif scene == 243:
        SCREEN.fill(WHITE)

    # 244 : THE END 화면
    elif scene == 244:
        SCREEN.fill(WHITE)
        t = BIG_FONT.render("THE END...", True, BLACK)
        x = (WIDTH - t.get_width()) // 2
        y = (HEIGHT - t.get_height()) // 2
        SCREEN.blit(t, (x, y))


# ------------------------------------------------------
# 입력 처리
# ------------------------------------------------------
def handle_input():
    global scene

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 다음 씬으로 진행
            if scene < 244:
                scene += 1
                if scene in dialogues:
                    start_typing(dialogues[scene])


# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    if scene in typing_scenes:
        update_typing()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
