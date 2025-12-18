import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# -----------------------------
# 화면 설정
# -----------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whispers Beyond The Wall")

CLOCK = pygame.time.Clock()
FPS = 60

# -----------------------------
# 색상 & 폰트
# -----------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 50, 50)
HOVER_RED = (255, 120, 120)
DARK_OVERLAY = (0, 0, 0, 180)
EPILOGUE_COLOR = (0, 60, 140)


FONT = pygame.font.Font("DOSGothic.ttf", 26)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 42)
INFO_FONT = pygame.font.Font("DOSGothic.ttf", 22)
INFO_TITLE_FONT = pygame.font.Font("DOSGothic.ttf", 40)
GAMEOVER_FONT = pygame.font.Font("DOSGothic.ttf", 120)
Q_FONT = pygame.font.Font("DOSGothic.ttf", 45)  # ??? 표시용

# -----------------------------
# 모드
# -----------------------------
MODE = "TITLE"   # TITLE → INFORMATION → GAME

# -----------------------------
# 사운드 로드
# -----------------------------
intro_bgm = "__1_3_intro.mp3"
bgm_4_22 = "__4_22 bgm.mp3"
walk_sfx = pygame.mixer.Sound("__24_walking.wav")
key_hold_sfx = pygame.mixer.Sound("__17_key_hold.wav")
key_put_sfx = pygame.mixer.Sound("__20_key_put.wav")
door_open_sfx = pygame.mixer.Sound("__22_open_door.wav")
stab_sfx = pygame.mixer.Sound("__25_stab.wav")
bgm_26_34 = "__26_34_bgm.m4a"
book_hold_sfx = pygame.mixer.Sound("__38_book_hold.wav")
book_open_sfx = pygame.mixer.Sound("__41_book_open.wav")
sound_48 = pygame.mixer.Sound("__48_sound.wav")
sound_gameover = pygame.mixer.Sound("__gameover.wav")
sound_50_52 = pygame.mixer.Sound("__50_52_sound.wav")
bgm_57_69 = "__57_69_bgm.mp3"
sound_68_rock = pygame.mixer.Sound("__68_rock.wav")
bgm_girl_cry = "__71_73_girl_cry.mp3"
sound_73_laugh = pygame.mixer.Sound("__73_laugh.wav")
sound_86_stab_king = pygame.mixer.Sound("__86_stab_king.wav")
sound_133_walk = pygame.mixer.Sound("__133_girl_walk.wav")
bgm_134_scream = "__134_girl_scream.mp3"
click_button_sfx = pygame.mixer.Sound("__click_button.wav")
sound_240_244 = "__240_244_sound.wav"

pygame.mixer.music.set_volume(0.5)

# -----------------------------
# 공통 배경 이미지
# -----------------------------
start_bg = pygame.transform.scale(
    pygame.image.load("start.png").convert(), (WIDTH, HEIGHT)
)
room_bg = pygame.transform.scale(
    pygame.image.load("room.png").convert(), (WIDTH, HEIGHT)
)
table_bg = pygame.transform.scale(
    pygame.image.load("table_selection1.png").convert(), (WIDTH, HEIGHT)
)
keyhole_bg_main = pygame.transform.scale(
    pygame.image.load("key hole_background.png").convert(), (WIDTH, HEIGHT)
)
hallway_bg = pygame.transform.scale(
    pygame.image.load("hallway_background.png").convert(), (WIDTH, HEIGHT)
)
gameover_bg = pygame.transform.scale(
    pygame.image.load("gameover_background.png").convert(), (WIDTH, HEIGHT)
)

# 문틈 배경
keyhole_bg2 = pygame.transform.scale(
    pygame.image.load("keyhole_key2.png").convert(), (WIDTH, HEIGHT)
)
king_eye_bg = pygame.transform.scale(
    pygame.image.load("keyhole_king1.png").convert(), (WIDTH, HEIGHT)
)

# 침대 아래, 감옥 복도, 왕 방 등
underbed_bg = pygame.transform.scale(
    pygame.image.load("underbed.png").convert(), (WIDTH, HEIGHT)
)
hand_img = pygame.transform.scale(
    pygame.image.load("hand.png").convert_alpha(), (400, 400)
)
hand_rect = hand_img.get_rect(center=(640, 550))

hall1_bg = pygame.transform.scale(
    pygame.image.load("enjail_background1.png").convert(), (WIDTH, HEIGHT)
)
hall2_bg = pygame.transform.scale(
    pygame.image.load("enjail_background2.png").convert(), (WIDTH, HEIGHT)
)
door_bg = pygame.transform.scale(
    pygame.image.load("king's place.png").convert(), (WIDTH, HEIGHT)
)
sleeping_bg = pygame.transform.scale(
    pygame.image.load("sleeping king.png").convert(), (WIDTH, HEIGHT)
)
underground_bg = pygame.transform.scale(
    pygame.image.load("underground_room.png").convert(), (WIDTH, HEIGHT)
)

# 지하 통로 / 계단 / 오른쪽 통로 / 괴물
underway_bg = pygame.transform.scale(
    pygame.image.load("underway.png").convert(), (WIDTH, HEIGHT)
)
stairway_bg = pygame.transform.scale(
    pygame.image.load("stairway.png").convert(), (WIDTH, HEIGHT)
)
underway_hall_bg = pygame.transform.scale(
    pygame.image.load("underway_hall.png").convert(), (WIDTH, HEIGHT)
)
underway_monster_bg = pygame.transform.scale(
    pygame.image.load("underway_monster.png").convert(), (WIDTH, HEIGHT)
)

# 왼쪽길 & 벽 글귀 배경 (140~149에서 사용)
leftway_bg = pygame.transform.scale(
    pygame.image.load("left way.png").convert(), (WIDTH, HEIGHT)
)
wall_bg = pygame.transform.scale(
    pygame.image.load("wall_written.png").convert(), (WIDTH, HEIGHT)
)

# 151~155용 추가 계단 배경
stair2_bg = pygame.transform.scale(
    pygame.image.load("additional stairway.png").convert(), (WIDTH, HEIGHT)
)

stair_bg = pygame.transform.scale(
    pygame.image.load("additional stairway.png").convert(), (WIDTH, HEIGHT)
)
bg_william = pygame.transform.scale(
    pygame.image.load("william_underway.png"), (WIDTH, HEIGHT)
)

bg_under = pygame.transform.scale(
    pygame.image.load("underroom_underway.png"), (WIDTH, HEIGHT)
)
william_bg = pygame.transform.scale(
    pygame.image.load("william_underway.png").convert(), (WIDTH, HEIGHT)
)

jeffrey_bg = pygame.transform.scale(
    pygame.image.load("Jeffrey_underway.png").convert(), (WIDTH, HEIGHT)
)

castle_outside = pygame.transform.scale(
    pygame.image.load("castle_outside.png").convert(), (WIDTH, HEIGHT)
)

castle_outside2 = pygame.transform.scale(
    pygame.image.load("castle_outside2.png").convert(), (WIDTH, HEIGHT)
)

# -----------------------------
# 탁자 위 아이템들
# -----------------------------
cup_img = pygame.transform.scale(
    pygame.image.load("cup_selection1.png").convert_alpha(), (170, 170)
)
notebook_img = pygame.transform.scale(
    pygame.image.load("notebook_selection1.png").convert_alpha(), (170, 170)
)
handkerchief_img = pygame.transform.scale(
    pygame.image.load("handkerchief_selection1.png").convert_alpha(), (170, 170)
)
key_img = pygame.transform.scale(
    pygame.image.load("key_selection1.png").convert_alpha(), (150, 150)
)

cup_rect      = cup_img.get_rect(center=(320, 360))
notebook_rect = notebook_img.get_rect(center=(640, 360))
handker_rect  = handkerchief_img.get_rect(center=(960, 360))
key_rect      = key_img.get_rect(center=(640, 200))

# 공책 루트용 이미지
notebook_table_img = pygame.transform.scale(
    pygame.image.load("notebook_selection1.png").convert_alpha(), (280, 280)
)
notebook_table_rect = notebook_table_img.get_rect(center=(960, 360))

notebook_big_img = pygame.transform.scale(
    pygame.image.load("notebook_selection1.png").convert_alpha(), (500, 500)
)
notebook_big_rect = notebook_big_img.get_rect(center=(640, 330))

paper_raw = pygame.image.load("paper.png").convert_alpha()
PAPER_W = WIDTH // 3
ratio_p = PAPER_W / paper_raw.get_width()
PAPER_H = int(paper_raw.get_height() * ratio_p)
paper_img = pygame.transform.scale(paper_raw, (PAPER_W, PAPER_H))
paper_rect = paper_img.get_rect(center=(330, 330))

# -----------------------------
# 채팅 박스 & 선택 박스
# -----------------------------
chatbox_img = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (WIDTH, 200)
)
choice_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (400, 110)
)
select_box_large = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (400, 120)
)

# -----------------------------
# 공통 선택 위치
# -----------------------------
select_rect = choice_box.get_rect(center=(640, 610))
select_retry_rect = select_box_large.get_rect(center=(640, 450))

# 공책 루트 선택 위치
select_41_rect = choice_box.get_rect(center=(1000, 600))
choice_left_rect = choice_box.get_rect(center=(420, 400))
choice_right_rect = choice_box.get_rect(center=(860, 400))

