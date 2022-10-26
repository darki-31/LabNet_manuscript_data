from pyControl.utility import *
from devices import *

# pyControl state machine implementation for the latency measurements.
# We need to cennect two pins to the measurement RasPi. One for the external trigger event "Y7" and for the response "Y8".
# On the RasPi we need to start the "perf_test" program from "examples/cpp/perf_test" folder.

# we need both rising and falling events
p_in  = Digital_input('Y7', rising_event='p_on', falling_event='p_off')
p_out = Digital_output('Y8')

# States and events.

states = ['on_state',
          'off_state']

events = ['p_on', 'p_off']

initial_state = 'on_state'
        
# state machine flow description:
# 1. enter “on_state” -> turn “p_out” off
# 2. wait until external trigger “p_on” -> go to the state “off_state”
# 3. enter “off_state” -> turn p_out on
# 4. wait until external trigger “p_off” -> go to the state “on_state” and repeat from 1.


def on_state(event):
    if event == 'entry':
        p_out.off()
    elif event == 'p_on':
        goto_state('off_state')

def off_state(event):
    if event == 'entry':
        p_out.on()
    elif event == 'p_off':
        goto_state('on_state')

