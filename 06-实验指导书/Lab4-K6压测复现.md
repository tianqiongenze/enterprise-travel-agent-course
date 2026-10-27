# Lab4 K6 压测复现（LF5，随 L13 课，企业机房）

## 目标
在真实集群复现第四轮压测基线，并与官方数据对比（±15% 合格）。

## 基线（2026-10-26 实测）
| 档位 | 吞吐 | P95 | 错误率 |
|---|---|---|---|
| 50 VU | 252 req/s | 262ms | 0% |
| 200 VU | 155 req/s | 4.52s | 0% |

## 步骤（教师 SSH 执行，学生记录）
1. `ssh root@10.167.2.175`
2. `kubectl -n travel-prod delete job k6-fourth-round --ignore-not-found`
3. `kubectl apply -f /root/fourth/k6job.yaml`（VUS=50，DURATION=3m）
4. 等待 4 分钟：`kubectl -n travel-prod logs job/k6-fourth-round --tail=40`
5. 记录：http_reqs、http_req_duration p95、checks、http_req_failed
6. 另开窗口：`kubectl -n travel-prod get hpa travel-agent-api-hpa -w` 观察副本数
7. 压测后：`kubectl -n travel-prod get pods` 确认副本回落

## 数据表（填写）
| 指标 | 官方基线 | 本组实测 | 偏差% | 结论 |
|---|---|---|---|---|
| 吞吐 req/s | 252 | | | |
| P95 ms | 262 | | | |
| 错误率 | 0% | | | |

## 安全纪律
- 只对 travel-prod 命名空间压测；VU 不得超过 100；执行前教师报备
