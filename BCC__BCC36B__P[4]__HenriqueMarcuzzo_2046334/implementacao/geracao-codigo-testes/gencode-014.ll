; ModuleID = "gencode-014.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

define i32 @"fibonacciRec"(i32 %"n") 
{
entry:
  %"l" = alloca i32, align 4
  %"m" = alloca i32, align 4
  %"var_comper_right" = alloca i32
  %"var_comper_left" = alloca i32
  store i32 %"n", i32* %"var_comper_left"
  store i32 1, i32* %"var_comper_right"
  %"if_test" = icmp sle i32* %"var_comper_left", %"var_comper_right"
  br i1 %"if_test", label %"iftrue", label %"iffalse"
iftrue:
  br label %"exit"
iffalse:
  %"expression" = add i32 0, %"n"
  %"expression.1" = sub i32 %"expression", 1
  store i32 %"expression.1", i32* %"l"
  %"expression.2" = add i32 0, %"n"
  %"expression.3" = sub i32 %"expression.2", 2
  store i32 %"expression.3", i32* %"m"
  br label %"exit.1"
ifend:
  br label %"exit.2"
exit:
  ret i32 %"n"
exit.1:
  br label %"ifend"
exit.2:
  ret i32 0
}

define i32 @"fibonacciIter"(i32 %"n") 
{
entry:
  %"i" = alloca i32, align 4
  %"f" = alloca i32, align 4
  %"k" = alloca i32, align 4
  %"expression" = add i32 0, 1
  store i32 %"expression", i32* %"i"
  %"expression.1" = add i32 0, 0
  store i32 %"expression.1", i32* %"f"
  %"expression.2" = add i32 0, 1
  store i32 %"expression.2", i32* %"k"
  %"var_comper" = alloca i32
  br label %"loop"
loop:
  %".7" = load i32, i32* %"i"
  %"expression.3" = add i32 0, %".7"
  %".8" = load i32, i32* %"f"
  %"expression.4" = add i32 %"expression.3", %".8"
  store i32 %"expression.4", i32* %"f"
  %".10" = load i32, i32* %"f"
  %"expression.5" = add i32 0, %".10"
  %".11" = load i32, i32* %"i"
  %"expression.6" = sub i32 %"expression.5", %".11"
  store i32 %"expression.6", i32* %"i"
  %".13" = load i32, i32* %"k"
  %"expression.7" = add i32 0, %".13"
  %"expression.8" = add i32 %"expression.7", 1
  store i32 %"expression.8", i32* %"k"
  br label %"loop_val"
loop_val:
  %".16" = load i32, i32* %"k"
  %"expression.9" = icmp sle i32 %".16", %"n"
  br i1 %"expression.9", label %"loop", label %"loop_end"
loop_end:
  br label %"exit"
exit:
  %".19" = load i32, i32* %"f"
  ret i32 %".19"
}

define i32 @"main"() 
{
entry:
  %"n" = alloca i32, align 4
  %"i" = alloca i32, align 4
  %".2" = call i32 @"leiaInteiro"()
  store i32 %".2", i32* %"n", align 4
  %"expression" = add i32 0, 1
  store i32 %"expression", i32* %"i"
  %"var_comper" = alloca i32
  br label %"loop"
loop:
  %".6" = load i32, i32* %"i"
  %".7" = call i32 @"fibonacciIter"(i32 %".6")
  call void @"escrevaInteiro"(i32 %".7")
  %".9" = load i32, i32* %"i"
  call void @"escrevaInteiro"(i32 %".9")
  %".11" = load i32, i32* %"i"
  %"expression.1" = add i32 0, %".11"
  %"expression.2" = add i32 %"expression.1", 1
  store i32 %"expression.2", i32* %"i"
  br label %"loop_val"
loop_val:
  %".14" = load i32, i32* %"i"
  %".15" = load i32, i32* %"n"
  %"expression.3" = icmp slt i32 %".14", %".15"
  br i1 %"expression.3", label %"loop", label %"loop_end"
loop_end:
  %"expression.4" = add i32 0, 1
  store i32 %"expression.4", i32* %"i"
  %"var_comper.1" = alloca i32
  br label %"loop.1"
loop.1:
  %".19" = load i32, i32* %"i"
  %".20" = call i32 @"fibonacciRec"(i32 %".19")
  call void @"escrevaInteiro"(i32 %".20")
  %".22" = load i32, i32* %"i"
  %"expression.5" = add i32 0, %".22"
  %"expression.6" = add i32 %"expression.5", 1
  store i32 %"expression.6", i32* %"i"
  br label %"loop_val.1"
loop_val.1:
  %".25" = load i32, i32* %"i"
  %".26" = load i32, i32* %"n"
  %"expression.7" = icmp slt i32 %".25", %".26"
  br i1 %"expression.7", label %"loop.1", label %"loop_end.1"
loop_end.1:
  br label %"exit"
exit:
  ret i32 0
}
