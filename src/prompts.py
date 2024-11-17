SUMMARY_PROMPT = """Summarize the transcript provided, focusing on key points and using a simplified Chinese structure similar to the example below.

Include a brief introductory statement followed by numbered sections that clearly highlight the main topics discussed. Maintain conciseness and a logical flow, providing at least 6 to 10 distinct sections or categories. Each section should contain a clear title, a detailed summary in bullet-point format, and include one quote from the interview where applicable.

# Summary Template
访谈总体介绍，与[访谈对象]对谈长达[时长]，以下是访谈总结，文末有原文链接。访谈内容涵盖了[关键主题]，以下为主要讨论内容。

1. [主要主题1]
- [详细讨论内容]
- 引用: "[访谈中的直接引用]"

2. [主要主题2]
- [详细讨论内容]
- 引用: "[访谈中的直接引用]"

[Repeat for additional sections, maintaining similar detail and structure.]

# Output Format
Provide the summary in simplified Chinese as a structured list of key points with at least 6 sections or categories. Each section should be formatted with a title, bullet points, and include a relevant quote where applicable, strictly following the example structure provided. Aim for an overview length between 250-400 characters per section.

# Notes
- Ensure clarity and conciseness for non-technical audiences.
- Use simplified Chinese to ensure accessibility.
- Preserve the logical flow of categories, keeping related points together.
- Include at least one quote per section where relevant to add depth to the summary."""