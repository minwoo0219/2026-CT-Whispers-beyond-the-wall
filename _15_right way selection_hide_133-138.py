import pygame
import sys

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 133~138 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 120)

TEXT_SPEED = 2  # 타자기 속도


# ------------------------------------------------------
# 타자기 상태
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
# 대사 출력
# ------------------------------------------------------
def draw_dialogue():
    x = 380
    y = HEIGHT - 120
    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, WHITE)
        SCREEN.blit(surf, (x, y + i * 32))


# ------------------------------------------------------
# 선택창 출력
# ------------------------------------------------------
select_box = pygame.transform.scale(pygame.image.load("selection box.png"), (400, 120))
select_retry_rect = select_box.get_rect(center=(640, 500))


def draw_select_text(rect, text):
    surf = FONT.render(text, True, BLACK)
    SCREEN.blit(surf, surf.get_rect(center=rect.center))


# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
monster_bg = pygame.transform.scale(pygame.image.load("underway_monster.png"), (WIDTH, HEIGHT))
chatbox = pygame.transform.scale(pygame.image.load("chatbox.png"), (WIDTH, 200))

# 엘리노어 이미지
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elen_raw.get_height()
ELENORE_WIDTH = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# ------------------------------------------------------
# 대사
# ------------------------------------------------------
typing_dialogues = {
    133: ["저… 저게… 뭐지…"],
    134: ["으아…!!"],
}

dialogue_136 = [
    "당신은 겁에 질려 뒤로 물러났지만, 괴물은 순식간에 당신의 목을 잡아채며",
    "당신을 벽에 강하게 내던졌다. 그 충격으로 당신은 정신을 잃었고,",
    "괴물은 당신의 몸을 질질 끌고 어둠 속으로 사라졌다.",
]

typing_scenes = {133, 134}


# ------------------------------------------------------
# 씬 번호
# ------------------------------------------------------
scene = 133
start_typing(typing_dialogues[133])

fade_alpha = 0
fade_out = False
fade_in = False


# ------------------------------------------------------
# 페이드 처리
# ------------------------------------------------------
def draw_fade():
    global fade_alpha
    fade_layer = pygame.Surface((WIDTH, HEIGHT))
    fade_layer.fill(BLACK)
    fade_layer.set_alpha(fade_alpha)
    SCREEN.blit(fade_layer, (0, 0))


# ------------------------------------------------------
# 장면 그림
# ------------------------------------------------------
def draw_scene():
    global fade_alpha

    # 133 : 검정 배경 + 대사
    if scene == 133:
        SCREEN.fill(BLACK)
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue()

    # 134 : 몬스터 배경 + 엘리노어 + 대사
    elif scene == 134:
        SCREEN.blit(monster_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELENORE_POS)
        draw_dialogue()

    # 135 : 페이드 아웃
    elif scene == 135:
        SCREEN.fill(BLACK)
        draw_fade()

    # 136 : 검정 화면 + 빨간 대사
    elif scene == 136:
        SCREEN.fill(BLACK)
        start_y = 200
        for i, line in enumerate(dialogue_136):
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            SCREEN.blit(t, (x, start_y + i * 32))

    # 137 : 페이드 인
    elif scene == 137:
        SCREEN.fill(BLACK)
        draw_fade()

    # 138 : GAME OVER + 선택창
    elif scene == 138:
        SCREEN.fill(BLACK)
        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)

        SCREEN.blit(t1, ((WIDTH - t1.get_width()) // 2, 150))
        SCREEN.blit(t2, ((WIDTH - t2.get_width()) // 2, 150 + t1.get_height()))

        SCREEN.blit(select_box, select_retry_rect)
        draw_select_text(select_retry_rect, "다시 진행")


# ------------------------------------------------------
# 입력 처리
# ------------------------------------------------------
def handle_input():
    global scene, fade_alpha, fade_out, fade_in

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if scene == 133:
                scene = 134
                start_typing(typing_dialogues[134])

            elif scene == 134:
                scene = 135
                fade_alpha = 0
                fade_out = True

            elif scene == 136:
                scene = 137
                fade_alpha = 255
                fade_in = True

            elif scene == 138:
                pass  # 선택 기능 없음


# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
while True:
    CLOCK.tick(FPS)
    handle_input()

    if scene in typing_scenes:
        update_typing()

    # Fade out 처리 (135)
    if fade_out and scene == 135:
        fade_alpha += 5
        if fade_alpha >= 255:
            fade_alpha = 255
            fade_out = False
            scene = 136

    # Fade in 처리 (137)
    if fade_in and scene == 137:
        fade_alpha -= 5
        if fade_alpha <= 0:
            fade_alpha = 0
            fade_in = False
            scene = 138

    draw_scene()
    pygame.display.flip()
