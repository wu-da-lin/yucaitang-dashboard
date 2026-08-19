# 育材堂生产数据看板

> C-103 切割产线 OEE (设备综合效率) 看板 · 数据源：生产记录表 (.xlsm)

## 特性

- **9 大 KPI**：生产总数、OK 数、报废、合格率、报废率、时间稼动率、性能稼动率、OEE 等
- **停机 / 报废原因归类 + 帕累托分析**：按产线隔离的分类体系
- **多产线对比**：C103 / B101 / C105 / C106 / souring 系列
- **月度报告导出**：自动生成 OEE 月报 PPT
- **多端访问**：本机 / 局域网 / 公网（GitHub Pages）

## 在线访问

部署到 GitHub Pages 后，永久 URL 形如：
```
https://wu-da-lin.github.io/yucaitang-dashboard/
```

## 本目录文件

| 文件 | 用途 |
|---|---|
| `index.html` | 看板本体（4.3 MB，已内嵌全部数据 + Chart.js + xlsx，零依赖，双击即开） |
| `README_部署.md` | 三种部署方式的详细步骤（GitHub Pages / 局域网 / 本地离线） |
| `部署到GitHubPages.bat` | Windows 一键 git 推送脚本（可选，命令行玩家用） |
| `dashboard_serve.py` | 局域网服务脚本（Python 跨平台，本机起 8090 给同事访问） |

## 最快上手（30 秒）

直接双击 `index.html`，浏览器打开即用。**零网络、零安装、零依赖**。

## 更新数据

看板的数据是发布时打进去的（4.3 MB 内嵌）。要更新：

1. 在原项目里重新生成 `生产数据看板_独立版.html`
2. 把同名文件覆盖到这个目录的 `index.html`
3. 在 GitHub 仓库页面上传覆盖（或跑 `部署到GitHubPages.bat`）

详细部署步骤见 [README_部署.md](./README_部署.md)。