import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 204~216 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2


# -----------------------------------
# 타자기 상태
# -----------------------------------
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


# -----------------------------------
# 대사 출력
# -----------------------------------
def draw_dialogue():
    x = 380
    y = HEIGHT - 150
    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, WHITE)
        SCREEN.blit(surf, (x, y + i * 32))


# -----------------------------------
# 선택지 텍스트 출력
# -----------------------------------
def draw_select_text(rect, text):
    # 여러 줄 지원
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        txt = FONT.render(ln, True, BLACK)
        txtr = txt.get_rect(center=(rect.centerx, rect.centery + i * 18))
        SCREEN.blit(txt, txtr)


# -----------------------------------
# 이미지 로드
# -----------------------------------
bg_william = pygame.transform.scale(
    pygame.image.load("william_underway.png"), (WIDTH, HEIGHT)
)

bg_under = pygame.transform.scale(
    pygame.image.load("underroom_underway.png"), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (380, 110)
)

# 선택창 위치
choice_left = select_box.get_rect(center=(450, 520))
choice_right = select_box.get_rect(center=(830, 520))

# 캐릭터 이미지
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 600
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
elenore_img = pygame.transform.scale(
    elenore_raw, (int(elenore_raw.get_width() * ratio), ELENORE_HEIGHT)
)
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

jeff_raw = pygame.image.load("Jeffrey.png").convert_alpha()
JEFF_HEIGHT = 580
ratio2 = JEFF_HEIGHT / jeff_raw.get_height()
jeff_img = pygame.transform.scale(
    jeff_raw, (int(jeff_raw.get_width() * ratio2), JEFF_HEIGHT)
)
JEFF_POS = (50, HEIGHT - JEFF_HEIGHT)


# -----------------------------------
# 대사
# -----------------------------------
dialogues = {
    204: [
        "나는 제프리의 경고를 무시하고, 윌리엄의 목소리를 따라가기로 결정했다.",
        "그 목소리는 너무 익숙하고 따듯해, 정말 그가 손을 내밀고 있을 것 같았다.",
    ],
    205: [
        "하지만 이 선택이 위험하다는 것도 알고 있었다.",
        "난 조심스레 목소리가 올라온 방향으로 걸어갔다.",
    ],
    206: [
        "나는 이미 지하실 깊은 통로로 들어서 있었다.",
        "차갑고 축축한 공기가 피부에 달라붙고 촛불은 위태롭게 흔들렸다.",
    ],
    207: [
        "그때- 앞쪽에서 아주 선명한 남자의 목소리가 들려왔다.",
    ],
    208: [
        "???: “엘리노어... 그래, 잘 왔어! 나야, 정말 나야...!”",
    ],
    209: [
        "너무 익숙한 목소리, 하지만 뭔가 이상했다.",
        "웃음과 어조는 같았지만...",
    ],
    210: [
        "통로 깊숙한 곳에서 형체가 손을 내밀고 있었다.",
        "하지만 어둠 속이라 얼굴은 잘 보이지 않았다.",
    ],
    211: [
        "???: “왜 겁내? 나야 엘리노어, 드디어 우리 둘이 만났잖아.”",
    ],
    212: [
        "뒤에서 제프리가 날 향해 소리쳤다.",
    ],
    213: [
        "“그건 살아있는 것이 아닙니다! 돌아오시오!”",
    ],
    214: [
        "하지만 그 존재는 부드럽게 웃으며 속삭였다.",
    ],
    215: [
        "???: “널 한참 동안 찾아 헤맸지... 드디어 찾았네.”",
    ],
}


typing_scenes = set(dialogues.keys())

scene = 204
start_typing(dialogues[204])


# -----------------------------------
# 장면 그리기
# -----------------------------------
def draw_scene():
    # 204~205 : william_underway
    if scene in (204, 205):
        SCREEN.blit(bg_william, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue()

    # 206~215 : underroom_underway
    elif 206 <= scene <= 215:
        SCREEN.blit(bg_under, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue()

        # 등장 캐릭터 처리
        if scene in (212, 213):
            SCREEN.blit(jeff_img, JEFF_POS)

    # 216 : 선택지
    elif scene == 216:
        SCREEN.blit(bg_under, (0, 0))

        SCREEN.blit(select_box, choice_left)
        SCREEN.blit(select_box, choice_right)

        draw_select_text(choice_left, "형체에게 다가가\n얼굴을 확인한다")
        draw_select_text(choice_right, "뒤로 돌아\n제프리 쪽으로 간다")


# -----------------------------------
# 입력 처리
# -----------------------------------
def handle_input():
    global scene

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if scene in dialogues:
                scene += 1
                if scene in dialogues:
                    start_typing(dialogues[scene])
            elif scene == 215:
                scene = 216
            elif scene == 216:
                pass


# -----------------------------------
# 메인 루프
# -----------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    if scene in typing_scenes:
        update_typing()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
