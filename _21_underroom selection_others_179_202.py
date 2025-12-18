import pygame
import sys
import textwrap

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 179~202 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2

# ------------------------------------------------------
# 자동 줄바꿈 (최대 3줄)
# ------------------------------------------------------
def wrap_text(text, width=46, max_lines=3):
    wrapped = textwrap.wrap(text, width)
    if len(wrapped) > max_lines:
        wrapped = wrapped[:max_lines]
    return wrapped

# ------------------------------------------------------
# 타자기 상태
# ------------------------------------------------------
current_text = ""
full_text = ""
text_index = 0
typing_done = False
displayed_text = ""

def start_typing(lines):
    """타자기 텍스트 초기화 — 자동 줄바꿈 포함"""
    global full_text, current_text, text_index, typing_done, displayed_text
    wrapped = []
    for line in lines:
        wrapped.extend(wrap_text(line))  # 3줄 제한 자동 적용
    full_text = "\n".join(wrapped)
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
# 대사 출력
# ------------------------------------------------------
def draw_dialogue_line():
    x = 360
    y = HEIGHT - 160  # 전체적으로 조금 올림
    lines = displayed_text.split("\n")[:3]  # 안전하게 최대 3줄
    for i, line in enumerate(lines):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))

# ------------------------------------------------------
# 선택창 텍스트 출력
# ------------------------------------------------------
def draw_select_text(rect, text):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        t = FONT.render(line, True, BLACK)
        SCREEN.blit(t, (
            rect.centerx - t.get_width() // 2,
            rect.centery - len(lines) * 14 + i * 32
        ))

# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
underground_bg = pygame.transform.scale(
    pygame.image.load("underground_room.png").convert(), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (380, 130)
)

# 선택창 간격 넓힘 (좌우 520px 간격)
choice_left = select_box.get_rect(center=(380, 520))
choice_right = select_box.get_rect(center=(900, 520))

# ------------------------------------------------------
# 캐릭터 이미지
# ------------------------------------------------------
# 엘리노어
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELEN_H = 620
ratio_e = ELEN_H / elen_raw.get_height()
ELEN_W = int(elen_raw.get_width() * ratio_e)
elen_img = pygame.transform.scale(elen_raw, (ELEN_W, ELEN_H))
ELEN_POS = (-200, HEIGHT - ELEN_H)

# 제프리
jeff_raw = pygame.image.load("Jeffrey.png").convert_alpha()
JEFF_H = 620
ratio_j = JEFF_H / jeff_raw.get_height()
JEFF_W = int(jeff_raw.get_width() * ratio_j)
jeff_img = pygame.transform.scale(jeff_raw, (JEFF_W, JEFF_H))
JEFF_POS = (-180, HEIGHT - JEFF_H)

# ------------------------------------------------------
# 대사
# ------------------------------------------------------
dialogues = {
    179: ["“난, 당신의 정략결혼 상대인 제프리라고 한다. 그러니 너무 겁내지 마시오.”"],
    180: [
        "돌바닥이 차갑게 발끝을 스치고, 촛불이 흔들리며 그의 얼굴을 비췄다.",
        "그의 표정은 무심했지만, 입가가 엷게 일그러져 있었다.",
        "그리고 잠깐 떨린 눈동자가... 무언가를 숨기고 있었다."
    ],
    181: ["그는 나의 뒷걸음질을 눈치채곤 말했다."],
    182: ["“난..그저 왕이 오기 전에 그대를 내보내려고 했다.”"],
    183: ["목소리는 낮아졌고, 다음 말은 더 이상한 방향으로 흘렀다."],
    184: ["“그대가..윌리엄의 목소리를 무시하고 계단을 택할 줄 알고 있었다.”"],
    185: ["나는 순간 심장이 철렁 내려앉았다. 그는 그 ‘존재’의 목소리를 알고 있다."],
    186: ["그는 한 발 앞으로 내딛었고, 설명할 수 없는 긴장감이 따라왔다."],
    187: ["나는 촛불을 꽉 쥔다. 그리고 그에게 말했다."],
    188: [
        "“책상 위 태그도, 생김새도.. 당신이 바로 제프리였군요?",
        "제 약혼자이자 제가 이 성에 감금된 원인.”"
    ],
    189: ["...."],
    190: [
        "하지만 그의 정체보다 방금 그가 한 말을 넘길 수 없었다.",
        "나는 낮은 목소리로 물었다."
    ],
    191: ["“그 목소리.. 당신은 알고 있었죠? 그게 뭐였는지.”"],
    192: [
        "제프리는 말이 없었다. 공기가 차갑게 내려앉았다.",
        "그는 바닥을 보다 고개를 들어 작은 목소리로 말했다."
    ],
    193: ["“그건... 왕의 성이 품고 있는 또 다른 주인입니다.”"],
    194: ["나는 목덜미가 서늘해졌다. 제프리는 말을 이어갔다."],
    195: ["“그 존재는 당신을 끌어들이기 위해 윌리엄의 목소리를 흉내 낸 것입니다.”"],
    196: ["표정은 담담했지만, 그의 목소리는 떨리고 있었다."],
    197: [
        "“그 존재는 오래전부터 당신을 알고 있었소.",
        "당신 아버지를 협박하기 위한 목적이지요.”"
    ],
    198: ["지하실 어둠 속에서 또렷한 윌리엄의 목소리가 울렸다."],
    199: [
        "???: “엘리노어... 그 자와 있지 마!",
        "속으면 안돼! 다시 내게 와!”"
    ],
    200: ["제프리는 즉시 이를 악물고 외쳤다."],
    201: ["“듣지 마시오! 그건 윌리엄이 아닙니다!”"],
}

typing_scenes = set(dialogues.keys())

# 캐릭터 등장 구간
jeff_scenes = {179, 182, 184, 193, 195, 197}
elen_scenes = {187, 188, 191}

# 선택지 (202)
choice_texts = [
    "윌리엄을 믿고\n그의 목소리를 따라간다.",
    "제프리를 믿고 그의 뒤로 서며\n지하실 다른 출구로 향한다."
]

# ------------------------------------------------------
# 씬 관리
# ------------------------------------------------------
scene = 179
start_typing(dialogues[179])

# ------------------------------------------------------
# 장면 렌더링
# ------------------------------------------------------
def draw_scene():

    if scene <= 201:
        SCREEN.blit(underground_bg, (0, 0))

    if scene in jeff_scenes:
        SCREEN.blit(jeff_img, JEFF_POS)
    if scene in elen_scenes:
        SCREEN.blit(elen_img, ELEN_POS)

    if scene <= 201:
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    if scene == 202:
        SCREEN.fill(BLACK)
        SCREEN.blit(select_box, choice_left)
        SCREEN.blit(select_box, choice_right)

        draw_select_text(choice_left, choice_texts[0])
        draw_select_text(choice_right, choice_texts[1])

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

            if scene < 201:
                scene += 1
                if scene in dialogues:
                    start_typing(dialogues[scene])

            elif scene == 201:
                scene = 202  # 선택창 등장

            elif scene == 202:
                pass  # 기능 없음

# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    if scene in typing_scenes:
        update_typing()

    draw_scene()
    pygame.display.flip()
