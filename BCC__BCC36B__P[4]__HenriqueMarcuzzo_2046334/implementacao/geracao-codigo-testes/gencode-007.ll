; ModuleID = "gencode-007.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

define i32 @"soma"(i32 %"x", i32 %"y") 
{
entry:
  br label %"exit"
exit:
  %".5" = add i32 %"x", %"y"
  ret i32 %".5"
}

define i32 @"sub"(i32 %"z", i32 %"t") 
{
entry:
  br label %"exit"
exit:
  %".5" = add i32 %"z", %"t"
  ret i32 %".5"
}

define i32 @"main"() 
{
entry:
  %"a" = alloca i32, align 4
  %"b" = alloca i32, align 4
  %"c" = alloca i32, align 4
  %"i" = alloca i32, align 4
  br label %"exit"
exit:
  ret i32 0
}
