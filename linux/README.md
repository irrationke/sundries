# 要在 Linux 上查看网络流量大小，你可以使用一些命令行工具。以下是一些常用的选项：

1. **iftop**: 这是一个交互式的实时流量监视器。你可以使用 `iftop` 命令来查看当前的网络流量情况，包括每个连接的流量信息。

   ```bash
   sudo iftop
   ```

2. **nload**: 这个工具会以图形化的方式显示网络流量情况，包括实时的上传和下载速率。

   ```bash
   sudo nload
   ```

3. **iftop + tcpdump**: 你可以使用 `iftop` 结合 `tcpdump` 来更详细地查看流量信息。

   ```bash
   sudo tcpdump -i <interface> -w - | sudo iftop -i <interface> -
   ```

   其中 `<interface>` 是你想要监视的网络接口，如 `eth0` 或 `wlan0`。

4. **vnstat**: 这是一个用于监视网络流量的工具，它可以提供汇总的数据，包括每天、每月和每年的流量统计信息。

   安装并启用 vnstat：

   ```bash
   sudo apt-get install vnstat
   sudo vnstat -u -i <interface>
   ```

   查看网络流量统计：

   ```bash
   vnstat
   ```

5. **iptraf**: 这是一个功能强大的交互式网络监视器，可以提供各种网络统计和流量信息。

   ```bash
   sudo iptraf-ng
   ```

# 添加特定 ip 连接的防火墙

## 开放端口 9100

sudo firewall-cmd --zone=public --add-port=9100/tcp --permanent

## 只允许特定 IP 地址访问端口 9100

```shell
sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.100" port port=9100 protocol=tcp accept' --permanent
```

## 重新加载 firewalld 以应用更改

```shell
sudo firewall-cmd --reload
```

# 创建 SSH 密钥对

```shell
ssh-keygen -m PEM -t rsa -b 4096 -C "name@hostname"
# 参数解析 -m 密钥格式 -t 密钥类型 -b 密钥位数 -C 公钥末尾识别文本 -f 保存名称 -N 私钥密码
```

# Linux 下的 btmp、wtmp 和 utmp 日志文件

- btmp 为 ssh 登录失败日志

- utmp 文件记录用户登录信息，包括用户登录的终端，登出状态，系统时间，当前系统的状态，系统启动的时间（被 uptime 命令使用）等等

- wtmp 会记录 utmp 文件的历史记录，包括了当前登录用户信息和历史用户登录信息

- 查看方法

  - 使用 last -f /var/log/btmp

  - `lastb` 命令，默认会读取 `/var/log/btmp` 文件

  - utmpdump /var/log/btmp

##
