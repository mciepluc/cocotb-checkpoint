
module sub_cnt (
  clk, 
  rst_n, 
  cnt_value
);

  input clk, rst_n;
  output reg [7:0] cnt_value;
  
  always @(posedge clk, negedge rst_n)
    if (~rst_n)
      cnt_value <= 8'd0;
    else
      cnt_value <= cnt_value + 1'b1;

endmodule

module counter (
  clk, 
  rst_n, 
  cnt_value,
  sub_cnt_value
);

  input clk, rst_n;
  output reg [7:0] cnt_value;
  output reg [7:0] sub_cnt_value;
 
  sub_cnt sub_cnt_i (
    .clk(clk),
    .rst_n(rst_n),
    .cnt_value(sub_cnt_value)
  );
  
  
  always @(posedge clk, negedge rst_n)
    if (~rst_n)
      cnt_value <= 8'd0;
    else
      cnt_value <= cnt_value + 1'b1;

endmodule

module top (); 

  logic clk;
  logic rst_n;
  logic [7:0] cnt_value;
  logic [7:0] sub_cnt_value;

  initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,dut);
  end
  
  counter dut (
    .clk(clk),
    .rst_n(rst_n),
    .cnt_value(cnt_value),
    .sub_cnt_value(sub_cnt_value)
  );

endmodule
