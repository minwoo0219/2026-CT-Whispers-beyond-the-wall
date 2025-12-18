import pygame
import sys

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 109~118 EVENT")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 50, 50)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2


# ------------------------------------------------------
# 타자기 텍스트 상태
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
def draw_dialogue_line(scene):
    x = 380
    y = HEIGHT - 120

    for i, line in enumerate(displayed_text.split("\n")):

        if scene == 113:  # 왕 대사 빨간 굵기
            t1 = FONT.render(line, True, RED)
            t2 = FONT.render(line, True, RED)
            SCREEN.blit(t1, (x, y + i * 32))
            SCREEN.blit(t2, (x + 2, y + i * 32))
        else:
            surf = FONT.render(line, True, WHITE)
            SCREEN.blit(surf, (x, y + i * 32))


# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
underway_bg = pygame.transform.scale(pygame.image.load("underway.png"), (WIDTH, HEIGHT))
stairway_bg = pygame.transform.scale(pygame.image.load("stairway.png"), (WIDTH, HEIGHT))

chatbox = pygame.transform.scale(pygame.image.load("chatbox.png"), (WIDTH, 200))
select_box = pygame.transform.scale(pygame.image.load("selection box.png"), (350, 110))

# 엘리노어 이미지
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

# ✅ 요청한 최종 좌표
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

# 왕 이미지 (113쪽)
king_raw = pygame.image.load("king.png").convert_alpha()
king_img = pygame.transform.scale(king_raw, (550, 550))
KING_POS = (WIDTH - 600, HEIGHT - 600)


# ------------------------------------------------------
# 선택창 위치 — PPT 배치와 동일
# ------------------------------------------------------
choice1_rect = select_box.get_rect(center=(640, 300))  # 위 1개
choice2_rect = select_box.get_rect(center=(450, 550))  # 아래 왼쪽
choice3_rect = select_box.get_rect(center=(830, 550))  # 아래 오른쪽


def draw_select_text(rect, text):
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=rect.center))


# ------------------------------------------------------
# 대사 데이터
# ------------------------------------------------------
dialogues = {
    109: [
        "나는 망설이지 않았다.",
        "문 앞의 인기척보다 이 계단이 더 안전하다고 느꼈다.",
        "그래서 촛불을 꼭 쥔 채 아래로 내려가기 시작했다.",
    ],
    110: [
        "나는 촛불을 들고 천천히 계단 아래로 내려갔다.",
        "발걸음마다 먼지와 오래된 돌 냄새가 피어올랐다.",
    ],
    111: [
        "몇 계단을 내려왔을 때,",
        "위쪽에서 삐걱이는 문소리가 들렸다.",
        "“누군가 침실에 들어왔어...”",
    ],
    112: [
        "그때, 낮고 무거운 남자의 목소리가 들렸다.",
    ],
    113: [
        "“엘리노어… 그 길을 택하는 순간,”",
        "“너에게 남은 삶은 아무 의미도 없게 될 터이다.”",
        "“지금 당장 돌아오거라!!!”",
    ],
    114: [
        "하지만 아래로 내려갈수록 왕의 목소리는 멀어지고,",
        "대신 아래쪽에서 다른 소리가 들리기 시작했다.",
    ],
    115: [
        "???: “여기로 내려와..!”",
    ],
    116: [
        "속삭임, 하지만 분명한 소리였다.",
        "왕의 목소리는 아니다.",
        "그때 길이 두 갈래로 갈라졌다.",
    ],
}


typing_scenes = set(dialogues.keys())


# ------------------------------------------------------
# 현재 씬
# ------------------------------------------------------
scene = 109
start_typing(dialogues[109])


# ------------------------------------------------------
# draw_scene()
# ------------------------------------------------------
def draw_scene():
    global scene

    # 109~116 : 대사 진행
    if 109 <= scene <= 116:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox, (0, HEIGHT - 200))

        # 111, 112 → 엘리노어 등장
        if scene in {111, 112}:
            SCREEN.blit(elenore_img, ELENORE_POS)

        # 113 → 왕 등장, 엘리노어 없음
        if scene == 113:
            SCREEN.blit(king_img, KING_POS)

        draw_dialogue_line(scene)

    # 117 : 배경만 표시
    elif scene == 117:
        SCREEN.blit(stairway_bg, (0, 0))

    # 118 : 선택창 3개 배치
    elif scene == 118:
        SCREEN.blit(stairway_bg, (0, 0))

        SCREEN.blit(select_box, choice1_rect)
        SCREEN.blit(select_box, choice2_rect)
        SCREEN.blit(select_box, choice3_rect)

        draw_select_text(choice1_rect, "왼쪽 길")
        draw_select_text(choice2_rect, "오른쪽 길")
        draw_select_text(choice3_rect, "다시 위로")


# ------------------------------------------------------
# handle_input()
# ------------------------------------------------------
def handle_input():
    global scene

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if scene == 109:
                scene = 110
                start_typing(dialogues[110])

            elif scene == 110:
                scene = 111
                start_typing(dialogues[111])

            elif scene == 111:
                scene = 112
                start_typing(dialogues[112])

            elif scene == 112:
                scene = 113
                start_typing(dialogues[113])

            elif scene == 113:
                scene = 114
                start_typing(dialogues[114])

            elif scene == 114:
                scene = 115
                start_typing(dialogues[115])

            elif scene == 115:
                scene = 116
                start_typing(dialogues[116])

            elif scene == 116:
                scene = 117

            elif scene == 117:
                scene = 118

            elif scene == 118:
                pass  # 선택 기능 없음


# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
while True:
    CLOCK.tick(FPS)

    handle_input()

    if scene in typing_scenes:
        update_typing()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
