#!/usr/bin/bash
  export DISPLAY=:0
  xrandr -o left
  xset s off
  xset -dpms
  xset s noblank
  chromium-browser --check-for-update-interval=604800 --simulate-critical-update --disable-component-update --noerrdialogs --incognito --kiosk https://dakboard.com/screen/uuid/{uuid} &
