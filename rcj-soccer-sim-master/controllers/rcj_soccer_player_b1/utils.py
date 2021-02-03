def get_direction(ball_angle: float) -> int:
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    if ball_angle >= 345 or ball_angle <= 15:
        return 0
    return -1 if ball_angle < 180 else 1
    
def get_distance(ball_pos, robot_pos):
     return ((((ball_pos['x'] - robot_pos['x'])**2) + ((ball_pos['y']-robot_pos['y'])**2) )**0.5)
    

