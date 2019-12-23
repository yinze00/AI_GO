# AI_GO
My AI course project based on alpha-belta pruning

>1.重点实现棋局评价，博弈树剪枝<br>
    2.尽可能比较不同评价策略或优化搜索，要有实验数据支持

### 棋局评价
* 基于五子棋的得分规则，设计不同得分判据
```python
shape_score = [(50, (0, 1, 1, 0, 0)),
               (50, (0, 0, 1, 1, 0)),
               (200, (1, 1, 0, 1, 0)),
               (500, (0, 0, 1, 1, 1)),
               (500, (1, 1, 1, 0, 0)),
               (5000, (0, 1, 1, 1, 0)),
               (5000, (0, 1, 0, 1, 1, 0)),
               (5000, (0, 1, 1, 0, 1, 0)),
               (5000, (1, 1, 1, 0, 1)),
               (5000, (1, 1, 0, 1, 1)),
               (5000, (1, 0, 1, 1, 1)),
               (5000, (1, 1, 1, 1, 0)),
               (5000, (0, 1, 1, 1, 1)), 
               (50000, (0, 1, 1, 1, 1, 0)),
               (99999999, (1, 1, 1, 1, 1))]
```
* 在纵横斜四个方向上探查某一点周围的点的情况
```python
my_score += cal_score(m, n, 0, 1, enemy_list, my_list, score_all_arr)   # 水平方向得分
my_score += cal_score(m, n, 1, 0, enemy_list, my_list, score_all_arr)   # 述职方向得分
my_score += cal_score(m, n, 1, 1, enemy_list, my_list, score_all_arr)   # 左斜方向得分
my_score += cal_score(m, n, -1, 1, enemy_list, my_list, score_all_arr)  # 右斜方向得分
```

### 博弈树剪枝
* α-β剪枝算法
