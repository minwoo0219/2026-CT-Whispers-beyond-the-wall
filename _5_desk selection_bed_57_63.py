import pygame
import sys

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 57~63 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2

# ------------------------------------------------------
# 타자기 시스템
# ------------------------------------------------------
current_text = ""
full_text = ""
text_index = 0
typing_done = False
displayed_text = ""

def start_typing(lines):
    global full_text, current_text, text_index, typing_done, displayed_text
    full_text = "\n".join(lines)
    current_text = ""
    displayed_text = ""
    text_index = 0
    typing_done = False

def update_typing():
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
# 이미지 로드
# ------------------------------------------------------
underbed_bg = pygame.transform.scale(
    pygame.image.load("underbed.png"), (WIDTH, HEIGHT)
)

hand_img = pygame.transform.scale(
    pygame.image.load("hand.png"), (400, 400)
)
# 🔽 손을 더 아래로 조정 (기존 450 → 550)
hand_rect = hand_img.get_rect(center=(640, 550))

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (380, 110)
)

# ------------------------------------------------------
# 엘리노어
# ------------------------------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
EH = 620
ratio = EH / elen_raw.get_height()
EW = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (EW, EH))
ELEN_POS = (-200, HEIGHT - EH)


# ------------------------------------------------------
# 선택창 위치
# ------------------------------------------------------
choice1_rect = select_box.get_rect(center=(240, 360))
choice2_rect = select_box.get_rect(center=(640, 360))
choice3_rect = select_box.get_rect(center=(1040, 360))

def draw_select_text(rect, text):
    lines = text.split("\n")

    if len(lines) == 1:
        txt = FONT.render(lines[0], True, BLACK)
        SCREEN.blit(txt, txt.get_rect(center=rect.center))

    elif len(lines) == 2:
        line1 = FONT.render(lines[0], True, BLACK)
        line2 = FONT.render(lines[1], True, BLACK)

        line1_rect = line1.get_rect(center=(rect.centerx, rect.centery - 18))
        line2_rect = line2.get_rect(center=(rect.centerx, rect.centery + 18))

        SCREEN.blit(line1, line1_rect)
        SCREEN.blit(line2, line2_rect)


# ------------------------------------------------------
# 대사
# ------------------------------------------------------
dialogues = {
    57: ["“뭐가 있는지 한 번 봐야겠어..”"],
    58: [
        "나는 조심스럽게 침대 아래에 몸을 숙였다.",
        "손 끝이 차가운 돌 표면을 스치자, 작은 떨림이 손목을 타고 올라온다.",
    ],
    60: ["“어..! 뭐지?”"],
    61: [
        "손 끝에 미세하게 감각이 다른 돌 판이 만져졌다.",
        "가운데에 손바닥만 한 흠이 파여있다.",
        "마치 무언가를 여기에 넣으라는 듯한 형태다.",
    ],
    62: [
        "그 순간 갑자기 또 벽 뒤에서 탁- 탁- 거리는 소리가 들리기 시작했다.",
        "“난 뭘 해야 하지?”",
    ],
}

typing_scenes = {57, 58, 60, 61, 62}

scene = 57
start_typing(dialogues[57])


# ------------------------------------------------------
# 대사 출력 함수
# ------------------------------------------------------
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 120
    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, WHITE)
        SCREEN.blit(surf, (x, y + i * 32))


# ------------------------------------------------------
# 장면 그리기
# ------------------------------------------------------
def draw_scene():
    global scene

    # 57,58,60,61,62 — 엘리노어 + 대사창 + 대사
    if scene in (57, 58, 60, 61, 62):
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELEN_POS)
        draw_dialogue_line()

    # 59 — 손 등장, 대사창 없음
    elif scene == 59:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(hand_img, hand_rect)

    # 63 — 선택창 3개 (두 줄 표시)
    elif scene == 63:
        SCREEN.blit(underbed_bg, (0, 0))

        SCREEN.blit(select_box, choice1_rect)
        SCREEN.blit(select_box, choice2_rect)
        SCREEN.blit(select_box, choice3_rect)

        draw_select_text(choice1_rect, "아까 열쇠를 가져와\n흠에 맞춰본다.")
        draw_select_text(choice2_rect, "일단 침대 밖으로 나와\n다른 단서를 찾는다.")
        draw_select_text(choice3_rect, "돌 판을\n들어올려본다.")


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

            if scene == 57:
                scene = 58
                start_typing(dialogues[58])

            elif scene == 58:
                scene = 59

            elif scene == 59:
                scene = 60
                start_typing(dialogues[60])

            elif scene == 60:
                scene = 61
                start_typing(dialogues[61])

            elif scene == 61:
                scene = 62
                start_typing(dialogues[62])

            elif scene == 62:
                scene = 63

            elif scene == 63:
                pass  # 기능 없음


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
