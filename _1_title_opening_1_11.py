import pygame
import sys

pygame.init()
pygame.mixer.init()

# 화면 설정
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whispers Beyond The Wall")

CLOCK = pygame.time.Clock()
FPS = 60

# 이미지 로드
start_bg = pygame.image.load("start.png").convert()
start_bg = pygame.transform.scale(start_bg, (WIDTH, HEIGHT))

room_bg = pygame.image.load("room.png").convert()
room_bg = pygame.transform.scale(room_bg, (WIDTH, HEIGHT))

elenore_raw = pygame.image.load("Elenore.png").convert_alpha()

ELENORE_HEIGHT = 620
ratio = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))

ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

chatbox_img = pygame.image.load("chatbox.png").convert_alpha()
chatbox_img = pygame.transform.scale(chatbox_img, (WIDTH, 200))

# 폰트
FONT = pygame.font.Font("DOSGothic.ttf", 26)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 42)
INFO_FONT = pygame.font.Font("DOSGothic.ttf", 22)
INFO_TITLE_FONT = pygame.font.Font("DOSGothic.ttf", 40)

# 색상
WHITE = (255, 255, 255)
RED = (200, 50, 50)
HOVER_RED = (255, 120, 120)
DARK_OVERLAY = (0, 0, 0, 180)

# 모드
MODE = "TITLE"   # TITLE → INFORMATION → GAME

# 페이드 전환
def fade_to_mode(next_mode):
    global MODE
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0, 0, 0))

    for alpha in range(0, 255, 10):
        fade.set_alpha(alpha)
        draw_screen()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(60)

    MODE = next_mode

    for alpha in range(255, -1, -10):
        fade.set_alpha(alpha)
        draw_screen()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(60)

# 버튼 클래스
class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.callback = callback
        self.hover = False
        self.rect = FONT.render(text, True, WHITE).get_rect(center=pos)

    def draw(self, surface):
        color = HOVER_RED if self.hover else RED
        txt = BIG_FONT.render(self.text, True, color)
        self.rect = txt.get_rect(center=self.rect.center)
        surface.blit(txt, self.rect)

    def handle(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.callback()

# 버튼 기능
def start_game():
    fade_to_mode("GAME")

def open_info():
    fade_to_mode("INFORMATION")

def close_info():
    fade_to_mode("TITLE")

# 버튼 생성
start_button = Button("START", (WIDTH // 2, HEIGHT // 2 + 180), start_game)
info_button = Button("INFORMATION", (WIDTH // 2, HEIGHT // 2 + 250), open_info)
back_button = Button("BACK", (WIDTH // 2, HEIGHT - 100), close_info)

buttons_title = [start_button, info_button]
buttons_info = [back_button]

# INFORMATION 텍스트
INFO_TEXT = (
    "아주 큰 미지존재 처리 회사를 운영하는 아버지를 둔 엘리노어(당신)는 "
    "사랑하는 연인 윌리엄과 함께 행복한 날들을 보내고 있었다. 하지만 점점 "
    "미지의 존재가 세계를 위협하게 되며 국왕은 그들을 처리할 방법을 고민하다가, "
    "엘리노어의 아버지와 자신의 아들을 결혼 시켜 비용들이지 않고 괴물들을 처리 할 "
    "방법을 생각하게 된다. 그리고 시간이 지나 실제로 계약은 이행된다. "
    "엘리노어는 자신의 실제 연인인 윌리엄과의 사랑을 포기할 수 없었고 급기야 "
    "도망 계획을 세우게 된다. 하지만 하늘도 무심하게 그 계획은 그녀의 아버지와 "
    "국왕에게 걸리게 되었고 엘리노어는 국왕에게 밉보이게 된다.\n\n"
    "그런데 이게 무슨 일 일까, 국왕이 주최한 무도회에 참석을 하였다가 술을 좀 먹고 "
    "잠에 들었는데 눈 떠보니 엘리노어는 너무 낮선 곳에 갇혀있는 상태였다. "
    "이젠 어떻게 하면 좋을까?\n\n"
    "당신은 이 방을 탈출해야한다. 당신의 선택에 따라 모든게 뒤바뀐다. "
    "어서 이야기 속으로 들어가서 어떻게 해야 나갈 수 있을지 판단해보자"
)

# INFORMATION 텍스트 출력
def draw_wrapped_bold_text(surface, text, x, y, max_width, line_height):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test = current_line + word + " "
        if INFO_FONT.size(test)[0] > max_width:
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line = test
    lines.append(current_line)

    for i, line in enumerate(lines):
        r1 = INFO_FONT.render(line.strip(), True, WHITE)
        r2 = INFO_FONT.render(line.strip(), True, WHITE)
        surface.blit(r1, (x, y + i * line_height))
        surface.blit(r2, (x + 1, y + i * line_height))

# dialogue 시스템 (한 줄)
current_text = ""
displayed_text = ""
text_index = 0
typing_speed = 25
last_typing_time = 0
dialogue_active = False

def dialogue(text):
    global current_text, displayed_text, text_index, dialogue_active, last_typing_time
    current_text = text
    displayed_text = ""
    text_index = 0
    dialogue_active = True
    last_typing_time = pygame.time.get_ticks()

dialogue_list = [
    "......",
    "여긴 어디지?",
    "침대... 문... 촛불... 아무리 봐도 내가 알던 곳이 아니야.",
    "분명 무도회에서 술을 조금 마시고 잠들었을 뿐인데...",
    "하필이면 이런 방에 갇히다니.",
    "심장이 너무 빨리 뛴다.",
    "문은 잠겨 있고, 밖에서는 아무 소리도 들리지 않아.",
    "일단... 주변을 살펴봐야겠어."
]

dialogue_step = 0
dialogue(dialogue_list[0])
def draw_dialogue_line():
    x = 380
    y = HEIGHT - 120
    txt = FONT.render(displayed_text, True, WHITE)
    SCREEN.blit(txt, (x, y))

# ✅ 화면 그리기
def draw_screen():
    if MODE == "TITLE":
        SCREEN.blit(start_bg, (0, 0))
        for b in buttons_title:
            b.draw(SCREEN)

    elif MODE == "INFORMATION":
        SCREEN.blit(start_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill(DARK_OVERLAY)
        SCREEN.blit(dark, (0, 0))

        title = INFO_TITLE_FONT.render("INFORMATION", True, RED)
        SCREEN.blit(title, title.get_rect(center=(WIDTH // 2, 80)))

        draw_wrapped_bold_text(
            SCREEN, INFO_TEXT,
            120, 140,
            WIDTH - 240, 32
        )

        for b in buttons_info:
            b.draw(SCREEN)

    elif MODE == "GAME":
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)

        global displayed_text, text_index, last_typing_time, dialogue_active
        if dialogue_active:
            now = pygame.time.get_ticks()
            if now - last_typing_time > typing_speed:
                if text_index < len(current_text):
                    displayed_text += current_text[text_index]
                    text_index += 1
                    last_typing_time = now
                else:
                    dialogue_active = False

        draw_dialogue_line()

# ✅ 메인 루프
while True:
    CLOCK.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if MODE == "TITLE":
            for b in buttons_title:
                b.handle(event)

        elif MODE == "INFORMATION":
            for b in buttons_info:
                b.handle(event)

        elif MODE == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not dialogue_active:
                    dialogue_step += 1
                    if dialogue_step < len(dialogue_list):
                        dialogue(dialogue_list[dialogue_step])

    draw_screen()
    pygame.display.flip()
