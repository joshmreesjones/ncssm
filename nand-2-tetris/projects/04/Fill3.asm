
//Fill
(START)
	@KBD
	D=M
	@BLACK
	D;JGT

(WHITE)
	@i
	M=0

	(LOOPW)
		@i
		D=M
		@8096
		D=D-A
		@START
		D;JEQ

		@i
		D=M
		M=M+1
		@SCREEN
		A=D+A
		M=0
		@LOOPW
		0;JMP

(BLACK)
	@i
	M=0

	(LOOPB)
		@i
		D=M
		@8096
		D=D-A
		@START
		D;JEQ

		@i
		D=M
		M=M+1
		@SCREEN
		A=D+A
		M=
		@32767

		@LOOPB
		0;JMP