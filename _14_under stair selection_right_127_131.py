import pygame
import sys

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 127~131 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2


# ------------------------------------------------------
# 타이핑 상태
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
chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

stair_bg = pygame.transform.scale(
    pygame.image.load("stairway.png"), (WIDTH, HEIGHT)
)

underway_bg = pygame.transform.scale(
    pygame.image.load("underway_hall.png"), (WIDTH, HEIGHT)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (420, 140)
)

# 선택창 위치
choice_left = select_box.get_rect(center=(430, 520))
choice_right = select_box.get_rect(center=(850, 520))


def draw_select_text(rect, text):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        txt = FONT.render(line, True, BLACK)
        pos = txt.get_rect(center=(rect.centerx, rect.centery - 15 + i * 30))
        SCREEN.blit(txt, pos)


# ------------------------------------------------------
# 엘레노어
# ------------------------------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elen_raw.get_height()
ELENORE_WIDTH = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# ------------------------------------------------------
# 대사
# ------------------------------------------------------
dialogues = {
    127: ["그래, 오른쪽 길로 한 번 가보자"],
    128: [
        "나는 조용히 침대 아래로 몸을 굴려 내려가",
        "어둡고 좁은 오른쪽 통로로 발을 들였다."
    ],
    129: ["???: 딸칵...딸칵..."],
    130: [
        "지하에 있는 무언가가 급속도로 나에게 다가오는 소리가 들렸다.",
        "어떻게 해야 할지 빨리 결정을 해야 한다."
    ],
}

typing_scenes = {127, 128, 129, 130}


# ------------------------------------------------------
# 초기 씬 설정
# ------------------------------------------------------
scene = 127
start_typing(dialogues[127])


# ------------------------------------------------------
# 대사 출력
# ------------------------------------------------------
def draw_dialogue():
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

    # 127 : 엘레노어 + 계단
    if scene == 127:
        SCREEN.blit(stair_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELENORE_POS)
        draw_dialogue()

    # 128~130 : 통로 + 대사
    elif scene in (128, 129, 130):
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue()

    # 131 : 대사창 제거 + 어둡게 + 선택창
    elif scene == 131:
        SCREEN.blit(underway_bg, (0, 0))

        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 150))
        SCREEN.blit(dark, (0, 0))

        SCREEN.blit(select_box, choice_left)
        SCREEN.blit(select_box, choice_right)

        draw_select_text(choice_left, "다시 뒤돌아\n왼쪽 길로 도망간다")
        draw_select_text(choice_right, "바로 보이는 큰 상자에\n숨는다.")


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

            if scene == 127:
                scene = 128
                start_typing(dialogues[128])

            elif scene == 128:
                scene = 129
                start_typing(dialogues[129])

            elif scene == 129:
                scene = 130
                start_typing(dialogues[130])

            elif scene == 130:
                scene = 131

            elif scene == 131:
                pass  # 선택지 기능 없음


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
