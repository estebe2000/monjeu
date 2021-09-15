import pygame
from application import Application


surfaceW = 1080  # Dimension de la fenêtre / Largeur
surfaceH = 720  # Dimension de la fenêtre / Longueur
global user_name

app = Application(surfaceW, surfaceH)
app.menu()

clock = pygame.time.Clock()

while app.statut:
    app.update()
    clock.tick(30)

pygame.quit()