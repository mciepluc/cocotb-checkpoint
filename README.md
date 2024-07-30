# cocotb-checkpoint
Checkpointing functionality for cocotb.
Logic state of the DUT is stored in a dict. You may create any number of checkpoints and restore them aribitrary. Check the unit test [example](https://github.com/mciepluc/cocotb-checkpoint/tree/main/tests).
Check the https://github.com/mciepluc/apbi2c_cocotb_example for an advanced testbench. 


### Code Example
```Python
from cocotb_checkpoint import checkpoint

@cocotb.test
async def example(dut):

    ...

    checkpoint.get_checkpoint_hier(dut)
    
    ...

    new_checkpoint = checkpoint.checkpoint() # save the DUT state at this point

    ...

    checkpoint.restore(new_checkpoint) # restore saved DUT state

    ...

```
