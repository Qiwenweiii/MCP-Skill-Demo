---
name: invoice-calc
description: 计算订单或发票总价，规则为单价乘数量后再加固定运费 10 元。当用户询问商品总价、订单金额、发票金额或"一共多少钱"时使用。
allowed-tools: mcp__math__add, mcp__math__multiply
---

# 发票总价计算

## 计算规则

总价 = 单价 × 数量 + 运费，运费固定为 10 元。

## 执行步骤

1. 从用户输入中提取单价（price）和数量（quantity）。
2. 调用 `multiply(a=price, b=quantity)` 计算商品小计。
3. 调用 `add(a=商品小计, b=10)` 计算总价。
4. 向用户报告商品小计、运费 10 元、总价三项结果。

## 约束

- 必须按顺序调用：先 `multiply`，后 `add`；禁止心算或把两步合并。
- 只能使用 `add` 和 `multiply` 两个工具。
- 缺少单价或数量时先询问用户，不要自行假设数值。
