## 创建会话

```sh
tmux new -s <session-name>
```

## 分离会话

`Ctrl+b d`

## 查看所有会话

`tmux ls`

## 回到会话

`tmux attach -t <session-name>`

# 窗格管理

## 创建窗格

`tmux split-window` `trl+b "` 上下划分

`tmux split-window -h` `Ctrl+b %` 左右划分

## 加入复制模式

`Ctrl+b [`

