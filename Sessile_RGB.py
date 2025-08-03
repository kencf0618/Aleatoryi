import pygame
import random
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()
    
    static_surface = pygame.Surface((width, height))
    pixarray = pygame.PixelArray(static_surface)
    
    red = static_surface.map_rgb((255, 0, 0))
    green = static_surface.map_rgb((0, 255, 0))
    blue = static_surface.map_rgb((0, 0, 255))
    colors = [red, green, blue]
    
    for x in range(width):
        for y in range(height):
            pixarray[x, y] = random.choice(colors)
    
    del pixarray  # Commit changes to the surface
    
    screen.blit(static_surface, (0, 0))
    pygame.display.flip()
    
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt
            pygame.time.wait(100)
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
