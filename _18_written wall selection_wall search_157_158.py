import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene 157~158 Only")

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
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 150  # 살짝 위로 올림
    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, WHITE)
        SCREEN.blit(surf, (x, y + i * 32))


# -----------------------------------
# 이미지 로드
# -----------------------------------
wall_bg = pygame.transform.scale(
    pygame.image.load("wall_written.png").convert(), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)

# 엘리노어
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

# -----------------------------------
# 대사
# -----------------------------------
dialogues = {
    157: [
        "“여기에 분명 무슨 장치가 있을 거야!”",
    ],
    158: [
        "하지만 나의 기대가 무색하게 아무것도 없었다. (다시 선택창)",
    ],
}

typing_scenes = {157, 158}

# -----------------------------------
# 초기 장면
# -----------------------------------
scene = 157
start_typing(dialogues[157])

# -----------------------------------
# 장면 렌더링
# -----------------------------------
def draw_scene():
    if scene == 157:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_dialogue_line()

    elif scene == 158:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()


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
            if scene == 157:
                scene = 158
                start_typing(dialogues[158])

            elif scene == 158:
                pygame.quit()
                sys.exit()  # 마지막 장면 → 종료


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
