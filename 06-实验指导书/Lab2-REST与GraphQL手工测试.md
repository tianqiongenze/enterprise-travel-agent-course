# Lab2 REST 与 GraphQL 手工测试（LF2，随 L03/L04 课）

## 目标
完整走一遍《局域网人工测试指南》§1-§3，产出接口用例表与守卫实验截图。

## REST 部分
1. 空参数：`curl -X POST $BASE/recommend -H "Content-Type: application/json" -d "{}"`
2. 错误类型：days 传 "abc" → 记录 422
3. 多城市对比：北京/上海/杭州各一次，记录酒店名与价格
4. 边界值：days=0、days=-1、days=999 → 记录响应

## GraphQL 部分（GraphiQL：$BASE/graphql/）
1. 变量化查询（Trip($city,$days)）
2. 深度守卫：构造 10 层嵌套 → 期望 errors
3. 成本守卫：列表字段多层嵌套 → 期望 errors
4. 双面一致性：同城市 REST 与 GraphQL 的 city/days/酒店名比对

## 成果物
- 接口用例表（≥8 行，含输入/期望/实际/结论）
- 守卫拒绝截图 ×2
- 双面一致比对表

## 检查单
- [ ] REST ≥8 用例执行
- [ ] 422 验证
- [ ] 深度守卫拒绝留证
- [ ] 成本守卫拒绝留证
- [ ] 双面一致比对完成
