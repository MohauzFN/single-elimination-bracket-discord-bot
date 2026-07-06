def draw_text_bracket(tournament):
    if not tournament.started:
        return "Tournament hasn't started yet!"
    
    lines = [f"=== ROUND {tournament.current_round + 1} ==="]
    current_matches = tournament.rounds[tournament.current_round]
    
    for idx, match in enumerate(current_matches):
        status = f"Winner: {match['winner']}" if match['winner'] else "(Pending)"
        lines.append(f"Match {idx + 1}: {match['p1']} vs {match['p2']} {status}")
        
    return "\n".join(lines)