import pygame
import sys
import time
import math
import configparser
import os
import ctypes

CONFIG_FILE = "settings.ini"

# === Load settings strictly from file ===
def load_settings():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"Missing {CONFIG_FILE}. Create it before running the game.")

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    required_keys = {
        "DISPLAY": ["VSync", "Fullscreen", "DebugMode", "FrameLimit", "AspectRatio",
                    "FullscreenWidth", "FullscreenHeight"]
    }

    for section, keys in required_keys.items():
        if section not in config:
            raise ValueError(f"[ERROR] Missing section [{section}] in {CONFIG_FILE}.")
        for key in keys:
            if key not in config[section]:
                raise ValueError(f"[ERROR] Missing key '{key}' under [{section}] in {CONFIG_FILE}.")

    vsync = config.getboolean("DISPLAY", "VSync")
    fullscreen = config.getboolean("DISPLAY", "Fullscreen")
    debug = config.getboolean("DISPLAY", "DebugMode")
    framelimit = config.getint("DISPLAY", "FrameLimit")
    aspect = config.get("DISPLAY", "AspectRatio")
    fs_width = config.getint("DISPLAY", "FullscreenWidth")
    fs_height = config.getint("DISPLAY", "FullscreenHeight")

    return vsync, fullscreen, debug, framelimit, aspect, fs_width, fs_height

VSYNC, FULLSCREEN, DEBUG_MODE, FRAME_LIMIT, ASPECT_RATIO, FULLSCREEN_W, FULLSCREEN_H = load_settings()

if not DEBUG_MODE:
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except Exception:
        pass

def log(*args):
    if DEBUG_MODE:
        print(*args)

pygame.init()

BASE_W, BASE_H = 640, 480
MAX_NAME_LEN = 12

BG = (15, 15, 20)
PANEL = (25, 25, 30)
TEXT = (240, 240, 240)
ACCENT = (210, 210, 255)
BORDER = (90, 90, 100)
CHESS_PIECES = ["♔", "♕", "♖", "♗", "♘", "♙"]

TARGET_RATIO = float(ASPECT_RATIO.split(":")[0]) / float(ASPECT_RATIO.split(":")[1])

screen = None
def update_display_mode():
    global screen, BASE_W, BASE_H
    if FULLSCREEN:
        BASE_W, BASE_H = FULLSCREEN_W, FULLSCREEN_H
        try:
            screen = pygame.display.set_mode((BASE_W, BASE_H), pygame.FULLSCREEN, vsync=1 if VSYNC else 0)
            log(f"Fullscreen: {FULLSCREEN}, VSync: {VSYNC}, Res: {BASE_W}x{BASE_H}")
        except TypeError:
            screen = pygame.display.set_mode((BASE_W, BASE_H), pygame.FULLSCREEN)
            log(f"Fullscreen fallback without vsync: {BASE_W}x{BASE_H}")
    else:
        BASE_W, BASE_H = 640, 480
        screen = pygame.display.set_mode((BASE_W, BASE_H), pygame.RESIZABLE)
        log(f"Windowed mode: {BASE_W}x{BASE_H}")

update_display_mode()
pygame.display.set_caption("ChessTale — Name Entry")
clock = pygame.time.Clock()

font_cache = {}
def get_font(size, name="couriernew", bold=True):
    key = (name, size, bold)
    if key not in font_cache:
        font_cache[key] = pygame.font.SysFont(name, size, bold=bold)
    return font_cache[key]

def draw_panel(surface, rect, border=4):
    pygame.draw.rect(surface, BORDER, rect.inflate(border*2, border*2))
    pygame.draw.rect(surface, PANEL, rect)

