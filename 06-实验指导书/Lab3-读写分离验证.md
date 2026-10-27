# Lab3 读写分离验证（LF3，随 L07 课）

## 目标
理解并验证 RoutingSessionFactory 的路由决策：写落主库、读落副本、副本无写。

## 步骤
1. 读源码 `services/techgroup-enterprise-travel-runtime/src/travel_agent/db/routing.py`，找到 `_RoutingSyncSession.get_bind`，回答：
   - flush 时走哪个引擎？
   - TextClause 的 INSERT/UPDATE/DELETE 前缀为什么也要判？
   - force_primary 靠什么字段传递？
2. 本地双 sqlite 实验：参照 `tests/test_db_read_write_routing.py` 三条断言，自行改写一份并跑通
3. 集群观察：`kubectl -n travel-prod set env deploy/travel-agent-api TRAVEL_DB_READ_URL=...`（由教师演示），观察环境变量生效后 pod 滚动重启
4. 思考题：如果 ReadURL 配错指向主库，会发生什么？为什么测试仍全绿？

## 成果物
- 路由验证报告（三断言 + 思考题答案）

## 检查单
- [ ] 源码三问回答
- [ ] 本地实验跑通
- [ ] 思考题有依据
