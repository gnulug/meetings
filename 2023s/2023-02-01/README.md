## GLUG Cloud Hardware Night

### Overview
   **GOAL:** 
   - All of the hardware either proven working or proven not working.<br/>
        - If it is proven working, get the firmware entirely updated.
        - If it is proven not working, write a quick log of what's wrong and remove it.
        - If it is not working, but you cannot proven that it is impossible for it to work in the future, write a quick log of what you tried.
    - Need to ID and match the Dell ready rails to each of the servers.

### General flow (an algorithm, if you will)
- Open up the servers and see if anything looks wrong, is out of place, or is missing or extra
    - Write down any thing for the inventory spreadsheet
- Firmware
    - Do the BIOS first, and go through most, if not all iterations:
        - Get the version of the BIOS
        - Set it to boot into compatibility mode (if applicable)
        - Set the boot order to boot from USB
        - See what other hardware is detected and if it has a firmware version number
    - Head over to the Dell Support page [GNULUG Cloud Wiki](https://github.com/gnulug/acm-glug-cloud/wiki/Server-hardware-manuals)
        - Search for "BIOS" -> Go through show more information -> Down at the bottom "other available versions"
        - Download all (if possible) or at least most versions and cat them onto your FreeDOS drive
        - **- Wouldn't hurt to run a search "site:reddit.com dell poweredge ${modelname} bios brick"**
    - Update, update, update
        - When you get to the DOS prompt, just type the name of the executable and press enter
    - Start on the BIOS now and then have a partner with a different FreeDOS drive loading up other firmware updates
        - On the Dell Support Site, filter on "Download Type: Firmware"

### Errata
- [HackerNews discussion that gives a good general overview of both the FreeDOS and the UEFI process](https://news.ycombinator.com/item?id=27039319)