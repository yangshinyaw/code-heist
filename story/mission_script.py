def intro_story():
    return """
🔍 [MISSION BRIEFING]
You're codenamed GHOST. A rogue whistleblower has requested your help to expose the secrets of NEUROCORP.

Your objective: break through 4 layers of digital security to access the CORE VAULT.

System Layers:
1. Employee Login Vault
2. Encrypted Internal Chat
3. Network Logic Firewall
4. Core Data Maze

Your every keystroke is being watched.
One mistake... and you're locked out for good.

Prepare yourself.

"""

def outro_story(success=True):
    if success:
        return """
🎉 [MISSION COMPLETE]

You've breached NEUROCORP's deepest vault.
The data has been extracted. Corruption will be exposed.

GHOST out. 🕶️
"""
    else:
        return """
💀 [MISSION FAILED]

The system detected your intrusion.
All connections have been terminated.

The truth remains hidden.
"""
