// R0 * R1 = R2
// index = R0
// value = R1

// set index to the value in R0
@R0
D=M
@index
M=D
@R2
M=0

(LOOP)
	// test if index <= 0
	@index
	D=M
	@END
	D;JEQ

	// R2 = R2 + R1
	@R1
	D=M
	@R2
	M=M+D

	// index = index - 1
	@index
	M=M-1

	// go to LOOP
	@LOOP
	0;JMP

(END)
	@END
	0;JMP