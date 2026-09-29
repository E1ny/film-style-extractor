# Film Style Extractor

一个可调用的 Codex 技能，用于分析电影截图、广告片画面和视觉参考图，将难以言说的“电影感”拆解为具体、可迁移的视觉语言，并生成可直接用于 AI 创作的提示词。

## 能做什么

- 拆解影像介质、颗粒、动态范围和成像质感
- 分析主光、补光、反差、阴影、高光与环境光
- 提取主色、分区色偏、饱和度和明暗关系
- 分析构图、视角、景别、透视、景深和镜头语感
- 描述空间介质、氛围、叙事节奏和视觉重心
- 将风格与参考图中的人物、物件、品牌、地点和剧情分离
- 输出模块化报告、单段正向提示词和针对性负向提示词
- 多图风格冲突时分别给出可直接复制的方案

提示词没有固定字数限制。输出长度由图片中可见且可靠的特征决定，优先保证准确、具体和可复用。

## 使用方法

在安装插件后的新 Codex 会话中上传一张或多张参考图，然后输入：

```text
$film-style-extractor 请完整拆解这张参考图的影视视觉风格，并生成可用于其他创作主体的提示词。
```

也可以指定输出方式：

```text
$film-style-extractor 只给我一段可复制的正向提示词。
```

```text
$film-style-extractor 比较这些参考图的共同风格和差异，冲突的方向分别输出。
```

## 目录

```text
.codex-plugin/plugin.json
skills/film-style-extractor/SKILL.md
skills/film-style-extractor/references/analysis-matrix.md
skills/film-style-extractor/references/output-contract.md
skills/film-style-extractor/scripts/check_prompt.py
```

## 设计原则

技能只依据实际可见像素做判断。无法从单帧确认的摄影机、镜头、胶片型号和精确参数不会被写成事实；字幕、网页界面、水印和说明文字也不会被误当成影视风格证据。

## 验证情况

插件已通过结构校验，并完成 Codex CLI 的单图、多图、缺图和指定模型分支调用验证。Codex 桌面应用中新聊天尚未单独实测。

