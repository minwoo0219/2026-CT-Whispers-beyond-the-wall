import pygame
import sys
import random

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 46~55 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 50, 50)

FONT      = pygame.font.Font("DOSGothic.ttf", 28)
BIG_FONT  = pygame.font.Font("DOSGothic.ttf", 120)   # GAME OVER
Q_FONT    = pygame.font.Font("DOSGothic.ttf", 45)    # ??? 글자용

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
# CHATBOX 대사 출력
# ------------------------------------------------------
def draw_dialogue_line(scene):
    x = 380
    y = HEIGHT - 120
    for i, line in enumerate(displayed_text.split("\n")):
        if scene == 51:
            # 51쪽은 빨간색 굵게
            t1 = FONT.render(line, True, RED)
            t2 = FONT.render(line, True, RED)
            SCREEN.blit(t1, (x, y + i * 32))
            SCREEN.blit(t2, (x + 2, y + i * 32))
        else:
            surf = FONT.render(line, True, WHITE)
            SCREEN.blit(surf, (x, y + i * 32))


# ------------------------------------------------------
# 선택창 텍스트 출력
# ------------------------------------------------------
def draw_select_text(rect, text):
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=rect.center))


# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
room_bg = pygame.transform.scale(pygame.image.load("room.png"), (WIDTH, HEIGHT))

keyhole_bg = pygame.transform.scale(
    pygame.image.load("keyhole_key2.png"), (WIDTH, HEIGHT)
)  # 열쇠구멍 실루엣 배경

king_eye_bg = pygame.transform.scale(
    pygame.image.load("keyhole_king1.png"), (WIDTH, HEIGHT)
)  # 눈이 보이는 배경

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (400, 120)
)

# 선택창 위치
select_47_rect   = select_box.get_rect(center=(640, 600))  # 47쪽
select_retry_rect = select_box.get_rect(center=(640, 450))  # 54~55쪽


# ------------------------------------------------------
# 엘레노어
# ------------------------------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elen_raw.get_height()
ELENORE_WIDTH = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)


# ------------------------------------------------------
# 랜덤 ??? 위치 생성
# ------------------------------------------------------
def generate_random_questions(count=40):
    arr = []
    for _ in range(count):
        x = random.randint(50, 1230)
        y = random.randint(50, 670)
        arr.append((x, y))
    return arr


random_q_positions = []  # 48~49에서 사용


def draw_random_questions():
    for (x, y) in random_q_positions:
        txt = Q_FONT.render("???", True, RED)
        SCREEN.blit(txt, (x, y))


# ------------------------------------------------------
# 대사
# ------------------------------------------------------
# 타자기 사용 씬용
typing_dialogues = {
    46: [
        "“열쇠구멍으로 뭐가 있는지 확인해 보아야겠어.”",
    ],
    49: [
        "?????????????????????????????????????????????????????"
    ],
    50: [
        "너무 놀라 비명을 지를 수 도 없다.",
        "내 손과 발이 덜덜 떨리기 시작했다.",
        "날 지켜보고 있는거야? (심장소리)",
    ],
    51: [
        "덜컥,,끼이이--익,,,",
    ],
}

# 53쪽은 타자기 없이 한 번에 출력
dialogue_53 = [
    "당신은 열쇠구멍을 들여다 보곤 깜짝놀라, 뒤로 자빠졌다.",
    "열쇠구멍으로 보이는 모습은 국왕인 것 같았다.",
    "그는 당신이 패닉에 빠져 아무것도 못하자, 문을 천천히 열고 들어와",
    "혼자 소리를 지르고, 자신이 원하는대로 행동하기만 했어도",
    "이런일은 일어나지 않았을 것이라고 했다.",
    "그 모습은 한 나라의 국왕이 아닌 정신 이상자 같았다.",
    "당신은 너무 무서워 달아나고 싶었지만, 결국",
    "그가 당신의 목을 칼로 찔렀고 사망하게 됐다.",
]

# 55쪽 마지막 문장
dialogue_55_last = "지켜보고 있을 줄이야,,,"


typing_scenes = {46, 49, 50, 51}


# ------------------------------------------------------
# 씬 번호
# ------------------------------------------------------
scene = 46
start_typing(typing_dialogues[46])


# ------------------------------------------------------
# 장면 렌더링
# ------------------------------------------------------
def draw_scene():
    global scene

    # 46 : 방 + 엘리노어 + 대사
    if scene == 46:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        SCREEN.blit(elen_img, ELENORE_POS)
        draw_dialogue_line(scene)

    # 47 : 열쇠구멍 배경 + 선택창
    elif scene == 47:
        SCREEN.blit(keyhole_bg, (0, 0))
        SCREEN.blit(select_box, select_47_rect)
        draw_select_text(select_47_rect, "더 자세히 보기")

    # 48 : 눈 배경 + 랜덤 ???만
    elif scene == 48:
        SCREEN.blit(king_eye_bg, (0, 0))
        draw_random_questions()

    # 49 : 눈 배경 + 랜덤 ??? + 대사
    elif scene == 49:
        SCREEN.blit(king_eye_bg, (0, 0))
        draw_random_questions()
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line(scene)

    # 50 : 방 + 대사
    elif scene == 50:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line(scene)

    # 51 : 방 + 빨간 굵은 대사
    elif scene == 51:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))
        draw_dialogue_line(scene)

    # 52 : 완전 검은 화면
    elif scene == 52:
        SCREEN.fill(BLACK)

    # 53 : 검은 화면 + 빨간 문장들 (타자기 X)
    elif scene == 53:
        SCREEN.fill(BLACK)
        start_y = 150
        for i, line in enumerate(dialogue_53):
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            y = start_y + i * 32
            SCREEN.blit(t, (x, y))

    # 54 : GAME OVER + 다시 진행 선택창
    elif scene == 54:
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

    # 55 : GAME OVER + 마지막 문장 (흰색)
    elif scene == 55:
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

        last = FONT.render(dialogue_55_last, True, WHITE)
        SCREEN.blit(last, ((WIDTH - last.get_width()) // 2, y_over + 120))


# ------------------------------------------------------
# 입력 처리
# ------------------------------------------------------
def handle_input():
    global scene, random_q_positions

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # 46 -> 47
            if scene == 46:
                scene = 47

            # 47 : 선택창 눌러야 48로
            elif scene == 47:
                if select_47_rect.collidepoint(event.pos):
                    scene = 48
                    random_q_positions = generate_random_questions()

            # 48 -> 49
            elif scene == 48:
                scene = 49
                start_typing(typing_dialogues[49])

            # 49 -> 50
            elif scene == 49:
                scene = 50
                start_typing(typing_dialogues[50])

            # 50 -> 51
            elif scene == 50:
                scene = 51
                start_typing(typing_dialogues[51])

            # 51 -> 52
            elif scene == 51:
                scene = 52

            # 52 -> 53
            elif scene == 52:
                scene = 53

            # 53 -> 54
            elif scene == 53:
                scene = 54

            # 54 -> 55 (선택창은 아직 기능 없음, 아무 곳이나 클릭)
            elif scene == 54:
                scene = 55

            # 55 : 선택창 기능 없음, 그대로 유지
            elif scene == 55:
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
