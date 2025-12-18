import pygame
import sys
import time

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene 86~90")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (220,50,50)

FONT = pygame.font.Font("DOSGothic.ttf", 32)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 120)

# -----------------------------------
# 대사창과 호환 위한 함수(사용 X)
# -----------------------------------
displayed_text = ""

def draw_dialogue_line():
    x = 380
    y = HEIGHT - 120
    txt = FONT.render(displayed_text, True, WHITE)
    SCREEN.blit(txt, (x, y))


# -----------------------------------
# 페이드 함수
# -----------------------------------
def fade_in():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for alpha in range(255, -1, -15):
        draw_scene(no_fade=True)
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0,0))
        pygame.display.flip()
        CLOCK.tick(60)

def fade_out():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for alpha in range(0, 255, 15):
        draw_scene(no_fade=True)
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0,0))
        pygame.display.flip()
        CLOCK.tick(60)


# -----------------------------------
# 이미지 로드
# -----------------------------------
sleeping_king = pygame.transform.scale(
    pygame.image.load("sleeping king.png"), (WIDTH, HEIGHT)
)

blood_img = pygame.image.load("blood2.png").convert_alpha()
blood_img = pygame.transform.scale(blood_img, (900, 500))
blood_rect = blood_img.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))

elenore_raw = pygame.image.load("Elenore3.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (1280, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (400, 130)
)
select_rect = select_box.get_rect(center=(640, 600))


def draw_select_text(text):
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=select_rect.center))


# -----------------------------------
# 씬 & 대사
# -----------------------------------
scene = 86
fade88_done = False
fade90_done = False
hold_time = None

dialogues = {
    86: "푸-욱...!  (사람들 비명소리)",
    88: (
        "당신은 결국 국왕의 목을 칼로 찔렀다. 국왕은 당신이 원하는대로 즉사 하였지만, "
        "당신의 행동으로 인해 그 안의 근위병들은 즉시 당신을 체포 하였고, "
        "고문을 받다가 죽게 된다."
    ),
    90: ["GAME OVER", "다시 선택"]
}


# -----------------------------------
# 장면 그리기
# -----------------------------------
def draw_scene(no_fade=False):
    global scene

    # ----------- 86 -----------
    if scene == 86:
        SCREEN.blit(sleeping_king, (0,0))
        SCREEN.blit(blood_img, blood_rect)

        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        t = FONT.render(dialogues[86], True, RED)
        SCREEN.blit(t, (260, HEIGHT - 140))

        SCREEN.blit(elenore_img, ELENORE_POS)

    # ----------- 87 -----------
    elif scene == 87:
        SCREEN.fill(BLACK)

    # ----------- 88 -----------
    elif scene == 88:
        SCREEN.fill(BLACK)

        text = dialogues[88]
        words = text.split()
        lines = []
        cur = ""

        for w in words:
            test = cur + w + " "
            if FONT.size(test)[0] > 1100:
                lines.append(cur)
                cur = w + " "
            else:
                cur = test
        lines.append(cur)

        for i, line in enumerate(lines):
            t = FONT.render(line, True, RED)
            SCREEN.blit(t, (80, 200 + i * 40))

    # ----------- 89 -----------
    elif scene == 89:
        SCREEN.fill(BLACK)

    # ----------- 90 -----------
    elif scene == 90:
        SCREEN.fill(BLACK)

        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)

        SCREEN.blit(t1, (WIDTH//2 - t1.get_width()//2, 150))
        SCREEN.blit(t2, (WIDTH//2 - t2.get_width()//2, 300))

        SCREEN.blit(select_box, select_rect)
        draw_select_text("다시 선택")


# -----------------------------------
# 입력 처리
# -----------------------------------
def handle_input():
    global scene, hold_time, fade88_done

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # 86 → fade out → 87
            if scene == 86:
                fade_out()
                scene = 87

            elif scene == 87:
                scene = 88

            elif scene == 88:
                fade_out()
                scene = 89
                hold_time = time.time()

            elif scene == 90:
                pass  # 선택 기능 없음


# -----------------------------------
# 메인 루프
# -----------------------------------
while True:
    CLOCK.tick(FPS)
    handle_input()

    # 88 처음 들어오면 fade-in
    if scene == 88 and not fade88_done:
        fade_in()
        fade88_done = True

    # 89에서 1초 후 90 + fade-in
    if scene == 89 and hold_time is not None:
        if time.time() - hold_time > 1.0:
            scene = 90
            if not fade90_done:
                fade_in()
                fade90_done = True

    draw_scene()
    pygame.display.flip()
