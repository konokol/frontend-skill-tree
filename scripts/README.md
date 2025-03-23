
# 初始化环境

运行 init.sh，初始化python环境并安装依赖

## 升级依赖

一键升级全部依赖： `pip3 list -o --format columns|  cut -d' ' -f1|xargs -n1 pip install -U`  
保存依赖：`pip3 freeze > requirements.txt`

# mkdocs部署

运行 `mkdocs serve`，本地预览。
执行 `mkdocs gh-deploy`，部署到Github上。

# 工具

## 修复图片路径

在项目根目录下执行

```bash
python3 scripts/fix_image.py xxx # 修复单个文件
```