# Jar of Love 素材缺口审计

## 审计结论

- 实拍输入:20 张 JPG,全部达到 1024px 以上,可作为 Ready 素材与对应花色生成参考。
- 已覆盖花色:黑色、酒红、blackmarble、charcoalblush、greyfloral、indigobark。
- 矩阵场景直接达标:greyfloral × 街拍逛街。
- 其余专属场景均需补生成;现有户外或室内图片不能用相近场景替代矩阵定义。
- 印花生成必须逐款绑定同花色实拍,纹样走向、图案比例、分布位置与配色任一漂移即不入 Approved 库。

## 花色 × 场景矩阵

| 花色 | 目标场景 | 现有覆盖 | 缺口 | 生成参考 |
|---|---|---|---|---|
| indigobark | 海边度假 | 户外站姿、办公室坐姿 | 缺海边度假 | `print-indigobark-front-outdoor-01.jpg` + `print-indigobark-front-01.jpg` |
| greyfloral | 街拍逛街 | 街道行走 | 已覆盖;另补不同景别以满足至少 2 次出镜 | `print-greyfloral-walk-street-01.jpg` + `print-greyfloral-front-02.jpg` |
| charcoalblush | 居家咖啡 | 正面、背面、肩带细节 | 缺居家咖啡 | `print-charcoalblush-front-01.jpg` + `print-charcoalblush-back-01.jpg` |
| blackmarble | 夜晚小聚 | 正面、白天户外背面/侧面 | 缺夜晚小聚 | `print-blackmarble-front-01.jpg` + `print-blackmarble-back-outdoor-01.jpg` |
| 黑色 | 日常通勤 | 正面、领口/肩带细节 | 缺通勤场景及背面 | `color-black-front-01.jpg` + `color-black-detail-strap-01.jpg` |
| 酒红 | 约会 | 正面、侧面、街景、室内全身 | 缺明确约会叙事 | `color-wine-full-indoor-01.jpg` + `color-wine-side-01.jpg` |

## 精简核心包缺口

| 优先级 | 缺口资产 | 数量 | 验收重点 |
|---|---|---:|---|
| P0 | 黑色背面模特 | 1 | 露肩交叉带、后领口、高低摆、黑色色相 |
| P0 | 弹力/垂坠感演示 | 1 | 只证明自然垂坠与轻微弹性,不虚构 4-way stretch |
| P0 | 高低摆侧面展示 | 1 | 前短后长轮廓清楚,不得收腰或改短衣长 |
| P0 | 专属场景矩阵 | 6 | 每花色唯一场景;四款印花逐张核对纹样 |
| P0 | 七分身尺码标注底图 | 1 | 黑色正面、手臂离身、胸围/衣长/袖长路径无遮挡 |
| P1 | 差异化搭配组合 | 3 | greyfloral+浅牛仔+凉鞋;黑色+黑短裙+高跟鞋;indigobark+白短裤+草编包 |
| P1 | greyfloral 第二景别 | 1 | 与现有街拍全身形成不同景别,满足至少两次出镜 |

## 规则 22 分配预案

| 资产 | 视线 | 表情 | 头向 |
|---|---|---|---|
| 黑色背面 | 回眸过肩 | 浅笑不露齿 | 左 |
| 黑色通勤 | 望向画外 | 平静松弛 | 右 |
| 酒红约会 | 看镜头 | 浅笑不露齿 | 正对 |
| indigobark 海边 | 望向画外 | 露齿笑 | 左 |
| greyfloral 街拍近景 | 低头看衣角 | 专注神态 | 右 |
| charcoalblush 居家咖啡 | 低头看杯子 | 平静松弛 | 左 |
| blackmarble 夜晚小聚 | 看镜头 | 平静松弛 | 正对 |
| 七分身尺码底图 | 看镜头 | 平静松弛 | 正对 |

## 停止条件

生成资产逐张通过服装结构、人体真实性、印花纹样和规则 22 检查后才登记 Approved。失败图不进入可用池。完成 INDEX 与缩略拼图后停止,等待用户验收,不得进入页面制作。

## 本轮生产结果

- Approved 生成素材:12 张。
- Draft 生成素材:3 张,均已在 `INDEX.md` 标明不可用于页面。
- 已完成:黑色背面、黑色通勤、酒红约会、indigobark 海边、charcoalblush 居家咖啡、greyfloral 第二景别、垂坠演示、高低摆侧面、黑色七分身尺码底图、3 组差异化搭配。
- 用户已拒绝 `blackmarble × 夜晚小聚` 精确合成图,该图已从素材库删除且不得用于页面。
- 前两张自由生成夜景仍保留 Draft 作为失败对照,不得用于页面。
- 页面制作阶段使用现有 Ready 的 blackmarble 实拍作为该印花出镜素材,不再补夜景图。
- 验收材料:`asset-contact-sheet-jaroflove.jpg`。

## 多人印花素材补充批次 01

- 新增 Approved:4 张。
- 人数结构:四人同框 1 张、三人同框 2 张、双人同框 1 张。
- 场景:海边度假露台、海边栈道、居家咖啡、城市逛街。
- 搭配覆盖:白短裤、浅色牛仔、米色长裤、黑裙、黑裤、白牛仔、牛仔裙及不同包鞋组合。
- 印花覆盖:indigobark / blackmarble / greyfloral / charcoalblush。
- 视线与表情:看镜头、望向画外、低头专注、回看;浅笑、露齿笑、平静无笑意均有覆盖。
- 专用验收拼图:`group-print-contact-sheet-01.jpg`。
