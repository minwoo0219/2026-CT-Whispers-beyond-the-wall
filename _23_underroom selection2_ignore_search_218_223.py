import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("218~223 Scene")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (220, 50, 50)
BLACK = (0, 0, 0)

FONT = pygame.font.Font("DOSGothic.ttf", 32)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 140)
MID_FONT = pygame.font.Font("DOSGothic.ttf", 38)

# -----------------------------------------------------
# 이미지 로드
# -----------------------------------------------------
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()

ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

# ✅ 요청한 최종 좌표
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

blood_bg = pygame.transform.scale(
    pygame.image.load("gameover_background.png"), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (380, 120)
)

retry_rect = select_box.get_rect(center=(640, 520))


# -----------------------------------------------------
# 타이핑 시스템
# -----------------------------------------------------
current_text = ""
full_text = ""
text_index = 0
typing_done = False
TEXT_SPEED = 2


def start_typing(lines):
    global full_text, current_text, text_index, typing_done
    full_text = "\n".join(lines)
    current_text = ""
    text_index = 0
    typing_done = False


def update_typing():
    global current_text, text_index, typing_done
    if typing_done:
        return

    for _ in range(TEXT_SPEED):
        if text_index < len(full_text):
            current_text += full_text[text_index]
            text_index += 1
        else:
            typing_done = True
            break


# -----------------------------------------------------
# 페이드 효과
# -----------------------------------------------------
def fade_in(color=BLACK, speed=5):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(color)
    for alpha in range(255, -1, -speed):
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0, 0))
        pygame.display.update()
        CLOCK.tick(60)


def fade_out(color=BLACK, speed=5):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(color)
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0, 0))
        pygame.display.update()
        CLOCK.tick(60)


# -----------------------------------------------------
# 대사 데이터
# -----------------------------------------------------
dialogues = {
    218: ["윌리엄 나도 널 너무 보고싶었어... 난 널 선택할래..."],
    220: [
        "당신이 윌리엄이라고 생각한 것은, 너무 위험해 성 아래에 감금하였던 괴물이었다.",
        "이 괴물은 당신의 아버지가 젊었을 때 직접 사냥해 왕에게 바쳤고,",
        "그 이후 사업이 승승장구하였다. 하지만 괴물은 평생 당신 아버지를 저주하며",
        "결국 그의 딸인 당신을 죽기 위해 손에 넣었다.",
        "그렇게 당신은 고통스럽게 죽었다.",
    ],
}

# -----------------------------------------------------
# 씬 상태
# -----------------------------------------------------
scene = 218
start_typing(dialogues[218])


# -----------------------------------------------------
# 선택창 글자 함수
# -----------------------------------------------------
def draw_select_text(rect, text):
    surf = MID_FONT.render(text, True, BLACK)
    SCREEN.blit(surf, surf.get_rect(center=rect.center))


# -----------------------------------------------------
# 장면 그리기
# -----------------------------------------------------
def draw_scene():
    SCREEN.fill(BLACK)

    # 218 -------------------------------------------------
    if scene == 218:
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        y = HEIGHT - 150
        for i, line in enumerate(current_text.split("\n")):
            SCREEN.blit(FONT.render(line, True, WHITE), (380, y + i * 36))

    # 219 -------------------------------------------------
    elif scene == 219:
        SCREEN.fill(BLACK)

    # 220 -------------------------------------------------
    elif scene == 220:
        SCREEN.fill(BLACK)
        y = 150
        for i, line in enumerate(dialogues[220]):
            t = FONT.render(line, True, RED)
            SCREEN.blit(t, ((WIDTH - t.get_width()) // 2, y + i * 36))

    # 221~223 ---------------------------------------------
    elif scene in (221, 222, 223):
        SCREEN.blit(blood_bg, (0, 0))

        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)

        SCREEN.blit(t1, (WIDTH//2 - t1.get_width()//2, 120))
        SCREEN.blit(t2, (WIDTH//2 - t2.get_width()//2, 260))

        SCREEN.blit(select_box, retry_rect)
        draw_select_text(retry_rect, "다시 선택")

        if scene == 223:
            extra = MID_FONT.render(
                "기회를 얼마나 줬는지 아십니까? 멍청하면 답도 없군요!",
                True, WHITE
            )
            SCREEN.blit(extra, (WIDTH//2 - extra.get_width()//2, 580))


# -----------------------------------------------------
# 입력 처리
# -----------------------------------------------------
def handle_input():
    global scene
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if scene == 218:
                scene = 219
                fade_out()

            elif scene == 219:
                scene = 220
                fade_in()

            elif scene == 220:
                scene = 221
                fade_out()

            elif scene == 221:
                scene = 222

            elif scene == 222:
                scene = 223

            elif scene == 223:
                pass  # 선택지는 아직 기능 없음


# -----------------------------------------------------
# 메인 루프
# -----------------------------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    if scene == 218:
        update_typing()

    draw_scene()

    pygame.display.update()
