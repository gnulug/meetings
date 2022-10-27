
test.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <func_call>:
   0:	f3 0f 1e fa          	endbr64 
   4:	c3                   	ret    

0000000000000005 <main>:
   5:	f3 0f 1e fa          	endbr64 
   9:	53                   	push   %rbx
   a:	90                   	nop
   b:	90                   	nop
   c:	b9 0e 00 00 00       	mov    $0xe,%ecx
  11:	48 8d 1d 00 00 00 00 	lea    0x0(%rip),%rbx        # 18 <main+0x13>
  18:	48 89 da             	mov    %rbx,%rdx
  1b:	be 01 00 00 00       	mov    $0x1,%esi
  20:	bf 01 00 00 00       	mov    $0x1,%edi
  25:	e8 00 00 00 00       	call   2a <main+0x25>
  2a:	90                   	nop
  2b:	90                   	nop
  2c:	b8 01 00 00 00       	mov    $0x1,%eax
  31:	ba 0e 00 00 00       	mov    $0xe,%edx
  36:	89 c7                	mov    %eax,%edi
  38:	48 89 de             	mov    %rbx,%rsi
  3b:	0f 05                	syscall 
  3d:	90                   	nop
  3e:	90                   	nop
  3f:	b8 00 00 00 00       	mov    $0x0,%eax
  44:	5b                   	pop    %rbx
  45:	c3                   	ret    
