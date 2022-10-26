from collections import OrderedDict as odict
import tables
import itertools
import time
import datetime

import autopilot.hardware.gpio
from autopilot.tasks.task import Task

# Autopilot implementation for the latency measurements.
# It is a simplified version of, in the official Autopilot repository included, “free water task’s”. 
# We need to cennect two pins to the measurement RasPi. One for the external trigger event "sig_in" and for the response "sig_out".
# For pin numbers see the "prefs.json" file.
# On the RasPi we need to start the "perf_test" program from "examples/cpp/perf_test" folder.

class Timing_Test(Task):
    STAGE_NAMES = ["water", "response"]

    # Params
    PARAMS = odict()
    PARAMS['on_time'] = {'tag':'on duration (ms)',
                        'type':'int'}

    # we want to inform the Autopilot "terminal" about the current latency measurement trial number.
    DATA = {
        'trial_num': {'type':'i32'}
    }

    class TrialData(tables.IsDescription):
        trial_num = tables.Int32Col()

    # our hardware pins
    HARDWARE = {
        'GPIO':{
            'sig_in': autopilot.hardware.gpio.Digital_In,
            'sig_out': autopilot.hardware.gpio.Digital_Out,
        }
    }

    # Plot parameters
    PLOT = {
        'data': {
            'target': 'point'
        }
    }

    def __init__(self, stage_block=None, current_trial=0, on_time=10, **kwargs):
        super(Timing_Test, self).__init__()
        print('superclass initialized')

        if not stage_block:
            print('No stage_block Event() was passed, youll need to handle stage progression on your own')
        else:
            self.stage_block = stage_block

        self.on_time = int(on_time)
        self.target = 'sig_out'
        self.trial_counter = itertools.count(int(current_trial))
        self.triggers = {}

        # Stage list to iterate
        stage_list = [self.water, self.response]
        self.num_stages = len(stage_list)
        self.stages = itertools.cycle(stage_list)

        # Init hardware
        self.hardware = {}
        self.pin_id = {} # Inverse pin dictionary
        self.init_hardware()
        print('hardware initialized')

    # wait in this state until the external trigger "sig_in" is 1
    # then turn "sig_out" on and switch to "response" state
    def water(self, *args, **kwargs):
        self.stage_block.clear()
        self.target = 'sig_out'

        # Set triggers
        self.triggers['sig_in'] = [lambda: self.hardware['GPIO']['sig_out'].set(1)]

        # Return data
        data = {
            'trial_num': next(self.trial_counter)
        }

        return data

    # wait in this state for "on_time"
    # then turn "sig_out" off and switch to "water" state
    def response(self):
        time.sleep(self.on_time / 1000)
        self.hardware['GPIO']['sig_out'].set(0)

        return {'TRIAL_END':True}



