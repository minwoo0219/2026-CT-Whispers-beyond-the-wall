import pygame
import sys

pygame.init()

# ------------------------------------------------------
# 기본 설정
# ------------------------------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT 36~44 EVENT FINAL CLEAN")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)
TEXT_SPEED = 2


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
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 120

    for i, line in enumerate(displayed_text.split("\n")):
        surf = FONT.render(line, True, WHITE)
        SCREEN.blit(surf, (x, y + i * 32))


# ------------------------------------------------------
# 선택창 텍스트 출력 (누락되어 오류났던 함수)
# ------------------------------------------------------
def draw_select_text(rect, text):
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=rect.center))


# ------------------------------------------------------
# Fade-in
# ------------------------------------------------------
def fade_in():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for a in range(255, -1, -35):
        fade.set_alpha(a)
        draw_scene()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(60)


# ------------------------------------------------------
# 이미지 로드
# ------------------------------------------------------
bg_table = pygame.transform.scale(pygame.image.load("table_selection1.png"), (WIDTH, HEIGHT))
room_bg = pygame.transform.scale(pygame.image.load("room.png"), (WIDTH, HEIGHT))

notebook = pygame.transform.scale(pygame.image.load("notebook_selection1.png"), (280, 280))
notebook_rect = notebook.get_rect(center=(960, 360))

cup_img = pygame.transform.scale(pygame.image.load("cup_selection1.png"), (160, 160))
cup_rect = cup_img.get_rect(center=(300, 360))

key_img = pygame.transform.scale(pygame.image.load("key_selection1.png"), (160, 160))
key_rect = key_img.get_rect(center=(480, 360))

handker_img = pygame.transform.scale(pygame.image.load("handkerchief_selection1.png"), (160, 160))
handker_rect = handker_img.get_rect(center=(640, 360))

notebook_big = pygame.transform.scale(pygame.image.load("notebook_selection1.png"), (500, 500))
notebook_big_rect = notebook_big.get_rect(center=(640, 330))


# ------------------------------------------------------
# 양피지 (화면의 1/3 크기)
# ------------------------------------------------------
paper_raw = pygame.image.load("paper.png").convert_alpha()
PAPER_W = WIDTH // 3
ratio = PAPER_W / paper_raw.get_width()
PAPER_H = int(paper_raw.get_height() * ratio)
paper_img = pygame.transform.scale(paper_raw, (PAPER_W, PAPER_H))
paper_rect = paper_img.get_rect(center=(330, 330))


# ------------------------------------------------------
# 선택창
# ------------------------------------------------------
select_box = pygame.transform.scale(pygame.image.load("selection box.png"), (400, 120))
select_41_rect = select_box.get_rect(center=(1000, 600))
choice_left_rect = select_box.get_rect(center=(420, 400))
choice_right_rect = select_box.get_rect(center=(860, 400))


chatbox = pygame.transform.scale(pygame.image.load("chatbox.png"), (1280, 200))


# ------------------------------------------------------
# 엘레노어 이미지 설정
# ------------------------------------------------------
elen_raw = pygame.image.load("Elenore.png")
EH = 620
ratio = EH / elen_raw.get_height()
EW = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (EW, EH))
ELEN_POS = (-200, HEIGHT - EH)


# ------------------------------------------------------
# 대사
# ------------------------------------------------------
dialogues = {
    39: [""],  # 글씨 없음
    40: [
        "엘리노어는 오래된 침실 한가운데에서 먼지로 덮인 작은 공책을 펼쳤다.",
        "종이는 누렇게 바랬지만 필체는 놀라울 정도로 정확했다.",
        "누군가 이곳에 갇히기 전 기록으로 보인다.",
    ],
    41: ["펼치기"],
    42: [
        "“성벽 아래에는 두 개의 길이 있다.”",
        "“하나는 죽음을 불러오고 하나는 속삭임의 목소리를 잠재운다.”",
        "",
        "“그 길의 입구는 침대 아래 숨겨져 있다.”",
        "“왕 리처드는 이곳의 비밀을 알고 있다.”"
    ],
    43: [
        "“음.. 아직은 무슨 말인지 잘 모르겠다,”",
        "“하지만 분명히 큰 힌트가 될거야.”",
        "“그럼 이제 다시 뭘 해볼까?”",
    ],
    44: ["침대 아래를 살펴본다.", "문틈 너머 소리를 확인해본다."],
}


