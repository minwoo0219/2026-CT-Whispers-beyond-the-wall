import pygame
import sys

pygame.init()

# -----------------------------------
# 기본 설정
# -----------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene 92~98")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

FONT = pygame.font.Font("DOSGothic.ttf", 28)

# -----------------------------------
# 배경 & 이미지 로드
# -----------------------------------
bg_under = pygame.transform.scale(pygame.image.load("underbed.png"), (WIDTH, HEIGHT))

key_img = pygame.transform.scale(
    pygame.image.load("key hole_key.png"),
    (220, 150)
)
key_rect = key_img.get_rect(center=(660, 460))

chatbox = pygame.transform.scale(
    pygame.image.load("chatbox.png"), (WIDTH, 200)
)

select_box = pygame.transform.scale(
    pygame.image.load("selection box.png"), (380, 120)
)


# -----------------------------------
# 선택창 위치
# -----------------------------------
select_main = select_box.get_rect(center=(1100, 550))

choice_left = select_box.get_rect(center=(500, 520))
choice_right = select_box.get_rect(center=(900, 520))


def draw_select_text(rect, text):
    """선택창 글씨 중앙 배치"""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        txt = FONT.render(line, True, BLACK)
        SCREEN.blit(txt, txt.get_rect(center=(rect.centerx, rect.centery + i*25)))


# -----------------------------------
# 대사 데이터
# -----------------------------------
dialogues = {
    92: ["맞춰보기"],
    93: ["???끼이익...."],
    94: [
        "나는 떨리는 숨을 고르고, 열쇠를 홈 위에 맞춰보았다. 그러자 딱. 소리와 함께 무언가 맞물리는 소리가 났다.",
        "그리곤 바닥이 아주 미세하게 흔들렸다. 돌판이 스르륵- 거짓말 처럼 부드럽게 아래로 내려가기 시작했다.",
        "마치 오래 전 부터 이 움직임만 기다려온 장치처럼..."
    ],
    95: [
        "곧, 침대 아래 어둠 속에서 계단 입구가 열렸다. 서늘한 바람이 위로 밀려 올라오고,",
        "아래쪽 깊은 곳에서 누군가의 속삭임 같은 목소리가 희미하게 들린다."
    ],
    96: [
        "???: “...엘리노어, 여기야...”"
    ],
    97: [
        "하지만, 갑자기 복도에서 쇠사슬 끌리는 소리가 멈춘다.",
        "누군가 문 앞을 스친 것 같다."
    ],
    98: [
        "바로 계단 아래로  내려간다",
        "문 쪽을 먼저  확인한다"
    ],
}


# -----------------------------------
# 대사 출력
# -----------------------------------
def draw_dialogue(scene):
    SCREEN.blit(chatbox, (0, HEIGHT - 200))

    lines = dialogues[scene]
    x = 260
    y = HEIGHT - 160
    for i, line in enumerate(lines):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i*32))


# -----------------------------------
# 씬 상태
# -----------------------------------
scene = 92


# -----------------------------------
# 장면 렌더링
# -----------------------------------
def draw_scene():
    SCREEN.blit(bg_under, (0,0))

    # 92: 열쇠 + 선택창
    if scene == 92:
        SCREEN.blit(key_img, key_rect)
        SCREEN.blit(select_box, select_main)
        draw_select_text(select_main, "맞춰보기")

    # 93~97: 대사 진행
    elif 93 <= scene <= 97:
        draw_dialogue(scene)

    # 98: 선택창 2개
    elif scene == 98:
        SCREEN.blit(select_box, choice_left)
        SCREEN.blit(select_box, choice_right)

        draw_select_text(choice_left, "바로 계단 아래로\n내려간다")
        draw_select_text(choice_right, "문 쪽을 먼저\n확인한다")


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

            if scene == 92:
                if select_main.collidepoint(event.pos):
                    scene = 93

            elif 93 <= scene <= 97:
                scene += 1

            elif scene == 98:
                pass  # 선택 기능 없음


# -----------------------------------
# 메인 루프
# -----------------------------------
while True:
    CLOCK.tick(FPS)
    handle_input()
    draw_scene()
    pygame.display.flip()
