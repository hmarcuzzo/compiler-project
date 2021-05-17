; ModuleID = "gencode-011.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

@"a" = common global i32 0, align 4
define i32 @"main"() 
{
entry:
  %"b" = alloca i32, align 4
  %"expression" = add i32 0, 10
  store i32 %"expression", i32* @"a"
  %"if_test" = icmp sge i32* @"a", i32 5
  br i1 %"if_test", label %"iftrue", label %"iffalse"
iftrue:
  %"expression.1" = add i32 0, 50
  store i32 %"expression.1", i32* %"b"
  br label %"ifend"
iffalse:
  %"expression.2" = add i32 0, 100
  store i32 %"expression.2", i32* %"b"
  br label %"ifend"
ifend:
  %".8" = load i32, i32* %"b"
  call void @"escrevaInteiro"(i32 %".8")
  br label %"exit"
exit:
  ret i32 0
}
