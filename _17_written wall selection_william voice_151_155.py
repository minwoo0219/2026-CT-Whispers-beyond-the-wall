import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 151~155 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 50, 50)

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
# 대사 출력
# -----------------------------------
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 150   # 🔼 대사 전체 위치 위로 올림
    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, WHITE)
        SCREEN.blit(surf, (x, y + i * 32))


# -----------------------------------
# 선택창 텍스트
# -----------------------------------
def draw_select_text(rect, text):
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=rect.center))


# -----------------------------------
# 이미지 로드
# -----------------------------------
wall_bg = pygame.transform.scale(
    pygame.image.load("wall_written.png").convert(), (WIDTH, HEIGHT)
)

stair2_bg = pygame.transform.scale(
    pygame.image.load("additional stairway.png").convert(), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (350, 110)
)

select_retry_rect = select_box.get_rect(center=(640, 500))


# -----------------------------------
# 엘리노어
# -----------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elen_raw.get_height()
ELENORE_WIDTH = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# -----------------------------------
# 대사
# -----------------------------------
dialogues = {
    151: [
        "“아무래도 윌리엄의 목소리를 따라가 보아야겠어..!”",
    ],
    152: [
        "“뭐지..? 여기보다 더 내려가야 하나, 이미 너무 깊게 내려 왔는데...”",
    ],
}

typing_scenes = {151, 152}

story_153 = [
    "당신은 닿을 수 없는 목소리에 닿고 싶어, 그 목소리를 향해 계속해서",
    "아래로 내려갔지만 그곳에는 아무도 없었다. 하지만 당신은 이미 지하",
    "깊은 곳에서 너무 많은 길을 헤집고 다녔고, 지도도 없었기에 영원히",
    "그 곳에 갇혀서 결국은  3개월 후 아사하게 되었다.",
]


# -----------------------------------
# 씬 설정
# -----------------------------------
scene = 151
start_typing(dialogues[151])


# -----------------------------------
# 장면 렌더링
# -----------------------------------
def draw_scene():

    # 151 : 벽 + 엘리노어 + 대사
    if scene == 151:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELENORE_POS)
        draw_dialogue_line()

    # 152 : 새로운 계단 배경 + 엘리노어 + 대사
    elif scene == 152:
        SCREEN.blit(stair2_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELENORE_POS)
        draw_dialogue_line()

    # 153 : 빨간 글씨 전체 문장
    elif scene == 153:
        SCREEN.fill(BLACK)
        y = 200
        for line in story_153:
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            SCREEN.blit(t, (x, y))
            y += 34

    # 154 : 검정 화면
    elif scene == 154:
        SCREEN.fill(BLACK)

    # 155 : GAME OVER + 다시 선택
    elif scene == 155:
        SCREEN.fill(BLACK)

        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)

        SCREEN.blit(t1, ((WIDTH - t1.get_width()) // 2, 150))
        SCREEN.blit(t2, ((WIDTH - t2.get_width()) // 2, 150 + t1.get_height() + 10))

        SCREEN.blit(select_box, select_retry_rect)
        draw_select_text(select_retry_rect, "다시 선택")


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

            if scene == 151:
                scene = 152
                start_typing(dialogues[152])

            elif scene == 152:
                scene = 153

            elif scene == 153:
                scene = 154

            elif scene == 154:
                scene = 155

            elif scene == 155:
                pass  # 선택 기능 없음


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
