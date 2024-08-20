## 创建命令行代理

```powershell
Set-Item Env:all_proxy "socks://127.0.0.1:2080"

Set-Item Env:http_proxy "http://127.0.0.1:2080"

Set-Item Env:https_proxy "http://127.0.0.1:2080"

$env:HTTP_PROXY="http://127.0.0.1:7897"; $env:HTTPS_PROXY="http://127.0.0.1:7897"
```