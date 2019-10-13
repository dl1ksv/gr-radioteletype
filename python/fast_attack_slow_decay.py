# -*- coding: utf-8 -*-

import numpy
from gnuradio import blocks
from gnuradio import gr

class fast_attack_slow_decay(gr.sync_block):
    """ Generate a variable threshold for fading signals
        See Frerking: Digital Signal Processing in Communication Systems
        pp 415 ff
    """
    def __init__(self,attack=0.7, decay=0.01):
        gr.sync_block.__init__(self,
            name = "Fast attack slow decay threshold",
            in_sig =  [numpy.float32,numpy.float32],
            out_sig = [numpy.float32,numpy.float32],
        )
        self.attack = attack
        self.decay  = decay
        self.max_mark =0.
        self.max_space =0.

    def work(self, input_items, output_items):  

        to_be_processed = len(output_items[0])

        for i in range(0,to_be_processed):
            if input_items[0][i] > self.max_mark :
                self.max_mark = (1. - self.attack ) * self.max_mark + self.attack * input_items[0][i]
            else:
                self.max_mark = (1. - self.decay ) * self.max_mark - self.decay * input_items[0][i]

            if input_items[1][i] > self.max_space :
                self.max_space = (1. - self.attack ) * self.max_space + self.attack * input_items[1][i]
            else:
                self.max_space = (1. - self.decay ) * self.max_space - self.decay * input_items[1][i]

            #if ( (input_items[0][i] -0.5 * self.max_mark ) - (input_items[1][i] -0.5 * self.max_space ) ) > 0 :
            #    output_items[0][i] = 1.
            #else:
            #    output_items[0][i] = 0.
            output_items[0][i] = input_items[0][i] -0.5 * self.max_mark
            output_items[1][i] = input_items[1][i] -0.5 * self.max_space
            
        return to_be_processed

