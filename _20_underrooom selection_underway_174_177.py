import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 174~177 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 40, 40)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 120)

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
# 대사 출력 (채팅창)
# -----------------------------------
def draw_dialogue_line(color=WHITE):
    x = 380
    y = HEIGHT - 140  # 전체적으로 조금 올림
    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, color)
        SCREEN.blit(txt, (x, y + i * 32))


# -----------------------------------
# 페이드 처리
# -----------------------------------
def fade_in(surface, speed=5):
    for alpha in range(0, 255, speed):
        surface.set_alpha(alpha)
        SCREEN.fill(BLACK)
        SCREEN.blit(surface, (0, 0))
        pygame.display.update()
        CLOCK.tick(FPS)


def fade_out(surface, speed=5):
    for alpha in range(255, 0, -speed):
        surface.set_alpha(alpha)
        SCREEN.fill(BLACK)
        SCREEN.blit(surface, (0, 0))
        pygame.display.update()
        CLOCK.tick(FPS)


# -----------------------------------
# 이미지 로드
# -----------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elen_raw.get_height()
ELENORE_WIDTH = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

stair_bg = pygame.transform.scale(
    pygame.image.load("additional stairway.png").convert(), (WIDTH, HEIGHT)
)

black_surface = pygame.Surface((WIDTH, HEIGHT))
black_surface.fill(BLACK)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (350, 110)
)
retry_rect = select_box.get_rect(center=(640, 500))


# -----------------------------------
# 대사
# -----------------------------------
dialogues = {
    174: [
        "“아무리 생각해도 여긴 믿을 수 있는 사람이 없어,”",
        "“빨리 어디든 돌아다녀 보자..!”"
    ],
}

typing_scenes = {174}

scene = 174
start_typing(dialogues[174])

next_delay_timer = 0  # 176 유지시간


# -----------------------------------
# 장면 그리기
# -----------------------------------
def draw_scene():

    if scene == 174:
        SCREEN.blit(stair_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELENORE_POS)
        draw_dialogue_line()

    elif scene == 175:
        SCREEN.fill(BLACK)

        text_lines = [
            "당신은 그를 지나쳐 지하실 반대편 통로로 다시 향해 지하실을",
            "헤집고 돌아다녔지만, 미로 같은 지하실을 빠져 나오지 못하였다.",
            "당신은 지하실에 갇힌 채로 있다가 3개월 후 아사하게 되었다.",
        ]

        start_y = HEIGHT // 2 - 60
        for i, line in enumerate(text_lines):
            t = FONT.render(line, True, RED)
            SCREEN.blit(t, ((WIDTH - t.get_width()) // 2, start_y + i * 32))

    elif scene == 176:
        SCREEN.fill(BLACK)

    elif scene == 177:
        SCREEN.fill(BLACK)

        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)

        SCREEN.blit(t1, ((WIDTH - t1.get_width()) // 2, 150))
        SCREEN.blit(t2, ((WIDTH - t2.get_width()) // 2, 150 + t1.get_height() + 10))

        SCREEN.blit(select_box, retry_rect)
        retry_text = FONT.render("다시 진행", True, BLACK)
        SCREEN.blit(retry_text, retry_text.get_rect(center=retry_rect.center))


# -----------------------------------
# 입력 처리
# -----------------------------------
def handle_input():
    global scene, next_delay_timer

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if scene == 174 and typing_done:
                # Fade out Stair BG
                fade_out(stair_bg.copy())
                scene = 175

            elif scene == 175:
                # Fade in
                fade_in(black_surface.copy())
                scene = 176
                next_delay_timer = pygame.time.get_ticks()

            elif scene == 177:
                pass  # 선택 기능 없음


# -----------------------------------
# 메인 루프
# -----------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    if scene in typing_scenes:
        update_typing()

    if scene == 176:
        if pygame.time.get_ticks() - next_delay_timer > 1200:
            scene = 177

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
