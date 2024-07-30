import random
import cocotb
import cocotb_coverage

from cocotb_checkpoint import checkpoint

from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.clock import Clock, Timer

@cocotb.test
async def test_checkpoint(dut):
    """Testing Counter core"""

    checkpoint.get_checkpoint_hier(dut)
    
    log = cocotb.logging.getLogger("cocotb.test")
    cocotb.start_soon(Clock(dut.clk, 1000).start())
                
    #reset the DUT
    dut.rst_n.value = 0
    await Timer(1500)
    dut.rst_n.value = 1
    
    await Timer(100000)

    assert dut.cnt_value == 100
    assert dut.sub_cnt_value == 100

    chkp_cnt_is_100 = checkpoint.checkpoint()

    dut.rst_n.value = 0
    await Timer(1500)
    dut.rst_n.value = 1

    assert dut.cnt_value == 0
    assert dut.sub_cnt_value == 0

    checkpoint.restore(chkp_cnt_is_100)

    await RisingEdge(dut.clk)

    assert dut.cnt_value == 100
    assert dut.sub_cnt_value == 100

    await Timer(100000)

    assert dut.cnt_value == 200
    assert dut.sub_cnt_value == 200

    chkp_cnt_is_200 = checkpoint.checkpoint()

    checkpoint.restore(chkp_cnt_is_100)

    await RisingEdge(dut.clk)

    assert dut.cnt_value == 100
    assert dut.sub_cnt_value == 100

    checkpoint.restore(chkp_cnt_is_200)

    await RisingEdge(dut.clk)

    assert dut.cnt_value == 200
    assert dut.sub_cnt_value == 200  
    
    await Timer(50000)

    assert dut.cnt_value == 250
    assert dut.sub_cnt_value == 250