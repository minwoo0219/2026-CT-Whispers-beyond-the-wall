import pygame
import sys

pygame.init()

# ------------------------------------------------
# 기본 설정
# ------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("65 PAGE ONLY")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2

# ------------------------------------------------
# 타자기 시스템
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


# ------------------------------------------------
# 이미지 로드
# ------------------------------------------------
room_bg = pygame.transform.scale(pygame.image.load("underbed.png"), (WIDTH, HEIGHT))
chatbox = pygame.transform.scale(pygame.image.load("chatbox.png"), (1280, 200))

# ⭐ 엘리노어 스케일 (요청한 구조 유지)
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# ------------------------------------------------
# 65쪽 대사
# ------------------------------------------------
dialogue_65 = [
    "“침대에서 유일하게 살아있는 듯 보이는 곳은… 여기뿐인데.”",
    "“도대체 어떻게 해야 하지…?”"
]


# ------------------------------------------------
# 대사 출력
# ------------------------------------------------
def draw_dialogue():
    x = 380
    y = HEIGHT - 140

    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))


# ------------------------------------------------
# 화면 그리기
# ------------------------------------------------
def draw_scene():
    SCREEN.blit(room_bg, (0, 0))

    SCREEN.blit(chatbox, (0, HEIGHT - 200))

    # ⭐ 엘리노어는 chatbox보다 '뒤'가 아니라 '앞'에 그린다 (최전면 레이어)
    SCREEN.blit(elenore_img, ELENORE_POS)

    draw_dialogue()


# ------------------------------------------------
# 입력 처리
# ------------------------------------------------
def handle_input():
    global typing_active, displayed_text, text_index

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 타자기 스킵
            if typing_active:
                typing_active = False
                displayed_text = current_text
                text_index = len(current_text)


# ------------------------------------------------
# 메인 루프
# ------------------------------------------------
start_typing(dialogue_65)

while True:
    CLOCK.tick(FPS)
    handle_input()

    if typing_active:
        update_typing()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