def main():
    global FULLSCREEN, BASE_W, BASE_H
    name = ""
    start_time = time.time()
    running = True
    last_window_size = screen.get_size()
    virtual_surface = pygame.Surface((BASE_W, BASE_H))
    toggle_cooldown = 0  # prevent renderer break on rapid toggle

    while running:
        dt = clock.tick(0 if (VSYNC and FULLSCREEN) else FRAME_LIMIT) / 1000
        t = time.time() - start_time
        toggle_cooldown = max(0, toggle_cooldown - dt)

        window_w, window_h = screen.get_size()
        window_ratio = window_w / window_h
        if window_ratio > TARGET_RATIO:
            draw_h = window_h
            draw_w = int(draw_h * TARGET_RATIO)
        else:
            draw_w = window_w
            draw_h = int(draw_w / TARGET_RATIO)

        offset_x = (window_w - draw_w) // 2
        offset_y = (window_h - draw_h) // 2
        scale_w = draw_w / BASE_W
        scale_h = draw_h / BASE_H

        if last_window_size != (draw_w, draw_h):
            virtual_surface = pygame.Surface((BASE_W, BASE_H))
            last_window_size = (draw_w, draw_h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if len(name.strip()) > 0:
                        log(f"Confirmed name: {name}")
                        running = False
                elif event.key == pygame.K_F11 and toggle_cooldown <= 0:
                    FULLSCREEN = not FULLSCREEN
                    update_display_mode()
                    virtual_surface = pygame.Surface((BASE_W, BASE_H))
                    toggle_cooldown = 0.5
                    log(f"F11 pressed: Fullscreen={FULLSCREEN}")
                else:
                    ch = event.unicode
                    if ch.isprintable() and len(name) < MAX_NAME_LEN:
                        name += ch.upper()

        virtual_surface.fill(BG)

        def render_centered(text, base_y, size, color=TEXT, wave=False):
            font = get_font(max(1,int(size*scale_h)))
            x = BASE_W // 2
            y = int(base_y)
            if not wave:
                surf = font.render(text, True, color)
                rect = surf.get_rect(center=(x, y))
                virtual_surface.blit(surf, rect)
            else:
                offset = 0
                for i, ch in enumerate(text):
                    surf = font.render(ch, True, color)
                    rect = surf.get_rect(center=(x - (len(text)//2)*surf.get_width() + offset, y + int(math.sin((t*3)+i*0.4)*4)))
                    virtual_surface.blit(surf, rect)
                    offset += surf.get_width()

        def draw_chess(piece, base_x, base_y, size, color=ACCENT, anim=True):
            font = get_font(max(1,int(size*scale_h)), "dejavusans")
            x = int(base_x)
            y = int(base_y)
            if anim:
                x += math.sin(t*2 + base_x*0.01) * 10
                y += math.cos(t*2 + base_y*0.01) * 3
            surf = font.render(piece, True, color)
            rect = surf.get_rect(center=(x, y))
            virtual_surface.blit(surf, rect)

        render_centered("CHESSTALE", 80, 40, color=ACCENT, wave=True)
        draw_chess("♔", BASE_W//2 - 200, 70, 40)
        draw_chess("♚", BASE_W//2 + 160, 70, 40)
        render_centered("WHAT IS YOUR NAME, STRATEGIST?", BASE_H//2 - 80, 26, wave=True)
        panel_rect = pygame.Rect(int((BASE_W//2-260)), int((BASE_H//2-30)), 520, 120)
        draw_panel(virtual_surface, panel_rect)
        render_centered(name, BASE_H//2 + 30, 34)
        for i, piece in enumerate(CHESS_PIECES):
            draw_chess(piece, 50 + i*90, BASE_H-60, 40, color=(200,200,220))
        fps_text = f"FPS: {clock.get_fps():.1f} | VSync (Not working in Fullscreen): {VSYNC} | Limit: {FRAME_LIMIT if not VSYNC else 'Disabled'}"
        font = get_font(max(1,int(18)))
        fps_surf = font.render(fps_text, True, (160,160,160))
        virtual_surface.blit(fps_surf, (10, BASE_H - 26))

        scaled_surf = pygame.transform.smoothscale(virtual_surface, (draw_w, draw_h))
        screen.fill((0,0,0))
        screen.blit(scaled_surf, (offset_x, offset_y))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
