@echo off
setlocal EnableDelayedExpansion
set i=0
for %%a in (*.jpeg) do (
    set /a i+=1
    ren "%%a" "!i!.jpeg"
)
ren *.jpeg *.png