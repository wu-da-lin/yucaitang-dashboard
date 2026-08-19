# 部署说明

三种部署方式，按推荐度排序：

---

## 路径 A · GitHub Pages（永久在线，推荐）

部署一次，永久有效。10~30 分钟搞定。

### 方法一：网页拖拽（最简单，零命令）

1. 在 GitHub 仓库页面：**Add file → Upload files**
2. 把本目录的 `index.html` 拖进页面
3. 点 **Commit changes**
4. 仓库 **Settings → Pages** → Branch 选 `main` → **Save**
5. 等 1~2 分钟，访问：
   ```
   https://wu-da-lin.github.io/yucaitang-dashboard/
   ```

> 后续更新数据：重新上传 `index.html` 覆盖即可，无需改其他设置。

### 方法二：命令行推送（适合频繁更新）

直接双击本目录的 `部署到GitHubPages.bat`，按提示输入：

1. **仓库地址**：`https://github.com/wu-da-lin/yucaitang-dashboard.git`
2. **GitHub Token**：Settings → Developer settings → Personal access tokens → Generate new token（勾选 `repo` 权限，**永久**设为 expiration，不过期）

脚本会自动：复制独立版 → git init → add → commit → push main 分支。

> 第一次推送可能因为仓库是空的（没有 main 分支）失败，把脚本里的 `git push -u origin main` 改成 `git push -u origin master` 或先在 GitHub 网页创建任意 README 后再跑。

---

## 路径 B · 本地离线查看（零依赖，永不挂）

直接双击 `index.html`（或 `生产数据看板_独立版.html`，在项目主目录），浏览器打开即用。

- ✅ 零网络、零安装、零服务
- ✅ 永不过期、永不回收
- ❌ 只有本机看，局域网其他设备看不到

---

## 路径 C · 局域网服务（公司内网分享）

适合工厂场景——车间、办公室都在公司内网里。

1. 把 `index.html` 重命名或复制为 `dashboard.html`，放在与 `dashboard_serve.py` 同目录
2. 打开 cmd，进入该目录，执行：
   ```
   python dashboard_serve.py
   ```
3. 黑窗口里会显示本机 + 局域网地址，例如：
   ```
   http://127.0.0.1:8090/dashboard.html   ← 你自己看
   http://192.168.x.x:8090/dashboard.html ← 发给同事 / 手机
   ```
4. 关窗口 = 停服；电脑常开 = 一直在线

> `dashboard_serve.py` 就在本部署包内（5 KB，跨平台），也可从主目录 `C:\Users\86182\WorkBuddy\2026-06-23-14-20-16\` 获取。

---

## 数据源

- **来源**：Excel 生产记录表（.xlsm）经 ETL 处理后写入看板
- **字段**：日期 / 产品编码 / 班次 / 实际工时 / 停机原因 / 报废数等
- **OEE 公式**：OEE = 合格率 × 时间稼动率 × 性能稼动率
- **详细配置**：看看板内「归类配置」面板

## 备份与恢复

- 主文件：`生产数据看板.html`（约 400KB，读 IndexedDB）
- 独立版：`生产数据看板_独立版.html`（4.3MB，内嵌数据）
- 分类配置：浏览器 localStorage 键 `DT_CATEGORIES_V3` / `CAT_MAP_V3`
- 排除规则：浏览器 localStorage 键 `EXCLUDE_RULES_V2`

升级浏览器或换电脑时，**用同账号的浏览器配置同步** 或手动复制以上 localStorage 值。