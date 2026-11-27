# Custom GPT compatibility setup / 兼容配置

## English

First read COMPATIBILITY_AND_MIGRATION.md and HOST_REQUIREMENTS.md. Check the owning workspace notice and whether the intended GPT is actually creatable/editable, read-only or retired. This package does not establish eligibility. If unavailable, mark the configuration/Preview gate **blocked**, retain these materials and use portable or Projects.

Where the editor is available, apply the following manually; nothing has been installed in an account:

| Field | Proposed value / action |
| --- | --- |
| Name | Yuri Card Workbench Lite |
| Description | Create and adapt yuri roleplay card/worldbook drafts from conversation, supplied cards, posts and novel chapters, with explicit continuity and source limits. |
| Instructions | Paste all of GPT_INSTRUCTIONS.md; save and read back its version and ending. This must be active Instructions, not only knowledge. |
| Knowledge | Add only REFERENCE_PACK.md as reusable workflow knowledge; consult KNOWLEDGE_MAP.md. No real cards/chapters/checkpoints or Preview answers. |
| Conversation starters | “Create an original yuri card; you decide ordinary details.” / “Adapt this supplied JSON/text card within my stated scope.” / “Turn this supplied post into a card; the poster is {{user}}.” / “Continue my novel project: ask for my checkpoint and next text.” |
| Model | Use an actually available suitable model; no fixed model or tested equivalence is promised. For future trials use a cost-effective GPT instance. |
| Capabilities | Basic workflow: text only. Browsing, image generation and code/file tools are optional and may remain off. No actions or external integration required. |
| Visibility | Keep private while checking. Sharing/publication is a separate action outside this preparation. |

If the field or upload rejects the complete text, do not cut policy. Use the portable fallback and record the rejection. Run PREVIEW_TESTS.md only as a separately performed trial with actual observations; the cases here have not run. A fresh continuation must ask for the explicit checkpoint and necessary next source/current draft, without assuming memory or prior-chat access.

## 简体中文

先读 COMPATIBILITY_AND_MIGRATION.md 和 HOST_REQUIREMENTS.md，核对所属工作区通知及目标 GPT 是否实际可创建／编辑、只读或已退役。本包不证明账户资格。不可用时把配置／Preview 验收标为**阻塞**，保留兼容材料，改用通用包或 Projects。

编辑器可用时，手工填写上表。名称用 Yuri Card Workbench Lite；简介说明通过对话、角色卡、帖子和小说章节创作百合角色／世界书草稿，并明确连续性和来源限制。将 GPT_INSTRUCTIONS.md 全部粘贴到实际 Instructions，保存后回读版本和末尾。Knowledge 仅添加 REFERENCE_PACK.md，不放真实卡、章节、检查点或 Preview 答案。基础流程只需文本，联网、图像、代码／文件能力可关闭，不需要 Actions。配置检查期间保持私人；本次准备不包含共享或发布。

中文开场提示可用：“创作原创百合卡，普通细节由你决定。”“在指定范围内改编我提供的 JSON／文本卡。”“把提供的帖子改编成卡，发帖者绑定为 {{user}}。”“续接我的小说项目，先接收检查点和下一批正文。”使用实际可选模型，不承诺固定模型或已验证等效性；后续测试用经济型 GPT 实例。

若指令或上传被拒绝，不要删政策，改用通用路径并记录拒绝。PREVIEW_TESTS.md 仅是未执行方案；必须另行观察结果。新会话续接需要显式检查点和必要的新原文／当前草稿，不假定记忆或旧会话访问。
