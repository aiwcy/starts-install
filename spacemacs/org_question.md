# spacemacs 启用 org 错误解决方法

1. I solved this problem by using following solutions (in evil mode):

2. SPC h SPC, input "org" , and then select layer -> org. press Enter.
3. SPC f j, select "package.el" and press Enter to open that file.
4. /org-projectile:per-repo, find that line and g c c or just comment this line.
5. restart spacemacs.
[链接]("https://github.com/syl20bnr/spacemacs/issues/9374")
