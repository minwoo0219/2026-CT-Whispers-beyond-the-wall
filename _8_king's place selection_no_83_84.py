import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene 83~84")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 50, 50)

FONT = pygame.font.Font("DOSGothic.ttf", 32)

# -----------------------------------
# 타자기 효과 변수
# -----------------------------------
current_text = ""
full_text = ""
text_index = 0
typing_done = False
text_speed = 2

def start_typing(text):
    global full_text, current_text, text_index, typing_done
    full_text = text
    current_text = ""
    text_index = 0
    typing_done = False

def update_typing():
    global current_text, text_index, typing_done

    if typing_done:
        return

    for _ in range(text_speed):
        if text_index < len(full_text):
            current_text += full_text[text_index]
            text_index += 1
        else:
            typing_done = True
            break


# -----------------------------------
# 이미지 로드
# -----------------------------------
sleeping_king = pygame.transform.scale(
    pygame.image.load("sleeping king.png"), (WIDTH, HEIGHT)
)

# 엘레노어 새 이미지 (더 크게 중앙 배치)
elenore_raw = pygame.image.load("Elenore2.png").convert_alpha()

# 가까이 보이는 큰 크기로 조정
ELENORE_HEIGHT = 800
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)

elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

# 대화창 위쪽 중앙에 위치시키기
ELENORE_POS = (
    WIDTH // 2 - ELENORE_WIDTH // 2,   # 중앙 정렬
    HEIGHT - 350 - ELENORE_HEIGHT // 2 # 대사창보다 위
)

# -----------------------------------
# 대사창
# -----------------------------------
chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (1280, 200)
)

# 선택창
select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (380, 130)
)

left_choice_rect = select_box.get_rect(center=(450, 600))
right_choice_rect = select_box.get_rect(center=(830, 600))

def draw_choice(rect, text):
    SCREEN.blit(select_box, rect)
    txt = FONT.render(text, True, BLACK)
    SCREEN.blit(txt, txt.get_rect(center=rect.center))

# -----------------------------------
# 씬 번호 및 대사
# -----------------------------------
scene = 83

dialogues = {
    83: "“어쩜 이리도 잘 주무시는지 참...”"
}

# -----------------------------------
# 화면 그리기
# -----------------------------------
def draw_scene():
    global scene

    SCREEN.blit(sleeping_king, (0, 0))

    if scene == 83:
        # 엘레노어 (가장 앞)
        SCREEN.blit(elenore_img, ELENORE_POS)

        # 대사창
        SCREEN.blit(chatbox, (0, HEIGHT - 200))

        # 대사 출력 (타자기)
        update_typing()
        t = FONT.render(current_text, True, RED)
        SCREEN.blit(t, (260, HEIGHT - 140))

    elif scene == 84:
        # 선택창만 등장
        draw_choice(left_choice_rect, "찌르기")
        draw_choice(right_choice_rect, "안 찌르기")


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

            if scene == 83:
                # 클릭 → 선택창 등장
                scene = 84

            elif scene == 84:
                pass  # 기능 없음


# -----------------------------------
# 초기화
# -----------------------------------
start_typing(dialogues[83])

# -----------------------------------
# 메인 루프
# -----------------------------------
while True:
    CLOCK.tick(FPS)
    handle_input()
    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
