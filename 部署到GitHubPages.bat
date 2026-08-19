@echo off
chcp 65001 >nul
setlocal
title 生产看板 → GitHub Pages 一键部署

:: 使用本机自带的 PortableGit（无需额外安装）
set "GIT=C:\Users\86182\.workbuddy\binaries\PortableGit\versions\1.2.0\cmd\git.exe"
if not exist "%GIT%" (
  echo [错误] 未找到本机 Git：%GIT%
  echo 请改用 README 里的"方法一：网页拖拽"，或安装 Git for Windows 后重试。
  pause
  exit /b 1
)

cd /d "%~dp0"

if not exist "index.html" (
  echo [错误] 当前目录缺少 index.html，请把本脚本与 index.html 放在同一文件夹。
  pause
  exit /b 1
)

echo ============================================
echo   生产看板 一键部署到 GitHub Pages
echo ============================================
echo.
echo 准备步骤（详见 README）：
echo   1. 在 GitHub 建一个空仓库（Public）
echo   2. 生成一个有 repo 权限的 Personal Access Token
echo.
set /p "REPO=1) 粘贴仓库 HTTPS 地址 (形如 https://github.com/用户名/仓库.git): "
if "%REPO%"=="" ( echo 未输入仓库地址 & pause & exit /b 1 )

set /p "TOKEN=2) 粘贴 GitHub Personal Access Token: "
if "%TOKEN%"=="" ( echo 未输入 Token & pause & exit /b 1 )

:: 拼接带 token 的 push 地址：https://<token>@github.com/<用户名>/<仓库>.git
set "TOKEN_REPO=https://%TOKEN%@github.com/%REPO:*github.com/%"

echo.
echo [1/5] 初始化 git ...
"%GIT%" init -q
echo [2/5] 添加 index.html ...
"%GIT%" add index.html
echo [3/5] 提交 ...
"%GIT%" -c user.name="yucaitang" -c user.email="dashboard@local" commit -q -m "deploy production dashboard"
echo [4/5] 设置分支为 main ...
"%GIT%" branch -M main
echo [5/5] 推送到 GitHub ...
"%GIT%" remote add origin "%TOKEN_REPO%"
"%GIT%" push -u origin main
if errorlevel 1 (
  echo.
  echo [失败] 推送出错。请检查：仓库地址 / Token 是否正确、仓库是否为空、网络是否连通。
  pause
  exit /b 1
)

echo.
echo ============================================
echo   推送成功！
echo   下一步：打开 GitHub 仓库 → Settings → Pages
echo   选 Branch: main → Save，1~2 分钟后访问：
echo   https://^<你的用户名^>.github.io/^<仓库名^>/
echo ============================================
pause
