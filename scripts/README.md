# 快速开始

## 初始化环境

项目统一使用根目录下的 `.venv` 虚拟环境。初始化脚本不依赖当前工作目录，也不会使用 Shell 中的 `python`、`pip` alias。

```bash
./scripts/init.sh
```

默认使用 `python3`。如需指定解释器：

```bash
PYTHON_BIN=/usr/local/opt/python@3.15/bin/python3.15 ./scripts/init.sh
```

脚本发现 `.venv` 损坏或 Python 主次版本不一致时会自动重建环境。

## 激活虚拟环境

每次打开新的终端后执行：

```bash
source .venv/bin/activate
```

命令行提示符出现 `(.venv)` 表示环境已激活。

如需退出虚拟环境：

```bash
deactivate
```

以下命令均默认已经激活 `.venv`。

### 检查环境

```bash
python --version
python -m pip --version
```

### 升级 pip

```bash
python -m pip install --upgrade pip
```

### 升级项目依赖

```bash
python -m pip list --outdated
python -m pip install --upgrade -r requirements.txt
```

依赖升级会遵守 `requirements.txt` 中的版本上限。不要使用 `pip list | xargs pip install -U`，该命令会绕过项目约束并可能调用全局 pip。

## MkDocs 部署

```bash
mkdocs serve
mkdocs gh-deploy
```

## 工具

以下命令均在项目根目录执行。

### 生成 MkDocs 导航

扫描 `docs/pages` 并重新生成 `mkdocs.yml` 中的导航：

```bash
python scripts/build.py
```

### 修复图片路径

```bash
python scripts/fix-image.py docs/path/to/file.md
```

不传文件路径时会扫描整个 `docs`：

```bash
python scripts/fix-image.py
```

### 生成 Markdown 文件路径

```bash
python scripts/path-gen.py write
python scripts/path-gen.py repair
python scripts/path-gen.py append
```
