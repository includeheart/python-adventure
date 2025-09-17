# Python Adventure (Text RPG)

A tiny text-based adventure you run in the terminal. You’re an intrepid adventurer hired to retrieve a rare potion from a mysterious house and escape through the garden — but a hungry monster lurks within.

## What’s here
- Single-file game: `main.py`
- Starting room: Foyer
- Rooms to explore: Foyer, Hall, Kitchen, Dining Room, Garden, Pantry, Bedroom, Bathroom, Basement
- Items to find: dagger, key, potion (and possibly a monster…)

## How to run
Prerequisites: Python 3.x — If you don’t have Python installed, download it here: https://www.python.org/downloads/

On Windows PowerShell, from this folder:

```powershell
python .\main.py
# or
py .\main.py
```

On macOS/Linux (Terminal):

```bash
python3 ./main.py
# or, if `python` already points to Python 3
python ./main.py
```

On Windows Command Prompt (cmd.exe):

```cmd
python main.py
``` 

## How to play
Type commands at the prompt. Available commands:

- `go [direction]` — Move between rooms (e.g., `go north`, `go east`, `go down`, `go up`).
- `look` — Look around the current room for a richer description.
- `get [item]` — Pick up an item in the room.
- `drop [item]` — Drop an item from your inventory into the current room.
- `examine [item]` — Inspect an item in your inventory.
- `quit` — Exit the game.

Your current room and inventory are shown each turn. If a room contains an item, you’ll see it in the status line.

## Goal and outcomes
- Win: Carry the `potion` into the `Garden`.
- Lose: Enter a room with the `monster` without having the `dagger` in your inventory.
- If you do have the `dagger` when you meet the monster, you’ll slay it and can continue.

## Notes
- Movement: Typical directions are `north`, `south`, `east`, `west`, plus `up`/`down` for stairs.
- The `look` command provides a different description when a room currently contains an item.
- The `key` is collectible; it’s a hook for future features (e.g., unlocking a chest in the basement).

## Ideas to extend (later)
- Locked containers/doors that use the key
- More rooms and items (health, armor, spells)
- Save/load and scoring
- Better parser and input validation

Have fun exploring — and watch out for that kitchen…