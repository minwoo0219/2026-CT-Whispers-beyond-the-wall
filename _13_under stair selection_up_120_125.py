import pygame
import sys
import random

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 120~125 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 50, 50)

FONT      = pygame.font.Font("DOSGothic.ttf", 28)
BIG_FONT  = pygame.font.Font("DOSGothic.ttf", 120)   # GAME OVER

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


# ------------------------------------------------------
# CHATBOX 대사 출력 (여러 줄, x=380 고정)
# ------------------------------------------------------
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 120
    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))


# ------------------------------------------------------
# Fade 효과
# ------------------------------------------------------
def fade_out():
    """현재 scene 화면에서 검은색으로 서서히 어두워짐 (123용)"""
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for a in range(0, 255, 8):
        fade.set_alpha(a)
        draw_scene()                 # 현재 scene 화면 그리기
        SCREEN.blit(fade, (0, 0))
        pygame.display.update()
        CLOCK.tick(60)


def fade_in():
    """현재 scene 화면이 검은색에서 서서히 나타남 (125용)"""
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for a in range(255, -1, -8):
        draw_scene()                 # 이미 바뀐 scene 화면 그리기
        fade.set_alpha(a)
        SCREEN.blit(fade, (0, 0))
        pygame.display.update()
        CLOCK.tick(60)


# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
underway_bg = pygame.transform.scale(
    pygame.image.load("underway.png"), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (400, 120)
)

# 선택창 위치 (125)
select_retry_rect = select_box.get_rect(center=(640, 450))


# ------------------------------------------------------
# 엘레노어
# ------------------------------------------------------
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

# ✅ 요청한 최종 좌표
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


def draw_select_text(rect, text):
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=rect.center))


# ------------------------------------------------------
# 대사
# ------------------------------------------------------
dialogues = {
    120: [
        "“그냥 다시 올라가야겠어, 너무 무서워..”",
    ],
    121: [
        "그때, 어디선가 묵직한 발걸음 소리가 들렸다.",
        "그 소리는 점점 나에게 가까워지고 있었다.",
    ],
    122: [
        "걸음을 멈추자, 국왕은 시뻘건 눈을 하곤 날 노려보고 있었다.",
        "그의 오른손에는 칼이 쥐어져 있었다.",
    ],
}

# 124쪽: 문단형 설명 (타자기 X, 빨간색)
dialogue_124 = [
    "당신은 왕을 피해 도망치려 했지만, 계단에서 미끄러져 크게 넘어졌다.",
    "부러진 다리의 통증에 몸을 일으키지도 못한 채 바닥에 쓰러져 있었다.",
    "왕은 천천히 다가오며 비웃듯 큰 소리를 냈고, 당신을 내려다보았다.",
    "그리고 아무 망설임 없이 배를 깊숙이 찔러버렸다.",
    "그렇게 왕은 계단을 유유히 올라갔고, 당신은 서서히 죽어갔다.",
]

typing_scenes = {120, 121, 122}


# ------------------------------------------------------
# 씬 번호
# ------------------------------------------------------
scene = 120
start_typing(dialogues[120])


# ------------------------------------------------------
# 장면 렌더링
# ------------------------------------------------------
def draw_scene():
    global scene

    # 120 : 통로 + 엘레노어 + 대사
    if scene == 120:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_dialogue_line()

    # 121 : 통로 + 대사(2줄)
    elif scene == 121:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    # 122 : 통로 + 대사
    elif scene == 122:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    # 123 : 완전 검은 화면 (fade_out 이후 상태)
    elif scene == 123:
        SCREEN.fill(BLACK)

    # 124 : 검은 화면 + 빨간 문장들 (타자기 X)
    elif scene == 124:
        SCREEN.fill(BLACK)
        start_y = 150
        for i, line in enumerate(dialogue_124):
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            y = start_y + i * 32
            SCREEN.blit(t, (x, y))

    # 125 : GAME OVER + 다시 진행 선택창 (fade_in 대상)
    elif scene == 125:
        SCREEN.fill(BLACK)

        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)

        x_game = (WIDTH - t1.get_width()) // 2
        y_game = 150
        x_over = (WIDTH - t2.get_width()) // 2
        y_over = 150 + t1.get_height() + 10

        SCREEN.blit(t1, (x_game, y_game))
        SCREEN.blit(t2, (x_over, y_over))

        SCREEN.blit(select_box, select_retry_rect)
        draw_select_text(select_retry_rect, "다시 진행")


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

            # 120 -> 121
            if scene == 120:
                scene = 121
                start_typing(dialogues[121])

            # 121 -> 122
            elif scene == 121:
                scene = 122
                start_typing(dialogues[122])

            # 122 -> 123 (fade out)
            elif scene == 122:
                fade_out()
                scene = 123

            # 123 -> 124
            elif scene == 123:
                scene = 124

            # 124 -> 125 (fade in)
            elif scene == 124:
                scene = 125
                fade_in()

            # 125 : 선택창은 아직 기능 없음
            elif scene == 125:
                pass


# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    # 타자기 효과가 있는 씬에서만 업데이트
    if scene in typing_scenes:
        update_typing()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
