def show_statistics(stats):
    """Show the current game session statistics."""
    print(f"\n{COLOR_MAGENTA}=== SESSION SCOREBOARD ==={COLOR_RESET}")
    print(f"Games Won:    {stats['wins']}")
    print(f"Games Lost:   {stats['losses']}")
    print(f"Total Score:  {stats['score']} points")
    print(f"==========================\n")

    # Esto va DENTRO de def show_menu():
game_stats = {
    "wins": 0,
    "losses": 0,
    "score": 0
}