; ModuleID = "gencode-010.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

@"n" = common global i32 0, align 4
define i32 @"fatorial"(i32 %"n") 
{
entry:
  %"fat" = alloca i32, align 4
  %"var_comper_right" = alloca i32
  %"var_comper_left" = alloca i32
  store i32 %"n", i32* %"var_comper_left"
  store i32 0, i32* %"var_comper_right"
  %"if_test" = icmp sgt i32* %"var_comper_left", %"var_comper_right"
  br i1 %"if_test", label %"iftrue", label %"iffalse"
iftrue:
  %"expression" = add i32 0, 1
  store i32 %"expression", i32* %"fat"
  %"var_comper" = alloca i32
  store i32 0, i32* %"var_comper"
  br label %"loop"
iffalse:
  br label %"exit.1"
ifend:
  call void @"escrevaInteiro"(i32 %"n")
  br label %"exit.2"
loop:
  %".9" = load i32, i32* %"fat"
  %"expression.1" = add i32 0, %".9"
  %"expression.2" = mul i32 %"expression.1", %"n"
  store i32 %"expression.2", i32* %"fat"
  %"expression.3" = add i32 0, %"n"
  %"expression.4" = sub i32 %"expression.3", 1
  %"var_pointer" = alloca i32
  store i32 %"n", i32* %"var_pointer"
  store i32 %"expression.4", i32* %"var_pointer"
  br label %"loop_val"
loop_val:
  %".14" = load i32, i32* %"var_comper"
  %"expression.5" = icmp eq i32 %"n", %".14"
  br i1 %"expression.5", label %"loop_end", label %"loop"
loop_end:
  br label %"exit"
exit:
  %".17" = load i32, i32* %"fat"
  ret i32 %".17"
exit.1:
  ret i32 0
exit.2:
  ret i32 0
}

define i32 @"main"() 
{
entry:
  %".2" = call i32 @"leiaInteiro"()
  store i32 %".2", i32* @"n", align 4
  %".4" = load i32, i32* @"n"
  %".5" = call i32 @"fatorial"(i32 %".4")
  call void @"escrevaInteiro"(i32 %".5")
  br label %"exit"
exit:
  ret i32 0
}
