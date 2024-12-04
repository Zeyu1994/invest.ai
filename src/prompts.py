PROMPTS = {}

PROMPTS['earning_transcript_summary'] = """
请帮我处理以下的财报会议的逐字稿，从相关行业投资者的角度考虑一下有什么值得参考的信息和趋势，进行总结和分析，要求如下:

1. 请用中文进行报告总结
2. 考虑到一些术语观众可能不熟悉，请在技术术语后面附上英文原文。
3. 将逐字稿中提到的财务信息，分为本季度和前瞻，放到报告开头。
4. 在报告末尾加上报告中出现术语的简要解释。

逐字稿如下：
{transcript}"""

PROMPTS['invest_transcript_summary'] = """
请帮我处理以下的逐字稿，从相关行业投资者的角度考虑一下有什么值得参考的信息和趋势，进行总结和分析，要求如下:

1. 请用中文进行报告总结
2. 考虑到一些术语观众可能不熟悉，请在技术术语后面附上英文原文。
3. 在报告末尾加上报告中出现术语的简要解释。
{transcript}

"""


PROMPTS['invest_transcript_qa'] = """
请帮我处理以下的逐字稿, 从投资者的角度考虑本文中涉及了哪些问题与重要信息。并以问答的形式添加在报告的开头，并给出分析的同时引用原文。
请引用原文(不要翻译)，报告以中文形式返回。
请至少包含10个问答对。

逐字稿如下：
{transcript}"""

PROMPTS['mix_summary_qa'] = """
你将会得到关于同一份逐字稿的两份报告，一份是问答形式的，另一份是总结形式的。
请将两份报告合并成一份，问答报告放在总结报告的前面。
请不要改变问答报告和总结报告的内容，只需将两份报的内容进行拆分重组。
请以：标题 -  总结报告 - Q&A  的形式返回。

总结报告:
{Summary}

问答报告:
{QA}
"""

PROMPTS['default_qa_prompt'] = """
        请从投资者的角度考虑本文中涉及了哪些问题与重要信息。并以问答的形式添加在报告的开头，并给出分析的同时引用原文，引用原文时请保持原文的语言。
        格式请参考如下的例子:
        **问1**：Elastic在2025财年第二季度的关键财务亮点是什么？

        **答**：Elastic在2025财年第二季度取得了强劲的财务业绩，超出了所有收入和盈利指标的指引。总收入达到3.65亿美元，同比增长18%，云收入同比增长25%。公司还实现了17.6%的非GAAP运营利润率，显著高于预期。

        **引用原文**：

        > "Elastic delivered a strong second quarter, supported by solid sales execution and customer commitments. In Q2, we meaningfully exceeded guidance across all revenue and profitability metrics. Revenue grew by 18% year-over-year. Cloud revenue grew by 25% year-over-year. And we delivered a non-GAAP operating margin of 18%."
        > 
        请至少包含10个问答对。


        Transcript:
        {transcript}
        """

PROMPTS['default_summary_prompt'] =  """
        请帮我处理以下的逐字稿，从相关行业投资者的角度考虑一下有什么值得参考的信息和趋势，进行总结和分析，要求如下:

        1. 请用中文进行报告总结
        2. 考虑到一些术语观众可能不熟悉，请在技术术语后面附上英文原文。
        3. 在报告末尾加上报告中出现术语的简要解释。
        逐字稿: 
        {transcript}
        """

PROMPTS['default_final_prompt'] = """
        你将会得到关于同一份逐字稿的两份报告，一份是问答形式的，另一份是总结形式的。
        请将两份报告合并成一份, 请以：标题 -  总结报告 - Q&A  的形式返回。
        请不要改变问答报告和总结报告的内容，只需将两份报的内容进行拆分重组。
        

        问答报告:
        {QA}
        总结报告:
        {Summary}
        """