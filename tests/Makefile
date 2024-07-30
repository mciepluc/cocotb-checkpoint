TOPLEVEL := top
TOPLEVEL_LANG := verilog

PWD=$(shell pwd)
DUT = $(PWD)/hdl

VERILOG_SOURCES = $(DUT)/counter.v

MODULE := test_checkpoint

include $(shell cocotb-config --makefiles)/Makefile.sim
