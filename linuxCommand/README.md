# tail 展示文件

```shell
# 显示文件的最后 5 行

tail -n 5 filename.txt

# 显示文件的最后 20 行

tail -n 20 filename.txt

# 实时查看文件内容更新

tail -f filename.txt

# 显示文件的最后 10 行，并附带行号

tail -n 10 filename.txt | nl
```

# 展示某路径从大到小的占用排序

```shell
du -ahx / | sort -rh | head -n 50
```

## 查看工具所在路径

```zsh
which command
```
