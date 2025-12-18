import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 160~172 EVENT")

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
    y = HEIGHT - 150  # 전체적으로 위로 올림
    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))


# -----------------------------------
# 선택창 출력
# -----------------------------------
def draw_select_text(rect, text):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        txt = FONT.render(line, True, BLACK)
        txt_rect = txt.get_rect(center=(rect.centerx, rect.centery + (i - 0.5) * 22))
        SCREEN.blit(txt, txt_rect)


# -----------------------------------
# 이미지 로드
# -----------------------------------
stairway_bg = pygame.transform.scale(
    pygame.image.load("stairway.png").convert(), (WIDTH, HEIGHT)
)

underground_bg = pygame.transform.scale(
    pygame.image.load("underground_room.png").convert(), (WIDTH, HEIGHT)
)

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (350, 110)
)

# 엘레노어 이미지
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# 선택창 위치
choice_left_rect = select_box.get_rect(center=(300, 520))
choice_mid_rect = select_box.get_rect(center=(640, 520))
choice_right_rect = select_box.get_rect(center=(980, 520))


# -----------------------------------
# 대사
# -----------------------------------
dialogues = {
    160: [
        "나는 숨을 억누르며 윌리엄의 목소리에 반응하지 않기로 결심했다.",
        "그의 목소리는 너무 자연스러웠고, 너무 가까웠다.",
        "그래서 오히려... 진짜가 아닐 가능성이 더 컸다."
    ],
    161: [
        "촛불을 최대한 가리고 조용히 발걸음을 옮기자,",
        "그 목소리는 계속 뒤에서 다정하게 속삭였다."
    ],

    # ⭐ 162 → 2줄로 재구성
    162: [
        "“왜 대답 안 해..? 나야 엘리노어, 겁내지마…”",
        "“여기 있어… 내가… 널 찾고 있어.”"
    ],

    163: [
        "난 이제 정말 확신 할 수 있었다.",
    ],
    164: [
        "진짜 윌리엄은... 이렇게 따라오라고 재촉하지 않아.",
    ],
    165: [
        "계단 깊숙이 내려가자 목소리는 서서히 사라지고,",
        "대신 아래쪽에 푸르스름한 빛이 희미하게 퍼지는 것이 보였다.",
        "그리고 계단이 끝난 자리에서 넓은 지하실이 모습을 드러냈다."
    ],

    # 166: 어둠 전환

    # ⭐ 168 → 4줄로 확장
    168: [
        "그 안은 고대 문양이 새겨진 기둥들과 오래된 사슬들,",
        "그리고 반쯤 부서져 먼지가 내려앉은 상자들이 널브러져 있었다.",
        "가운데 작은 책상 하나가 놓여 있었고,",
        "그 위엔 ‘제프리’라는 이름 태그가 놓여 있었다."
    ],

    169: [
        "그때, 지하실 구석에서 낮고 건조한 목소리가 작게 울렸다.",
    ],
    170: [
        "???: ...늦었군.",
    ],
    171: [
        "어둠 속에서 누군가 걸어 나왔다.",
        "그의 표정은 무심했지만 눈빛만은 흔들리고 있었다."
    ]
}

typing_scenes = {160, 161, 162, 163, 164, 165, 168, 169, 170, 171}

scene = 160
start_typing(dialogues[160])


# -----------------------------------
# 장면 렌더링
# -----------------------------------
def draw_scene():

    # -------- 계단 구간 --------
    if scene in {160, 161, 162, 163, 164, 165}:
        SCREEN.blit(stairway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))

        # ⭐ 특정 장면에서만 엘레노어 등장
        if scene in {162, 164, 165}:
            SCREEN.blit(elenore_img, ELENORE_POS)

        draw_dialogue_line()

    # -------- 암전 --------
    elif scene == 166:
        SCREEN.fill(BLACK)

    # -------- 지하실 --------
    elif scene in {168, 169, 170, 171}:
        SCREEN.blit(underground_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line()

    # -------- 선택창 --------
    elif scene == 172:
        SCREEN.blit(underground_bg, (0, 0))

        SCREEN.blit(select_box, choice_left_rect)
        SCREEN.blit(select_box, choice_mid_rect)
        SCREEN.blit(select_box, choice_right_rect)

        draw_select_text(choice_left_rect, "당신은 누구죠?\n물어본다.")
        draw_select_text(choice_mid_rect, "그를 경계하며\n뒤로 물러선다.")
        draw_select_text(choice_right_rect, "그를 지나쳐\n반대편으로 향한다.")


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

            if scene == 160:
                scene = 161
                start_typing(dialogues[161])

            elif scene == 161:
                scene = 162
                start_typing(dialogues[162])

            elif scene == 162:
                scene = 163
                start_typing(dialogues[163])

            elif scene == 163:
                scene = 164
                start_typing(dialogues[164])

            elif scene == 164:
                scene = 165
                start_typing(dialogues[165])

            elif scene == 165:
                scene = 166

            elif scene == 166:
                scene = 168
                start_typing(dialogues[168])

            elif scene == 168:
                scene = 169
                start_typing(dialogues[169])

            elif scene == 169:
                scene = 170
                start_typing(dialogues[170])

            elif scene == 170:
                scene = 171
                start_typing(dialogues[171])

            elif scene == 171:
                scene = 172

            elif scene == 172:
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
