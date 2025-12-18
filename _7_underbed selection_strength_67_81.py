import pygame
import sys

pygame.init()

# ------------------------------------------------
# 기본 설정
# ------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EVENT 67~81 FINAL PATCH")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (220,40,40)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 36)

TEXT_SPEED = 2


def load_bg(path):  
    return pygame.transform.scale(
        pygame.image.load(path).convert_alpha(), (WIDTH, HEIGHT)
    )


def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if font.size(test)[0] <= max_width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------
# 이미지 로드
# ------------------------------------------------
underbed_bg      = load_bg("underbed.png")
hall1_bg         = load_bg("enjail_background1.png")   # 71~73용
hall2_bg         = load_bg("enjail_background2.png")   # 74~75용
door_bg          = load_bg("king's place.png")         # 77~78용
sleeping_bg      = load_bg("sleeping king.png")        # 79~81용

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (1280, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (400, 120)
)

select75_rect = select_box.get_rect(center=(WIDTH//2, 540))
select81_left  = select_box.get_rect(center=(WIDTH//2 - 220, 540))
select81_right = select_box.get_rect(center=(WIDTH//2 + 220, 540))


def draw_select_text(rect, text, color=BLACK):
    lines = text.split("\n")
    total = len(lines) * 32
    start_y = rect.centery - total // 2
    for i, line in enumerate(lines):
        surf = FONT.render(line, True, color)
        SCREEN.blit(surf, (rect.centerx - surf.get_width()//2,
                           start_y + i*32))


# ------------------------------------------------
# 엘리노어 (공식 그대로 유지)
# ------------------------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elen_raw.get_height()
ELENORE_WIDTH = int(elen_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elen_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# ------------------------------------------------
# 타자기 상태
# ------------------------------------------------
current_text = ""
displayed_text = ""
text_index = 0
typing_active = False


def start_typing(lines):
    global current_text, displayed_text, text_index, typing_active
    current_text = "\n".join(lines)
    displayed_text = ""
    text_index = 0
    typing_active = True


def update_typing():
    global displayed_text, text_index, typing_active

    if not typing_active:
        return
    for _ in range(TEXT_SPEED):
        if text_index < len(current_text):
            displayed_text += current_text[text_index]
            text_index += 1
        else:
            typing_active = False
            break


def skip_typing():
    global displayed_text, text_index, typing_active
    typing_active = False
    displayed_text = current_text
    text_index = len(current_text)


# ------------------------------------------------
# 대사
# ------------------------------------------------
dialogues = {
    67: ["으... 으... 너무 무거워..!"],
    68: ["??? (돌 판이 부러지는 소리)"],

    70: [
        "당신은 돌 판을 들어 올리려 했지만 결국 부러지고 말았다.",
        "그 돌 판은 왕의 감시를 피할 수 있는 유일한 루트였고, 결국 당신은 윌리엄을 만나지 못한 채",
        "정략결혼을 하게 된다. 그리고 갇혀 살다 정신이 서서히 무너져 갔다."
    ],

    71: [],   # 요청: 텍스트 없음

    72: ["너무 원망스러워.."],

    # 73 — 고정 패턴용
    73: ["너무 원망스러워"],

    # 74 — 요청: 3줄 대사
    74: [
        "“이렇게 할 수 밖에 없어요… 이렇게 해야만 이제 윌리엄과 전 함께 할 수 있잖아요.”",
        "“아닐 수도 있지만… 전 정말 이렇게 하지 않고는 버틸 수가 없는걸요.”",
        "“누가 뭐래도… 전 이렇게 할 수밖에 없어요.”"
    ],

    75: ["문 열기"],

    77: [
        "근위병1: 엘리노어님, 여기는 무슨 일로 오셨습니까?",
        "죄송하지만 왕의 침전에 마음대로 들어가실 수는 없습니다."
    ],

    78: ["“아, 잠깐 볼 일이 있어서요.”"],

    80: ["“어쩜 이리도 잘 주무시는지 참...”"],

    81: ["찌르기", "안 찌르기"],
}

typing_scenes = {67,68,70,72,74,77,78,80}


def draw_chat_text(color=WHITE):
    x = 380
    y = HEIGHT - 140
    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, color)
        SCREEN.blit(surf, (x, y + i*32))


# ------------------------------------------------
# 장면 그리기
# ------------------------------------------------
def draw_scene():
    global scene

    # ---------------- 67~68 ----------------
    if scene in (67,68):
        SCREEN.blit(underbed_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))
        draw_chat_text(WHITE)

    # ---------------- 69 ----------------
    elif scene == 69:
        SCREEN.fill(BLACK)

    # ---------------- 70 ----------------
    elif scene == 70:
        SCREEN.fill(BLACK)
        y = 200
        for i, line in enumerate(dialogues[70]):
            txt = FONT.render(line, True, RED)
            SCREEN.blit(txt, ((WIDTH - txt.get_width())//2, y + i*38))

    # ---------------- 71 ----------------
    elif scene == 71:
        SCREEN.blit(hall1_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        # 요청: 텍스트 없음

    # ---------------- 72 ----------------
    elif scene == 72:
        SCREEN.blit(hall1_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_chat_text(RED)

    # ---------------- 73 — 원망 퍼진 패턴 ----------------
    elif scene == 73:
        SCREEN.blit(hall1_bg, (0,0))

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,210))
        SCREEN.blit(dark, (0,0))

        word = "너무 원망스러워"
        spacing_x = 200
        spacing_y = 50
        start_x = -100
        start_y = -120

        for row in range(12):
            for col in range(12):
                txt = FONT.render(word, True, RED)
                SCREEN.blit(txt, (
                    start_x + col*spacing_x,
                    start_y + row*spacing_y
                ))

    # ---------------- 74 ----------------
    elif scene == 74:
        SCREEN.blit(hall2_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))
        SCREEN.blit(elenore_img, ELENORE_POS)

        y = HEIGHT - 150
        for i,line in enumerate(dialogues[74]):
            txt = FONT.render(line, True, RED)
            SCREEN.blit(txt, (380, y + i*32))

    # ---------------- 75 ----------------
    elif scene == 75:
        SCREEN.blit(hall2_bg, (0,0))

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,150))
        SCREEN.blit(dark, (0,0))

        SCREEN.blit(select_box, select75_rect)
        draw_select_text(select75_rect, "문 열기")

    # ---------------- 76 ----------------
    elif scene == 76:
        SCREEN.fill(BLACK)

    # ---------------- 77 ----------------
    elif scene == 77:
        SCREEN.blit(door_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))

        y = HEIGHT - 150
        for i,line in enumerate(dialogues[77]):
            txt = FONT.render(line, True, WHITE)
            SCREEN.blit(txt, (380, y + i*32))

    # ---------------- 78 ----------------
    elif scene == 78:
        SCREEN.blit(door_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_chat_text(RED)

    # ---------------- 79 ----------------
    elif scene == 79:
        SCREEN.blit(sleeping_bg, (0,0))

    # ---------------- 80 ----------------
    elif scene == 80:
        SCREEN.blit(sleeping_bg, (0,0))
        SCREEN.blit(chatbox, (0,HEIGHT-200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_chat_text(RED)

    # ---------------- 81 ----------------
    elif scene == 81:
        SCREEN.blit(sleeping_bg, (0,0))
        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,160))
        SCREEN.blit(dark, (0,0))

        SCREEN.blit(select_box, select81_left)
        SCREEN.blit(select_box, select81_right)

        draw_select_text(select81_left, "찌르기", RED)
        draw_select_text(select81_right, "안 찌르기", RED)


# ------------------------------------------------
# 입력 처리
# ------------------------------------------------
def handle_input():
    global scene

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if scene in typing_scenes and typing_active:
                skip_typing()
                return

            if scene == 67:
                scene = 68
                start_typing(dialogues[68])

            elif scene == 68:
                scene = 69

            elif scene == 69:
                scene = 70
                start_typing(dialogues[70])

            elif scene == 70:
                scene = 71
                start_typing(dialogues[71])

            elif scene == 71:
                scene = 72
                start_typing(dialogues[72])

            elif scene == 72:
                scene = 73

            elif scene == 73:
                scene = 74
                start_typing(dialogues[74])

            elif scene == 74:
                scene = 75

            elif scene == 75:
                if select75_rect.collidepoint(event.pos):
                    scene = 76

            elif scene == 76:
                scene = 77
                start_typing(dialogues[77])

            elif scene == 77:
                scene = 78
                start_typing(dialogues[78])

            elif scene == 78:
                scene = 79

            elif scene == 79:
                scene = 80
                start_typing(dialogues[80])

            elif scene == 80:
                scene = 81

            elif scene == 81:
                pass


# ------------------------------------------------
# 메인 루프
# ------------------------------------------------
scene = 67
start_typing(dialogues[67])

while True:
    CLOCK.tick(FPS)
    handle_input()

    if scene in typing_scenes:
        update_typing()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
