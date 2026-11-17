# MCP-Skill-Demo

极简本地测试环境：一个 FastMCP 数学服务器 + 一个发票计算技能。

## 目录结构

- `math_mcp.py`：FastMCP 服务器，暴露 `add` 和 `multiply` 两个工具
- `.qoder/skills/invoice-calc/SKILL.md`：`invoice-calc` 技能，按"单价 × 数量 + 运费 10 元"计算总价
- `skills_src/invoice-calc/SKILL.md`：技能源文件副本
- `eval_test.py`：本地轨迹断言示例（可选自测）
- `requirements.txt`：Python 依赖

## 安装

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## 注册 MCP 服务器

在 MCP 设置中新增 stdio 服务器：

- 名称：`math`
- 命令：`.venv/bin/python`
- 参数：`math_mcp.py`

## 验证

验证方式为接入 WorkBuddy：在 WorkBuddy 中注册 `math` MCP 服务器并加载 `invoice-calc` 技能，通过实际对话确认调用顺序为 `multiply` → `add`。

技能执行规则：先调用 `multiply(a=单价, b=数量)` 得到小计，再调用 `add(a=小计, b=10)` 得到总价。
