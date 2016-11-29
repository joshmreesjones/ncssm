@index
M=0

// main loop
(MAIN)
	// check for keyboard input
	@index
	M=D
	(KBDLOOP)
		// test for input
		@KBD
		D=M
		@index
		D=D-M
		
		// jump to KUP if no key is pressed
		@KDOWN
		D;JEQ

		@index
		M=M+1
		
		@KBDLOOP
		0;JMP
	
	// jump to KUP because no key is pressed
	@KUP
	0;JMP

(KDOWN)
	// fill screen
	@R1
	M=1
	@MAIN
	0;JMP

(KUP)
	// clear screen
	@R2
	M=1
	@MAIN
	0;JMP