import pygame
import sys
import time

pygame.init()

VSYNC = 0 # Refresh Rate can only be pulled after setting display window size

# --- Config ---
WIDTH, HEIGHT = 640, 480
FPS = VSYNC # Set a custom FPS limit if needed, or use monitor refresh rate by setting to "VSYNC"
MAX_NAME_LEN = 15

BG_COLOR = (0, 0, 0)
PANEL_COLOR = (10, 10, 10)
TEXT_COLOR = (255, 255, 255)
ACCENT = (127, 255, 212)  # teal-ish Undertale like text
BORDER_COLOR = (40, 40, 40)


def load_font(size):
    # Try common Undertale-like font family names (may not exist on user's system).
    for name in ["Determination Mono", "Determination Sans", "Undertale", "PixelFont", "Courier New"]:
        try:
            f = pygame.font.SysFont(name, size)
            # quick check: ensure the font can render text width > 0
            if f.size("X")[0] > 0:
                return f
        except Exception:
            pass
    # ultimate fallback:
    return pygame.font.SysFont("couriernew", size, bold=True)

TITLE_FONT = load_font(40)
PROMPT_FONT = load_font(28)
INPUT_FONT = load_font(34)
SMALL_FONT = load_font(18)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Choose Your Name")
clock = pygame.time.Clock()

# State
name = ""
cursor_visible = True
cursor_timer = 0.0
CURSOR_BLINK_INTERVAL = 0.5

# Utility: draw a rounded-ish panel (simple)
def draw_panel(surface, rect, border=4):
    pygame.draw.rect(surface, BORDER_COLOR, rect.inflate(border*2, border*2))
    pygame.draw.rect(surface, PANEL_COLOR, rect)

def render_centered_text(surface, font, text, y, color=TEXT_COLOR):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    surface.blit(surf, rect)
    return rect

def main_loop():
    global name, cursor_visible, cursor_timer

    running = True
    confirmed_name = None
    last_time = time.time()

    while running:
        dt = time.time() - last_time
        last_time = time.time()
        cursor_timer += dt
        if cursor_timer >= CURSOR_BLINK_INTERVAL:
            cursor_visible = not cursor_visible
            cursor_timer -= CURSOR_BLINK_INTERVAL

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                confirmed_name = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    confirmed_name = None
                elif event.key == pygame.K_BACKSPACE:
                    # remove last char
                    name = name[:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # confirm
                    if len(name.strip()) == 0:
                        # slightly refusing empty names; you can allow if you prefer
                        # flash or beep - we'll flash the panel by toggling accent quickly
                        flash_panel()
                    else:
                        confirmed_name = name
                        running = False
                else:
                    # accept visible characters, uppercase them to match Undertale style
                    ch = event.unicode
                    if ch.isprintable() and len(name) < MAX_NAME_LEN:
                        # You can limit to alphanum + space + punctuation as needed:
                        name += ch.upper()

        # draw frame
        screen.fill(BG_COLOR)
        VSYNC = pygame.display.() # Pulls Screen Refresh Rate if FPS CAP is set to VSYNC

        # Title top-left (small)
        title_surf = SMALL_FONT.render("UNDERTALE - NAME ENTRY", True, ACCENT)
        screen.blit(title_surf, (12, 12))

        # Main centered prompt
        render_centered_text(screen, TITLE_FONT, "WHAT IS YOUR NAME?", HEIGHT // 2 - 80)

        # Input panel dims
        panel_w, panel_h = 520, 120
        panel_rect = pygame.Rect((WIDTH//2 - panel_w//2, HEIGHT//2 - panel_h//2 + 30), (panel_w, panel_h))

        # Draw panel with border
        draw_panel(screen, panel_rect)

        # Draw name text inside panel, left padded
        padding = 24
        input_area = pygame.Rect(panel_rect.left + padding, panel_rect.top + padding,
                                 panel_rect.width - padding*2, panel_rect.height - padding*2)

        # Draw sample underscore boxes like Undertale (optional)
        # We'll draw a thin baseline and the typed name above it.
        baseline_y = input_area.top + input_area.height // 2 + 10
        pygame.draw.line(screen, BORDER_COLOR, (input_area.left, baseline_y), (input_area.right, baseline_y), 2)

        # Render current name
        name_surf = INPUT_FONT.render(name, True, TEXT_COLOR)
        name_rect = name_surf.get_rect(midleft=(input_area.left + 6, baseline_y - 12))
        screen.blit(name_surf, name_rect)

        # small help text
        help_text = "ENTER to confirm — ESC to cancel — Backspace to delete"
        render_centered_text(screen, SMALL_FONT, help_text, panel_rect.bottom + 18, color=(180,180,180))

        # character count
        count_text = f"{len(name)}/{MAX_NAME_LEN}"
        count_surf = SMALL_FONT.render(count_text, True, (180,180,180))
        screen.blit(count_surf, (panel_rect.right - count_surf.get_width() - 8, panel_rect.bottom + 6))

        pygame.display.flip()
        clock.tick(FPS)

    # after loop
    if confirmed_name is not None:
        print("CONFIRMED NAME:", confirmed_name)
    else:
        print("Name entry cancelled.")
    pygame.quit()
    sys.exit()

def flash_panel(duration=0.12, times=2):
    # Quick visual flash by toggling the whole screen accent a couple times.
    # This is called when user tries to confirm empty name.
    original_bg = screen.copy()
    for _ in range(times):
        screen.fill(ACCENT)
        pygame.display.flip()
        pygame.time.delay(int(duration*1000))
        screen.blit(original_bg, (0,0))
        pygame.display.flip()
        pygame.time.delay(int(duration*1000))

if __name__ == "__main__":
    main_loop()

