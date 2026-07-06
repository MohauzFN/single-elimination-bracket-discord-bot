# Single Elimination Bracket

A modular Python framework designed to handle a single elimination bracket tournament using multiple asynchronous events. This project allows users to host tournaments solely through discord, without the need of any third-party applications.

## Features & Roadmap
- [x] **Automatic Bracket generation:** Generates players and seeds byes, and brackets fill to a power of two. 
- [x] **Text-based bracket interface:** Presents a visual match of the current round.
- [x] **Match reporting:**  Report winners match-by-match; the bot automatically advances to the next round once all results for the current round are reported
- [x] **User Hierarchy:** Role based access separating administrators and players

## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Math, Random

## Commands

| Commands | Role | State | Description |
| :--- | :---: | :---: | ---: |
| **!t_create** | Admin | Not Applicable | Creates a tournament with registration |
| **!t_start** | Admin | Not Started | Generates the tournament bracket, requires two players minimum |
| **!join** | Anyone | Not Started | Registers user for tournament |
| **!leave** | Anyone | Not Started | Removes user from tournament |
| **!report** | Anyone | Started | Reports winner of the match |
| **!bracket** | Anyone | Started | Presents visual of the current round of the bracket |


## Notes
- The discord bot runs locally, the discord server ID needs to be hardcoded
