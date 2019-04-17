# nx-sd 

nx-sd is a lightweight, ready-to-use custom firmware package for the Nintendo Switch. It includes everything necessary for launching homebrew.


## Quick Start Guide

1. Download and extract the [latest release](https://github.com/designgears/nx-sd/releases/latest) of nx-sd.
2. Copy the contents of the `sdcard` folder to the root of your microSD card.
3. Power on your Nintendo Switch in RCM and inject the payload in `payload` folder.
4. Atmosphère will boot automatically.

## Building

1. Install [Docker](https://hub.docker.com/search/?type=edition&offering=community) and [Python 3.7](https://www.python.org/downloads/).

2. Clone this repo and all submodules recursively.

       git clone https://github.com/designgears/nx-sd.git --recurse-submodules

3. Run `python3 build.py`.

## Components

### Core components

| Component                                                 | Description |
| --------------------------------------------------------- | ----------- |
| [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere) | Custom firmware for the Nintendo Switch |
| [nx-hbloader](https://github.com/switchbrew/nx-hbloader)  | Host process for loading homebrew NROs |
| [nx-hbmenu](https://github.com/switchbrew/nx-hbmenu)      | The Nintendo Switch homebrew menu |
| [sigpatches](https://bit.ly/2EYbEHg)                      | Sweet patches! |

### Addons

| Component                                                 | Description |
| --------------------------------------------------------- | ----------- |
| [EdiZon](https://github.com/WerWolv/EdiZon)               | Save manager, editing tool, and memory trainer |
| [EdiZon Scripts](https://bit.ly/2V0kXMt)                  | Cheats, configs, and scripts for EdiZon |
| [ldn_mitm](https://github.com/spacemeowx2/ldn_mitm)       | Play local wireless supported games online |
| [Lockpick_RCM](https://github.com/shchmue/Lockpick_RCM)   | Encryption key derivation bare metal RCM payload |
| [sys-CLK](https://github.com/retronx-team/sys-clk)        | Overclocking/underclocking system module |
| [Goldleaf](https://github.com/XorTroll/Goldleaf)          | Nintendo Switch multipurpose homebrew tool |
