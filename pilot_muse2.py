pilot_muse2.py
 
# This script is for the piloting of the Muse 2. The task will be completed twice, once with the EEG and once with the muse. 
# It includes to following parts for 3 minutes each: Resting state (RS), Heartbeat Counting (HBC), and Hand Squeeze (HS).

import psychopy
import os.path as op
from psychopy import event, visual, gui, core, parallel

# Task 1 = Resting State
# Task 2 = Heartbeat counting
# Task 3 = Hand Squeeze

### Create Window ###
win = visual.Window(color = '#000000', fullscr = False, monitor="testMonitor", units="pix") # Will need to change units to 'degree' when we know distance from monitor 
win.mouseVisible = False

### Link to Computer ###
p_port_resp = parallel.ParallelPort(address='0xDFF8')

## Fixation Cross function ###
### FIXATION CROSS COORDINATES 
horiz_line_fixation_start = [-25, 0]
horiz_line_fixation_end = [25, 0]

vert_line_fixation_start = [0, 25]
vert_line_fixation_end = [0, -25]
   
  ### FIXATION CROSS WHITE ### 
fixation_cross_vertical_white = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=white)

fixation_cross_horizontal_white = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=white)

fixation_cross_vertical_white.start = vert_line_fixation_start
fixation_cross_vertical_white.end = vert_line_fixation_end

fixation_cross_horizontal_white.start = horiz_line_fixation_start
fixation_cross_horizontal_white.end = horiz_line_fixation_end

### Instructions ###
instruction_RS_str = "In the following 3 minutes, try and stay as still as possible while looking at the fixation cross."
instruction_HBC_str = "In the following 3 minutes, count your heartbeats while looking at the fixation cross. Try and stay as still as possible."
instruction_HS_str = "In the following 3 minutes, squeeze your hand while looking at the fixation cross. Tru and stay as still as possible while doing so. Remember to keep squeezing throughout!"

instruction_RS = psychopy.visual.TextStim(win, text = instruction_RS_str, height = 0.80)
instruction_HBC = psychopy.visual.TextStim(win, text = instruction_HBC_str, height = 0.80)
instruction_HS = psychopy.visual.TextStim(win, text = instruction_HS_str, height = 0.80)


### RS Experiment ###
p_port_resp.setData(1) # marking the start of the RS

instruction_RS.draw()
win.flip()
core.wait(info['cueTIME'])


# Insert Fixation Cross + timings 
vert_line_fixation_start.draw()
vert_line_fixation_end.draw()
win.flip()
core.wait(180)

p_port_resp.setData(1) # marking the end of the RS

### HBC Experiment ###
p_port_resp.setData(2) # marking the start of the HBC

instruction_HBC.draw()
win.flip()
core.wait(info['cueTIME'])

# Insert Fixation Cross + timings 
vert_line_fixation_start.draw()
vert_line_fixation_end.draw()
win.flip()
core.wait(180)

p_port_resp.setData(2) # marking the end of the HBC

### HS Experiment ###
p_port_resp.setData(3) # marking the start of the HS

instruction_HS.draw()
win.flip()
core.wait(info['cueTIME'])

# Insert Fixation Cross + timings 
vert_line_fixation_start.draw()
vert_line_fixation_end.draw()
win.flip()
core.wait(180)

p_port_resp.setData(3) # marking the end of the HS

