import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 140~149 EVENT")

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
# 대사 출력 (전체적으로 위로 이동한 버전)
# -----------------------------------
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 160   # ← 기존 120에서 40px 상승
    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))


# -----------------------------------
# 선택창 텍스트 (두 줄 중앙정렬)
# -----------------------------------
def draw_select_text_multiline(rect, text):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        surf = FONT.render(line, True, BLACK)
        SCREEN.blit(surf, surf.get_rect(center=(
            rect.centerx, rect.centery + (i * 22)
        )))


# -----------------------------------
# 이미지 로드
# -----------------------------------
stair_bg = pygame.transform.scale(pygame.image.load("stairway.png"), (WIDTH, HEIGHT))
leftway_bg = pygame.transform.scale(pygame.image.load("left way.png"), (WIDTH, HEIGHT))
wall_bg = pygame.transform.scale(pygame.image.load("wall_written.png"), (WIDTH, HEIGHT))
chatbox = pygame.transform.scale(pygame.image.load("chatbox.png"), (WIDTH, 200))

# 선택창 축소 버전
select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (380, 120)
)

# 선택창 간격 더 넓게
choice_left_rect  = select_box.get_rect(center=(260, 520))
choice_mid_rect   = select_box.get_rect(center=(640, 520))
choice_right_rect = select_box.get_rect(center=(1020, 520))


# -----------------------------------
# 엘리노어
# -----------------------------------
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
    140: [
        "“그래, 왼쪽 길로 한 번 가보자.”",
    ],

    # ← 요청한 4줄 버전 적용됨
    141: [
        "나는 촛불이 흔들리며 조금 더 따뜻한 공기가 흐르는 왼쪽 길을 택한다.",
        "서늘한 돌 벽 사이로 희미한 바람이 스치고, 아래로 내려갈수록",
        "누군가 오래 전 이곳을 드나든 흔적 같은 마른 흙 냄새가 퍼져왔다.",
        "그 공기 속에서 알 수 없는 불안함이 서서히 몸을 감싸기 시작했다.",
    ],

    142: [
        "촛불의 작은 불꽃이 벽에 조용히 흔들리고, 그 사이로 잠깐—",
        "누군가 지나간 듯한 그림자가 스쳤다. 하지만 발자국 소리는 없다.",
        "나는 촛대를 더 가까이 들이댔다. 그림자는 이미 사라졌지만",
        "대신 벽에 희미하게 새겨진 글귀가 눈에 들어왔다.",
    ],

    145: [
        "“두려움을 낮추면, 길이 너에게 응답할 것이다..?”",
    ],

    146: [
        "그 아래엔 가느다란 손자국이, 마치 누군가 벽을 붙잡고 끌려간 듯",
        "길게 남아 있었다. 내가 글귀를 따라 시선을 내리는 순간,",
        "아래쪽 어둠에서 부드럽고 익숙한 목소리가 들려왔다.",
    ],

    147: [
        "“이건.. 윌리엄 목소리야...!, 하지만 지금 윌리엄은 분명 성 밖에",
        "있을텐데...” 목소리가 너무 자연스럽고 가까워서, 난 발걸음을 멈췄다.",
    ],
}

typing_scenes = {140, 141, 142, 145, 146, 147}

scene = 140
start_typing(dialogues[140])


# -----------------------------------
# 장면 렌더링
# -----------------------------------
def draw_scene():
    if scene == 140:
        SCREEN.blit(stair_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_dialogue_line()

    elif scene == 141:
        SCREEN.blit(leftway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    elif scene == 142:
        SCREEN.blit(leftway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    elif scene == 143:
        SCREEN.fill(BLACK)

    elif scene == 144:
        SCREEN.blit(wall_bg, (0, 0))

    elif scene == 145:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_dialogue_line()

    elif scene == 146:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    elif scene == 147:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_dialogue_line()

    elif scene == 148:
        SCREEN.blit(wall_bg, (0, 0))

    elif scene == 149:
        SCREEN.blit(wall_bg, (0, 0))

        SCREEN.blit(select_box, choice_left_rect)
        SCREEN.blit(select_box, choice_mid_rect)
        SCREEN.blit(select_box, choice_right_rect)

        draw_select_text_multiline(choice_left_rect, "윌리엄의 목소리를\n따라간다.")
        draw_select_text_multiline(choice_mid_rect, "대답하지 않고 계속\n아래로 내려간다.")
        draw_select_text_multiline(choice_right_rect, "벽에 숨겨진 장치가 있는지\n조사한다.")


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

            if scene == 140:
                scene = 141
                start_typing(dialogues[141])

            elif scene == 141:
                scene = 142
                start_typing(dialogues[142])

            elif scene == 142:
                scene = 143

            elif scene == 143:
                scene = 144

            elif scene == 144:
                scene = 145
                start_typing(dialogues[145])

            elif scene == 145:
                scene = 146
                start_typing(dialogues[146])

            elif scene == 146:
                scene = 147
                start_typing(dialogues[147])

            elif scene == 147:
                scene = 148

            elif scene == 148:
                scene = 149

            elif scene == 149:
                pass


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