# ------------------------------------------------------
# 씬 번호
# ------------------------------------------------------
scene = 36


# ------------------------------------------------------
# 장면 렌더링
# ------------------------------------------------------
def draw_scene():
    global scene

    # ------------ 36 ------------
    if scene == 36:
        SCREEN.blit(bg_table,(0,0))
        SCREEN.blit(cup_img,cup_rect)
        SCREEN.blit(key_img,key_rect)
        SCREEN.blit(handker_img,handker_rect)

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,200))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(notebook, notebook_rect)

    # ------------ 37 ------------
    elif scene == 37:
        SCREEN.blit(bg_table,(0,0))
        SCREEN.blit(cup_img,cup_rect)
        SCREEN.blit(key_img,key_rect)
        SCREEN.blit(handker_img,handker_rect)

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,200))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(notebook, notebook_rect)

    # ------------ 38 ------------
    elif scene == 38:
        SCREEN.blit(bg_table,(0,0))

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,210))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(notebook, notebook_rect)

        SCREEN.blit(select_box, select_41_rect)
        draw_select_text(select_41_rect, "공책 집어들기")

    # ------------ 39 ------------
    elif scene == 39:
        SCREEN.blit(room_bg,(0,0))
        SCREEN.blit(notebook_big, notebook_big_rect)
        update_typing()

    # ------------ 40 ------------
    elif scene == 40:
        SCREEN.blit(room_bg,(0,0))
        SCREEN.blit(notebook_big, notebook_big_rect)
        update_typing()

        x = 200
        y = 540
        for i, line in enumerate(displayed_text.split("\n")):
            surf = FONT.render(line, True, WHITE)
            SCREEN.blit(surf, (x, y + i * 32))

    # ------------ 41 ------------
    elif scene == 41:
        SCREEN.blit(room_bg,(0,0))
        SCREEN.blit(notebook_big, notebook_big_rect)

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,180))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(select_box, select_41_rect)
        draw_select_text(select_41_rect, "펼치기")

    # ------------ 42 (양피지 + 중앙 오른쪽 대사)------------
    elif scene == 42:
        SCREEN.blit(room_bg,(0,0))
        SCREEN.blit(paper_img, paper_rect)

        update_typing()

        # 글씨를 조금 왼쪽으로 이동
        x = WIDTH//2 - 200
        y = 250

        for i, line in enumerate(displayed_text.split("\n")):
            surf = FONT.render(line, True, WHITE)
            SCREEN.blit(surf, (x, y + i * 32))

    # ------------ 43 ------------
    elif scene == 43:
        SCREEN.blit(room_bg,(0,0))
        SCREEN.blit(chatbox,(0,HEIGHT - 200))
        SCREEN.blit(elen_img, ELEN_POS)

        update_typing()
        draw_dialogue_line()

    # ------------ 44 ------------
    elif scene == 44:
        SCREEN.blit(room_bg,(0,0))

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,160))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(select_box, choice_left_rect)
        SCREEN.blit(select_box, choice_right_rect)

        draw_select_text(choice_left_rect, "침대 아래를 살펴본다.")
        draw_select_text(choice_right_rect, "문틈 너머 소리를 확인해본다.")


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

            if scene == 36: scene = 37
            elif scene == 37: scene = 38
            elif scene == 38:
                if select_41_rect.collidepoint(event.pos):
                    scene = 39
                    start_typing(dialogues[39])

            elif scene == 39:
                scene = 40
                start_typing(dialogues[40])

            elif scene == 40:
                scene = 41

            elif scene == 41:
                if select_41_rect.collidepoint(event.pos):
                    scene = 42
                    start_typing(dialogues[42])

            elif scene == 42:
                scene = 43
                start_typing(dialogues[43])

            elif scene == 43:
                scene = 44
                fade_in()

            elif scene == 44:
                pass


# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
while True:
    CLOCK.tick(FPS)
    handle_input()
    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
