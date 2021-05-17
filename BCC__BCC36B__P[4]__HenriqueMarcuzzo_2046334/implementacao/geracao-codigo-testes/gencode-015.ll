; ModuleID = "gencode-015.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

define i32 @"func"(i32 %"p1", float %"p2") 
{
entry:
  %"r" = alloca i32, align 4
  br label %"exit"
exit:
  %".5" = load i32, i32* %"r"
  ret i32 %".5"
}

define i32 @"main"() 
{
entry:
  %"x" = alloca i32, align 4
  %".2" = call i32 @"func"(i32 1, float 0x4000000000000000)
  %"expression" = add i32 0, %".2"
  store i32 %"expression", i32* %"x"
  br label %"exit"
exit:
  ret i32 0
}
