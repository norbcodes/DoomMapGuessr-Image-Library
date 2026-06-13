# DoomMapGuessr Image Library (v3.0.0)
Image library for DoomMapGuessr v3.0.0. Does not contain the actual database.

## Contents
Contains screenshots used in the game [DoomMapGuessr (v3.0.0+)](https://github.com/mf366-dev/DoomMapGuessr), by [Matthew](https://github.com/mf366-dev).

Screenshots are organized by:
* Game
* Episode
* Map

It is recommended to take a look at the DoomMapGuessr screenshot database to better understand the organization of the image library.

## Statistics
Read the most recent statistics report [here](https://github.com/mf366-dev/DoomMapGuessr/blob/v3.0.0-dev/data/reports/13-06-26/REPORT.md).

## Contibutions
Anyone is welcome to contribute to this image library, however certain rules must be followed.

### Step 1: Before Contributing
1. Fork this repository.
2. Use one of the recommended source ports (for simplicity): DSDA-Doom or GZDoom (for Classic DOOM) and DOOM 64 EX Plus (for DOOM 64).
3. In the source port you'll use make sure all HUD (status bar, messages and cross-hairs) are disabled or invisible (in GZDoom, this means setting screen size to the maximum value in order to remove all HUD; in DSDA-Doom, it means pressing F5 repeatedly until the HUD is invisible).
4. In the very same source port, make sure freelooking is also disabled.
5. In the very same source port, you may hide the weapon if you feel it improves the quality of your screenshots, but it's not an obligation to do so.

**Information:**
* Some source ports (like GZDoom) sometimes display `-0` as a coordinate. Consider it to be `0`.

### Step 2: Screenshotting
1. Open your source port (preferably DSDA-Doom or GZDoom) with the WAD you want to screenshot.
2. Select the episode and map.
3. Move to the place you wish to take a screenshot of.
4. Before screenshotting, register the position somewhere you'll remember (use cheat **`idmypos`** or command `myinfo` if using ZDoom). It is up to the individual screenshotting to decide whether they wish to play with no monsters or with monsters *(no monsters is recommended for most cases)*. **You must register only X and Y. Both Angle and Z are unnecessary.**
5. Upon registering the position (X and Y), remove all clutter from the screen and take the actual screenshot.
6. Rename the screenshot to match the following convention: `<x value>_<y value>_TO-BE-RANKED.<format>` (example: `-551_35_TO-BE-RANKED.png`). Only JPG/PNG are accepted (`.jpeg` extension is accepted), preferably with ratio 16:9, although 4:3 and 1:1 are equally accepted.

#### Refusal of database changes
**DO NOT MAKE CHANGES TO THE DATABASE!**

Changes to the official database are strictly forbidden. Your Pull Request may add 10000 screenshots for all I care - if it has DB changes, it's getting rejected.

#### Note
The image library does not care about the coordinates - only DoomMapGuessr does. That's why screenshots that have been accepted, ranked, evaluated and added to the database by Matthew will have their names changed to something simpler, for simplification purposes.

### Step 3: Contributing
1. Place the screenshot(s) in their correct folders, respecting the `Game -> Episode -> Map` structure.
2. Edit the `TODO.md` file, but **DON'T** mark the maps you screenshotted as complete - simply add a note next to them saying `TO BE EVALUATED AND RANKED`.
3. Create a Pull Request.

**Thank you for contributing!** :heart:
