# Lab1 环境就绪与首次连通（LF1，随 L02 课）

## 目标
完成课程实训环境的全部连通性验证，产出《环境就绪检查表》。

## 前置条件
- 电脑接入校园/企业局域网（能 ping 通 10.167.2.175）
- 任意现代浏览器（Chrome/Edge）

## 步骤
1. 浏览器打开 `http://10.167.2.175:30181/health` → 期望 `{"status":"ok"}`
2. 打开 `http://10.167.2.175:30181/graphql/health` → 期望 `{"status":"graphql-schema-loaded"}`
3. 打开 `http://10.167.2.175:30181/metrics` → 期望 200 并看到 `travel_` 开头的指标
4. 打开 GraphiQL：`http://10.167.2.175:30181/graphql/`
5. 在左侧输入 `query { health }`，点执行 ▶ → 右侧出 `{"data":{"health":"ok"}}`
6. 换 worker 节点重复 1-3（`http://10.167.2.176:30181/...`）

## 检查单（逐项打钩）
- [ ] master 节点三探针通过
- [ ] worker 节点三探针通过
- [ ] GraphiQL 首查成功
- [ ] metrics 打开并找到 travel_runtime_requests_total
- [ ] 签名与日期

## 常见问题
| 现象 | 处理 |
|---|---|
| NodePort 不通 | 换另一节点 IP；仍不通找教师（防火墙） |
| /graphql 空白页 | 用带斜杠的 /graphql/ |
