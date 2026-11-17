# 参考文献格式规范

编辑 `docs/**/*.md` 中的参考文献时，必须遵循本规范。

## 通用要求

- 参考区块使用 `----` 分隔线和 `*参考*` 标题。
- 引用按出现顺序连续编号：`[1]`、`[2]`、`[3]`。
- 标题必须使用 Markdown 链接，不裸露 URL。
- 作者、组织、标题、平台、版本及日期应根据原始来源核实，不得臆造。
- 发布年份未知时，不得用访问年份冒充；官方文档使用实际访问日期，格式为 `Accessed YYYY-MM-DD`。
- 中文与英文、英文与数字之间保留空格；条目以英文句点结尾。

## 技术文章 / 博客

格式：`[编号] 作者/机构. [文章标题](URL). 平台/博客名, 发布年份.`

示例：`[1] 阮一峰. [ES6 入门教程](https://ruanyifeng.com). 网道, 2023.`

## 官方文档 / API 手册

格式：`[编号] 产品/组织名. [文档章节标题](URL). Accessed YYYY-MM-DD.`

示例：`[2] React Team. [useEffect – React Reference](https://react.dev). Accessed 2026-11-17.`

## 开源项目 / GitHub 仓库

格式：`[编号] 维护者/组织. [仓库名: 简短描述](URL). GitHub, 版本号/年份.`

示例：`[3] Vercel. [Next.js: The React Framework](https://github.com). GitHub, v15.0.`

## 学术论文

格式：`[编号] 第一作者等. [论文标题](arXiv 或 PDF URL). 会议/期刊简称, 年份.`

示例：`[4] Vaswani A, et al. [Attention Is All You Need](https://arxiv.org). NeurIPS, 2017.`