# 돌판 루트 선택 위치
select75_rect = select_box_large.get_rect(center=(WIDTH // 2, 540))
select81_left_rect  = select_box_large.get_rect(center=(WIDTH // 2 - 220, 540))
select81_right_rect = select_box_large.get_rect(center=(WIDTH // 2 + 220, 540))

# 침대 아래(63) 선택 위치
choice1_rect = select_box_large.get_rect(center=(240, 360))
choice2_rect = select_box_large.get_rect(center=(640, 360))
choice3_rect = select_box_large.get_rect(center=(1040, 360))

# 92~98 열쇠 홈 선택
key_under_img = pygame.transform.scale(
    pygame.image.load("key hole_key.png").convert_alpha(), (220, 150)
)
key_under_rect = key_under_img.get_rect(center=(660, 460))
select_92_rect = select_box_large.get_rect(center=(1100, 550))
choice98_left_rect = select_box_large.get_rect(center=(500, 520))
choice98_right_rect = select_box_large.get_rect(center=(900, 520))

# 109~118 갈래길 선택 박스
choice118_top_rect  = select_box_large.get_rect(center=(640, 300))   # 위쪽 길
choice118_left_rect = select_box_large.get_rect(center=(350, 550))   # 왼쪽 길
choice118_right_rect= select_box_large.get_rect(center=(930, 550))   # 오른쪽 길

# 127~138 오른쪽 길 선택
choice131_left_rect = select_box_large.get_rect(center=(430, 520))
choice131_right_rect = select_box_large.get_rect(center=(850, 520))
select_retry_box_138 = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (400, 120)
)
select_retry_rect_138 = select_retry_box_138.get_rect(center=(640, 500))

# 149 왼쪽길 세 갈래 선택창
choice149_left_rect  = select_box_large.get_rect(center=(260, 520))
choice149_mid_rect   = select_box_large.get_rect(center=(640, 520))
choice149_right_rect = select_box_large.get_rect(center=(1020, 520))
choice_mid_rect = select_box_large.get_rect(center=(640, 520))

# 155 "다시 진행" 선택창
select_retry_rect_155 = select_box_large.get_rect(center=(640, 500))

# 177 GAME OVER에서 쓸 다시 진행 버튼 위치
retry_rect = select_box_large.get_rect(center=(640, 500))

choice_left  = choice_box.get_rect(center=(420, 520))
choice_right = choice_box.get_rect(center=(900, 520))

choice_texts = [
    "윌리엄을 믿고\n그의 목소리를 따라간다.",
    "제프리를 믿고 그의 뒤로 서며\n지하실 다른 출구로 향한다."
]

# -----------------------------
# 캐릭터 / 왕 / 키 / 피 이미지
# -----------------------------
elenore_raw = pygame.image.load("Elenore.png").convert_alpha()
ELENORE_HEIGHT = 620
ratio_e = ELENORE_HEIGHT / elenore_raw.get_height()
ELENORE_WIDTH = int(elenore_raw.get_width() * ratio_e)
elenore_img = pygame.transform.scale(elenore_raw, (ELENORE_WIDTH, ELENORE_HEIGHT))
ELENORE_POS = (-200, HEIGHT - ELENORE_HEIGHT)

keyhole_key_raw = pygame.image.load("key hole_key.png").convert_alpha()
KH = 150
ratio_k = KH / keyhole_key_raw.get_height()
KW = int(keyhole_key_raw.get_width() * ratio_k)
keyhole_key_img = pygame.transform.scale(keyhole_key_raw, (KW, KH))

blood_img = pygame.transform.scale(
    pygame.image.load("blood.png").convert_alpha(), (WIDTH, HEIGHT)
)

# 돌판 루트 추가 캐릭터 & 피
elenore2_raw = pygame.image.load("Elenore2.png").convert_alpha()
ELENORE2_HEIGHT = 800
ratio_e2 = ELENORE2_HEIGHT / elenore2_raw.get_height()
ELENORE2_WIDTH = int(elenore2_raw.get_width() * ratio_e2)
elenore2_img = pygame.transform.scale(elenore2_raw, (ELENORE2_WIDTH, ELENORE2_HEIGHT))
ELENORE2_POS = (WIDTH // 2 - ELENORE2_WIDTH // 2, HEIGHT - 350 - ELENORE2_HEIGHT // 2)

elenore3_raw = pygame.image.load("Elenore3.png").convert_alpha()
ELENORE3_HEIGHT = 620
ratio_e3 = ELENORE3_HEIGHT / elenore3_raw.get_height()
ELENORE3_WIDTH = int(elenore3_raw.get_width() * ratio_e3)
elenore3_img = pygame.transform.scale(elenore3_raw, (ELENORE3_WIDTH, ELENORE3_HEIGHT))

blood2_img = pygame.transform.scale(
    pygame.image.load("blood2.png").convert_alpha(), (900, 500)
)
blood2_rect = blood2_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))

# 제프리
jeff_raw = pygame.image.load("Jeffrey.png").convert_alpha()
JEFF_H = 620
ratio_j = JEFF_H / jeff_raw.get_height()
JEFF_W = int(jeff_raw.get_width() * ratio_j)
jeff_img = pygame.transform.scale(jeff_raw, (JEFF_W, JEFF_H))
JEFF_POS = (0, HEIGHT - JEFF_H)

ELEN_SCENES = {225, 227, 232}
JEFF_SCENES = {229, 234, 235, 238}

# -----------------------------
# 씬 13 선택지 좌표 (2x2)
# -----------------------------
choice13_rects = []
choice_w, choice_h = choice_box.get_size()
margin_x = 80
margin_y = 40
start_x = (WIDTH - (choice_w * 2 + margin_x)) // 2
start_y = 220

for row in range(2):
    for col in range(2):
        x = start_x + col * (choice_w + margin_x)
        y = start_y + row * (choice_h + margin_y)
        choice13_rects.append(pygame.Rect(x, y, choice_w, choice_h))

# -----------------------------
# INFORMATION 텍스트
# -----------------------------
INFO_TEXT = (
    "아주 큰 미지존재 처리 회사를 운영하는 아버지를 둔 엘리노어(당신)는 "
    "사랑하는 연인 윌리엄과 함께 행복한 날들을 보내고 있었다. 하지만 점점 "
    "미지의 존재가 세계를 위협하게 되며 국왕은 그들을 처리할 방법을 고민하다가, "
    "엘리노어의 아버지와 자신의 아들을 결혼 시켜 비용 들이지 않고 괴물들을 처리할 "
    "방법을 생각하게 된다. 그리고 시간이 지나 실제로 계약은 이행된다. "
    "엘리노어는 자신의 실제 연인인 윌리엄과의 사랑을 포기할 수 없었고 급기야 "
    "도망 계획을 세우게 된다. 하지만 하늘도 무심하게 그 계획은 그녀의 아버지와 "
    "국왕에게 걸리게 되었고 엘리노어는 국왕에게 밉보이게 된다.\n\n"
    "그런데 이게 무슨 일 일까, 국왕이 주최한 무도회에 참석을 하였다가 술을 좀 먹고 "
    "잠에 들었는데 눈 떠보니 엘리노어는 너무 낯선 곳에 갇혀있는 상태였다. "
    "이젠 어떻게 하면 좋을까?\n\n"
    "당신은 이 방을 탈출해야한다. 당신의 선택에 따라 모든게 뒤바뀐다. "
    "어서 이야기 속으로 들어가서 어떻게 해야 나갈 수 있을지 판단해보자."
)

def draw_wrapped_bold_text(surface, text, x, y, max_width, line_height):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if INFO_FONT.size(test_line)[0] > max_width:
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line = test_line
    lines.append(current_line)

    for i, line in enumerate(lines):
        r1 = INFO_FONT.render(line.strip(), True, WHITE)
        r2 = INFO_FONT.render(line.strip(), True, WHITE)
        surface.blit(r1, (x, y + i * line_height))
        surface.blit(r2, (x + 1, y + i * line_height))

# -----------------------------
# 버튼 시스템 (TITLE/INFO)
# -----------------------------
class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.callback = callback
        self.rect = BIG_FONT.render(text, True, RED).get_rect(center=pos)

    def draw(self, surface):
        txt = BIG_FONT.render(self.text, True, RED)
        self.rect = txt.get_rect(center=self.rect.center)  # 위치 유지
        surface.blit(txt, self.rect)

    def handle(self, event):
        # 오직 '클릭'만 처리
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                play_sfx(click_button_sfx)  # 클릭 사운드
                self.callback()
        # --- Click 처리 ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                play_sfx(click_button_sfx)  # 클릭 소리
                self.callback()

def fade_to_mode(next_mode):
    global MODE
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0, 0, 0))

    for alpha in range(0, 255, 10):
        fade.set_alpha(alpha)
        SCREEN.fill(BLACK)
        draw_screen()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(60)

    MODE = next_mode

    for alpha in range(255, -1, -10):
        fade.set_alpha(alpha)
        SCREEN.fill(BLACK)
        draw_screen()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(60)

def start_game():
    fade_to_mode("GAME")

def open_info():
    fade_to_mode("INFORMATION")

def close_info():
    fade_to_mode("TITLE")

start_button = Button("START", (WIDTH // 2, HEIGHT // 2 + 180), start_game)
info_button = Button("INFORMATION", (WIDTH // 2, HEIGHT // 2 + 250), open_info)
back_button = Button("BACK", (WIDTH // 2, HEIGHT - 100), close_info)

buttons_title = [start_button, info_button]
buttons_info = [back_button]

# -----------------------------
# 타자기 시스템 (공통)
# -----------------------------
current_text = ""
displayed_text = ""
text_index = 0
typing_speed = 25
last_typing_time = 0
dialogue_active = False

def start_typing(text_or_lines):
    """문자열 또는 문자열 리스트를 타자기 출력으로 준비"""
    global current_text, displayed_text, text_index, dialogue_active, last_typing_time
    if isinstance(text_or_lines, list):
        current_text = "\n".join(text_or_lines)
    else:
        current_text = str(text_or_lines)
    displayed_text = ""
    text_index = 0
    dialogue_active = True
    last_typing_time = pygame.time.get_ticks()

def update_typing():
    """한 글자씩 출력"""
    global displayed_text, text_index, dialogue_active, last_typing_time, current_text
    if not dialogue_active:
        return
    now = pygame.time.get_ticks()
    if now - last_typing_time > typing_speed:
        if text_index < len(current_text):
            displayed_text += current_text[text_index]
            text_index += 1
            last_typing_time = now
        else:
            dialogue_active = False

# -----------------------------
# 대사 출력 함수
# -----------------------------
def draw_game_scene_with_char():
    SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
    SCREEN.blit(elenore_img, ELENORE_POS)
    x = 380
    y = HEIGHT - 130
    for i, line in enumerate(displayed_text.split("\n")):
        SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

def draw_game_scene_no_char():
    SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
    x = 60
    y = HEIGHT - 130
    for i, line in enumerate(displayed_text.split("\n")):
        SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

def draw_select_text_box(rect, text, color=BLACK):
    lines = text.split("\n")
    if len(lines) == 1:
        txt = FONT.render(lines[0], True, color)
        SCREEN.blit(txt, txt.get_rect(center=rect.center))
    else:
        total_h = len(lines) * 28
        base_y = rect.centery - total_h // 2
        for i, line in enumerate(lines):
            t = FONT.render(line, True, color)
            t_rect = t.get_rect(center=(rect.centerx, base_y + i * 28))
            SCREEN.blit(t, t_rect)

def draw_keyhole_dialogue(scene_id):
    SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
    x = 380
    y = HEIGHT - 120
    for i, line in enumerate(displayed_text.split("\n")):
        if scene_id in (51, 103):  # 효과주는 장면
            t1 = FONT.render(line, True, RED)
            t2 = FONT.render(line, True, RED)
            SCREEN.blit(t1, (x, y + i * 32))
            SCREEN.blit(t2, (x + 2, y + i * 32))
        else:
            SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

def draw_game_scene_line():
    x = 60
    y = HEIGHT - 150
    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))

def draw_game_scene_line_with_offset(has_char):
    # 기본 위치
    x = 60
    if has_char:
        x = 380   # 캐릭터가 나타나면 오른쪽으로 이동

    y = HEIGHT - 150

    for i, line in enumerate(displayed_text.split("\n")):
        txt = FONT.render(line, True, WHITE)
        SCREEN.blit(txt, (x, y + i * 32))

def draw_select_text(rect, text, color=BLACK):
    lines = text.split("\n")
    total_h = len(lines) * 28
    base_y = rect.centery - total_h // 2
    
    for i, line in enumerate(lines):
        t = FONT.render(line, True, color)
        SCREEN.blit(
            t,
            (rect.centerx - t.get_width() // 2, base_y + i * 28)
        )

jeff_scenes = {179, 182, 184, 193, 195, 197}
elen_scenes = {187, 188, 191}

def draw_gameover_ui():
    # "GAME OVER" 텍스트
    t1 = GAMEOVER_FONT.render("GAME", True, RED)
    t2 = GAMEOVER_FONT.render("OVER", True, RED)
    SCREEN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
    SCREEN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 260))

    # 다시 선택 버튼
    SCREEN.blit(select_box_large, retry_rect)
    draw_select_text_box(retry_rect, "다시 선택", BLACK)

# -----------------------------
# 랜덤 ??? (문틈 & 100 루트 공용)
# -----------------------------
random_q_positions = []

def generate_random_questions(count=40):
    arr = []
    for _ in range(count):
        x = random.randint(50, 1230)
        y = random.randint(50, 670)
        arr.append((x, y))
    return arr

def draw_random_questions():
    for (x, y) in random_q_positions:
        txt = Q_FONT.render("???", True, RED)
        SCREEN.blit(txt, (x, y))

# -----------------------------
# 인트로 (1~13)
# -----------------------------
intro_dialogues = {
    1: "......",
    2: "여긴 어디지?",
    3: "침대... 문... 촛불... 아무리 봐도 내가 알던 곳이 아니야.",
    4: "분명 무도회에서 술을 조금 마시고 잠들었을 뿐인데...",
    5: "하필이면 이런 방에 갇히다니.",
    6: "심장이 너무 빨리 뛴다.",
    7: "문은 잠겨 있고, 밖에서는 아무 소리도 들리지 않아.",
    8: "일단... 주변을 살펴봐야겠어.",
    9: "조용하지만 어딘가에서 낮은 속삭임 같은 소리가 들린다.",
    10: "어둠 속 사물들만이 날 지켜보고 있는 것 같다.",
    11: "...",
    12: "그래도 무언가 단서가 있을 거야.",
    13: "어디부터 조사해볼까?",
}

scene9_text_lines = [
    "조용하지만 어디선가 속삭임 같은 낮은 울음소리가 벽 너머에서 흘러온다.",
    "내가 주변을 둘러보자 작은 탁자 하나가 눈에 들어왔다."
]

choices13 = [
    "침대 아래를 살펴본다. (찐)",
    "탁자 위 열쇠를 확인한다.",
    "문틈으로 밖의 움직임을 확인한다.",
    "작은 공책을 펼쳐본다.",
]

# -----------------------------
# 열쇠 루트 21~30
# -----------------------------
dialogues_21_30 = {
    21: ["???: 덜컥, 끼이--익....."],
    22: ["“뭐지.. 문이 이렇게 쉽게 열리다니.”", "한 번 문을 열고 나가보자."],
    23: [
        "문을 열자 보이는 것은 매우 넓은 복도였다.",
        "앞의 문에 정신이 팔려 이제 되었다는 안도감과 벅차오름에",
        "잠시 멍을 때리고 있었다."
    ],
    24: ["???: 터벅-, 터벅-"],
    25: ["???: 휙- 탁!, 푹- (칼로 찌르는 소리)"],
    26: [
        "등에서 따듯한 느낌과 함께 무언가 흘러내린다.",
        "내 피인건가 장기인건가...",
        "뒤를 돌아보자 왕이 내 뒤에 서 있다."
    ],
    27: [
        "“내 딸과 같은 엘레노어, 넌 늘 똑똑한 아이였지.",
        "그래서 내가 널 내 아들 제프리와 결혼시키려 한거란다.",
        "하지만 엘레노어, 네가 이렇게까지 결혼하기 싫어한다면…"
    ],
    28: [
        "지금쯤이면 내가 보낸 사람에 의해 네 사랑 윌리엄도 죽었을거네.",
        "웃기지 않은가? 자기가 사랑하는 여자 하나 못지키다니.",
        "둘이 함께 하늘에서 평안하길 비네."
    ],
    29: [
        "“Knights, to me!, 이 여자 들고가서 태워!",
    ],
    30: [
        "이제 진짜 끝이구나...",
        "아... 윌리엄..."
    ]
}

dialogue_18_lines = ["좋아, 이 열쇠… 여기에 맞을지도 몰라."]

key_start    = pygame.Vector2(640, 200)
key_hole_pos = pygame.Vector2(440, 300)
key_pos      = key_start.copy()
key_anim     = False

def fade_out_game():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for a in range(0, 255, 25):
        fade.set_alpha(a)
        SCREEN.fill(BLACK)
        draw_screen()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(FPS)

def fade_in_game():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)
    for a in range(255, -1, -25):
        fade.set_alpha(a)
        SCREEN.fill(BLACK)
        draw_screen()
        SCREEN.blit(fade, (0, 0))
        pygame.display.flip()
        CLOCK.tick(FPS)

def draw_keyroute_dialogue(scene_id: int):
    SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
    char = None
    if scene_id == 18:
        char = "elenore"
    elif 27 <= scene_id <= 29:
        char = "king"

    color = RED if 24 <= scene_id <= 29 else WHITE
    x = 260 if char is None else 380
    y = HEIGHT - 160

    lines = displayed_text.split("\n")

    for i, line in enumerate(lines):
        if 24 <= scene_id <= 29:
            t1 = FONT.render(line, True, color)
            t2 = FONT.render(line, True, color)
            SCREEN.blit(t1, (x, y + i * 32))
            SCREEN.blit(t2, (x + 2, y + i * 32))
        else:
            t = FONT.render(line, True, color)
            SCREEN.blit(t, (x, y + i * 32))

    if char == "elenore":
        SCREEN.blit(elenore_img, ELENORE_POS)

# -----------------------------
# 사운드 재생 함수
# -----------------------------
def play_bgm(path, loop=True):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1 if loop else 0)

def stop_bgm():
    pygame.mixer.music.stop()

def play_sfx(sound):
    sound.play()

def play_bgm_once(path):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)  # 1회 재생

# -----------------------------
# 공책 루트 36~44
# -----------------------------
dialogues_notebook = {
    40: [
        "엘리노어는 오래된 침실 한가운데에서 먼지로 덮인 작은 공책을 펼쳤다.",
        "종이는 누렇게 바랬지만 필체는 놀라울 정도로 정확했다.",
        "누군가 이곳에 갇히기 전 기록으로 보인다.",
    ],
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
}

# -----------------------------
# 문틈 루트 46~55
# -----------------------------
typing_dialogues_keyhole = {
    46: ["“열쇠구멍으로 뭐가 있는지 확인해 보아야겠어.”"],
    49: ["?????????????????????????????????????????????????????"],
    50: ["너무 놀라 비명을 지를 수 도 없다.", "내 손과 발이 떨린다."],
    51: ["덜컥,,끼이이--익,,,"],
}

dialogue_53_lines = [
    "당신은 열쇠구멍을 들여다보곤 뒤로 넘어졌다.",
    "열쇠구멍으로 보이는 모습은 국왕인 것 같았다.",
    "그는 당신이 패닉에 빠져 아무것도 못하자, 문을 천천히 열고 들어와",
    "혼자 소리를 지르고, 자신이 원하는대로 행동하기만 했어도",
    "이런일은 일어나지 않았을 것이라고 했다.",
    "그 모습은 한 나라의 국왕이 아닌 정신 이상자 같았다.",
    "당신은 너무 무서워 달아나고 싶었지만, 결국",
    "그가 당신의 목을 칼로 찔렀고 사망하게 됐다.",
]
dialogue_55_last = "지켜보고 있을 줄이야,,,"

# -----------------------------
# 침대 아래 루트 57~63
# -----------------------------
dialogues_underbed = {
    57: ["“뭐가 있는지 한 번 봐야겠어..”"],
    58: [
        "나는 조심스럽게 침대 아래에 몸을 숙였다.",
        "손 끝이 차가운 돌 표면을 스치자, 작은 떨림이 손목을 타고 올라온다."
    ],
    60: ["“어..! 뭐지?”"],
    61: [
        "손 끝에 미세하게 감각이 다른 돌 판이 만져졌다.",
        "가운데에 손바닥만 한 흠이 파여있다.",
        "마치 무언가를 여기에 넣으라는 듯한 형태다.",
    ],
    62: [
        "그 순간 갑자기 또 벽 뒤에서 탁- 탁- 거리는 소리가 들리기 시작했다.",
        "“난 뭘 해야 하지?”"
    ],
}

dialogue_65_lines = [
    "“침대에서 유일하게 살아있는 듯 보이는 곳은… 여기뿐인데.”",
    "“도대체 어떻게 해야 하지…?”"
]

# -----------------------------
# 돌판 루트 67~90
# -----------------------------
dialogues_67_90 = {
    67: ["으... 으... 너무 무거워..!"],
    68: ["??? (돌 판이 부러지는 소리)"],
    70: [
        "당신은 돌 판을 들어 올리려 했지만 결국 부러지고 말았다.",
        "그 돌 판은 왕의 감시를 피할 수 있는 유일한 루트였다."
    ],
    72: ["너무 원망스러워.."],
    74: [
        "“이렇게 하는 수밖에 없어요… 윌리엄을 위해서라도.”",
        "“전 이렇게 하지 않으면 버틸 수 없어요.”"
    ],
    77: ["근위병: 엘리노어님, 여긴 들어오시면 안 됩니다."],
    78: ["“अ, 잠깐 볼 일이 있어서요.”"],
    80: ["“어쩜 이리도 잘 주무시는지 참...”"],
    83: ["“어쩜 이리도 잘 주무시는지 참...”"],
    86: ["푸-욱...!  (사람들 비명소리)"],
    88: [
        "국왕은 즉사했다.",
        "근위병들은 즉시 당신을 체포했고 당신은 고문을 받게 된다."
    ]
}

# -----------------------------
# 92~98 열쇠 홈 사용 루트
# -----------------------------
dialogues_92_98 = {
    93: ["???끼이익...."],
    94: [
        "나는 떨리는 숨을 고르고, 열쇠를 홈 위에 맞춰보았다.",
        "딱— 소리와 함께 무언가 맞물리는 소리가 났다.",
        "그리고 바닥이 부드럽게 아래로 내려가기 시작했다."
    ],
    95: [
        "곧, 침대 아래 어둠 속에서 계단 입구가 열렸다.",
        "서늘한 바람이 위로 밀려 올라온다."
    ],
    96: [
        "???: “...엘리노어, 여기야...”"
    ],
    97: [
        "하지만, 갑자기 복도에서 쇠사슬 끌리는 소리가 멈춘다.",
        "누군가 문 앞을 스친 것 같다."
    ],
}

# -----------------------------
# 100~106 문 쪽 확인 DEAD END 루트
# -----------------------------
dialogues_100_106 = {
    100: ["“그래, 먼저 문 쪽에서 들린 소리가 뭐였는지 확인 해 봐야겠어.”"],
    102: ["?????????????????????????????????????????????????????"],  # 102
    103: ["덜컥,,끼이이--익,,,"],
}
dialogue_105 = [
    "당신은 열쇠구멍을 들여다 보곤 깜짝놀라, 뒤로 자빠졌다.",
    "열쇠구멍으로 보이는 모습은 국왕인 것 같았다.",
    "그는 당신이 패닉에 빠져 아무것도 못하자, 문을 천천히 열고 들어와",
    "혼자 소리를 지르고, 자신이 원하는대로 행동하기만 했어도",
    "이런일은 일어나지 않았을 것이라고 했다.",
    "그 모습은 한 나라의 국왕이 아닌 정신 이상자 같았다.",
    "당신은 너무 무서워 달아나고 싶었지만, 결국",
    "그가 당신의 목을 칼로 찔렀고 사망하게 됐다.",
]

# -----------------------------
# 109~118 계단 내려가는 루트
# -----------------------------
dialogues_109_116 = {
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

# -----------------------------
# 120~125 다시 위로 올라가려는 루트
# -----------------------------
dialogues_120_122 = {
    120: ["“그냥 다시 올라가야겠어, 너무 무서워..”"],
    121: [
        "그때, 어디선가 묵직한 발걸음 소리가 들렸다.",
        "그 소리는 점점 나에게 가까워지고 있었다.",
    ],
    122: [
        "걸음을 멈추자, 국왕은 시뻘건 눈을 하곤 날 노려보고 있었다.",
        "그의 오른손에는 칼이 쥐어져 있었다.",
    ],
}
dialogue_124 = [
    "당신은 왕을 피해 도망치려 했지만, 계단에서 미끄러져 크게 넘어졌다.",
    "부러진 다리의 통증에 몸을 일으키지도 못한 채 바닥에 쓰러져 있었다.",
    "왕은 천천히 다가오며 비웃듯 큰 소리를 냈고, 당신을 내려다보았다.",
    "그리고 아무 망설임 없이 배를 깊숙이 찔러버렸다.",
    "그렇게 왕은 계단을 유유히 올라갔고, 당신은 서서히 죽어갔다.",
]

# -----------------------------
# 127~138 오른쪽 길 + 상자에 숨는 루트
# -----------------------------
dialogues_127_130 = {
    127: ["그래, 오른쪽 길로 한 번 가보자"],
    128: ["나는 조용히 침대 아래로 몸을 굴려 내려가", "어둡고 좁은 오른쪽 통로로 발을 들였다."],
    129: ["???: 딸칵...딸칵..."],
    130: ["지하에 있는 무언가가 급속도로 나에게 다가오는 소리가 들렸다.", "어떻게 해야 할지 빨리 결정을 해야 한다."],
}
typing_dialogues_2 = {
    133: ["저… 저게… 뭐지…"],
    134: ["으아…!!"],
}
dialogue_136 = [
    "당신은 겁에 질려 뒤로 물러났지만, 괴물은 순식간에 당신의 목을 잡아채며",
    "당신을 벽에 강하게 내던졌다. 그 충격으로 당신은 정신을 잃었고,",
    "괴물은 당신의 몸을 질질 끌고 어둠 속으로 사라졌다.",
]

# -----------------------------
# 140~149 왼쪽 길 루트 대사
# -----------------------------
dialogues_left_route = {
    140: [
        "“그래, 왼쪽 길로 한 번 가보자.”",
    ],
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

# -----------------------------
# 151~155 윌리엄 목소리 루트 (추가)
# -----------------------------
dialogues_151_155 = {
    151: [
        "“아무래도 윌리엄의 목소리를 따라가 보아야겠어..!”",
    ],
    152: [
        "“뭐지..? 여기보다 더 내려가야 하나, 이미 너무 깊게 내려 왔는데...”",
    ],
}

story_153 = [
    "당신은 닿을 수 없는 목소리에 닿고 싶어, 그 목소리를 향해 계속해서",
    "아래로 내려갔지만 그곳에는 아무도 없었다. 하지만 당신은 이미 지하",
    "깊은 곳에서 너무 많은 길을 헤집고 다녔고, 지도도 없었기에 영원히",
    "그 곳에 갇혀서 결국은  3개월 후 아사하게 되었다.",
]

dialogues_157 = {
    157: ["“여기에 분명 무슨 장치가 있을 거야!”"],
    158: ["하지만 나의 기대와 달리 아무것도 없었다. (다시 선택창)"]
}

dialogues_160 = {
    160: [
        "나는 숨을 억누르며 윌리엄의 목소리에 반응하지 않기로 결심했다.",
        "그의 목소리는 너무 자연스러웠고, 너무 가까웠다.",
        "그래서 오히려... 진짜가 아닐 가능성이 더 컸다."
    ],
    161: [
        "촛불을 최대한 가리고 조용히 발걸음을 옮기자,",
        "그 목소리는 계속 뒤에서 다정하게 속삭였다."
    ],
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
    168: [
        "그 안은 고대 문양이 새겨진 기둥들과 오래된 사슬들,",
        "그리고 반쯤 부서져 먼지가 내려앉은 상자들이 널브러져 있었다.",
        "가운데 작은 책상 하나가 놓여 있었고,",
        "그 위엔 ‘제프리’라는 이름 태그가 놓여 있었다."
    ],
    169: ["그때, 지하실 구석에서 낮고 건조한 목소리가 작게 울렸다."],
    170: ["???: ...늦었군."],
    171: [
        "어둠 속에서 누군가 걸어 나왔다.",
        "그의 표정은 무심했지만 눈빛만은 흔들리고 있었다."
    ]
}

dialogues_174 = {
    174: [
        "“아무리 생각해도 여긴 믿을 수 있는 사람이 없어,”",
        "“빨리 어디든 돌아다녀 보자..!”"
    ],
    175: [
        "당신은 그를 지나쳐 지하실 반대편 통로로 다시 향해 지하실을",
        "헤집고 돌아다녔지만, 미로 같은 지하실을 빠져 나오지 못하였다.",
        "당신은 지하실에 갇힌 채로 있다가 3개월 후 아사하게 되었다."
    ]
}

dialogues_179 = {
    179: ["“난, 당신의 정략결혼 상대인 제프리라고 한다. 그러니 너무 겁내지 마시오.”"],
    180: [
        "돌바닥이 차갑게 발끝을 스치고, 촛불이 흔들리며 그의 얼굴을 비췄다.",
        "그의 표정은 무심했지만, 입가가 엷게 일그러져 있었다.",
        "그리고 잠깐 떨린 눈동자가... 무언가를 숨기고 있었다."
    ],
    181: ["그는 나의 뒷걸음질을 눈치채곤 말했다."],
    182: ["“난..그저 왕이 오기 전에 그대를 내보내려고 했다.”"],
    183: ["목소리는 낮아졌고, 다음 말은 더 이상한 방향으로 흘렀다."],
    184: ["“그대가..윌리엄의 목소리를 무시하고 계단을 택할 줄 알고 있었다.”"],
    185: ["나는 순간 심장이 철렁 내려앉았다. 그는 그 ‘존재’의 목소리를 알고 있다."],
    186: ["그는 한 발 앞으로 내딛었고, 설명할 수 없는 긴장감이 따라왔다."],
    187: ["나는 촛불을 꽉 쥔다. 그리고 그에게 말했다."],
    188: [
        "“책상 위 태그도, 생김새도.. 당신이 바로 제프리였군요?",
        "제 약혼자이자 제가 이 성에 감금된 원인.”"
    ],
    189: ["...."],
    190: [
        "하지만 그의 정체보다 방금 그가 한 말을 넘길 수 없었다.",
        "나는 낮은 목소리로 물었다."
    ],
    191: ["“그 목소리.. 당신은 알고 있었죠? 그게 뭐였는지.”"],
    192: [
        "제프리는 말이 없었다. 공기가 차갑게 내려앉았다.",
        "그는 바닥을 보다 고개를 들어 작은 목소리로 말했다."
    ],
    193: ["“그건... 왕의 성이 품고 있는 또 다른 주인입니다.”"],
    194: ["나는 목덜미가 서늘해졌다. 제프리는 말을 이어갔다."],
    195: ["“그 존재는 당신을 끌어들이기 위해 윌리엄의 목소리를 흉내 낸 것입니다.”"],
    196: ["표정은 담담했지만, 그의 목소리는 떨리고 있었다."],
    197: [
        "“그 존재는 오래전부터 당신을 알고 있었소.",
        "당신 아버지를 협박하기 위한 목적이지요.”"
    ],
    198: ["지하실 어둠 속에서 또렷한 윌리엄의 목소리가 울렸다."],
    199: [
        "???: “엘리노어... 그 자와 있지 마!",
        "속으면 안돼! 다시 내게 와!”"
    ],
    200: ["제프리는 즉시 이를 악물고 외쳤다."],
    201: ["“듣지 마시오! 그건 윌리엄이 아닙니다!”"],
}

dialogues_204 = {
    204: [
        "나는 제프리의 경고를 무시하고, 윌리엄의 목소리를 따라가기로 결정했다.",
        "그 목소리는 너무 익숙하고 따듯해, 정말 그가 손을 내밀고 있을 것 같았다.",
    ],
    205: [
        "하지만 이 선택이 위험하다는 것도 알고 있었다.",
        "난 조심스레 목소리가 올라온 방향으로 걸어갔다.",
    ],
    206: [
        "나는 이미 지하실 깊은 통로로 들어서 있었다.",
        "차갑고 축축한 공기가 피부에 달라붙고 촛불은 위태롭게 흔들렸다.",
    ],
    207: [
        "그때- 앞쪽에서 아주 선명한 남자의 목소리가 들려왔다.",
    ],
    208: [
        "???: “엘리노어... 그래, 잘 왔어! 나야, 정말 나야...!”",
    ],
    209: [
        "너무 익숙한 목소리, 하지만 뭔가 이상했다.",
        "웃음과 어조는 같았지만...",
    ],
    210: [
        "통로 깊숙한 곳에서 형체가 손을 내밀고 있었다.",
        "하지만 어둠 속이라 얼굴은 잘 보이지 않았다.",
    ],
    211: [
        "???: “왜 겁내? 나야 엘리노어, 드디어 우리 둘이 만났잖아.”",
    ],
    212: [
        "뒤에서 제프리가 날 향해 소리쳤다.",
    ],
    213: [
        "“그건 살아있는 것이 아닙니다! 돌아오시오!”",
    ],
    214: [
        "하지만 그 존재는 부드럽게 웃으며 속삭였다.",
    ],
    215: [
        "???: “널 한참 동안 찾아 헤맸지... 드디어 찾았네.”",
    ],
}

dialogues_218 = {
    218: ["윌리엄 나도 널 너무 보고싶었어... 난 널 선택할래..."],
    220: [
        "당신이 윌리엄이라고 생각한 것은, 너무 위험해 성 아래에 감금하였던 괴물이었다.",
        "이 괴물은 당신의 아버지가 젊었을 때 직접 사냥해 왕에게 바쳤고,",
        "그 이후 사업이 승승장구하였다. 하지만 괴물은 평생 당신 아버지를 저주하며",
        "결국 그의 딸인 당신을 죽기 위해 손에 넣었다.",
        "그렇게 당신은 고통스럽게 죽었다.",
    ],
}

dialogues_225 = {
    225: [
        "“하... 아무리 생각해도 제프리는",
        "거짓말하지 않는 것 같아.”",
    ],
    226: [
        "나는 그렇게 제프리의 뒤에 서서 걸음을 옮겼다.",
        "통로 끝에서 무언가 이상한 형체가 희미하게 보였다.",
    ],
    227: [
        "“저기... 무언가가 있어요.",
        "윌리엄의 목소리를 가진 존재.. 너무 이상해요.”",
    ],
    228: [
        "그는 잠시 눈을 감았다가 떴다.",
        "그의 표정은 평소처럼 무심하지만, 눈 끝이 날카롭게 빛났다.",
    ],
    229: [
        "“...알고 있었다.. 성벽 너머의 속삭임,",
        "그 존재는 너를 증오하는 자고 목소리를 흉내 낼 수 있다.",
        "당신이 아는 윌리엄 목소리도, 그 존재가 흉내낸 것 뿐이다.”",
    ],
    230: [
        "나는 안도의 한숨을 내쉬었다.",
        "아직 위험은 남아있지만, 정체를 알고 있다는 사실만으로",
        "마음이 조금 놓였다.",
    ],
    231: [
        "엘리노어는 제프리에게 조심스럽게 말했다.",
    ],
    232: [
        "“제프리... 제발, 제가 안전하게",
        "나갈 수 있도록 도와줘요.”",
    ],
    233: [
        "제프리는 나를 잠시 바라보다가",
        "무심하게 고개를 끄덕였다.",
    ],
    234: [
        "“좋다. 하지만 내가 말하는 길을 따라 가야 한다.”",
    ],
    235: [
        "“조금이라도 벗어난다면, 그 존재에 잡힐 것이다.”",
    ],
    236: [
        "그는 석조 벽을 따라 통로를 안내하며 숨겨진 비밀 문을 열어준다.",
        "작은 열쇠와 기계 장치 덕분에 지하실 깊은 곳으로",
        "안전하게 이동할 수 있는 길이 열렸다.",
    ],
    237: [
        "드디어 성에서 나왔다.",
        "나는 긴장 속에서도 제프리의 안내를 따라",
        "조심스럽게 발걸음을 옮겼다.",
    ],
    238: [
        "“저 길 끝에는 오래된 출구가 있어.",
        "하지만 성 벽을 넘어야 한다.",
        "속삭임이 따라올 수 있으니 끝까지 긴장을 늦추지 마라.”",
    ],
    239: [
        "나는 고개를 끄덕였다.",
        "조금씩 안도의 숨이 나왔다.",
    ],
    240: [
        "나는 그렇게, 문을 나와 낮은 성벽과 마주했다.",
        "다행히 성벽은 조금만 발을 딛고 올라가면",
        "바깥으로 통할 수 있었다.",
    ],
    241: [
        "이 성을 탈출한 직후 보이는 성의 모습은",
        "내가 겪은 상황과는 대조되게 고요하고 평온했다.",
        "하지만 나는 한참 길을 이동한 뒤에야 비로소 안심할 수 있었다.",
    ],
}
epilogue_242 = [
    "당신은 그렇게, 성을 몰래 빠져나와 윌리엄을 만날 수 있게 되었다.",
    "나중에 들리는 소문으론 국왕은 당신이 나간 직후부터",
    "시름시름 앓다가 원인 모를 병에 걸려 죽어버렸다고 한다.",
    "이후 제프리는 나라의 왕 자리를 물려 받았다.",
    "당신은 더 이상 성 내부의 상황은 듣고 싶지 않았다.",
    "그저 윌리엄과 평화로운 나날들을 보내는 것에 집중했을 뿐...",
    "이제 난 행복했다.",
]

# -----------------------------
# 현재 씬
# -----------------------------
scene = 1
start_typing(intro_dialogues[1])

# 176 → 177 넘어갈 때 사용할 딜레이 타이머 (지금은 사용 안 함)
next_delay_timer = 0

# -----------------------------
# GAME 장면 그리기
# -----------------------------
fade_alpha = 0
fade_out_flag = False
fade_in_flag = False
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill(BLACK)
fade_surface.set_alpha(fade_alpha)

def draw_game_scene():
    global scene, key_pos, key_anim, fade_alpha

    update_typing()

    # 1~8 인트로
    if 1 <= scene <= 8:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()
        return

    # 9~13 방/탁자
    if scene == 9:
        SCREEN.blit(room_bg, (0, 0))
        draw_game_scene_no_char()

    elif scene == 10:
        SCREEN.blit(room_bg, (0, 0))

    elif scene == 11:
        SCREEN.blit(room_bg, (0, 0))
        rect = choice_box.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(choice_box, rect.topleft)
        txt = BIG_FONT.render("탁자로 이동", True, BLACK)
        SCREEN.blit(txt, txt.get_rect(center=rect.center))

    elif scene == 12:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(notebook_img, notebook_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        SCREEN.blit(key_img, key_rect)

    elif scene == 13:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(notebook_img, notebook_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        SCREEN.blit(key_img, key_rect)
        for i, rect in enumerate(choice13_rects):
            SCREEN.blit(choice_box, rect.topleft)
            draw_select_text_box(rect, choices13[i], color=BLACK)

    # 열쇠 루트 15~17
    elif scene == 15:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(notebook_img, notebook_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        SCREEN.blit(key_img, key_rect)

    elif scene == 16:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(notebook_img, notebook_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 180))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(key_img, key_rect)

    elif scene == 17:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(notebook_img, notebook_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 180))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(key_img, key_rect)
        SCREEN.blit(choice_box, select_rect)
        draw_select_text_box(select_rect, "열쇠를 집는다", BLACK)

    # 열쇠 루트 18~32
    elif scene == 18:
        SCREEN.blit(room_bg, (0, 0))
        draw_keyroute_dialogue(scene)

    elif scene == 19:
        SCREEN.blit(keyhole_bg_main, (0, 0))
        SCREEN.blit(keyhole_key_img, keyhole_key_img.get_rect(center=key_pos))
        SCREEN.blit(choice_box, select_rect)
        draw_select_text_box(select_rect, "열쇠를 사용한다", BLACK)

    elif scene == 20:
        SCREEN.blit(keyhole_bg_main, (0, 0))
        SCREEN.blit(keyhole_key_img, keyhole_key_img.get_rect(center=key_pos))

    elif 21 <= scene <= 30:
        SCREEN.blit(hallway_bg, (0, 0))
        draw_keyroute_dialogue(scene)
        if 24 <= scene <= 29:
            SCREEN.blit(blood_img, (0, 0))

    elif scene == 31:
        SCREEN.blit(gameover_bg, (0, 0))

    elif scene == 32:
        SCREEN.blit(gameover_bg, (0, 0))
        t1 = GAMEOVER_FONT.render("GAME OVER", True, RED)
        SCREEN.blit(t1, (640 - t1.get_width() // 2, 150))
        last = FONT.render("사랑도 권력 앞에선 우습나봅니다...", True, WHITE)
        SCREEN.blit(last, (640 - last.get_width() // 2, 330))
        SCREEN.blit(choice_box, select_rect)
        draw_select_text_box(select_rect, "다시 진행", BLACK)

    # 공책 루트 36~44
    elif scene == 36:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(key_img, key_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 200))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(notebook_table_img, notebook_table_rect)

    elif scene == 37:
        SCREEN.blit(table_bg, (0, 0))
        SCREEN.blit(cup_img, cup_rect)
        SCREEN.blit(key_img, key_rect)
        SCREEN.blit(handkerchief_img, handker_rect)
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 200))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(notebook_table_img, notebook_table_rect)

    elif scene == 38:
        SCREEN.blit(table_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 210))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(notebook_table_img, notebook_table_rect)
        SCREEN.blit(choice_box, select_41_rect)
        draw_select_text_box(select_41_rect, "공책 집어들기", BLACK)

    elif scene == 39:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(notebook_big_img, notebook_big_rect)

    elif scene == 40:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(notebook_big_img, notebook_big_rect)
        x = 200
        y = 540
        for i, line in enumerate(displayed_text.split("\n")):
            SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

    elif scene == 41:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(notebook_big_img, notebook_big_rect)
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 180))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(choice_box, select_41_rect)
        draw_select_text_box(select_41_rect, "펼치기", BLACK)

    elif scene == 42:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(paper_img, paper_rect)
        x = WIDTH // 2 - 200
        y = 250
        for i, line in enumerate(displayed_text.split("\n")):
            SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

    elif scene == 43:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_no_char()

    elif scene == 44:
        SCREEN.blit(room_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 160))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(choice_box, choice_left_rect)
        SCREEN.blit(choice_box, choice_right_rect)
        draw_select_text_box(choice_left_rect, "침대 아래를 살펴본다.", BLACK)
        draw_select_text_box(choice_right_rect, "문틈 너머 소리를 확인해본다.", BLACK)

    # 문틈 루트 46~55
    elif scene == 46:
        SCREEN.blit(room_bg, (0, 0))
        draw_keyhole_dialogue(scene)
        SCREEN.blit(elenore_img, ELENORE_POS)

    elif scene == 47:
        SCREEN.blit(keyhole_bg2, (0, 0))
        SCREEN.blit(select_box_large, select_rect)
        draw_select_text_box(select_rect, "더 자세히 보기", BLACK)

    elif scene == 48:
        SCREEN.blit(king_eye_bg, (0, 0))
        draw_random_questions()

    elif scene == 49:
        SCREEN.blit(king_eye_bg, (0, 0))
        draw_random_questions()
        draw_keyhole_dialogue(scene)

    elif scene == 50:
        SCREEN.blit(room_bg, (0, 0))
        draw_keyhole_dialogue(scene)
        SCREEN.blit(elenore_img, ELENORE_POS)

    elif scene == 51:
        SCREEN.blit(room_bg, (0, 0))
        draw_keyhole_dialogue(scene)
        SCREEN.blit(elenore_img, ELENORE_POS)

    elif scene == 52:
        SCREEN.fill(BLACK)

    elif scene == 53:
        SCREEN.fill(BLACK)
        y = 150
        for i, line in enumerate(dialogue_53_lines):
            SCREEN.blit(FONT.render(line, True, RED),
                        ((WIDTH - FONT.size(line)[0]) // 2, y + i * 32))

    elif scene == 54:
        SCREEN.fill(BLACK)
        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
        SCREEN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 280))
        SCREEN.blit(select_box_large, select_retry_rect)
        draw_select_text_box(select_retry_rect, "다시 진행", BLACK)

    elif scene == 55:
        SCREEN.fill(BLACK)
        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
        SCREEN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 280))
        SCREEN.blit(select_box_large, select_retry_rect)
        draw_select_text_box(select_retry_rect, "다시 진행", BLACK)
        last = FONT.render(dialogue_55_last, True, WHITE)
        SCREEN.blit(last, ((WIDTH - last.get_width()) // 2, 420))

    # 침대 아래 57~63
    elif scene in (57, 58, 60, 61, 62):
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 59:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(hand_img, hand_rect)

    elif scene == 63:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(select_box_large, choice1_rect)
        SCREEN.blit(select_box_large, choice2_rect)
        SCREEN.blit(select_box_large, choice3_rect)
        draw_select_text_box(choice1_rect, "아까 열쇠를 가져와\n흠에 맞춰본다.", BLACK)
        draw_select_text_box(choice2_rect, "일단 침대 밖으로 나와\n다른 단서를 찾는다.", BLACK)
        draw_select_text_box(choice3_rect, "돌 판을\n들어올려본다.", BLACK)

    # 92~98 열쇠 홈 사용 루트
    elif scene == 92:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(key_under_img, key_under_rect)
        SCREEN.blit(select_box_large, select_92_rect)
        draw_select_text_box(select_92_rect, "맞춰보기", BLACK)

    elif 93 <= scene <= 97:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        x = 260
        y = HEIGHT - 160
        for i, line in enumerate(displayed_text.split("\n")):
            SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

    elif scene == 98:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(select_box_large, choice98_left_rect)
        SCREEN.blit(select_box_large, choice98_right_rect)
        draw_select_text_box(choice98_left_rect, "바로 계단 아래로\n내려간다", BLACK)
        draw_select_text_box(choice98_right_rect, "문 쪽을 먼저\n확인한다", BLACK)

    # 65 (침대 밖)
    elif scene == 65:
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        x = 380
        y = HEIGHT - 130
        for i, line in enumerate(displayed_text.split("\n")):
            SCREEN.blit(FONT.render(line, True, WHITE), (x, y + i * 32))

    # 돌판 루트 67~90
    elif scene in (67, 68):
        SCREEN.blit(underbed_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 69:
        SCREEN.fill(BLACK)

    elif scene == 70:
        SCREEN.fill(BLACK)
        y = 200
        for i, line in enumerate(dialogues_67_90[70]):
            SCREEN.blit(FONT.render(line, True, RED),
                        (WIDTH // 2 - 300, y + i * 40))

    elif scene == 71:
        SCREEN.blit(hall1_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)

    elif scene == 72:
        SCREEN.blit(hall1_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 73:
        SCREEN.blit(hall1_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 210))
        SCREEN.blit(dark, (0, 0))
        word = "너무 원망스러워"
        for r in range(12):
            for c in range(12):
                SCREEN.blit(FONT.render(word, True, RED),
                            (-100 + c * 200, -120 + r * 50))

    elif scene == 74:
        SCREEN.blit(hall2_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        y = HEIGHT - 150
        for i, line in enumerate(dialogues_67_90[74]):
            SCREEN.blit(FONT.render(line, True, RED), (380, y + i * 32))

    elif scene == 75:
        SCREEN.blit(hall2_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 150))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(select_box_large, select75_rect)
        draw_select_text_box(select75_rect, "문 열기", BLACK)

    elif scene == 76:
        SCREEN.fill(BLACK)

    elif scene == 77:
        SCREEN.blit(door_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        y = HEIGHT - 150
        for i, line in enumerate(dialogues_67_90[77]):
            SCREEN.blit(FONT.render(line, True, WHITE), (380, y + i * 32))

    elif scene == 78:
        SCREEN.blit(door_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 79:
        SCREEN.blit(sleeping_bg, (0, 0))

    elif scene == 80:
        SCREEN.blit(sleeping_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 81:
        SCREEN.blit(sleeping_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 160))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(select_box_large, select81_left_rect)
        SCREEN.blit(select_box_large, select81_right_rect)
        draw_select_text_box(select81_left_rect, "찌르기", RED)
        draw_select_text_box(select81_right_rect, "안 찌르기", RED)

    elif scene == 83:
        SCREEN.blit(sleeping_bg, (0, 0))
        SCREEN.blit(elenore2_img, ELENORE2_POS)
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_with_char()

    elif scene == 84:
        SCREEN.blit(sleeping_bg, (0, 0))
        SCREEN.blit(elenore2_img, ELENORE2_POS)
        SCREEN.blit(select_box_large, select81_left_rect)
        SCREEN.blit(select_box_large, select81_right_rect)
        draw_select_text_box(select81_left_rect, "찌르기", BLACK)
        draw_select_text_box(select81_right_rect, "안 찌르기", BLACK)

    elif scene == 86:
        SCREEN.blit(sleeping_bg, (0, 0))
        SCREEN.blit(blood2_img, blood2_rect)
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore3_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 87:
        SCREEN.fill(BLACK)

    elif scene == 88:
        SCREEN.fill(BLACK)
        lines = dialogues_67_90[88]
        total = len(lines) * 40
        start_y = HEIGHT // 2 - total // 2
        for i, line in enumerate(lines):
            txt = FONT.render(line, True, RED)
            SCREEN.blit(txt, (WIDTH // 2 - txt.get_width() // 2,
                              start_y + i * 40))

    elif scene == 89:
        SCREEN.fill(BLACK)

    elif scene == 90:
        SCREEN.fill(BLACK)
        t1 = GAMEOVER_FONT.render("GAME", True, RED)
        t2 = GAMEOVER_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
        SCREEN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 300))
        SCREEN.blit(select_box_large, select75_rect)
        draw_select_text_box(select75_rect, "다시 진행", BLACK)

    # 100~106 문 확인 루트
    elif scene == 100:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_keyhole_dialogue(scene)

    elif scene == 101:
        SCREEN.blit(king_eye_bg, (0, 0))
        draw_random_questions()

    elif scene == 102:
        SCREEN.blit(king_eye_bg, (0, 0))
        draw_random_questions()
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_keyhole_dialogue(scene)

    elif scene == 103:
        SCREEN.blit(room_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_keyhole_dialogue(scene)

    elif scene == 104:
        SCREEN.fill(BLACK)

    elif scene == 105:
        SCREEN.fill(BLACK)
        start_y = 150
        for i, line in enumerate(dialogue_105):
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            y = start_y + i * 32
            SCREEN.blit(t, (x, y))

    elif scene == 106:
        SCREEN.fill(BLACK)
        t1 = GAMEOVER_FONT.render("GAME", True, RED)
        t2 = GAMEOVER_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
        SCREEN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 280))
        SCREEN.blit(select_box_large, select_retry_rect)
        draw_select_text_box(select_retry_rect, "다시 진행", BLACK)

    # 109~118 계단 내려가기 루트
    elif 109 <= scene <= 116:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_keyhole_dialogue(scene)
        if scene in (111, 112):
            SCREEN.blit(elenore_img, ELENORE_POS)

    elif scene == 117:
        SCREEN.blit(stairway_bg, (0, 0))

    elif scene == 118:
        SCREEN.blit(stairway_bg, (0, 0))
        SCREEN.blit(select_box_large, choice118_top_rect)
        SCREEN.blit(select_box_large, choice118_left_rect)
        SCREEN.blit(select_box_large, choice118_right_rect)
        draw_select_text_box(choice118_top_rect,  "위쪽 길로 간다", BLACK)
        draw_select_text_box(choice118_left_rect, "왼쪽 길로 간다", BLACK)
        draw_select_text_box(choice118_right_rect,"오른쪽 길로 간다", BLACK)

    # 120~125 다시 위로 DEAD END
    elif scene == 120:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 121:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_with_char()

    elif scene == 122:
        SCREEN.blit(underway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_with_char()

    elif scene == 123:
        SCREEN.fill(BLACK)

    elif scene == 124:
        SCREEN.fill(BLACK)
        start_y = 150
        for i, line in enumerate(dialogue_124):
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            y = start_y + i * 32
            SCREEN.blit(t, (x, y))

    elif scene == 125:
        SCREEN.fill(BLACK)
        t1 = GAMEOVER_FONT.render("GAME", True, RED)
        t2 = GAMEOVER_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 150))
        SCREEN.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 280))
        SCREEN.blit(select_box_large, select_retry_rect)
        draw_select_text_box(select_retry_rect, "다시 진행", BLACK)

    # 127~138 오른쪽 길 루트
    elif scene == 127:
        SCREEN.blit(stairway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene in (128, 129, 130):
        SCREEN.blit(underway_hall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_with_char()

    elif scene == 131:
        SCREEN.blit(underway_hall_bg, (0, 0))
        dark = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark.fill((0, 0, 0, 150))
        SCREEN.blit(dark, (0, 0))
        SCREEN.blit(select_box_large, choice131_left_rect)
        SCREEN.blit(select_box_large, choice131_right_rect)
        draw_select_text_box(choice131_left_rect, "다시 뒤돌아\n왼쪽 길로 도망간다", BLACK)
        draw_select_text_box(choice131_right_rect, "바로 보이는 큰 상자에\n숨는다.", BLACK)

    elif scene == 133:
        SCREEN.fill(BLACK)
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_with_char()

    elif scene == 134:
        SCREEN.blit(underway_monster_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 135:
        SCREEN.fill(BLACK)
        fade_layer = pygame.Surface((WIDTH, HEIGHT))
        fade_layer.fill(BLACK)
        fade_layer.set_alpha(fade_alpha)
        SCREEN.blit(fade_layer, (0, 0))

    elif scene == 136:
        SCREEN.fill(BLACK)
        start_y = 200
        for i, line in enumerate(dialogue_136):
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            SCREEN.blit(t, (x, start_y + i * 32))

    elif scene == 137:
        SCREEN.fill(BLACK)
        fade_layer = pygame.Surface((WIDTH, HEIGHT))
        fade_layer.fill(BLACK)
        fade_layer.set_alpha(fade_alpha)
        SCREEN.blit(fade_layer, (0, 0))

    elif scene == 138:
        SCREEN.fill(BLACK)
        t1 = GAMEOVER_FONT.render("GAME", True, RED)
        t2 = GAMEOVER_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, ((WIDTH - t1.get_width()) // 2, 150))
        SCREEN.blit(t2, ((WIDTH - t2.get_width()) // 2, 150 + t1.get_height()))
        SCREEN.blit(select_retry_box_138, select_retry_rect_138)
        draw_select_text_box(select_retry_rect_138, "다시 진행", BLACK)

    # 140~149 왼쪽 길 루트
    elif scene == 140:
        SCREEN.blit(stairway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 141:
        SCREEN.blit(leftway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_no_char()

    elif scene == 142:
        SCREEN.blit(leftway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_no_char()

    elif scene == 143:
        SCREEN.fill(BLACK)

    elif scene == 144:
        SCREEN.blit(wall_bg, (0, 0))

    elif scene == 145:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 146:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_no_char()

    elif scene == 147:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 148:
        SCREEN.blit(wall_bg, (0, 0))

    elif scene == 149:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(select_box_large, choice149_left_rect)
        SCREEN.blit(select_box_large, choice149_mid_rect)
        SCREEN.blit(select_box_large, choice149_right_rect)
        draw_select_text_box(choice149_left_rect, "윌리엄의 목소리를\n따라간다.", BLACK)
        draw_select_text_box(choice149_mid_rect, "대답하지 않고 계속\n아래로 내려간다.", BLACK)
        draw_select_text_box(choice149_right_rect, "벽에 숨겨진 장치가 있는지\n조사한다.", BLACK)

    # 151~155 윌리엄 목소리 루트
    elif scene == 151:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 152:
        SCREEN.blit(stair2_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 153:
        SCREEN.fill(BLACK)
        y = 200
        for line in story_153:
            t = FONT.render(line, True, RED)
            x = (WIDTH - t.get_width()) // 2
            SCREEN.blit(t, (x, y))
            y += 34

    elif scene == 154:
        SCREEN.fill(BLACK)

    elif scene == 155:
        SCREEN.fill(BLACK)
        t1 = GAMEOVER_FONT.render("GAME", True, RED)
        t2 = GAMEOVER_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, ((WIDTH - t1.get_width()) // 2, 150))
        SCREEN.blit(t2, ((WIDTH - t2.get_width()) // 2, 150 + t1.get_height() + 10))
        SCREEN.blit(select_box_large, select_retry_rect_155)
        draw_select_text_box(select_retry_rect_155, "다시 진행", BLACK)

    # 157~158 벽 조사 루트
    elif scene == 157:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_with_char()

    elif scene == 158:
        SCREEN.blit(wall_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_no_char()

    # 160~165 계단 구간
    elif scene in (160, 161, 162, 163, 164, 165):
        SCREEN.blit(stairway_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        if scene in (162, 164, 165):
            SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_no_char()

    elif scene == 166:
        SCREEN.fill(BLACK)

    elif scene in (168, 169, 170, 171):
        SCREEN.blit(underground_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_no_char()

    elif scene == 172:
        SCREEN.blit(underground_bg, (0, 0))
        SCREEN.blit(select_box_large, choice_left_rect)
        SCREEN.blit(select_box_large, choice_mid_rect)
        SCREEN.blit(select_box_large, choice_right_rect)
        draw_select_text(choice_left_rect, "당신은 누구죠?\n물어본다")
        draw_select_text(choice_mid_rect, "뒤로 물러선다")
        draw_select_text(choice_right_rect, "반대편으로 향한다")

    # 174~177 : 반대편 지하실로 향한 루트
    elif scene == 174:
        SCREEN.blit(stair_bg, (0, 0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_no_char()

    elif scene == 175:
        SCREEN.fill(BLACK)
        y = HEIGHT//2 - 60
        for i, line in enumerate(dialogues_174[175]):
            txt = FONT.render(line, True, RED)
            SCREEN.blit(txt, ((WIDTH - txt.get_width()) // 2, y + i * 32))

    elif scene == 176:
        SCREEN.fill(BLACK)

    elif scene == 177:
        SCREEN.fill(BLACK)
        t1 = BIG_FONT.render("GAME", True, RED)
        t2 = BIG_FONT.render("OVER", True, RED)
        SCREEN.blit(t1, ((WIDTH - t1.get_width()) // 2, 150))
        SCREEN.blit(t2, ((WIDTH - t2.get_width()) // 2, 150 + t1.get_height() + 10))
        SCREEN.blit(select_box_large, retry_rect)
        retry_text = FONT.render("다시 진행", True, BLACK)
        SCREEN.blit(retry_text, retry_text.get_rect(center=retry_rect.center))
    
    # 179~202 : 제프리와의 대면 루트
    elif 179 <= scene <= 201:
        SCREEN.blit(underground_bg, (0, 0))  
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))

        # 캐릭터가 있는지 여부에 따라 대사 위치 변경
        char_exists = (scene in jeff_scenes) or (scene in elen_scenes)

        draw_game_scene_line_with_offset(char_exists)

        # 캐릭터는 항상 가장 마지막에 표시
        if scene in jeff_scenes:
            SCREEN.blit(jeff_img, JEFF_POS)
        if scene in elen_scenes:
            SCREEN.blit(elenore_img, ELENORE_POS)

    elif scene == 202:
        SCREEN.fill(BLACK)
        SCREEN.blit(choice_box, choice_left)
        SCREEN.blit(choice_box, choice_right)
        draw_select_text(choice_left, choice_texts[0])   # 윌리엄을 따른다
        draw_select_text(choice_right, choice_texts[1])  # 제프리를 따른다

    # 204~216 : 윌리엄 선택 루트
    elif scene in (204, 205):
        SCREEN.blit(bg_william, (0,0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_no_char()

    elif 206 <= scene <= 215:
        SCREEN.blit(bg_under, (0,0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        if scene in (212, 213):
            SCREEN.blit(jeff_img, JEFF_POS)
            draw_game_scene_with_char()
        else:
            draw_game_scene_no_char()

    elif scene == 216:
        SCREEN.blit(bg_under, (0,0))
        SCREEN.blit(select_box_large, choice_left_rect)
        SCREEN.blit(select_box_large, choice_right_rect)
        draw_select_text(choice_left_rect, "형체에게 다가가\n얼굴을 확인한다")
        draw_select_text(choice_right_rect, "뒤로 돌아\n제프리 쪽으로 간다")

    # 218~223 : 얼굴 확인 사망 루트
    elif scene == 218:
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        SCREEN.blit(elenore_img, ELENORE_POS)
        draw_game_scene_no_char()

    elif scene == 219:
        SCREEN.fill(BLACK)

    elif scene == 220:
        SCREEN.fill(BLACK)
        for i, line in enumerate(dialogues_218[220]):
            t = FONT.render(line, True, RED)
            SCREEN.blit(t, ((WIDTH - t.get_width())//2, 150 + i*36))

    elif scene in (221, 222, 223):
        SCREEN.blit(gameover_bg, (0,0))
        draw_gameover_ui()

    # 225~244 : 제프리 엔딩 루트
    elif 225 <= scene <= 230:
        SCREEN.blit(william_bg, (0,0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        if scene in ELEN_SCENES: SCREEN.blit(elenore_img, ELENORE_POS)
        if scene in JEFF_SCENES: SCREEN.blit(jeff_img, JEFF_POS)
        draw_game_scene_line()

    elif 231 <= scene <= 236:
        SCREEN.blit(jeffrey_bg, (0,0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        if scene in ELEN_SCENES: SCREEN.blit(elenore_img, ELENORE_POS)
        if scene in JEFF_SCENES: SCREEN.blit(jeff_img, JEFF_POS)
        draw_game_scene_line()

    elif 237 <= scene <= 240:
        SCREEN.blit(castle_outside, (0,0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_line()

    elif scene == 241:
        SCREEN.blit(castle_outside2, (0,0))
        SCREEN.blit(chatbox_img, (0, HEIGHT - 200))
        draw_game_scene_line()

    elif scene == 242:
        SCREEN.fill(WHITE)
        start_y = 150
        for i, line in enumerate(epilogue_242):
            t = FONT.render(line, True, EPILOGUE_COLOR)
            x = (WIDTH - t.get_width()) // 2
            y = start_y + i * 32
            SCREEN.blit(t, (x, y))

    elif scene == 243:
        SCREEN.fill(WHITE)

    elif scene == 244:
        SCREEN.fill(WHITE)
        t = BIG_FONT.render("THE END...", True, BLACK)
        x = (WIDTH - t.get_width()) // 2
        y = (HEIGHT - t.get_height()) // 2
        SCREEN.blit(t, (x, y))

# -----------------------------
# 모드별 화면 그리기
# -----------------------------
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
        draw_game_scene()

# -----------------------------
# 입력 처리 (재구성 버전)
# -----------------------------
def handle_input():
    global scene, key_anim, key_pos, random_q_positions
    global dialogue_active, displayed_text, current_text, text_index
    global fade_alpha, fade_out_flag, fade_in_flag, MODE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ✅ 마우스 움직임(MOUSEMOTION)은 완전히 무시
        if event.type == pygame.MOUSEMOTION:
            continue

        # ------------------------
        # BTN CLICK (ALL BUTTONS)
        # ------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            play_sfx(click_button_sfx)

        # ------------------------
        # TYPING SKIP
        # ------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dialogue_active:
                displayed_text = current_text
                text_index = len(current_text)
                dialogue_active = False
                return

        # ------------------------
        # TITLE MODE
        # ------------------------
        if MODE == "TITLE":
            for b in buttons_title:
                b.handle(event)
            play_bgm(intro_bgm)
            return

        # ------------------------
        # INFORMATION MODE
        # ------------------------
        if MODE == "INFORMATION":
            for b in buttons_info:
                b.handle(event)
            play_bgm(intro_bgm)
            return

        # ========================================================
        # GAME MODE
        # ========================================================
        if MODE == "GAME" and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # --------------------------------
            # SCENE SOUND: ~22
            # --------------------------------
            if scene <= 22 and MODE == "GAME":
                play_bgm(bgm_4_22)

            # --------------------------------
            # SCENE SOUND: 48
            # --------------------------------
            if scene == 48:
                play_sfx(sound_48)

            # --------------------------------
            # SCENE SOUND: 50~52
            # --------------------------------
            if scene in (50, 51, 52):
                play_sfx(sound_50_52)

            # --------------------------------
            # SCENE SOUND: 68 (ROCK)
            # --------------------------------
            if scene == 68:
                play_sfx(sound_68_rock)

            # --------------------------------
            # SCENE SOUND: 73 (LAUGH)
            # --------------------------------
            if scene == 73:
                play_sfx(sound_73_laugh)

            # --------------------------------
            # SCENE SOUND: 86 (KING STAB)
            # --------------------------------
            if scene == 86:
                play_sfx(sound_86_stab_king)

            # --------------------------------
            # SCENE SOUND: 133 (GIRL WALK)
            # --------------------------------
            if scene == 133:
                play_sfx(sound_133_walk)

            # --------------------------------
            # SCENE BGM: 57~69
            # --------------------------------
            if scene == 57:
                play_bgm(bgm_57_69)

            # --------------------------------
            # SCENE BGM: 71~73 GIRL CRY
            # --------------------------------
            if scene == 71:
                play_bgm(bgm_girl_cry)

            # --------------------------------
            # SCENE BGM: 134 GIRL SCREAM (ONE-SHOT)
            # --------------------------------
            if scene == 134:
                play_bgm_once(bgm_134_scream)

            # --------------------------------
            # GAME OVER SOUND (174~177 / 221~223)
            # --------------------------------
            if scene in (174, 175, 176, 177, 221, 222, 223):
                play_sfx(sound_gameover)

            # --------------------------------
            # SCENE 240~244 BGM LOOP
            # --------------------------------
            if scene == 240:
                play_bgm(sound_240_244)

        # 타이핑 스킵 (대사 스킵)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dialogue_active:
                displayed_text = current_text
                text_index = len(current_text)
                dialogue_active = False
                return

        # TITLE 모드
        if MODE == "TITLE":
            for b in buttons_title:
                b.handle(event)
            return

        # INFORMATION 모드
        if MODE == "INFORMATION":
            for b in buttons_info:
                b.handle(event)
            return

        # GAME 모드
        if MODE == "GAME" and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # 인트로 1~8
            if 1 <= scene <= 8:
                if not dialogue_active:
                    scene += 1
                    if 1 <= scene <= 8:
                        start_typing(intro_dialogues[scene])
                    else:
                        scene = 9
                        start_typing(scene9_text_lines)
                return

            # 9~13
            if scene == 9:
                if not dialogue_active:
                    scene = 10
                return

            if scene == 10:
                scene = 11
                return

            if scene == 11:
                rect = choice_box.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                if rect.collidepoint((mx, my)):
                    scene = 12
                return

            if scene == 12:
                scene = 13
                return

            if scene == 13:
                if choice13_rects[0].collidepoint((mx, my)):
                    scene = 57
                    start_typing(dialogues_underbed[57])
                elif choice13_rects[1].collidepoint((mx, my)):
                    scene = 15
                elif choice13_rects[2].collidepoint((mx, my)):
                    scene = 46
                    start_typing(typing_dialogues_keyhole[46])
                elif choice13_rects[3].collidepoint((mx, my)):
                    scene = 36
                return

            # 열쇠 루트 15~32
            if scene == 15:
                fade_out_game()
                scene = 16
                return

            if scene == 16:
                scene = 17
                return

            if scene == 17:
                if select_rect.collidepoint((mx, my)):
                    fade_out_game()
                    scene = 18
                    start_typing(dialogue_18_lines)
                return

            if scene == 18:
                if not dialogue_active:
                    scene = 19
                return

            if scene == 19:
                if select_rect.collidepoint((mx, my)):
                    fade_out_game()
                    scene = 20
                    key_anim = True
                    key_pos = key_start.copy()
                return

            if scene == 20:
                # 애니메이션으로 진행
                return

            if 21 <= scene <= 30:
                if not dialogue_active:
                    scene += 1
                    if 21 <= scene <= 30 and scene in dialogues_21_30:
                        start_typing(dialogues_21_30[scene])
                return

            if scene == 31:
                scene = 32
                return

            if scene == 32:
                if select_rect.collidepoint((mx, my)):
                    scene = 13
                return

            # 공책 루트 36~44
            if scene == 36:
                scene = 37
                return

            if scene == 37:
                scene = 38
                return

            if scene == 38:
                if select_41_rect.collidepoint((mx, my)):
                    scene = 39
                    start_typing(dialogues_notebook[40])
                return

            if scene == 39:
                scene = 40
                start_typing(dialogues_notebook[40])
                return

            if scene == 40:
                scene = 41
                return

            if scene == 41:
                if select_41_rect.collidepoint((mx, my)):
                    scene = 42
                    start_typing(dialogues_notebook[42])
                return

            if scene == 42:
                scene = 43
                start_typing(dialogues_notebook[43])
                return

            if scene == 43:
                scene = 44
                fade_in_game()
                return

            if scene == 44:
                if choice_left_rect.collidepoint((mx, my)):
                    scene = 57
                    start_typing(dialogues_underbed[57])
                elif choice_right_rect.collidepoint((mx, my)):
                    scene = 46
                    start_typing(typing_dialogues_keyhole[46])
                return

            # 문틈 루트 46~55
            if scene == 46:
                if not dialogue_active:
                    scene = 47
                return

            if scene == 47:
                if select_rect.collidepoint((mx, my)):
                    scene = 48
                    random_q_positions = generate_random_questions()
                return

            if scene == 48:
                scene = 49
                start_typing(typing_dialogues_keyhole[49])
                return

            if scene == 49:
                if not dialogue_active:
                    scene = 50
                    start_typing(typing_dialogues_keyhole[50])
                return

            if scene == 50:
                if not dialogue_active:
                    scene = 51
                    start_typing(typing_dialogues_keyhole[51])
                return

            if scene == 51:
                if not dialogue_active:
                    scene = 52
                return

            if scene == 52:
                scene = 53
                return

            if scene == 53:
                scene = 54
                return

            if scene == 54:
                if select_retry_rect.collidepoint((mx, my)):
                    scene = 13
                return

            if scene == 55:
                if select_retry_rect.collidepoint((mx, my)):
                    scene = 13
                return

            # 침대 아래 57~63, 65
            if scene == 57:
                scene = 58
                start_typing(dialogues_underbed[58])
                return

            if scene == 58:
                scene = 59
                return

            if scene == 59:
                scene = 60
                start_typing(dialogues_underbed[60])
                return

            if scene == 60:
                scene = 61
                start_typing(dialogues_underbed[61])
                return

            if scene == 61:
                scene = 62
                start_typing(dialogues_underbed[62])
                return

            if scene == 62:
                scene = 63
                return

            if scene == 63:
                if choice1_rect.collidepoint((mx, my)):
                    scene = 92
                    return
                if choice2_rect.collidepoint((mx, my)):
                    scene = 65
                    start_typing(dialogue_65_lines)
                    return
                if choice3_rect.collidepoint((mx, my)):
                    scene = 67
                    start_typing(dialogues_67_90[67])
                    return

            if scene == 65:
                if not dialogue_active:
                    scene = 63
                return

            # 돌판 루트 67~89
            if 67 <= scene <= 89:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_67_90:
                        start_typing(dialogues_67_90[scene])
                return

            # 92~98 : 열쇠 홈
            if scene == 92:
                if select_92_rect.collidepoint((mx, my)):
                    scene = 93
                    start_typing(dialogues_92_98[93])
                return

            if 93 <= scene <= 97:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_92_98:
                        start_typing(dialogues_92_98[scene])
                return

            if scene == 98:
                if choice98_left_rect.collidepoint((mx, my)):
                    scene = 109
                    start_typing(dialogues_109_116[109])
                elif choice98_right_rect.collidepoint((mx, my)):
                    scene = 100
                    start_typing(dialogues_100_106[100])
                return

            # 돌판 GAME OVER
            if scene == 90:
                if select75_rect.collidepoint((mx, my)):
                    scene = 63
                return

            # 100~106 문 확인 사망 루트
            if scene == 100:
                if not dialogue_active:
                    scene = 101
                return

            if scene == 101:
                scene = 102
                start_typing(dialogues_100_106[102])
                return

            if scene == 102:
                if not dialogue_active:
                    scene = 103
                    start_typing(dialogues_100_106[103])
                return

            if scene == 103:
                if not dialogue_active:
                    scene = 104
                return

            if scene == 104:
                scene = 105
                return

            if scene == 105:
                scene = 106
                return

            if scene == 106:
                if select_retry_rect.collidepoint((mx, my)):
                    scene = 98
                return

            # 109~118 계단
            if 109 <= scene <= 116:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_109_116:
                        start_typing(dialogues_109_116[scene])
                return

            if scene == 117:
                scene = 118
                return

            if scene == 118:
                if choice118_top_rect.collidepoint((mx, my)):
                    scene = 120
                    start_typing(dialogues_120_122[120])
                elif choice118_left_rect.collidepoint((mx, my)):
                    scene = 140
                    start_typing(dialogues_left_route[140])
                elif choice118_right_rect.collidepoint((mx, my)):
                    scene = 127
                    start_typing(dialogues_127_130[127])
                return

            # 120~125 되돌아가기
            if scene == 120:
                if not dialogue_active:
                    scene = 121
                    start_typing(dialogues_120_122[121])
                return

            if scene == 121:
                if not dialogue_active:
                    scene = 122
                    start_typing(dialogues_120_122[122])
                return

            if scene == 122:
                if not dialogue_active:
                    scene = 123
                return

            if scene == 123:
                scene = 124
                return

            if scene == 124:
                scene = 125
                return

            if scene == 125:
                if select_retry_rect.collidepoint((mx, my)):
                    scene = 118
                return

            # 127~138 오른쪽 길
            if 127 <= scene <= 130:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_127_130:
                        start_typing(dialogues_127_130[scene])
                return

            if scene == 131:
                if choice131_left_rect.collidepoint((mx, my)):
                    scene = 140
                    start_typing(dialogues_left_route[140])
                elif choice131_right_rect.collidepoint((mx, my)):
                    scene = 133
                    start_typing(typing_dialogues_2[133])
                return

            if scene == 133:
                if not dialogue_active:
                    scene = 134
                    start_typing(typing_dialogues_2[134])
                return

            if scene == 134:
                if not dialogue_active:
                    scene = 135
                    fade_alpha = 0
                    fade_out_flag = True
                return

            if scene == 135:
                if not fade_out_flag:
                    scene = 136
                return

            if scene == 136:
                scene = 137
                fade_alpha = 255
                fade_in_flag = True
                return

            if scene == 137:
                if not fade_in_flag:
                    scene = 138
                return

            if scene == 138:
                if select_retry_rect_138.collidepoint((mx, my)):
                    scene = 118
                return

            # 140~149 왼쪽 길
            if scene == 140:
                if not dialogue_active:
                    scene = 141
                    start_typing(dialogues_left_route[141])
                return

            if scene == 141:
                if not dialogue_active:
                    scene = 142
                    start_typing(dialogues_left_route[142])
                return

            if scene == 142:
                if not dialogue_active:
                    scene = 143
                return

            if scene == 143:
                scene = 144
                return

            if scene == 144:
                scene = 145
                start_typing(dialogues_left_route[145])
                return

            if scene == 145:
                if not dialogue_active:
                    scene = 146
                    start_typing(dialogues_left_route[146])
                return

            if scene == 146:
                if not dialogue_active:
                    scene = 147
                    start_typing(dialogues_left_route[147])
                return

            if scene == 147:
                if not dialogue_active:
                    scene = 148
                return

            if scene == 148:
                scene = 149
                return

            if scene == 149:
                if choice149_left_rect.collidepoint((mx, my)):
                    scene = 151
                    start_typing(dialogues_151_155[151])
                elif choice149_mid_rect.collidepoint((mx, my)):
                    scene = 160
                    start_typing(dialogues_160[160])
                elif choice149_right_rect.collidepoint((mx, my)):
                    scene = 157
                    start_typing(dialogues_157[157])
                return

            # 151~155 윌리엄 목소리 아사 루트
            if scene == 151:
                if not dialogue_active:
                    scene = 152
                    start_typing(dialogues_151_155[152])
                return

            if scene == 152:
                if not dialogue_active:
                    scene = 153
                return

            if scene == 153:
                scene = 154
                return

            if scene == 154:
                scene = 155
                return

            if scene == 155:
                if select_retry_rect_155.collidepoint((mx, my)):
                    scene = 149
                return

            # 157~158 벽 조사
            if scene == 157:
                if not dialogue_active:
                    scene = 158
                    start_typing(dialogues_157[158])
                return

            if scene == 158:
                if not dialogue_active:
                    scene = 149
                return

            # 160~166, 168~172 제프리 만나기 전
            if scene in (160, 161, 162, 163, 164):
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_160:
                        start_typing(dialogues_160[scene])
                return

            if scene == 165:
                if not dialogue_active:
                    scene = 166
                return

            if scene == 166:
                scene = 168
                start_typing(dialogues_160[168])
                return

            if scene in (168, 169, 170):
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_160:
                        start_typing(dialogues_160[scene])
                return

            if scene == 171:
                if not dialogue_active:
                    scene = 172
                return

            # 172 : 제프리 첫 만남 선택
            if scene == 172:
                if choice_left_rect.collidepoint((mx, my)):
                    scene = 179
                    start_typing(dialogues_179[179])
                elif choice_mid_rect.collidepoint((mx, my)) or choice_right_rect.collidepoint((mx, my)):
                    scene = 174
                    start_typing(dialogues_174[174])
                return

            # 174~177 아사 GAME OVER
            if scene == 174:
                if not dialogue_active:
                    scene = 175
                    start_typing(dialogues_174[175])
                return

            if scene == 175:
                if not dialogue_active:
                    scene = 176
                return

            if scene == 176:
                scene = 177
                return

            if scene == 177:
                if retry_rect.collidepoint((mx, my)):
                    scene = 172
                return

            # 179~202 제프리 루트
            if 179 <= scene <= 201:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_179:
                        start_typing(dialogues_179[scene])
                return

            if scene == 202:
                if choice_left.collidepoint((mx, my)):
                    scene = 204
                    start_typing(dialogues_204[204])
                elif choice_right.collidepoint((mx, my)):
                    scene = 225
                    start_typing(dialogues_225[225])
                return

            # 204~216 윌리엄(괴물) 루트
            if 204 <= scene <= 215:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_204:
                        start_typing(dialogues_204[scene])
                return

            if scene == 216:
                if choice_left_rect.collidepoint((mx, my)):
                    scene = 218
                    start_typing(dialogues_218[218])
                elif choice_right_rect.collidepoint((mx, my)):
                    scene = 225
                    start_typing(dialogues_225[225])
                return

            # 218~223 괴물 GAME OVER
            if scene == 218:
                if not dialogue_active:
                    scene = 219
                return

            if scene == 219:
                scene = 220
                return

            if scene == 220:
                scene = 221
                return

            if scene in (221, 222, 223):
                if retry_rect.collidepoint((mx, my)):
                    scene = 202
                return

            # 225~244 제프리 엔딩
            if 225 <= scene <= 241:
                if not dialogue_active:
                    scene += 1
                    if scene in dialogues_225:
                        start_typing(dialogues_225[scene])
                return

            if scene == 242:
                scene = 243
                return

            if scene == 243:
                scene = 244
                return

            if scene == 244:
                return

# -----------------------------
# 메인 루프
# -----------------------------
while True:
    CLOCK.tick(60)
    handle_input()

    # 열쇠 애니메이션 (씬 20)
    if MODE == "GAME" and key_anim and scene == 20:
        direction = key_hole_pos - key_pos
        if direction.length() > 1:
            direction = direction.normalize() * 5
            key_pos += direction
        else:
            key_anim = False
            scene = 21
            start_typing(dialogues_21_30[21])

    draw_screen()

    # 페이드 처리
    if MODE == "GAME":
        if fade_out_flag and fade_alpha < 255:
            fade_alpha += 5
            fade_surface.set_alpha(fade_alpha)
            SCREEN.blit(fade_surface, (0, 0))
            if fade_alpha >= 255:
                fade_out_flag = False

        if fade_in_flag and fade_alpha > 0:
            fade_alpha -= 5
            fade_surface.set_alpha(fade_alpha)
            SCREEN.blit(fade_surface, (0, 0))
            if fade_alpha <= 0:
                fade_in_flag = False

    pygame.display.flip()
