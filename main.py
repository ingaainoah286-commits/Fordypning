import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Running Girl")
clock = pygame.time.Clock()

# Check if files exist
if not os.path.exists("BG.png"):
    print("ERROR: BG.png not found!")
if not os.path.exists("Run(1).png"):
    print("ERROR: Run(1).png not found!")

background = pygame.image.load("BG.png")


# Load your PNG sprites from folders
running_frames = [
    pygame.image.load("Run/Run(1).png"),
    pygame.image.load("Run/Run(2).png"),
    pygame.image.load("Run/Run(3).png"),
    pygame.image.load("Run/Run(4).png"),
    pygame.image.load("Run/Run(5).png"),
    pygame.image.load("Run/Run(6).png"),
    pygame.image.load("Run/Run(7).png"),
    pygame.image.load("Run/Run(8).png"),
    pygame.image.load("Run/Run(9).png"),
    pygame.image.load("Run/Run(10).png"),
    pygame.image.load("Run/Run(11).png"),
    pygame.image.load("Run/Run(12).png"),
    pygame.image.load("Run/Run(13).png"),
    pygame.image.load("Run/Run(14).png"),
    pygame.image.load("Run/Run(15).png"),
    pygame.image.load("Run/Run(16).png"),
    pygame.image.load("Run/Run(17).png"),
    pygame.image.load("Run/Run(18).png"),
    pygame.image.load("Run/Run(19).png"),
    pygame.image.load("Run/Run(20).png"),
]

jumping_frames = [
    pygame.image.load("Jump/Jump(1).png"),
    pygame.image.load("Jump/Jump(2).png"),
    pygame.image.load("Jump/Jump(3).png"),
    pygame.image.load("Jump/Jump(4).png"),
    pygame.image.load("Jump/Jump(5).png"),
    pygame.image.load("Jump/Jump(6).png"),
    pygame.image.load("Jump/Jump(7).png"),
    pygame.image.load("Jump/Jump(8).png"),
    pygame.image.load("Jump/Jump(9).png"),
    pygame.image.load("Jump/Jump(10).png"),
    pygame.image.load("Jump/Jump(11).png"),
    pygame.image.load("Jump/Jump(12).png"),
    pygame.image.load("Jump/Jump(13).png"),
    pygame.image.load("Jump/Jump(14).png"),
    pygame.image.load("Jump/Jump(15).png"),
    pygame.image.load("Jump/Jump(16).png"),
    pygame.image.load("Jump/Jump(17).png"),
    pygame.image.load("Jump/Jump(18).png"),
    pygame.image.load("Jump/Jump(19).png"),
    pygame.image.load("Jump/Jump(20).png"),
    pygame.image.load("Jump/Jump(21).png"),
    pygame.image.load("Jump/Jump(22).png"),
    pygame.image.load("Jump/Jump(23).png"),
    pygame.image.load("Jump/Jump(24).png"),
    pygame.image.load("Jump/Jump(25).png"),
    pygame.image.load("Jump/Jump(26).png"),
    pygame.image.load("Jump/Jump(27).png"),
    pygame.image.load("Jump/Jump(28).png"),
    pygame.image.load("Jump/Jump(29).png"),
    pygame.image.load("Jump/Jump(30).png"),
]

idle_frames = [
    pygame.image.load("Idle/Idle(1).png"),
    pygame.image.load("Idle/Idle(2).png"),
    pygame.image.load("Idle/Idle(3).png"),
    pygame.image.load("Idle/Idle(4).png"),
    pygame.image.load("Idle/Idle(5).png"),
    pygame.image.load("Idle/Idle(6).png"),
    pygame.image.load("Idle/Idle(7).png"),
    pygame.image.load("Idle/Idle(8).png"),
    pygame.image.load("Idle/Idle(9).png"),
    pygame.image.load("Idle/Idle(10).png"),
    pygame.image.load("Idle/Idle(11).png"),
    pygame.image.load("Idle/Idle(12).png"),
    pygame.image.load("Idle/Idle(13).png"),
    pygame.image.load("Idle/Idle(14).png"),
    pygame.image.load("Idle/Idle(15).png"),
    pygame.image.load("Idle/Idle(16).png"),
]

dead_frames = [
    pygame.image.load("Dead/Dead(3).png"),
    pygame.image.load("Dead/Dead(4).png"),
    pygame.image.load("Dead/Dead(5).png"),
    pygame.image.load("Dead/Dead(6).png"),
    pygame.image.load("Dead/Dead(7).png"),
    pygame.image.load("Dead/Dead(8).png"),
    pygame.image.load("Dead/Dead(9).png"),
    pygame.image.load("Dead/Dead(10).png"),
    pygame.image.load("Dead/Dead(11).png"),
    pygame.image.load("Dead/Dead(12).png"),
    pygame.image.load("Dead/Dead(13).png"),
    pygame.image.load("Dead/Dead(14).png"),
    pygame.image.load("Dead/Dead(15).png"),
    pygame.image.load("Dead/Dead(16).png"),
    pygame.image.load("Dead/Dead(17).png"),
    pygame.image.load("Dead/Dead(18).png"),
    pygame.image.load("Dead/Dead(19).png"),
    pygame.image.load("Dead/Dead(20).png"),
    pygame.image.load("Dead/Dead(21).png"),
    pygame.image.load("Dead/Dead(22).png"),
    pygame.image.load("Dead/Dead(23).png"),
    pygame.image.load("Dead/Dead(24).png"),
    pygame.image.load("Dead/Dead(25).png"),
    pygame.image.load("Dead/Dead(26).png"),
    pygame.image.load("Dead/Dead(27).png"),
    pygame.image.load("Dead/Dead(28).png"),
    pygame.image.load("Dead/Dead(29).png"),
    pygame.image.load("Dead/Dead(30).png"),
]



# Player setup
player_x = 100
player_y = 400
player_width = 50
player_height = 50
is_jumping = False
jump_velocity = 0
gravity = 0.5

# Animation
frame_index = 0
frame_counter = 0

# Obstacles
obstacles = []
obstacle_spawn_timer = 0

# Game state
running = True
game_over = False

# Main game loop
while running:
    clock.tick(60)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                is_jumping = True
                jump_velocity = -15
    
    # Spawn obstacles
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer > 60:
        obstacles.append(pygame.Rect(800, 450, 40, 40))
        obstacle_spawn_timer = 0
    
    # Move obstacles
    for obstacle in obstacles:
        obstacle.x -= 7
    
    # Remove off-screen obstacles
    obstacles = [obs for obs in obstacles if obs.x > 0]
    
    # Jump physics
    if is_jumping:
        jump_velocity += gravity
        player_y += jump_velocity
        
        if player_y >= 400:
            player_y = 400
            is_jumping = False
    
    # Animation frame cycling
    frame_counter += 1
    if frame_counter >= 5:
        frame_index = (frame_index + 1) % len(running_frames)
        frame_counter = 0
    
    # Draw background
    screen.blit(background, (0, 0))
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
    
    # Draw player
    if game_over:
        current_frame = dead_frames[frame_index % len(dead_frames)]
    elif is_jumping:
        current_frame = jumping_frames[frame_index % len(jumping_frames)]
    else:
        current_frame = running_frames[frame_index]
    
    screen.blit(current_frame, (player_x, player_y))
    
    pygame.display.flip()

pygame.quit()
